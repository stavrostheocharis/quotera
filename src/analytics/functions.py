from nltk.tokenize import sent_tokenize
from parrot import Parrot
import streamlit as st


def create_paraphrase(
    parrot_model: Parrot,
    text: str,
    adequacy_threshold: float = 0.75,
    fluency_threshold: float = 0.90,
    diversity_ranker: str = "levenshtein",
) -> str:
    print("Tokenising text.........")
    sentences = list(sent_tokenize(text))
    new_text = ""
    print("Creating paraphrased text for each sentence.........")
    for sentence in sentences:
        dif_sentences = parrot_model.augment(
            input_phrase=sentence,
            diversity_ranker=diversity_ranker,
            adequacy_threshold=adequacy_threshold,
            fluency_threshold=fluency_threshold,
        )

        if dif_sentences != None:
            kept_sentence = dif_sentences[0][0].capitalize()
            kept_sentence = kept_sentence.capitalize()
            kept_sentence = kept_sentence + ". "
            new_text = new_text + kept_sentence

    return new_text


@st.experimental_singleton
def get_model() -> Parrot:

    return Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)
