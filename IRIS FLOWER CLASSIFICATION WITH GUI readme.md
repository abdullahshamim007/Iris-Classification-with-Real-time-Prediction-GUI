**IRIS FLOWER CLASSIFICATION WITH GUI**



This project uses a machine learning model to classify Iris flowers into three species based on their sepal and petal measurements. A custom-built Tkinter GUI allows users to input flower features and get instant predictions.



---



**Project Structure**



```

Iris Classification/

iris\_gui\_app.py           # Tkinter GUI script

iris\_model.pkl            # Trained KNN model

scaler.pkl                # StandardScaler used on features

iris\_dataset.csv          # Cleaned dataset (optional)

README.md                 # Project documentation

Iris Classification with Real-time Prediction GUI    # Full ML pipeline notebook

```



---



**Dataset Overview**



-Source: UCI Machine Learning Repository – Iris Dataset

\-Samples: 147 (after removing 3 duplicates)

\-Features:



&nbsp; **Sepal Length (cm)**

  **Sepal Width (cm)**

  **Petal Length (cm)**

  **Petal Width (cm)**





\-Target Classes:



&nbsp; **Iris-setosa**

  **Iris-versicolor**

  **Iris-virginica**



---



**Technologies Used**



-Python 3.11

-Pandas, NumPy

-Scikit-learn

-Matplotlib, Seaborn

-Tkinter

-Joblib



---



**Model Details**



-Algorithm Used: K-Nearest Neighbors (K=3)

-Scaler: StandardScaler

-Accuracy Achieved: 93.3%

-Evaluation: Confusion Matrix and Classification Report



---

**Hyperparameter Tuning – Finding the Best k**

We performed a cross-validation sweep over odd k values from 1 to 15 for the K-Nearest Neighbors classifier.  
The highest accuracy was achieved at **k = 3**, which we used for our final model.

---

Additional Evaluation Metrics

- **Accuracy:** 93.3%  
- **Macro F1 Score:** 0.93  
- **Precision/Recall:** Balanced across all three classes  
- Only **2 misclassifications** in the test set.

---

**Visualization Enhancements**

### 1. Decision Boundary Plot (Petal Features)
A 2D visualization of how KNN separates species based on Petal Length and Petal Width.



### 2. 3D Scatter Plot
A 3D visualization using Sepal Length, Petal Length, and Petal Width.

---

**GUI Application (Tkinter)**

The desktop GUI allows users to:



-Input 4 numerical features (sepal \& petal measurements)

-Click **Predict**

-Get the Iris species as output



To run the GUI:

**python iris\_gui\_app.py**



---

**How to Install Requirements**

**pip install pandas numpy scikit-learn matplotlib seaborn joblib**

(Tkinter is built-in with Python)



 Video Presentation Link:
 https://drive.google.com/drive/folders/1s8poyn9_XZ01XGX-YpuWyu_eCZaozQzn?usp=sharing



---


## Conclusion

This project was all about taking the well-known Iris dataset and turning it into a working, interactive machine learning application. We started by exploring and cleaning the data to make sure everything was ready for modeling. Then, we analyzed the patterns in the sepal and petal measurements, which gave us useful insights into how different flower species can be separated.

We trained a K-Nearest Neighbors (KNN) model, which turned out to be a great fit for this dataset. With an accuracy of **93.3%** and a strong macro F1 score of **0.93**, the model performed very well, making only a couple of mistakes on the test set. We also checked which samples were misclassified to understand where the model struggled.

The best part was turning the model into something anyone can use — a simple GUI built with Tkinter. Now, instead of running Python code, a user can just type in the flower’s measurements, click a button, and instantly get the prediction.


Overall, this project shows the complete journey — from raw data to an easy-to-use application. It’s accurate, interactive, and could be extended or improved further, but even as it stands, it’s a solid example of taking machine learning beyond theory and making it work in the real world.

