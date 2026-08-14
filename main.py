from fastapi import FastAPI,HTTPException

app = FastAPI()

# 1st session
# -----------
# @app.get("/")
# def  hello():
#     return {'message' : 'Hello world'}

# @app.get("/about")
# def about():
#     return {'message' : 'ThynxAi is company who is working on AI technologies'}


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

# to see all the patient at a time 
@app.get("/view")
def view():
    data = load_data()
    return data 

# to see particularly one data and using path parameter for enhance the readability
from fastapi import Path

@app.get("/patient/{id}")
def parient_view(id : str = Path(..., description='ID of the pateint in the DB', example='P001')):
    data = load_data()
    if id in data:
        return data[id]
    raise HTTPException(status_code=404,detail='Patient not found')

