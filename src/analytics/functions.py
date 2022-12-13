from nltk.tokenize import sent_tokenize
from parrot import Parrot
import streamlit as st
from fuzzywuzzy import fuzz
import re
from typing import List
import logging

logging.basicConfig(level=logging.NOTSET)


def read_txt_file(filename: str) -> str:
    with open(filename) as f:
        token = f.readlines()[0]
    return token


def check_text_similarity(first_text: str, second_text: str) -> float:
    """
    Checks similarity between 2 given texts based on the fuzz partial ratio
    """
    return (
        fuzz.partial_ratio(
            first_text,
            second_text,
        )
        / 100
    )


def get_most_diverse_text(original_text: str, text_variations_list: List) -> str:
    """
    Get an original text and compare it with text variations coming as a list.
    kept_sentence: Str text coming as the least similar to the original text

    """
    similarity_list = []

    for temp_dif_sentence in text_variations_list:
        temp_text_similarity = check_text_similarity(
            original_text, temp_dif_sentence[0].capitalize()
        )
        similarity_list.append(temp_text_similarity)

    min_index = similarity_list.index(min(similarity_list))
    kept_sentence = text_variations_list[min_index][0].capitalize()
    kept_sentence = kept_sentence + ". "

    return kept_sentence


def create_paraphrase(
    parrot_model: Parrot,
    text: str,
    adequacy_threshold: float = 0.75,
    fluency_threshold: float = 0.90,
    diversity_ranker: str = "levenshtein",
) -> str:
    """
    Creates the new paraphrased text
    """
    logging.info("Spliting to sentences.........")
    sentences = re.split("[,.!?;]", text)
    new_text = ""
    logging.info("Creating paraphrased text for each sentence.........")
    for sentence in sentences:
        dif_sentences = parrot_model.augment(
            input_phrase=sentence,
            diversity_ranker=diversity_ranker,
            adequacy_threshold=adequacy_threshold,
            fluency_threshold=fluency_threshold,
        )

        if dif_sentences != None:
            kept_sentence = get_most_diverse_text(sentence, dif_sentences)
            new_text = new_text + kept_sentence

    return new_text


@st.experimental_singleton
def get_model() -> Parrot:

    return Parrot(
        model_tag="prithivida/parrot_paraphraser_on_T5",
        use_gpu=False,
    )
