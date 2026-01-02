from abc import ABC
from typing import Optional
from pydantic import UUID4, Field
from .base import NoSQLBaseDocument
from .types import DataCategory
from enum import StrEnum

class DataCategory(StrEnum):
    PROMPT = "prompt"
    QUERIES = "queries"
    INSTRUCT_DATASET_SAMPLES = "instruct_dataset_samples"
    INSTRUCT_DATASET = "instruct_dataset"
    PREFERENCE_DATASET_SAMPLES = "preference_dataset_samples"
    PREFERENCE_DATASET = "preference_dataset"
    POSTS = "posts"
    ARTICLES = "articles"
    REPOSITORIES = "repositories"