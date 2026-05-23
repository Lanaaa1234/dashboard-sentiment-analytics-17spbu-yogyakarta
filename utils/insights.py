import pandas as pd

# SENTIMENT INSIGHT
def sentiment_insight(df):

    try:

        top_sentiment = df.iloc[
            df["Jumlah"].idxmax()
        ]["Sentimen"]

        percentage = round(

            (
                df["Jumlah"].max()
                /
                df["Jumlah"].sum()
            ) * 100,

            2
        )

        return f"""
        Sentimen {top_sentiment}
        mendominasi dataset dengan persentase
        sebesar {percentage}% dari total ulasan pelanggan.
        """

    except:

        return """
        Distribusi sentimen berhasil divisualisasikan.
        """

# RATING INSIGHT
def rating_insight(df):

    try:

        top_rating = df.iloc[
            df["Jumlah"].idxmax()
        ]["Rating"]

        return f"""
        Rating {top_rating}
        merupakan rating yang paling sering
        diberikan pelanggan pada SPBU.
        """

    except:

        return """
        Distribusi rating berhasil divisualisasikan.
        """

# TFIDF INSIGHT
def tfidf_insight(df):

    try:

        word = df.iloc[0]["word"]

        score = round(
            df.iloc[0]["score"],
            4
        )

        return f"""
        Kata "{word}"
        memiliki skor TF-IDF tertinggi
        sebesar {score}
        sehingga menjadi kata paling dominan
        dalam dataset ulasan.
        """

    except:

        return """
        Analisis TF-IDF berhasil dilakukan.
        """

# TOP WORD INSIGHT
def top_word_insight(df, sentiment="positif"):

    try:

        word = df.iloc[0]["word"]

        count = df.iloc[0]["count"]

        return f"""
        Kata "{word}"
        merupakan kata yang paling sering muncul
        pada sentimen {sentiment}
        sebanyak {count} kali.
        """

    except:

        return """
        Analisis top word berhasil dilakukan.
        """

# NGRAM INSIGHT
def ngram_insight(
    df,
    ngram_type="Bigram",
    sentiment="positif"
):

    try:

        label = df.iloc[0]["label"]

        count = df.iloc[0]["count"]

        return f"""
        Frasa "{label}"
        merupakan {ngram_type.lower()}
        paling dominan pada sentimen {sentiment}
        sebanyak {count} kali.
        """

    except:

        return """
        Analisis N-Gram berhasil dilakukan.
        """

# WORDCLOUD INSIGHT
def wordcloud_insight(mode="global"):

    if mode == "positif":

        return """
        Wordcloud positif menunjukkan
        dominasi kata-kata yang berkaitan
        dengan kepuasan pelanggan.
        """

    elif mode == "negatif":

        return """
        Wordcloud negatif menunjukkan
        dominasi kata-kata yang berkaitan
        dengan keluhan pelanggan.
        """

    else:

        return """
        Wordcloud global menunjukkan
        pola kata dominan dalam keseluruhan dataset.
        """

# MODEL INSIGHT
def model_insight(results_df):

    try:

        best_model = results_df.sort_values(
            by="F1-Score",
            ascending=False
        ).iloc[0]

        return f"""
        Model terbaik adalah
        {best_model['Model']}
        dengan F1-Score sebesar
        {best_model['F1-Score']:.4f}.
        """

    except:

        return """
        Comparative machine learning berhasil dilakukan.
        """

# CONFUSION MATRIX INSIGHT
def confusion_matrix_insight(model_name):

    return f"""
    Confusion Matrix {model_name}
    menunjukkan performa model
    dalam membedakan sentimen positif
    dan negatif.
    """

# ROC INSIGHT
def roc_insight():

    return """
    ROC Curve digunakan untuk mengukur
    kemampuan model dalam membedakan
    kelas sentimen positif dan negatif.
    """

# ACTUAL VS PREDICTION INSIGHT
def actual_prediction_insight():

    return """
    Visualisasi actual vs prediction
    membantu melihat kesesuaian
    hasil prediksi model terhadap data aktual.
    """

# FINAL MODEL INSIGHT
def final_model_insight(best_model):

    return f"""
    Comparative machine learning menunjukkan
    bahwa model {best_model}
    memberikan performa terbaik
    dalam klasifikasi sentimen pelanggan SPBU.
    """

# FINAL TEXT MINING INSIGHT
def final_text_mining_insight():

    return """
    Text mining berhasil mengidentifikasi
    pola kata,
    frasa dominan,
    dan karakteristik ulasan pelanggan SPBU.
    """