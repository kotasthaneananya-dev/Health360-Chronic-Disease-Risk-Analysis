
from flask import Flask, render_template

app = Flask(__name__)

DASHBOARDS = [
    {
        "id": "clinical",
        "name": "Clinical Risk Assessment",
        "description": "Explore diabetes prevalence alongside BMI, blood pressure, cholesterol, and other health indicators.",
        "url": "https://public.tableau.com/views/ChronicDiseaseRiskAnalysis/ClinicalRiskAssessment?:showVizHome=no"
    },
    {
        "id": "lifestyle",
        "name": "Lifestyle Behavior",
        "description": "Explore associations between diabetes and lifestyle indicators such as smoking, physical activity, alcohol consumption, and diet.",
        "url": "https://public.tableau.com/views/ChronicDiseaseRiskAnalysis/Dashboard2?:showVizHome=no"
    },
    {
        "id": "population",
        "name": "Population Health",
        "description": "Explore health patterns across age groups, income levels, and healthcare access.",
        "url": "https://public.tableau.com/views/ChronicDiseaseRiskAnalysis/PopulationHealth?:showVizHome=no"
    }
]


@app.route("/")
def home():
    selected = request_dashboard()
    return render_template("index.html", dashboards=DASHBOARDS, selected=selected)


def request_dashboard():
    from flask import request
    requested_id = request.args.get("dashboard", "clinical")
    valid_ids = {dashboard["id"] for dashboard in DASHBOARDS}
    return requested_id if requested_id in valid_ids else "clinical"


if __name__ == "__main__":
    app.run(debug=True)
