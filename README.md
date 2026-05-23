# ⛽ SPBU Sentiment Analytics Dashboard

Dashboard interaktif berbasis **Streamlit** untuk analisis sentimen ulasan Google Maps pada 17 SPBU di Kota Yogyakarta menggunakan pendekatan **Web Mining**, **Text Mining**, dan **Comparative Machine Learning Models**.

Dashboard ini dirancang untuk membantu eksplorasi data, visualisasi sentimen pelanggan, serta perbandingan performa model machine learning secara interaktif dan modern.

---

## 📌 Deskripsi Project

Project ini dikembangkan untuk membantu proses:

- Web scraping ulasan pelanggan dari Google Maps
- Exploratory Data Analysis (EDA)
- Text preprocessing dan text mining
- Analisis sentimen pelanggan SPBU
- Visualisasi data interaktif
- Comparative machine learning models
- Evaluasi performa model klasifikasi sentimen

Dashboard dibangun menggunakan framework **Streamlit** dengan tampilan modern dan interaktif sehingga pengguna dapat mengeksplorasi data secara real-time melalui berbagai halaman analisis.

---

## 🎯 Tujuan Penelitian

Project ini dibuat untuk:

- Menganalisis karakteristik dataset ulasan pelanggan SPBU
- Menerapkan preprocessing dan text mining pada data ulasan
- Melakukan exploratory data analysis (EDA)
- Membandingkan performa beberapa model machine learning
- Menyajikan hasil analisis dalam dashboard interaktif berbasis visual analytics
- Membantu memahami persepsi pelanggan terhadap layanan SPBU di Kota Yogyakarta

---

## 🚀 Live Dashboard

🌐 Streamlit App:  
https://dashboard-sentiment-analytics-17spbu-yogyakarta.streamlit.app

---

## 🛠️ Tools & Libraries

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-Learn
- Matplotlib
- WordCloud
- Sastrawi
- NLTK

---

## 🚀 Fitur Dashboard

### 🏠 Dashboard Utama
- Ringkasan dataset ulasan SPBU
- Statistik sentimen pelanggan
- Informasi distribusi rating
- Insight hasil analisis

### 📈 Exploratory Data Analysis (EDA)
- Distribusi sentimen
- Distribusi rating pelanggan
- Analisis panjang teks ulasan
- Visualisasi tren ulasan
- Word frequency analysis
- WordCloud positif & negatif

### 🤖 Comparative Machine Learning Models
- Perbandingan beberapa algoritma machine learning
- Evaluasi akurasi model
- Precision, Recall, dan F1-Score
- Confusion Matrix
- Visualisasi performa model

### 📁 Dataset Exploration
- Menampilkan dataset hasil scraping
- Filtering data secara interaktif
- Eksplorasi preprocessing text

### ℹ️ About Project
- Informasi penelitian
- Metodologi penelitian
- Penjelasan dashboard
- Author & contact

---

## 📄 Dataset

Dataset berasal dari hasil **web scraping ulasan Google Maps** pada 17 SPBU di Kota Yogyakarta.

Dataset mencakup:

- Nama SPBU
- Rating pelanggan
- Tanggal review
- Text review
- Hasil preprocessing
- Label sentimen
- Tokenization
- Stemming
- Stopword removal

---

## ⚙️ Metodologi Analisis

Tahapan analisis pada project ini meliputi:

### 1️⃣ Web Mining
- Scraping ulasan Google Maps
- Pengumpulan data pelanggan SPBU

### 2️⃣ Text Preprocessing
- Case folding
- Cleansing
- Tokenization
- Stopword removal
- Stemming

### 3️⃣ Exploratory Data Analysis
- Analisis distribusi data
- Visualisasi statistik
- Analisis kata dominan

### 4️⃣ Sentiment Analysis
- Labeling sentimen
- Feature extraction
- TF-IDF Vectorization

### 5️⃣ Comparative Machine Learning
Perbandingan beberapa algoritma seperti:

- Naive Bayes
- Support Vector Machine (SVM)
- Random Forest
- Logistic Regression
- K-Nearest Neighbor (KNN)

---

## ⚙️ Instalasi & Menjalankan Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Lanaaa1234/SPBU-Sentiment-Dashboard.git
```

### 2️⃣ Masuk ke Folder Project

```bash
cd SPBU-Sentiment-Dashboard
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Jalankan Streamlit

```bash
streamlit run SPBU_Dashboard.py
```

---

## 📂 Struktur Project

```bash
SPBU-SENTIMENT-DASHBOARD/
│
├── assets/
│   └── style.css
│
├── dataset/
│   └── dataset_spbu.csv
│
├── pages/
│   ├── 1_📈_EDA.py
│   ├── 2_🤖_Modelling.py
│   ├── 3_📁_Dataset.py
│   └── 4_ℹ️_About.py
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
```

---

## 📊 Output Analisis

Dashboard menghasilkan berbagai insight analisis seperti:

- Distribusi sentimen pelanggan SPBU
- SPBU dengan rating tertinggi dan terendah
- Kata dominan pada ulasan pelanggan
- Perbandingan performa model machine learning
- Visualisasi data interaktif berbasis dashboard

---

## 👨‍💻 Author & Contact

- **Nama** : Maulana Diki Wicaksono  
- **Email** : maulanadiki963@gmail.com  
- **GitHub** : https://github.com/Lanaaa1234  
- **LinkedIn** : https://www.linkedin.com/in/maulana-diki-wicaksono/  
- **Instagram** : https://www.instagram.com/maulanadikii_24/

---

## 📜 License

Project ini dibuat untuk kebutuhan penelitian, pembelajaran, dan pengembangan analisis data berbasis dashboard interaktif menggunakan Streamlit.
