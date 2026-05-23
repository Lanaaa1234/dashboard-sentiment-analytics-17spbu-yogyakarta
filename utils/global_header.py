import streamlit as st

def global_header():

    st.html(
        """
        <div class="global-header">

            <h1>
                ⛽ SPBU Sentiment Analytics Dashboard
            </h1>

            <p>
                Analisis Sentimen Ulasan Google Maps
                pada 17 SPBU di Kota Yogyakarta
                menggunakan Web Mining,
                Text Mining,
                dan Comparative Machine Learning.
            </p>

        </div>
        """
    )