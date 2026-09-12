import os
import google.generativeai as genai
from dotenv import load_dotenv

print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)