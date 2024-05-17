import tkinter as tk
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

# Assuming you have a DataFrame 'df' with symptom features and 'disease' target
# df = pd.read_csv('your_data.csv')

# For the sake of example, let's create a DataFrame
df = pd.DataFrame({
    'fever': [1, 0, 1, 0, 1],
    'cough': [0, 1, 1, 0, 1],
    'fatigue': [1, 1, 0, 0, 1],
    'disease': ['flu', 'cold', 'flu', 'healthy', 'flu']
})

# Train a RandomForestClassifier
model = RandomForestClassifier()
model.fit(df[['fever', 'cough', 'fatigue']], df['disease'])

# Create the main window
root = tk.Tk()

# Create a StringVar to hold the selected symptom
selected_symptom = tk.StringVar()

# Create a dropdown menu with the symptom options
symptom_dropdown = tk.OptionMenu(root, selected_symptom, *df.columns[:-1])
symptom_dropdown.pack()

# Create a function to predict the disease based on the selected symptom
def predict_disease():
    symptom_data = np.zeros(len(df.columns) - 1)
    symptom_index = df.columns.get_loc(selected_symptom.get())
    symptom_data[symptom_index] = 1
    prediction = model.predict([symptom_data])
    result_label.config(text=f"Predicted disease: {prediction[0]}")

# Create a button that will call the predict_disease function when clicked
predict_button = tk.Button(root, text="Predict Disease", command=predict_disease)
predict_button.pack()

# Create a label to display the prediction result
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()