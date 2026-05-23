import streamlit as st

# GLOBAL TOPBAR FILTER
def topbar_filter(df):

    st.markdown(
        """
        <div class="topbar-container">
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1.2, 2.5, 1])

    # YEAR RANGE
    with col1:

        min_year = int(df["year"].min())
        max_year = int(df["year"].max())

        year_range = st.slider(
            "Pilih Rentang Tahun",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year),
            key="global_year_slider"
        )

    # SPBU
    with col2:

        spbu_options = sorted(
            df["title"].unique()
        )

        selected_spbu = st.multiselect(
            "Pilih SPBU",
            spbu_options,
            placeholder="Pilih SPBU...",
            key="global_spbu_multiselect"
        )

    # ACTIVE DATA
    with col3:

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="total-data-card">

            <p>Total Data</p>

            <h2>{len(df):,}</h2>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # FILTERING
    filtered_df = df.copy()

    # YEAR RANGE
    filtered_df = filtered_df[
        (
            filtered_df["year"] >= year_range[0]
        )
        &
        (
            filtered_df["year"] <= year_range[1]
        )
    ]

    # SPBU
    if selected_spbu:

        filtered_df = filtered_df[
            filtered_df["title"].isin(
                selected_spbu
            )
        ]

    # SAVE GLOBAL STATE
    st.session_state["filtered_df"] = filtered_df

    return filtered_df