import streamlit as st

# GLOBAL PROJECT HEADER
def project_header():

    st.markdown(
        """
        <div class="project-header">

        <div>

        <h1>
            ⛽ SPBU Sentiment Analytics Dashboard
        </h1>

        <p>
            Analisis Sentimen Ulasan Google Maps
            pada 17 SPBU di Kota Yogyakarta
            menggunakan Web Mining,
            Text Mining,
            dan Comparative Machine Learning Models.
        </p>

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )