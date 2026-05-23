import plotly.express as px
import plotly.graph_objects as go

POSITIVE_COLOR = "#16A34A"
NEGATIVE_COLOR = "#DC2626"
NEUTRAL_COLOR = "#FACC15"

# DONUT CHART
def donut_chart(df, names, values, title):

    fig = px.pie(

        df,

        names=names,

        values=values,

        hole=0.6,

        color=names,

        color_discrete_map={

            "positif": POSITIVE_COLOR,
            "negatif": NEGATIVE_COLOR
        }
    )

    fig.update_traces(

        textposition="inside",

        textinfo="percent+label",

        marker=dict(
            line=dict(
                color="white",
                width=2
            )
        )
    )

    fig.update_layout(

        title=title,

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=500
    )

    return fig

# VERTICAL BAR
def vertical_bar(df, x, y, title):

    fig = px.bar(

        df,

        x=x,

        y=y,

        text=y,

        color=x,

        color_discrete_map={

            "positif": POSITIVE_COLOR,
            "negatif": NEGATIVE_COLOR
        }
    )

    fig.update_traces(

        textposition="inside",

        textfont=dict(
            color="white",
            size=14
        )
    )

    fig.update_layout(

        title=title,

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=500,

        showlegend=False
    )

    return fig

# HORIZONTAL BAR
def horizontal_bar(df, x, y, title):

    fig = px.bar(

        df,

        x=x,

        y=y,

        orientation="h",

        text=x,

        color=x,

        color_continuous_scale="YlOrRd"
    )

    fig.update_traces(

        textposition="inside",

        textfont=dict(
            color="white",
            size=12
        )
    )

    fig.update_layout(

        title=title,

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=550
    )

    return fig

# STACKED BAR
def stacked_bar(
    df,
    x,
    positive_col,
    negative_col,
    title
):

    fig = go.Figure()

    # NEGATIVE
    fig.add_trace(

        go.Bar(

            x=df[x],

            y=df[negative_col],

            name="Negatif",

            marker_color=NEGATIVE_COLOR,

            text=df[negative_col],

            textposition="inside"
        )
    )

    # POSITIVE
    fig.add_trace(

        go.Bar(

            x=df[x],

            y=df[positive_col],

            name="Positif",

            marker_color=POSITIVE_COLOR,

            text=df[positive_col],

            textposition="inside"
        )
    )

    fig.update_layout(

        barmode="stack",

        title=title,

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=650
    )

    fig.update_xaxes(
        tickangle=45
    )

    return fig

# LINE CHART
def line_chart(df, x, y, title):

    fig = px.line(

        df,

        x=x,

        y=y,

        markers=True
    )

    fig.update_traces(

        line=dict(
            width=4,
            color="#DC2626"
        ),

        marker=dict(
            size=10
        ),

        text=df[y],

        textposition="top center"
    )

    fig.update_layout(

        title=title,

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=500
    )

    return fig

# HISTOGRAM
def histogram_chart(df, x, title):

    fig = px.histogram(

        df,

        x=x,

        nbins=40,

        text_auto=True,

        color_discrete_sequence=[
            NEUTRAL_COLOR
        ]
    )

    fig.update_layout(

        title=title,

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=500
    )

    return fig

# BOXPLOT
def boxplot_chart(df, x, y, title):

    fig = px.box(

        df,

        x=x,

        y=y,

        color=x,

        color_discrete_map={

            "positif": POSITIVE_COLOR,
            "negatif": NEGATIVE_COLOR
        }
    )

    fig.update_layout(

        title=title,

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=500
    )

    return fig

# HEATMAP
def heatmap_chart(cm, title):

    fig = go.Figure(

        data=go.Heatmap(

            z=cm,

            x=["Negatif", "Positif"],

            y=["Negatif", "Positif"],

            text=cm,

            texttemplate="%{text}",

            colorscale=[

                [0.0, "#DC2626"],
                [0.5, "#FACC15"],
                [1.0, "#16A34A"]
            ]
        )
    )

    fig.update_layout(

        title=title,

        template="plotly_white",

        height=500
    )

    return fig

# ROC CURVE LAYOUT
def roc_curve_layout(fig):

    fig.update_layout(

        title="ROC Curve Comparison",

        xaxis_title="False Positive Rate",

        yaxis_title="True Positive Rate",

        template="plotly_white",

        paper_bgcolor="white",

        plot_bgcolor="white",

        height=550
    )

    return fig