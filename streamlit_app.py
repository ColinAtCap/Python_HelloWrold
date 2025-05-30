import streamlit as st
import pandas as pd  # Add pandas import

def main():
    st.title("🎈 My new app")
    st.write(
        "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
    )

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded CSV:")
        st.dataframe(df)

main()
# Run the app with the command: streamlit run streamlit_app.py
