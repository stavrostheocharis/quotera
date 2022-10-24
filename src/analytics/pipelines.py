from parrot import Parrot
from typing import Dict
import warnings

warnings.filterwarnings("ignore")

from src.analytics.functions import *
from src.analytics.utils import *

random_state(1234)


def create_paraphrase_text(
    parrot_model: Parrot,
    text: str,
    adequacy_threshold: float,
    fluency_threshold: float,
    diversity_ranker: str,
) -> Dict[str, str]:
    print("Running....................")
    return {
        "text": create_paraphrase(
            parrot_model, text, adequacy_threshold, fluency_threshold, diversity_ranker
        )
    }
