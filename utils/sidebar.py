import streamlit as st

# SIDEBAR NAVIGATION
def sidebar_navigation():

    with st.sidebar:

        st.markdown(
            """
            <div style="
                padding-top:20px;
                padding-bottom:30px;
            ">

            <h1 style="
                color:#DC2626;
                font-size:34px;
                font-weight:800;
                margin-bottom:0;
            ">
                ⛽
            </h1>

            <h2 style="
                color:#DC2626;
                margin-top:10px;
                margin-bottom:0;
            ">
                SPBU Dashboard
            </h2>

            <p style="
                color:#6B7280;
                font-size:14px;
            ">
                Sentiment Analytics Dashboard
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.markdown(
            """
            <p style="
                color:#111827;
                font-weight:700;
                font-size:16px;
            ">
                Navigation
            </p>
            """,
            unsafe_allow_html=True
        )