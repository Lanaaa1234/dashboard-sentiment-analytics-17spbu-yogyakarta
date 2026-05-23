import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.model_selection import (
    train_test_split
)

from sklearn.naive_bayes import (
    MultinomialNB
)

from sklearn.linear_model import (
    LogisticRegression
)

from sklearn.svm import (
    LinearSVC
)

from sklearn.metrics import (
    accuracy_score,
    f1_score
)

from utils.helper import (
    load_data,
    sentiment_percentage
)

from utils.cards import (
    section_header,
    page_footer
)

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="About Dashboard",
    page_icon="ℹ️",
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
with st.spinner("Loading about dashboard..."):

    df = load_data()

df["text_kalimat"] = (
    df["text_kalimat"]
    .fillna("")
    .astype(str)
)

# =========================================================
# FILTERED DATA
# =========================================================
if "filtered_df" not in st.session_state:

    st.session_state.filtered_df = df.copy()

filtered_df = st.session_state.filtered_df

# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <div style="
        background:linear-gradient(
            135deg,
            #1E3A8A,
            #2563EB
        );
        padding:35px;
        border-radius:28px;
        margin-bottom:35px;
        color:white;
        box-shadow:0 10px 30px rgba(37,99,235,0.15);
    ">

    <h1 style="
        color:white;
        margin-bottom:12px;
        font-size:52px;
        font-weight:800;
    ">
        ℹ️ About Research
    </h1>

    <p style="
        font-size:18px;
        line-height:1.9;
        margin-bottom:0;
        color:white;
        opacity:0.95;
    ">
        Informasi penelitian, metodologi,
        kesimpulan, dan rekomendasi pengembangan
        dashboard analisis sentimen SPBU.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SENTIMENT SUMMARY
# =========================================================
positive_pct, negative_pct = sentiment_percentage(
    filtered_df
)

# =========================================================
# SIMPLE MODELLING
# =========================================================
X = filtered_df[
    "text_kalimat"
].astype(str)

y = filtered_df[
    "sentiment_label"
]

tfidf = TfidfVectorizer(
    max_features=3000
)

X_tfidf = tfidf.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(

    X_tfidf,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)

models = {

    "Naive Bayes":
    MultinomialNB(),

    "Logistic Regression":
    LogisticRegression(
        max_iter=1000
    ),

    "SVM":
    LinearSVC()
}

results = []

for name, model in models.items():

    model.fit(
        X_train,
        y_train
    )

    y_pred = model.predict(
        X_test
    )

    results.append({

        "Model":
        name,

        "Accuracy":
        accuracy_score(
            y_test,
            y_pred
        ),

        "F1-Score":
        f1_score(
            y_test,
            y_pred
        )
    })

results_df = pd.DataFrame(
    results
)

best_model = (

    results_df
    .sort_values(
        by="F1-Score",
        ascending=False
    )
    .iloc[0]
)

# =========================================================
# ABOUT RESEARCH
# =========================================================
section_header(
    "Tentang Penelitian",
    "Latar belakang dan tujuan penelitian."
)

st.markdown(
    f"""
<div style="
    background:white;
    padding:35px;
    border-radius:24px;
    box-shadow:0 6px 20px rgba(0,0,0,0.06);
    line-height:2;
    font-size:17px;
    color:#374151;
    margin-bottom:35px;
">

<h3 style="color:#111827;">
📌 Latar Belakang
</h3>

<p>
Penelitian ini membahas analisis sentimen
ulasan Google Maps pada 17 SPBU di Kota
Yogyakarta menggunakan pendekatan
Web Mining, Text Mining,
dan Comparative Machine Learning Models.
</p>

<p>
Dashboard dibangun menggunakan Streamlit
untuk membantu proses eksplorasi data,
visualisasi, dan interpretasi hasil analisis
sentimen secara interaktif.
</p>

<hr>

<h3 style="color:#111827;">
🎯 Tujuan Penelitian
</h3>

<ul>
<li>Menganalisis karakteristik dataset ulasan pelanggan SPBU.</li>
<li>Menerapkan text mining untuk analisis ulasan pelanggan.</li>
<li>Membandingkan performa machine learning klasifikasi sentimen.</li>
</ul>

<hr>

<h3 style="color:#111827;">
⚙️ Metodologi Penelitian
</h3>

<ol>
<li>Web Scraping Google Maps</li>
<li>Preprocessing Text</li>
<li>Exploratory Data Analysis</li>
<li>Text Mining dan Word Analysis</li>
<li>TF-IDF Vectorization</li>
<li>Comparative Machine Learning</li>
<li>Model Evaluation</li>
</ol>

<hr>

<h3 style="color:#111827;">
🤖 Comparative Machine Learning
</h3>

<p>
Model terbaik:
<b>{best_model['Model']}</b>
dengan F1-Score:
<b>{best_model['F1-Score']:.4f}</b>
</p>

<hr>

<h3 style="color:#111827;">
📊 Hasil Utama Penelitian
</h3>

<ul>
<li>Sentimen positif sebesar <b>{positive_pct:.2f}%</b>.</li>
<li>Dominasi pembahasan terkait pelayanan dan kualitas BBM.</li>
<li>Dashboard membantu visualisasi dan eksplorasi data secara interaktif.</li>
</ul>

</div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# CONCLUSION & DEVELOPMENT
# =========================================================
section_header(
    "Kesimpulan dan Pengembangan",
    "Kesimpulan penelitian, keterbatasan analisis, dan rekomendasi pengembangan lanjutan."
)

st.markdown(
    f"""
<div style="
    background:white;
    padding:35px;
    border-radius:24px;
    box-shadow:0 6px 20px rgba(0,0,0,0.06);
    line-height:2;
    font-size:17px;
    color:#374151;
    margin-bottom:30px;
">

<h3 style="
    color:#111827;
    margin-bottom:18px;
">
📌 Kesimpulan Penelitian
</h3>

<p>
Penelitian berhasil membangun dashboard analisis
sentimen interaktif berbasis Streamlit untuk
mengevaluasi ulasan pelanggan SPBU menggunakan
pendekatan Web Mining, Text Mining,
dan Comparative Machine Learning.
</p>

<p>
Berdasarkan hasil comparative machine learning,
model terbaik adalah
<b>{best_model['Model']}</b>
dengan F1-Score sebesar
<b>{best_model['F1-Score']:.4f}</b>.
</p>

<hr style="
    margin:28px 0;
    border:1px solid #E5E7EB;
">

<h3 style="
    color:#111827;
    margin-bottom:18px;
">
⚠️ Keterbatasan Penelitian
</h3>

<ul style="
    padding-left:22px;
    margin-top:0;
    color:#374151;
    line-height:2;
">

<li>
Dataset hanya berasal dari ulasan Google Maps
pada 17 SPBU di Kota Yogyakarta.
</li>

<li>
Analisis sentimen masih menggunakan
klasifikasi dua kelas sentimen.
</li>

<li>
Penelitian belum menggunakan pendekatan
deep learning seperti BERT atau IndoBERT.
</li>

</ul>

<hr style="
    margin:28px 0;
    border:1px solid #E5E7EB;
">

<h3 style="
    color:#111827;
    margin-bottom:18px;
">
🚀 Saran Pengembangan
</h3>


<ul style="
    padding-left:22px;
    margin-top:0;
    color:#374151;
    line-height:2;
">

<li>
Pengembangan model deep learning seperti
LSTM, BERT, dan IndoBERT untuk meningkatkan
performa klasifikasi sentimen.
</li>

<li>
Dashboard dapat dikembangkan menjadi
sistem monitoring sentimen pelanggan
berbasis real-time analytics.
</li>

<li>
Penggunaan dataset yang lebih besar
dan lebih beragam dari berbagai platform digital.
</li>

</ul>

</div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# FOOTER
# =========================================================
page_footer()