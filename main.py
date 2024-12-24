import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  


genai.configure(api_key=os.getenv('GEMINI_API_KEY'))


model = genai.GenerativeModel('gemini-pro')


def gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

if __name__ == '__main__':
    prompt_to_gemini = "What is the meaning of life?"
    response = gemini_response(prompt_to_gemini)
    print(response)
