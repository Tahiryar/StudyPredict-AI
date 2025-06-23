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


mean_x = df['StudyHours'].mean()
mean_y = df['Marks'].mean()
df['x_diff'] = df['StudyHours'] - mean_x
df['y_diff'] = df['Marks'] - mean_y
df['xy'] = df['x_diff'] * df['y_diff']
df['x2'] = df['x_diff'] ** 2
m = df['xy'].sum() / df['x2'].sum()
c = mean_y - m * mean_x

name = input("👤 Enter student name: ")
hours = float(input("⏱ Enter study hours: "))
predicted_marks = m * hours + c

# Step 5: GenAI Prompt
prompt = f"""
You are a study advisor bot. A student studied for {hours} hours and is predicted to score {predicted_marks:.2f} marks.
Give motivational advice in 2 lines, based on this.
"""

response = model.generate_content(prompt)
advice = response.text.strip()

# Step 6: Save data
df_new = pd.DataFrame([{
    'Name': name,
    'StudyHours': hours,
    'PredictedMarks': predicted_marks,
    'Advice': advice
}])

df_new.to_csv("student_prediction_with_advice.csv", index=False)

print("\n Prediction Summary:")
print(df_new)


plt.bar(['Predicted Marks'], [predicted_marks], color='orange')
plt.title(f'Marks Prediction for {name}')
plt.ylim(0, 100)
plt.ylabel("Marks")
plt.grid(True)
plt.show()
