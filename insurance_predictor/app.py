from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model import UserInput
from llm import get_gemini_prediction

app = FastAPI()

@app.post('/predict')
def predict_premium(data: UserInput):
    # 1. Prepare the optimized data from Pydantic
    data_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle': data.lifestyle,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    # 2. Send the cleaned data to Gemini
    prediction = get_gemini_prediction(data_input)
    
    # 3. Return the AI's verdict to the frontend
    return JSONResponse(status_code=200,content={'Predicted_category': prediction})