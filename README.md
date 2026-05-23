# ⛽ SPBU Sentiment Analytics Dashboard

Dashboard interaktif berbasis Streamlit untuk analisis sentimen ulasan Google Maps pada 17 SPBU di Kota Yogyakarta menggunakan pendekatan Web Mining, Text Mining, dan Comparative Machine Learning Models.

---

# 📌 Deskripsi Project

Project ini dikembangkan untuk membantu proses eksplorasi data, visualisasi analisis sentimen, text mining, dan comparative machine learning terhadap ulasan pelanggan SPBU yang diperoleh dari Google Maps.

Dashboard dirancang secara interaktif dan modern menggunakan Streamlit sehingga pengguna dapat melakukan eksplorasi data secara real-time melalui berbagai halaman analisis.

---

# 🎯 Tujuan Penelitian

- Menganalisis karakteristik dataset ulasan pelanggan SPBU.
- Menerapkan preprocessing dan text mining pada data ulasan.
- Melakukan exploratory data analysis (EDA).
- Membandingkan performa beberapa model machine learning.
- Menyajikan hasil analisis dalam dashboard interaktif berbasis visual analytics.

---

# 🛠️ Tools yang Digunakan

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-Learn
- Matplotlib
- WordCloud

---


# 🌐 Deployment
Dashboard dapat dideploy menggunakan:
- Streamlit Community Cloud
- GitHub Integration

# 📄 Dataset
Dataset berasal dari hasil web scraping ulasan Google Maps pada 17 SPBU di Kota Yogyakarta.

Dataset mencakup:
- Nama SPBU
- Rating pelanggan
- Tanggal review
- Text review
- Hasil preprocessing
- Label sentimen


# 📂 Struktur Project
SPBU-SENTIMENT-DASHBOARD/
│
├── assets/
│   └── style.css
│
├── dataset/
│   └── dataset_spbu.csv
│
├── pages/
│   ├── 1_📊_Overview.py
│   ├── 2_📈_EDA.py
│   ├── 3_🧠_Text_Mining.py
│   ├── 4_🤖_Modelling.py
│   ├── 5_📁_Dataset.py
│   └── 6_ℹ️_About.py
│
├── utils/
│   ├── helper.py
│   ├── charts.py
│   ├── cards.py
│   ├── insights.py
│   ├── global_filter.py
│   └── global_header.py
│
├── SPBU_Dashboard.py
├── requirements.txt
├── README.md
└── .gitignore

# 👨‍💻 Authors
© 2026
Maulana Diki Wicaksono