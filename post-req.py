from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated , Literal
import json

app = FastAPI()

@computed_field

@property
def bmi(self) -> float:
    bmi = round(self.weight / (self.height ** 2),2)
    return bmi

@computed_field
@property
def verdict(self) -> str:
    if self.bmi < 18.5:
        return "Underweight"
    elif self.bmi < 25:
        return 'Normal'
    elif self.bmi < 30:
        return 'Normal'
    elif self.bmi > 30:
        return 'obessis'

class Patient(BaseModel):
    id : Annotated[str,Field(...,description = "Id of the patient", example = ["p001"])]
    name : Annotated[str,Field(...,description = "Name of the patient")]
    city : Annotated[str,Field(...,description = "City where the patient is living")]
    gender : Annotated[Literal['male','female','others'],Field(...,description="Mention the Gender",)]
    height : Annotated[float, Field(...,gt =0, description = "Height of the patient in meter")]
    weight : Annotated[float,Field(...,gt=0,description="Weight of the patient in kgs")]


def load_data() : 
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)

@app.post('/create')

def create_patient(patient: Patient):
    # load existing data

    # check the patient is already exists.

    # new patient to the database.

    data = load_data()

    if patient.id in data : 
        raise HTTPException(status_code = 400 , detail = "Patient already exists")
    
    # new patient added to the database

    data[patient.id] = patient.model_dump(exclude=['id'])

    save_data(data)

    return JSONResponse(status_code=201, content = {
        'message' : "patient are created"
    })

