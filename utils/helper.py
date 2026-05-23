
# IMPORT LIBRARY


import pandas as pd
import streamlit as st


# LOAD DATA


@st.cache_data(show_spinner=False)

def load_data():

    df = pd.read_csv(
        "dataset_spbu_preprocessing.csv"
    )

    return df


# FILTER DATA


def filter_data(
    df,
    selected_year,
    selected_spbu
):

    filtered_df = df.copy()

    # FILTER YEAR
    if selected_year != "Semua Tahun":

        filtered_df = filtered_df[
            filtered_df["year"] == selected_year
        ]

    # FILTER SPBU
    if selected_spbu:

        filtered_df = filtered_df[
            filtered_df["title"].isin(selected_spbu)
        ]

    return filtered_df


# TEXT LENGTH


def add_text_length(df):

    df["text_length"] = (
        df["text_kalimat"]
        .fillna("")
        .astype(str)
        .apply(
            lambda x: len(x.split())
        )
    )

    return df


# SENTIMENT PERCENTAGE


def sentiment_percentage(df):

    positive_pct = (
        (
            df["ket_sentiment"] == "positif"
        ).mean() * 100
    )

    negative_pct = (
        (
            df["ket_sentiment"] == "negatif"
        ).mean() * 100
    )

    return positive_pct, negative_pct


# TOP WORDS


from collections import Counter

def get_top_words(
    text_series,
    top_n=10
):

    words = (
        " ".join(
            text_series.astype(str)
        )
        .split()
    )

    counter = Counter(words)

    top_words = counter.most_common(top_n)

    top_words_df = pd.DataFrame(
        top_words,
        columns=[
            "word",
            "count"
        ]
    )

    return top_words_df


# NGRAM FUNCTION
from nltk.util import ngrams

def get_top_ngram(
    text_series,
    n=2,
    top_k=10
):

    all_ngrams = []

    for text in text_series:

        tokens = str(text).split()

        generated = list(
            ngrams(tokens, n)
        )

        all_ngrams.extend(
            generated
        )

    result = Counter(
        all_ngrams
    ).most_common(top_k)

    result_df = pd.DataFrame(
        result,
        columns=[
            "ngram",
            "count"
        ]
    )

    result_df["label"] = result_df[
        "ngram"
    ].apply(
        lambda x:
        " ".join(x)
    )

    return result_df


# DATASET SUMMARY


def dataset_summary(df):

    summary = {

        "total_review":
        len(df),

        "total_spbu":
        df["title"].nunique(),

        "avg_rating":
        round(
            df["stars"].mean(),
            2
        ),

        "avg_text_length":
        round(
            df["text_kalimat"]
            .fillna("")
            .astype(str)
            .apply(
                lambda x: len(x.split())
            )
            .mean(),
            2
        )
    }

    return summary


# TOP SPBU


def top_spbu(df):

    result = (
        df["title"]
        .value_counts()
        .reset_index()
    )

    result.columns = [
        "SPBU",
        "Jumlah Review"
    ]

    return result


# SENTIMENT DISTRIBUTION


def sentiment_distribution(df):

    result = (
        df["ket_sentiment"]
        .value_counts()
        .reset_index()
    )

    result.columns = [
        "Sentimen",
        "Jumlah"
    ]

    return result


# MONTH ORDER


def month_order():

    return [

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


# TREND DATA


def trend_data(df):

    trend_df = (
        df.groupby("month_name")
        .size()
        .reset_index(name="Jumlah")
    )

    trend_df["month_name"] = pd.Categorical(
        trend_df["month_name"],
        categories=month_order(),
        ordered=True
    )

    trend_df = trend_df.sort_values(
        "month_name"
    )

    return trend_df


# MODEL COLOR


def model_colors():

    return {

        "Naive Bayes":
        "#DC2626",

        "Logistic Regression":
        "#FACC15",

        "SVM":
        "#16A34A"
    }


# SENTIMENT COLOR


def sentiment_colors():

    return {

        "positif":
        "#16A34A",

        "negatif":
        "#DC2626"
    }