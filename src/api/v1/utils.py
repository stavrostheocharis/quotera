import pandas as pd
from fastapi.encoders import jsonable_encoder
import requests
from src.schemas.input import TextIn
from typing import Tuple, Union, List, Dict, Any
import os
import logging


def transform_input_data(data):
    encoded_data = jsonable_encoder(data)

    return encoded_data


def get_transformations(
    body: TextIn,
) -> Tuple[str, float, float, str]:
    transformed_text = transform_input_data(body.text)
    transformed_adequacy_threshold = transform_input_data(body.adequacy_threshold)
    transformed_fluency_threshold = transform_input_data(body.fluency_threshold)
    transformed_diversity_ranker = transform_input_data(body.diversity_ranker)

    return (
        transformed_text,
        transformed_adequacy_threshold,
        transformed_fluency_threshold,
        transformed_diversity_ranker,
    )
