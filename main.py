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



#______________________3. UPDATE method practice_________________________ 
#_________________________________________________________________________

from typing import Optional


class Patient_Update(BaseModel):
    name : Annotated[Optional[str],Field(default=None)]
    city : Annotated[Optional[str],Field(default=None)]
    age : Annotated[Optional[int],Field(default=None,gt=0)]
    gender : Annotated[Optional[Literal['Male','Female']],Field(default=None)]
    height : Annotated[Optional[float],Field(default=None,gt=0)]
    weight : Annotated[Optional[float],Field(default=None,gt=0)]

@app.put('/edit/{patient_id}')
def update_patient(patient_id : str, patient_update : Patient_Update):

    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail='Patient not found')

    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key,value in updated_patient_info.items():
        existing_patient_info[key] = value

    # Full process
    # existing_patient_info -> pydantic object -> updated bmi  verdict 
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)

    # -> pydantic object -> dict
    existing_patient_info = patient_pydantic_obj.model_dump(exclude='id')

    # add this dictionary to data
    data[patient_id] = existing_patient_info

    # save the data 
    save_data(data)

    return JSONResponse(status_code=200,content={'message':'patient updated'})




#______________________3. DELETE method practice_________________________ 
#_________________________________________________________________________

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id : str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')

    del data[patient_id] 

    save_data(data)

    return JSONResponse(status_code=200,content={'message':'patient deleted'})