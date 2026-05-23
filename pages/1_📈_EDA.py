import streamlit as st
import pandas as pd
import plotly.express as px

from utils.helper import (
    load_data,
    add_text_length,
    sentiment_distribution,
    dataset_summary,
    sentiment_percentage
)

from utils.global_filter import global_filter
from utils.global_header import global_header

from utils.cards import (
    metric_card,
    section_header,
    info_card,
    success_card,
    warning_card,
    page_footer
)

from utils.charts import (
    donut_chart,
    vertical_bar,
    histogram_chart,
    boxplot_chart,
    stacked_bar,
    line_chart
)

from utils.insights import (
    sentiment_insight,
    rating_insight
)

# PAGE CONFIG
st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📈",
    layout="wide"
)

# LOAD CSS
with open("assets/style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# LOAD DATA
with st.spinner("Loading EDA dashboard..."):

    df = load_data()
df["text_kalimat"] = (
    df["text_kalimat"]
    .fillna("")
    .astype(str)
)
if "filtered_df" not in st.session_state:

    st.session_state.filtered_df = df.copy()

filtered_df = st.session_state.filtered_df

# FILTER SIDEBAR

# TEXT LENGTH
filtered_df = add_text_length(
    filtered_df
)

# HEADER
st.markdown(
    """
    <div style="
        background:linear-gradient(
            135deg,
            #FACC15,
            #F59E0B
        );
        padding:35px;
        border-radius:24px;
        margin-bottom:25px;
        color:white;
    ">

    <h1 style="
        color:white;
        margin-bottom:10px;
    ">
        📈 Exploratory Data Analysis
    </h1>

    <p style="
        font-size:16px;
        line-height:1.8;
        margin-bottom:0;
        color:white;
    ">
        Exploratory Data Analysis dilakukan
        untuk memahami karakteristik dataset,
        distribusi sentimen, pola review,
        rating pelanggan, serta perilaku
        ulasan pelanggan SPBU berdasarkan
        data Google Maps.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# SUMMARY
summary = dataset_summary(filtered_df)

positive_pct, negative_pct = sentiment_percentage(
    filtered_df
)

section_header(
    "EDA Summary",
    "Ringkasan statistik utama berdasarkan hasil filtering dashboard."
)

# KPI ROW 1
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
        "Rata-rata Rating",
        f"⭐ {summary['avg_rating']}",
        "⭐"
    )

with col4:

    metric_card(
        "Rata-rata Panjang Teks",
        f"{summary['avg_text_length']} kata",
        "📝"
    )

# KPI ROW 2
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    metric_card(
        "Sentimen Positif",
        f"{positive_pct:.2f}%",
        "🟢"
    )

with col2:

    metric_card(
        "Sentimen Negatif",
        f"{negative_pct:.2f}%",
        "🔴"
    )

success_card(
    """
    Exploratory Data Analysis membantu
    memahami pola data sebelum dilakukan
    text mining dan comparative machine
    learning modelling.
    """
)

# DISTRIBUSI SENTIMEN
section_header(
    "Distribusi Sentimen",
    "Visualisasi distribusi sentimen positif dan negatif pelanggan SPBU."
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
        use_container_width=True
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
        use_container_width=True
    )

info_card(
    sentiment_insight(sentiment_df)
)

# DISTRIBUSI RATING
section_header(
    "Distribusi Rating",
    "Visualisasi distribusi rating pelanggan terhadap layanan SPBU."
)

rating_df = (
    filtered_df["stars"]
    .value_counts()
    .sort_index()
    .reset_index()
)

rating_df.columns = [
    "Rating",
    "Jumlah"
]

fig = px.bar(
    rating_df,
    x="Rating",
    y="Jumlah",
    text="Jumlah",
    color="Jumlah",
    color_continuous_scale="YlOrRd"
)

fig.update_traces(
    textposition="outside"
)

fig.update_layout(
    template="plotly_white",
    paper_bgcolor="white",
    plot_bgcolor="white",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

info_card(
    rating_insight(rating_df)
)

# SENTIMEN PER SPBU
section_header(
    "Distribusi Sentimen per SPBU",
    "Perbandingan jumlah sentimen positif dan negatif pada setiap SPBU."
)

sentimen_spbu = pd.crosstab(
    filtered_df["title"],
    filtered_df["ket_sentiment"]
).reset_index()

fig = stacked_bar(
    sentimen_spbu,
    x="title",
    positive_col="positif",
    negative_col="negatif",
    title="Distribusi Sentimen per SPBU"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

info_card(
    """
    Distribusi sentimen per SPBU membantu
    mengidentifikasi SPBU dengan tingkat
    kepuasan maupun keluhan pelanggan tertinggi.
    """
)

# TREND REVIEW BULANAN
section_header(
    "Trend Review Bulanan",
    "Trend jumlah ulasan pelanggan berdasarkan bulan."
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
    use_container_width=True
)

info_card(
    """
    Trend review memperlihatkan aktivitas
    pelanggan dalam memberikan ulasan
    terhadap layanan SPBU dari waktu ke waktu.
    """
)

# DISTRIBUSI PANJANG TEKS
section_header(
    "Distribusi Panjang Teks",
    "Analisis distribusi jumlah kata pada ulasan pelanggan."
)

fig = histogram_chart(
    filtered_df,
    x="text_length",
    title="Distribusi Panjang Teks"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

info_card(
    """
    Distribusi panjang teks menunjukkan
    variasi jumlah kata yang digunakan
    pelanggan dalam memberikan ulasan.
    """
)

# PANJANG TEKS PER SENTIMEN
section_header(
    "Distribusi Panjang Teks per Sentimen",
    "Perbandingan panjang teks berdasarkan sentimen."
)

fig = boxplot_chart(
    filtered_df,
    x="ket_sentiment",
    y="text_length",
    title="Distribusi Panjang Teks per Sentimen"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

info_card(
    """
    Boxplot membantu melihat median,
    persebaran data, serta outlier
    panjang teks pada masing-masing sentimen.
    """
)

# PANJANG TEKS PER SPBU
section_header(
    "Distribusi Panjang Teks per SPBU",
    "Perbandingan panjang ulasan pelanggan pada masing-masing SPBU."
)

fig = px.box(
    filtered_df,
    x="title",
    y="text_length",
    color="title",
    points="outliers"
)

fig.update_layout(
    template="plotly_white",
    paper_bgcolor="white",
    plot_bgcolor="white",
    height=650,
    showlegend=False
)

fig.update_xaxes(
    tickangle=45
)

st.plotly_chart(
    fig,
    use_container_width=True
)

warning_card(
    """
    Variasi panjang teks menunjukkan
    bahwa pelanggan memberikan ulasan
    dengan tingkat detail yang berbeda-beda.
    """
)

# TOP SPBU
section_header(
    "Top SPBU Berdasarkan Jumlah Review",
    "SPBU dengan jumlah ulasan pelanggan terbanyak."
)

top_spbu_df = (
    filtered_df["title"]
    .value_counts()
    .reset_index()
)

top_spbu_df.columns = [
    "SPBU",
    "Jumlah Review"
]

top_spbu_df = top_spbu_df.head(10)

fig = px.bar(
    top_spbu_df.sort_values(
        "Jumlah Review"
    ),
    x="Jumlah Review",
    y="SPBU",
    orientation="h",
    text="Jumlah Review",
    color="Jumlah Review",
    color_continuous_scale="YlOrRd"
)

fig.update_traces(
    textposition="outside"
)

fig.update_layout(
    template="plotly_white",
    paper_bgcolor="white",
    plot_bgcolor="white",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

info_card(
    """
    SPBU dengan jumlah review tertinggi
    menunjukkan tingginya interaksi pelanggan
    terhadap layanan SPBU pada Google Maps.
    """
)

# DISTRIBUSI REVIEW PER TAHUN
section_header(
    "Distribusi Review per Tahun",
    "Distribusi jumlah ulasan pelanggan berdasarkan tahun."
)

year_df = (
    filtered_df["year"]
    .value_counts()
    .sort_index()
    .reset_index()
)

year_df.columns = [
    "Tahun",
    "Jumlah"
]

fig = px.line(
    year_df,
    x="Tahun",
    y="Jumlah",
    markers=True
)

fig.update_traces(
    line=dict(
        width=4,
        color="#DC2626"
    ),
    marker=dict(
        size=10
    )
)

fig.update_layout(
    template="plotly_white",
    paper_bgcolor="white",
    plot_bgcolor="white",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

info_card(
    """
    Distribusi review per tahun menunjukkan
    perkembangan aktivitas pelanggan
    dalam memberikan ulasan terhadap SPBU.
    """
)

# DATA PREVIEW
section_header(
    "Dataset Preview",
    "Contoh data hasil preprocessing ulasan pelanggan."
)

preview_df = filtered_df[
    [
        "title",
        "stars",
        "ket_sentiment",
        "text_length",
        "text_kalimat"
    ]
].copy()

preview_df.columns = [
    "SPBU",
    "Rating",
    "Sentimen",
    "Panjang Teks",
    "Text Preprocessing"
]

st.dataframe(
    preview_df.head(15),
    use_container_width=True
)

# FINAL INSIGHT
success_card(
    """
    Hasil Exploratory Data Analysis menunjukkan
    bahwa dataset memiliki distribusi sentimen,
    rating, dan karakteristik teks yang cukup
    beragam sehingga layak digunakan dalam
    proses text mining dan comparative
    machine learning modelling.
    """
)

# FOOTER
page_footer()