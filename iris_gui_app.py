import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load model and scaler
model = joblib.load("iris_model.pkl")
scaler = joblib.load("scaler.pkl")

# Prediction function
def predict_species():
    try:
        # Get user input
        inputs = [float(entry.get()) for entry in entries]
        inputs_scaled = scaler.transform([inputs])
        prediction = model.predict(inputs_scaled)[0]
        
        species = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
        result_label.config(text=f"Predicted Species: {species[prediction]}", fg="green")
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Set up GUI
root = tk.Tk()
root.title("Iris Flower Predictor")

labels = ["Sepal Length (cm)", "Sepal Width (cm)", "Petal Length (cm)", "Petal Width (cm)"]
entries = []

for idx, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=idx, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries.append(entry)

tk.Button(root, text="Predict", command=predict_species, bg="blue", fg="white").grid(row=4, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=5, columnspan=2, pady=10)

root.mainloop()
