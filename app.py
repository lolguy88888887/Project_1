import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)

# Load CSV
data = pd.read_csv("career_data.csv")

X = data[["Math", "Coding", "Art", "Social", "Science"]]
y = data["Career"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Prediction page
@app.route("/predict", methods=["POST"])
def predict():

    math = int(request.form["math"])
    coding = int(request.form["coding"])
    art = int(request.form["art"])
    social = int(request.form["social"])
    science = int(request.form["science"])

    prediction = model.predict([[math, coding, art, social, science]])

    return render_template(
        "index.html",
        prediction=prediction[0]
    )

# Run website
if __name__ == "__main__":
    app.run(debug=True)

