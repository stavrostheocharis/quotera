import streamlit as st
from src.analytics.pipelines import create_paraphrase_text
from src.analytics.functions import get_model, read_txt_file
from src.streamlit_quotera.utils.load import load_config, load_image
from src.streamlit_quotera.utils.export import display_links
from cards import *
from inputs import input_text

from huggingface_hub import HfApi
from huggingface_hub.commands.user import _login

token = read_txt_file("token.txt")
_login(HfApi(), token=token)


# Load config
st.set_page_config(page_title="Quotera", layout="wide")
readme = load_config("config_readme.toml")

with st.spinner(
    "Loading and geting ready the AI models (this action may take some time)..."
):
    parrot_model = get_model()

# Info
st.title("Paraphrase Text")
with st.expander("What is this app?", expanded=False):
    st.write(readme["app"]["app_intro"])
    st.write("")
st.write("")
st.sidebar.image(load_image("logo.png"), use_column_width=True)
display_links(readme["links"]["repo"], readme["links"]["article"])

# Parameters
st.sidebar.title("Parameters")
adequacy_threshold = st.sidebar.slider(
    "Select adequacy threshold",
    0.0,
    1.0,
    step=0.01,
    value=0.90,
    help=readme["tooltips"]["adequacy_threshold"],
)
fluency_threshold = st.sidebar.slider(
    "Select fluency threshold",
    0.0,
    1.0,
    step=0.01,
    value=0.90,
    help=readme["tooltips"]["fluency_threshold"],
)
diversity_ranker = st.sidebar.selectbox(
    "Select diversity ranker",
    ("levenshtein", "euclidean", "diff"),
    help=readme["tooltips"]["diversity_ranker"],
)

# Text loading
text, button = input_text(readme)

# Paraphrase generation
with st.spinner("Generating Paraphrased text.."):
    if button and text:
        paraphrased_text = create_paraphrase_text(
            parrot_model,
            text,
            adequacy_threshold=adequacy_threshold,
            fluency_threshold=fluency_threshold,
            diversity_ranker="levenshtein",
        )
        st.markdown(
            """
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            """,
            unsafe_allow_html=True,
        )

        st.write(card(paraphrased_text["text"]))
        st.download_button("Download .txt", paraphrased_text["text"])
