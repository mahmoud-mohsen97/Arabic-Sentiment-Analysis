from typing import List
from fastapi import FastAPI
from model import ModelPredict
from request_response_object import RequestObject, ResponseObject, create_response_objects

app = FastAPI()

print("The server has been started....")

model = ModelPredict()


@app.post("/predict/")
def predict(batch_text: RequestObject) -> List[ResponseObject]:

    predictions = model.predict(batch_text.text)
    responses = create_response_objects(batch_text.text, predictions)
    
    return responses