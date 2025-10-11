from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    return {"message": "Hello from flask API!", "status": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
