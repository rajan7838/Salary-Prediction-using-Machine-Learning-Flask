from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("salary_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        data = {
            "age": int(request.form.get("age")),
            "experience": int(request.form.get("experience")),
            "education": request.form.get("education"),
            "job_title": request.form.get("job_title"),
            "location": request.form.get("location"),
            "gender": request.form.get("gender")
        }

        input_df = pd.DataFrame([data])
        prediction = round(model.predict(input_df)[0], 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)