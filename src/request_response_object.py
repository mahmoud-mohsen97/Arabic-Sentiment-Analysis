from pydantic import BaseModel, Field
from typing import List, Tuple
import torch


class RequestObject(BaseModel):
    text: List[str] = Field(..., min_items=1)


class ResponseObject(BaseModel):
    text: str
    probability: float
    label_number: int
    label_name: str



def create_response_objects(texts: List[str], predictions: List[Tuple]) -> List[ResponseObject]:
    """
    Create a list of ResponseObject instances from a list of texts and their corresponding predictions.
    """
    response_objects = []
    for text, prediction in zip(texts, predictions):
        probabilities, label_number, label_name = prediction
        max_probability = probabilities.max().item()
        response_object = ResponseObject(
            text=text,
            probability=max_probability,
            label_number=label_number.item(),
            label_name=label_name
        )
        response_objects.append(response_object)
    return response_objects

