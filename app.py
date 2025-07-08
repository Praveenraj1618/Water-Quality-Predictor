from flask import Flask, render_template, request, send_file, make_response
import pandas as pd
import joblib
import io
from xhtml2pdf import pisa

app = Flask(__name__)

# Load model and columns
model = joblib.load('pollution_model.pkl')
model_columns = joblib.load('model_columns.pkl')

pollutants = ['NH4', 'BSK5', 'Suspended', 'O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
safe_limits = {
    'NH4': 0.5, 'BSK5': 3.0, 'Suspended': 20.0,
    'O2': 6.0, 'NO3': 50.0, 'NO2': 0.3,
    'SO4': 250.0, 'PO4': 0.1, 'CL': 250.0
}
greater_is_better = {'O2': True}

last_prediction = {}

@app.route('/')
def home():
    return render_template('index.html', pollutants=None)

@app.route('/predict', methods=['POST'])
def predict():
    global last_prediction
    station_id = request.form['station_id']
    year = int(request.form['year'])

    input_df = pd.DataFrame({'year': [year], 'id': [station_id]})
    input_encoded = pd.get_dummies(input_df)

    for col in set(model_columns) - set(input_encoded.columns):
        input_encoded[col] = 0
    input_encoded = input_encoded[model_columns]

    prediction = model.predict(input_encoded)[0]
    values = dict(zip(pollutants, [float(round(x, 2)) for x in prediction]))

    status_per_pollutant = {}
    for p, val in values.items():
        limit = safe_limits[p]
        if greater_is_better.get(p, False):
            status_per_pollutant[p] = "Safe" if val >= limit else "Polluted"
        else:
            status_per_pollutant[p] = "Safe" if val <= limit else "Polluted"

    overall_status = "Clean" if list(status_per_pollutant.values()).count("Polluted") == 0 else "Polluted"

    last_prediction.update({
        "station_id": station_id,
        "year": year,
        "pollutants": values,
        "status_per_pollutant": status_per_pollutant,
        "overall_status": overall_status
    })

    return render_template("index.html",
        pollutants=values,
        statuses=status_per_pollutant,
        overall=overall_status,
        labels=list(values.keys()),
        values=[float(v) for v in values.values()]
    )

@app.route("/export/csv")
def export_csv():
    if not last_prediction:
        return "No prediction made yet", 400
    df = pd.DataFrame([last_prediction['pollutants']])
    df['Station'] = last_prediction['station_id']
    df['Year'] = last_prediction['year']
    df['OverallStatus'] = last_prediction['overall_status']
    output = io.StringIO()
    df.to_csv(output, index=False)
    response = make_response(output.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=prediction.csv"
    response.headers["Content-type"] = "text/csv"
    return response

@app.route("/export/pdf")
def export_pdf():
    if not last_prediction:
        return "No prediction made yet", 400

    html = render_template("pdf_template.html", data=last_prediction)
    pdf = io.BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf)
    if pisa_status.err:
        return "Error generating PDF", 500
    pdf.seek(0)
    return send_file(pdf, as_attachment=True, download_name="prediction.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
