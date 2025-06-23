import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai

genai.configure(api_key="API_Key") 
model = genai.GenerativeModel("gemini-1.5-flash")


data = {
    'Name': ['Tahir', 'Ali', 'Zara'],
    'StudyHours': [6, 2, 4],
    'Marks': [90, 55, 70]
}
df = pd.DataFrame(data)


