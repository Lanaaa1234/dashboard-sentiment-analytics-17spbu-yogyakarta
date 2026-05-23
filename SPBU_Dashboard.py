import streamlit as st
import pandas as pd
import plotly.express as px

from utils.helper import (
    load_data,
    sentiment_distribution,
    dataset_summary
)

from utils.global_filter import global_filter
from utils.global_header import global_header

from utils.cards import (
    metric_card,
    section_header,
    info_card,
    page_footer
)

from utils.charts import (
    donut_chart,
    vertical_bar,
    line_chart
)

from utils.insights import (
    sentiment_insight
)

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="SPBU Dashboard",
    page_icon="⛽",
    layout="wide"
)

# =========================================================
# LOAD CSS
# =========================================================
with open("assets/style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================================================
# LOAD DATA
# =========================================================
with st.spinner("Loading dashboard..."):

    df = load_data()

# HANDLE NULL TEXT
df["text_kalimat"] = (
    df["text_kalimat"]
    .fillna("")
    .astype(str)
)

# =========================================================
# SIDEBAR TITLE
# =========================================================
st.sidebar.markdown(
    """
    <div class="sidebar-title">
        ⛽ SPBU Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# GLOBAL HEADER
# =========================================================
global_header()

# =========================================================
# GLOBAL FILTER
# =========================================================
filtered_df = global_filter(df)

# =========================================================
# SUMMARY
# =========================================================
summary = dataset_summary(filtered_df)

# =========================================================
# OVERVIEW SECTION
# =========================================================
section_header(
    "📊 Dashboard Overview",
    "Dashboard interaktif analisis sentimen ulasan pelanggan SPBU."
)

# =========================================================
# EXECUTIVE SUMMARY
# =========================================================
section_header(
    "Executive Summary",
    "Ringkasan statistik utama berdasarkan hasil filtering dashboard."
)

# =========================================================
# KPI
# =========================================================
col1, col2, col3, col4 = st.columns(4)

with col1:

    metric_card(
        "Total Review",
        f"{summary['total_review']:,}",
        "📊"
    )

with col2:

    metric_card(
        "Jumlah SPBU",
        summary["total_spbu"],
        "⛽"
    )

with col3:

    metric_card(
        "Average Rating",
        f"⭐ {summary['avg_rating']}",
        "⭐"
    )

with col4:

    metric_card(
        "Average Text Length",
        f"{summary['avg_text_length']} kata",
        "📝"
    )

# =========================================================
# DISTRIBUSI SENTIMEN
# =========================================================
section_header(
    "Distribusi Sentimen",
    "Visualisasi distribusi sentimen pelanggan SPBU."
)

sentiment_df = sentiment_distribution(
    filtered_df
)

col1, col2 = st.columns(2)

# DONUT CHART
with col1:

    fig = donut_chart(
        sentiment_df,
        names="Sentimen",
        values="Jumlah",
        title="Distribusi Sentimen"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# BAR CHART
with col2:

    fig = vertical_bar(
        sentiment_df,
        x="Sentimen",
        y="Jumlah",
        title="Jumlah Sentimen"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

# =========================================================
# INSIGHT
# =========================================================
info_card(
    sentiment_insight(sentiment_df)
)

# =========================================================
# TREND REVIEW
# =========================================================
section_header(
    "Trend Review Bulanan",
    "Visualisasi trend jumlah ulasan pelanggan berdasarkan bulan."
)

trend_df = (
    filtered_df
    .groupby("month_name")
    .size()
    .reset_index(name="Jumlah")
)

month_order = [

    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

trend_df["month_name"] = pd.Categorical(
    trend_df["month_name"],
    categories=month_order,
    ordered=True
)

trend_df = trend_df.sort_values(
    "month_name"
)

fig = line_chart(
    trend_df,
    x="month_name",
    y="Jumlah",
    title="Trend Review Bulanan"
)

st.plotly_chart(
    fig,
    width="stretch"
)

info_card(
    """
    Trend review menunjukkan pola aktivitas pelanggan
    dalam memberikan ulasan terhadap layanan SPBU
    dari waktu ke waktu berdasarkan hasil filtering data.
    """
)

# =========================================================
# TOP SPBU
# =========================================================
section_header(
    "Top SPBU Berdasarkan Jumlah Review",
    "SPBU dengan jumlah ulasan pelanggan terbanyak."
)

# COUNT REVIEW
top_spbu_df = (
    filtered_df["title"]
    .value_counts()
    .reset_index()
)

# RENAME COLUMN
top_spbu_df.columns = [
    "SPBU",
    "Jumlah Review"
]

# TOP 10
top_spbu_df = top_spbu_df.head(10)

# SORT ASCENDING
top_spbu_df = top_spbu_df.sort_values(
    by="Jumlah Review",
    ascending=True
)

# COLOR GRADIENT
custom_colors = [

    "#DC2626",
    "#EA580C",
    "#F59E0B",
    "#FACC15",
    "#84CC16",
    "#65A30D",
    "#16A34A",
    "#15803D",
    "#166534",
    "#14532D"
]

# CREATE BAR CHART
fig = px.bar(

    top_spbu_df,

    x="Jumlah Review",

    y="SPBU",

    orientation="h",

    text="Jumlah Review"
)

# UPDATE BAR STYLE
fig.update_traces(

    marker_color=custom_colors,

    textposition="inside",

    insidetextanchor="middle",

    textfont=dict(
        color="white",
        size=13
    ),

    marker_line_color="white",

    marker_line_width=1.5
)

# UPDATE LAYOUT
fig.update_layout(

    showlegend=False,

    height=650,

    template="plotly_white",

    paper_bgcolor="white",

    plot_bgcolor="white",

    margin=dict(
        l=20,
        r=20,
        t=20,
        b=20
    ),

    xaxis_title=None,

    yaxis_title=None,

    font=dict(
        family="Arial",
        size=13,
        color="#111827"
    )
)

# SHOW CHART
st.plotly_chart(
    fig,
    width="stretch"
)

# INSIGHT
info_card(
    """
    Jumlah review yang tinggi menunjukkan
    tingginya interaksi pelanggan terhadap
    SPBU tertentu pada Google Maps.
    """
)

# =========================================================
# DATASET PREVIEW
# =========================================================
section_header(
    "Dataset Preview",
    "Contoh data hasil preprocessing ulasan pelanggan SPBU."
)

preview_df = filtered_df[
    [
        "title",
        "stars",
        "ket_sentiment",
        "text_kalimat"
    ]
].copy()

preview_df.columns = [
    "SPBU",
    "Rating",
    "Sentimen",
    "Text Preprocessing"
]

st.dataframe(
    preview_df.head(10),
    width=1200,
    height=420
)

# =========================================================
# FOOTER
# =========================================================
page_footer()