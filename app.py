from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://disease.sh/v3/covid-19/historical/{country}?lastdays=30"

def fetch_country_data(country):
    try:
        response = requests.get(API_URL.format(country=country))
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def find_peak(data, field):
    try:
        timeline = data['timeline'][field]
        date, value = max(timeline.items(), key=lambda x: x[1])
        return {"date": date, "value": value}
    except Exception as e:
        return {"error": str(e)}

@app.route('/status')
def status():
    try:
        test = requests.get("https://disease.sh/v3/covid-19/all")
        test.raise_for_status()
        return jsonify({"status": "success"})
    except:
        return jsonify({"status": "fail"})

@app.route('/newCasesPeak')
def new_cases_peak():
    country = request.args.get("country")
    data = fetch_country_data(country)
    if "error" in data:
        return jsonify({})
    result = find_peak(data, "cases")
    return jsonify({"country": country, "method": "newCasesPeak", **result})

@app.route('/recoveredPeak')
def recovered_peak():
    country = request.args.get("country")
    data = fetch_country_data(country)
    if "error" in data:
        return jsonify({})
    result = find_peak(data, "recovered")
    return jsonify({"country": country, "method": "recoveredPeak", **result})

@app.route('/deathsPeak')
def deaths_peak():
    country = request.args.get("country")
    data = fetch_country_data(country)
    if "error" in data:
        return jsonify({})
    result = find_peak(data, "deaths")
    return jsonify({"country": country, "method": "deathsPeak", **result})

@app.errorhandler(404)
def not_found(e):
    return jsonify({}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
