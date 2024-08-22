
import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyAAceK2tD3AZAO2UUzIY4R5AD3K-zKd1-4')

model = genai.GenerativeModel('gemini-1.5-flash')

entity = 'Rari'
sentence = "Crashed the 'Rari so I hopped in the Benz"

response = model.generate_content(f"What is the sentiment (positive/negative/neutral) of the {entity} in {sentence} in one word")
print(response.text)