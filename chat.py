import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))
generation_config = {"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}

# load the LLM model
model = genai.GenerativeModel("gemini-pro", generation_config = generation_config)


## test the chatbot
## question = input("Please enter a question that you have: ")
response = model.generate_content(["create a meal plan to gain lean muscle"])
print(response.text)