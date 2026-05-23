import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.global_filter import global_filter
from utils.global_header import global_header


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

from sklearn.metrics import (

    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_curve,
    auc,
    classification_report
)

from utils.helper import (
    load_data
)


from utils.cards import (

    metric_card,
    section_header,
    info_card,
    success_card,
    warning_card,
    page_footer
)

from utils.charts import (
    heatmap_chart,
    roc_curve_layout
)

from utils.insights import (
    model_insight,
    confusion_matrix_insight,
    roc_insight,
    actual_prediction_insight,
    final_model_insight
)

# PAGE CONFIG
st.set_page_config(
    page_title="Comparative ML Dashboard",
    page_icon="🤖",
    layout="wide"
)

# LOAD CSS
with open("assets/style.css") as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# LOAD DATA
with st.spinner("Loading modelling dashboard..."):

    df = load_data()

df["text_kalimat"] = (
    df["text_kalimat"]
    .fillna("")
    .astype(str)
)

if "filtered_df" not in st.session_state:

    st.session_state.filtered_df = df.copy()

filtered_df = st.session_state.filtered_df

# HEADER
st.markdown(
    """
    <div style="
        background:linear-gradient(
            135deg,
            #059669,
            #10B981
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
        🤖 Comparative Machine Learning
    </h1>

    <p style="
        font-size:16px;
        line-height:1.8;
        margin-bottom:0;
        color:white;
    ">
        Comparative machine learning dilakukan
        untuk membandingkan performa model
        klasifikasi sentimen menggunakan
        Naive Bayes, Logistic Regression,
        dan Support Vector Machine.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# DATA PREPARATION
section_header(
    "Machine Learning Pipeline",
    "Tahapan preprocessing dan modelling machine learning."
)

col1, col2, col3 = st.columns(3)

with col1:

    metric_card(
        "Total Dataset",
        f"{len(filtered_df):,}",
        "📊"
    )

with col2:

    metric_card(
        "Jumlah Fitur TF-IDF",
        "3000",
        "🧠"
    )

with col3:

    metric_card(
        "Jumlah Model",
        "3",
        "🤖"
    )

# PREPARE DATA
X = (
    filtered_df["text_kalimat"]
    .fillna("")
    .astype(str)
)

y = filtered_df[
    "sentiment_label"
]

# TF-IDF
tfidf = TfidfVectorizer(
    max_features=3000
)

X_tfidf = tfidf.fit_transform(X)

# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(

    X_tfidf,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)

success_card(
    """
    Dataset telah melalui proses
    TF-IDF vectorization dan pembagian
    data train-test sebelum dilakukan
    proses modelling machine learning.
    """
)

# DISTRIBUSI LABEL
section_header(
    "Distribusi Label Train-Test",
    "Distribusi label sentimen pada data train dan test."
)

train_count = (
    y_train
    .value_counts()
    .reset_index()
)

train_count.columns = [
    "Label",
    "Jumlah"
]

test_count = (
    y_test
    .value_counts()
    .reset_index()
)

test_count.columns = [
    "Label",
    "Jumlah"
]

col1, col2 = st.columns(2)

# TRAIN
with col1:

    fig = px.bar(
        train_count,
        x="Label",
        y="Jumlah",
        text="Jumlah",
        color="Jumlah",
        color_continuous_scale="Greens"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        title="Distribusi Label Train",
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# TEST
with col2:

    fig = px.bar(
        test_count,
        x="Label",
        y="Jumlah",
        text="Jumlah",
        color="Jumlah",
        color_continuous_scale="Reds"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        title="Distribusi Label Test",
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# MODELS
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

# TRAINING
results = []

predictions = {}

for name, model in models.items():

    model.fit(
        X_train,
        y_train
    )

    y_pred = model.predict(
        X_test
    )

    predictions[name] = y_pred

    results.append({

        "Model":
        name,

        "Accuracy":
        accuracy_score(
            y_test,
            y_pred
        ),

        "Precision":
        precision_score(
            y_test,
            y_pred
        ),

        "Recall":
        recall_score(
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

# BEST MODEL
best_model = (

    results_df
    .sort_values(
        by="F1-Score",
        ascending=False
    )
    .iloc[0]
)

# SUMMARY
section_header(
    "Model Evaluation Summary",
    "Ringkasan performa comparative machine learning."
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    metric_card(
        "Best Model",
        best_model["Model"],
        "🏆"
    )

with col2:

    metric_card(
        "Accuracy",
        f"{best_model['Accuracy']:.4f}",
        "🎯"
    )

with col3:

    metric_card(
        "Precision",
        f"{best_model['Precision']:.4f}",
        "📌"
    )

with col4:

    metric_card(
        "F1-Score",
        f"{best_model['F1-Score']:.4f}",
        "📈"
    )

success_card(
    model_insight(results_df)
)

# EVALUATION TABLE
section_header(
    "Evaluation Metric Table",
    "Perbandingan metric evaluasi antar model machine learning."
)

styled_df = results_df.style.format({

    "Accuracy":
    "{:.4f}",

    "Precision":
    "{:.4f}",

    "Recall":
    "{:.4f}",

    "F1-Score":
    "{:.4f}"
})

st.dataframe(
    styled_df,
    use_container_width=True
)

# METRIC COMPARISON
section_header(
    "Metric Comparison",
    "Visualisasi perbandingan metric evaluasi model."
)

results_melt = results_df.melt(

    id_vars="Model",

    var_name="Metric",

    value_name="Score"
)

fig = px.bar(

    results_melt,

    x="Metric",

    y="Score",

    color="Model",

    barmode="group",

    text="Score",

    color_discrete_sequence=[
        "#DC2626",
        "#FACC15",
        "#16A34A"
    ]
)

fig.update_traces(
    texttemplate="%{text:.4f}",
    textposition="outside"
)

fig.update_layout(

    template="plotly_white",

    paper_bgcolor="white",

    plot_bgcolor="white",

    height=550,

    yaxis_range=[0, 1.1]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

info_card(
    """
    Perbandingan metric menunjukkan
    kemampuan masing-masing model
    dalam melakukan klasifikasi sentimen.
    """
)

# CONFUSION MATRIX
section_header(
    "Confusion Matrix",
    "Visualisasi confusion matrix untuk masing-masing model."
)

tabs = st.tabs(
    list(models.keys())
)

for idx, model_name in enumerate(models.keys()):

    with tabs[idx]:

        cm = confusion_matrix(
            y_test,
            predictions[model_name]
        )

        fig = heatmap_chart(
            cm,
            f"Confusion Matrix - {model_name}"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        info_card(
            confusion_matrix_insight(
                model_name
            )
        )

# ROC CURVE
section_header(
    "ROC Curve Comparison",
    "Perbandingan ROC Curve antar model machine learning."
)

fig = go.Figure()

colors = {

    "Naive Bayes":
    "#DC2626",

    "Logistic Regression":
    "#FACC15",

    "SVM":
    "#16A34A"
}

for name, model in models.items():

    if hasattr(
        model,
        "predict_proba"
    ):

        y_score = model.predict_proba(
            X_test
        )[:, 1]

    else:

        y_score = model.decision_function(
            X_test
        )

    fpr, tpr, _ = roc_curve(
        y_test,
        y_score
    )

    roc_auc = auc(
        fpr,
        tpr
    )

    fig.add_trace(

        go.Scatter(

            x=fpr,

            y=tpr,

            mode="lines",

            name=f"{name} (AUC={roc_auc:.4f})",

            line=dict(
                width=4,
                color=colors[name]
            )
        )
    )

# RANDOM LINE
fig.add_trace(

    go.Scatter(

        x=[0, 1],

        y=[0, 1],

        mode="lines",

        line=dict(
            dash="dash",
            color="gray"
        ),

        showlegend=False
    )
)

fig = roc_curve_layout(fig)

st.plotly_chart(
    fig,
    use_container_width=True
)

info_card(
    roc_insight()
)

# CLASSIFICATION REPORT
section_header(
    "Classification Report",
    "Detail classification report untuk masing-masing model."
)

for name in models.keys():

    with st.expander(
        f"Classification Report - {name}"
    ):

        report = classification_report(

            y_test,

            predictions[name],

            output_dict=True
        )

        report_df = pd.DataFrame(
            report
        ).transpose()

        st.dataframe(
            report_df,
            use_container_width=True
        )

# ACTUAL VS PREDICTION
section_header(
    "Actual vs Prediction",
    "Perbandingan label aktual dan hasil prediksi model terbaik."
)

comparison_df = pd.DataFrame({

    "Actual":
    y_test.values
})

for name in models.keys():

    comparison_df[name] = predictions[name]

sample_df = comparison_df.head(40).copy()

sample_df["Index"] = range(
    1,
    len(sample_df) + 1
)

fig = go.Figure()

# ACTUAL
fig.add_trace(

    go.Scatter(

        x=sample_df["Index"],

        y=sample_df["Actual"],

        mode="lines+markers",

        name="Actual",

        line=dict(
            width=4,
            color="#111827"
        )
    )
)

# PREDICTION
fig.add_trace(

    go.Scatter(

        x=sample_df["Index"],

        y=sample_df[
            best_model["Model"]
        ],

        mode="lines+markers",

        name=best_model["Model"],

        line=dict(
            width=4,
            dash="dot",
            color="#16A34A"
        )
    )
)

fig.update_layout(

    template="plotly_white",

    paper_bgcolor="white",

    plot_bgcolor="white",

    height=600,

    yaxis=dict(

        tickmode="array",

        tickvals=[0, 1],

        ticktext=[
            "Negatif",
            "Positif"
        ]
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

warning_card(
    actual_prediction_insight()
)

# FINAL INSIGHT

success_card(
    final_model_insight(
        best_model["Model"]
    )
)

# FOOTER
page_footer()