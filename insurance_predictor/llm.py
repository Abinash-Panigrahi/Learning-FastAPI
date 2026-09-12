import os
from dotenv import load_dotenv
from google import genai  # <-- New import!

load_dotenv()

# Initialize the new modern client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def get_gemini_prediction(data_input: dict) -> str:
    """
    Takes the cleaned data dictionary and uses Gemini to classify the premium.
    """
    
    prompt = f"""
    You are an expert insurance underwriter and risk analyst. 
    Analyze the following processed customer profile and predict their insurance premium level.
    
    Customer Profile:
    - BMI: {data_input.get('bmi')}
    - Age Group: {data_input.get('age_group')}
    - Lifestyle Risk: {data_input.get('lifestyle')}
    - City Tier: {data_input.get('city_tier')}
    - Income (LPA): {data_input.get('income_lpa')}
    - Occupation: {data_input.get('occupation')}
    
    RULES:
    1. Assess the health risks (BMI, Lifestyle) and financial profile (Income, City, Occupation).
    2. You must output EXACTLY one word: High, Medium, or Low.
    3. Do not include any formatting, markdown, punctuation, or explanation.
    """
    
    # New syntax for generating content (using the latest flash model)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    return response.text.strip()