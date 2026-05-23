import streamlit as st

def global_filter(df):

    years = sorted(
        df["year"].unique()
    )

    min_year = int(min(years))
    max_year = int(max(years))

    # SESSION STATE
    if "year_range" not in st.session_state:

        st.session_state.year_range = (
            min_year,
            max_year
        )

    if "selected_spbu" not in st.session_state:

        st.session_state.selected_spbu = []

    # FILTER CONTAINER
    with st.container():

        col1, col2, col3 = st.columns(
            [1.2, 2.2, 1]
        )

        with col1:

            year_range = st.slider(
                "Pilih Rentang Tahun",
                min_value=min_year,
                max_value=max_year,
                value=st.session_state.year_range,
                key="global_year_slider"
            )

        with col2:

            spbu_options = sorted(
                df["title"].unique()
            )

            selected_spbu = st.multiselect(
                "Pilih SPBU",
                options=spbu_options,
                default=st.session_state.selected_spbu,
                placeholder="Pilih SPBU...",
                key="global_spbu_select"
            )

        with col3:

            st.markdown("<br>", unsafe_allow_html=True)

            st.metric(
                "Total Data",
                f"{len(df):,}"
            )

    # SAVE SESSION
    st.session_state.year_range = year_range
    st.session_state.selected_spbu = selected_spbu

    # FILTERING
    filtered_df = df[

        (df["year"] >= year_range[0]) &
        (df["year"] <= year_range[1])

    ]

    if len(selected_spbu) > 0:

        filtered_df = filtered_df[
            filtered_df["title"].isin(
                selected_spbu
            )
        ]

    # SAVE GLOBAL DF
    st.session_state.filtered_df = filtered_df

    return filtered_df