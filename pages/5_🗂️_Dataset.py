import streamlit as st
import pandas as pd


from utils.global_filter import global_filter
from utils.global_header import global_header

from utils.helper import (
    load_data,
    dataset_summary
)


from utils.cards import (

    metric_card,
    section_header,
    info_card,
    success_card,
    warning_card,
    page_footer
)

# PAGE CONFIG
st.set_page_config(
    page_title="Dataset Dashboard",
    page_icon="🗂️",
    layout="wide"
)

# LOAD CSS
with open("assets/style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# LOAD DATA
with st.spinner("Loading dataset dashboard..."):

    df = load_data()

# FILTER
if "filtered_df" not in st.session_state:

    st.session_state.filtered_df = df.copy()

filtered_df = st.session_state.filtered_df


# HEADER
st.markdown(
    """
    <div style="
        background:linear-gradient(
            135deg,
            #0F172A,
            #1E293B
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
        🗂️ Dataset Documentation
    </h1>

    <p style="
        font-size:16px;
        line-height:1.8;
        margin-bottom:0;
        color:white;
    ">
        Dokumentasi dataset hasil
        web scraping ulasan Google Maps
        pada 17 SPBU di Kota Yogyakarta
        beserta hasil preprocessing data.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# SUMMARY
summary = dataset_summary(filtered_df)

section_header(
    "Dataset Summary",
    "Ringkasan dataset berdasarkan hasil filtering dashboard."
)

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
        summary["avg_rating"],
        "⭐"
    )

with col4:

    metric_card(
        "Jumlah Kolom",
        len(filtered_df.columns),
        "🧾"
    )

# DATASET SOURCE
section_header(
    "Sumber Dataset",
    "Informasi sumber data penelitian."
)

info_card(
    """
    Dataset diperoleh melalui proses
    web scraping ulasan Google Maps
    pada 17 SPBU di Kota Yogyakarta.
    """
)

success_card(
    """
    Dataset berisi informasi review pelanggan,
    rating,
    tanggal ulasan,
    hasil preprocessing,
    dan label sentimen.
    """
)

# DATASET STRUCTURE
section_header(
    "Struktur Dataset",
    "Penjelasan setiap atribut pada dataset."
)

column_desc = pd.DataFrame({

    "Kolom": [

        "title",
        "stars",
        "year",
        "month_name",
        "ket_sentiment",
        "sentiment_label",
        "text",
        "text_kalimat"
    ],

    "Deskripsi": [

        "Nama SPBU",

        "Rating pelanggan",

        "Tahun review",

        "Nama bulan review",

        "Label sentimen",

        "Representasi numerik sentimen",

        "Text asli review",

        "Hasil preprocessing text"
    ]
})

st.dataframe(
    column_desc,
    use_container_width=True
)

# PREPROCESSING PIPELINE
section_header(
    "Preprocessing Pipeline",
    "Tahapan preprocessing text pada penelitian."
)

preprocess_df = pd.DataFrame({

    "Tahapan": [

        "Case Folding",
        "Cleaning Text",
        "Tokenization",
        "Stopword Removal",
        "Stemming",
        "Text Normalization"
    ],

    "Deskripsi": [

        "Mengubah text menjadi huruf kecil",

        "Menghapus karakter khusus dan simbol",

        "Memecah text menjadi token kata",

        "Menghapus kata tidak penting",

        "Mengubah kata menjadi bentuk dasar",

        "Menyeragamkan bentuk kata"
    ]
})

st.dataframe(
    preprocess_df,
    use_container_width=True
)

success_card(
    """
    Proses preprocessing dilakukan
    untuk meningkatkan kualitas data text
    sebelum dilakukan text mining
    dan machine learning modelling.
    """
)

# DATA PREVIEW
section_header(
    "Dataset Preview",
    "Contoh data hasil preprocessing."
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
    preview_df.head(20),
    use_container_width=True
)

# MISSING VALUE
section_header(
    "Missing Value Checking",
    "Pemeriksaan missing value pada dataset."
)

# ============================================
# MISSING VALUE CHECKING
# ============================================

missing_df = pd.DataFrame({

    "Kolom": filtered_df.columns,

    "Jumlah Missing": filtered_df.isnull().sum().values
})

# sembunyikan text_kalimat hanya di tabel
missing_df_display = missing_df[
    missing_df["Kolom"] != "text_kalimat"
]

st.dataframe(
    missing_df_display,
    use_container_width=True
)

warning_card(
    """
    Pemeriksaan missing value penting
    untuk memastikan kualitas dataset
    sebelum dilakukan proses modelling.
    """
)

# DATA TYPES
section_header(
    "Data Types",
    "Informasi tipe data setiap kolom."
)

dtype_df = pd.DataFrame({

    "Kolom":
    filtered_df.dtypes.index,

    "Data Type":
    filtered_df.dtypes.values.astype(str)
})

st.dataframe(
    dtype_df,
    use_container_width=True
)

# FINAL INSIGHT
section_header(
    "Kesimpulan Dataset",
    ""
)

success_card(
    """
    Dataset hasil preprocessing telah
    siap digunakan dalam proses
    exploratory data analysis,
    text mining,
    dan comparative machine learning.
    """
)

# FOOTER
page_footer()