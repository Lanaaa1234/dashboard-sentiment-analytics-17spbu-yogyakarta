import pandas as pd
import joblib

from sklearn.model_selection import (
    train_test_split
)

from sklearn.feature_extraction.text import (
    TfidfVectorizer
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

# LOAD DATA
df = pd.read_csv(
    "dataset_spbu_preprocessing.csv"
)

# FEATURE
X = df[
    "text_kalimat"
].astype(str)

# LABEL
y = df[
    "sentiment_label"
]

# TF-IDF
tfidf = TfidfVectorizer(
    max_features=3000
)

X_tfidf = tfidf.fit_transform(X)

# SPLIT
X_train, X_test, y_train, y_test = train_test_split(

    X_tfidf,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)

# MODELS
naive_bayes = MultinomialNB()

logistic_regression = LogisticRegression(
    max_iter=1000
)

svm = LinearSVC()

# TRAIN
naive_bayes.fit(
    X_train,
    y_train
)

logistic_regression.fit(
    X_train,
    y_train
)

svm.fit(
    X_train,
    y_train
)

# SAVE MODEL
joblib.dump(
    naive_bayes,
    "models/naive_bayes.pkl"
)

joblib.dump(
    logistic_regression,
    "models/logistic_regression.pkl"
)

joblib.dump(
    svm,
    "models/svm.pkl"
)

joblib.dump(
    tfidf,
    "models/tfidf_vectorizer.pkl"
)

print("Model berhasil disimpan.")