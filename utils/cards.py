import streamlit as st

# SECTION HEADER
def section_header(title, description=""):

    st.markdown(
        f"""
        <div style="margin-top:10px;margin-bottom:15px;">

        <h1 style="
            font-size:42px;
            font-weight:800;
            color:#111827;
            margin-bottom:5px;
        ">
            {title}
        </h1>

        <p style="
            color:#6B7280;
            font-size:16px;
            margin-top:0;
        ">
            {description}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# METRIC CARD
def metric_card(title, value, icon="📊"):

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:28px;
            border-radius:22px;
            border:1px solid #E5E7EB;
            box-shadow:0 4px 12px rgba(0,0,0,0.04);
            margin-bottom:15px;
        ">

        <div style="
            display:flex;
            align-items:center;
            gap:10px;
            margin-bottom:18px;
        ">

        <span style="font-size:24px;">
            {icon}
        </span>

        <span style="
            color:#6B7280;
            font-size:15px;
            font-weight:600;
        ">
            {title}
        </span>

        </div>

        <h1 style="
            color:#111827;
            margin:0;
            font-size:46px;
            font-weight:800;
        ">
            {value}
        </h1>

        </div>
        """,
        unsafe_allow_html=True
    )

# INFO CARD
def info_card(text):

    html = f"""
    <div style="
        background:#EFF6FF;
        border:1px solid #BFDBFE;
        padding:20px;
        border-radius:18px;
        margin-top:10px;
        margin-bottom:25px;
    ">

    <div style="
        color:#1D4ED8;
        line-height:1.8;
        font-size:15px;
    ">
        ℹ️ {text}
    </div>

    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True
    )

# SUCCESS CARD
def success_card(text):

    html = f"""
    <div style="
        background:#F0FDF4;
        border:1px solid #BBF7D0;
        padding:20px;
        border-radius:18px;
        margin-top:10px;
        margin-bottom:25px;
    ">

    <div style="
        color:#166534;
        line-height:1.8;
        font-size:15px;
    ">
        ✅ {text}
    </div>

    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True
    )

# WARNING CARD
def warning_card(text):

    html = f"""
    <div style="
        background:#FEF2F2;
        border:1px solid #FECACA;
        padding:20px;
        border-radius:18px;
        margin-top:10px;
        margin-bottom:25px;
    ">

    <div style="
        color:#991B1B;
        line-height:1.8;
        font-size:15px;
    ">
        ⚠️ {text}
    </div>

    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True
    )

# FOOTER
def page_footer():

    st.markdown(
        """
        <div style="
            margin-top:60px;
            padding:25px;
            text-align:center;
            color:#6B7280;
            font-size:14px;
            border-top:1px solid #E5E7EB;
        ">

        SPBU Sentiment Analytics Dashboard
        
        © 2026 Maulana Diki Wicaksono & Muhammad Irvan

        </div>
        """,
        unsafe_allow_html=True
    )