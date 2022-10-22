import streamlit as st
from src.analytics.pipelines import create_paraphrase_text

st.title("Paraphrase Text")
text = st.text_area('Please paste your text :', height=30)
button = st.button("Paraphrase")

adequacy_threshold = st.sidebar.slider('Select adequacy threshold', 0.0, 1.0, step=0.01, value=0.75)
fluency_threshold = st.sidebar.slider('Select fluency threshold', 0.0, 1.0, step=0.01, value=0.90)
diversity_ranker = st.sidebar.selectbox("Select diversity ranker", ("levenshtein", "euclidean", "diff"))

with st.spinner("Generating Paraphrased text.."):
    if button and text:
        paraphrased_text = create_paraphrase_text(
        text, adequacy_threshold = adequacy_threshold, fluency_threshold = fluency_threshold, diversity_ranker="levenshtein"
    ) 
        st.write(paraphrased_text)