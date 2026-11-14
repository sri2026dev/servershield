from flask import Flask, render_template, jsonify
import random
import psutil
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def get_data():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent

    # Simulated server request count
    requests = random.randint(100, 1000)

    # Simple load prediction
    if cpu > 80 or ram > 80 or requests > 800:
        status = "HIGH LOAD"
        alert = "Warning! Server overload risk detected."
    elif cpu > 60 or ram > 60 or requests > 600:
        status = "MEDIUM LOAD"
        alert = "Server load is increasing."
    else:
        status = "NORMAL"
        alert = "Server is working normally."

    return jsonify({
        "cpu": cpu,
        "ram": ram,
        "requests": requests,
        "status": status,
        "alert": alert
    })

if __name__ == "__main__":
    app.run(debug=True)