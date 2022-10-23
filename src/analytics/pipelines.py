import site; 


import warnings
warnings.filterwarnings("ignore")

from src.analytics.functions import *
from src.analytics.utils import *

random_state(1234)

def create_paraphrase_text(parrot_model, text, adequacy_threshold, fluency_threshold, diversity_ranker):
    print("Running....................")
    return {"text":create_paraphrase(parrot_model, text, adequacy_threshold, fluency_threshold, diversity_ranker)}