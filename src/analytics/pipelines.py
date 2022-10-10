from parrot import Parrot
import torch
import warnings
from nltk.tokenize import sent_tokenize
warnings.filterwarnings("ignore")

from src.analytics.functions import *
from src.analytics.utils import *

random_state(1234)

def create_paraphrase_text(text, adequacy_threshold, fluency_threshold, diversity_ranker):
    parrot_model = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)
    
    return create_paraphrase(parrot_model, text, adequacy_threshold, fluency_threshold, diversity_ranker)