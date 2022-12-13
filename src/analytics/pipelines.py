from parrot import Parrot
from typing import Dict
import warnings
import logging

warnings.filterwarnings("ignore")

from src.analytics.functions import *
from src.analytics.utils import *

random_state(1234)
logging.basicConfig(level=logging.NOTSET)


def create_paraphrase_text(
    parrot_model: Parrot,
    text: str,
    adequacy_threshold: float = 0.75,
    fluency_threshold: float = 0.90,
    diversity_ranker: str = "levenshtein",
) -> Dict[str, str]:
    logging.info("Running....................")
    return {
        "text": create_paraphrase(
            parrot_model, text, adequacy_threshold, fluency_threshold, diversity_ranker
        )
    }
