from fastapi import FastAPI,HTTPException

app = FastAPI()

# 1st session
# -----------
@app.get("/")
def  hello():
    return {'message' : 'Hello world'}

@app.get("/about")
def about():
    return {'message' : 'ThynxAi is company who is working on AI technologies'}


# 2nd session       
# -----------
import json
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def  hello():
    return {'message' : 'Patient management system API'}

@app.get("/about")
def about():
    return {'message' : 'A fully functional API to manage your patient records'}

# # to see all the patient at a time 
@app.get("/view")
def view():
    data = load_data()
    return data 

# # to see particularly one data and using path parameter for enhance the readability
from fastapi import Path

@app.get("/patient/{id}")
def parient_view(id : str = Path(..., description='ID of the pateint in the DB', example='P001')):
    data = load_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code=404,detail='Patient not found')



#________________________3. POST method practice_________________________ 
#__________________________________________________________________________
from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
import json


class Patient(BaseModel):
    id : Annotated[str,Field(...,description='ID of the patient',examples=['P001'])]
    name : Annotated[str,Field(...,description='Name of the patient')]
    city : Annotated[str,Field(...,description='Patient form which city')]
    age : Annotated[int,Field(...,gt=0,lt=120,description='Age of the patient')]
    gender : Annotated[Literal['Male','Female','Other'],Field(...,description='Gender of the patient')]
    height : Annotated[float,Field(gt=0,description='Height of the patient in meters')]
    weight : Annotated[float,Field(gt=0,description='Weight of the patient in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Under weight'
        elif self.bmi <25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        return data 

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


# API endpoint
# ____________

@app.post('/create')
def create_patient(patient : Patient):

    #1: load existing data
    data = load_data()

    #2: check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patinet is already exist')
    
    #3: new patient add to he db
    data[patient.id] = patient.model_dump(exclude=['id'])

    #4: save in to json file 
    save_data(data)

    return JSONResponse(status_code=201,content={'message':'Patient created successfull'})