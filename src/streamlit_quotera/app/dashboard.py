import streamlit as st
from src.analytics.pipelines import create_paraphrase_text
from src.streamlit_quotera.utils.load import load_config, load_image
from src.streamlit_quotera.utils.export import display_links

# Load config
st.set_page_config(page_title="Prophet", layout="wide")
readme = load_config("config_readme.toml")


st.title("Paraphrase Text")
# Info
with st.expander("What is this app?", expanded=False):
    st.write(readme["app"]["app_intro"])
    st.write("")
st.write("")
st.sidebar.image(load_image("logo.png"), use_column_width=True)
display_links(readme["links"]["repo"], readme["links"]["article"])
st.sidebar.title("Parameters")

text = st.text_area('Please paste your text :', height=30)
button = st.button("Paraphrase")

adequacy_threshold = st.sidebar.slider('Select adequacy threshold', 0.0, 1.0, step=0.01, value=0.75, help=readme["tooltips"]["adequacy_threshold"])
fluency_threshold = st.sidebar.slider('Select fluency threshold', 0.0, 1.0, step=0.01, value=0.90, help=readme["tooltips"]["fluency_threshold"])
diversity_ranker = st.sidebar.selectbox("Select diversity ranker", ("levenshtein", "euclidean", "diff"), help=readme["tooltips"]["diversity_ranker"])

with st.spinner("Generating Paraphrased text.."):
    if button and text:
        paraphrased_text = create_paraphrase_text(
        text, adequacy_threshold = adequacy_threshold, fluency_threshold = fluency_threshold, diversity_ranker="levenshtein"
    ) 
        st.write(paraphrased_text)