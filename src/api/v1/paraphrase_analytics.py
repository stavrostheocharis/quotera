from src.schemas.input import TextIn
from src.schemas.output import TextOut
from src.schemas.utils import HealthCheck
from fastapi import APIRouter
from typing import List
import os
import time
import logging

from src.api.v1.utils import *
from src.analytics.pipelines import create_paraphrase_text

paraphrase_analytics_router = APIRouter()

@paraphrase_analytics_router.post(
    "/text/paraphrase",
    tags=["Text Paraphrase"],
    summary="Paraphrase text based on each phrase",
    response_description="Paraphrased text",
    response_model=TextOut,
)
async def paraphrase_text(body: TextIn):
    """ 
    Use this route to paraphrase text.
    """
    start = time.time()
    logging.info("Triggering paraphrase pipeline")
    transformed_text, transformed_adequacy_threshold, transformed_fluency_threshold, transformed_diversity_ranker = get_transformations(body)
    logging.info("Processing & paraphrasing text")

    paraphrased_text = create_paraphrase_text(
        transformed_text, transformed_adequacy_threshold, transformed_fluency_threshold, transformed_diversity_ranker
    )
    end = time.time()
    logging.info("Runtime of the program is {}".format(end - start))

    return paraphrased_text
