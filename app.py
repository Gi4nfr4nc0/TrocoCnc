from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def calcolo_trocoidale(d, width, pct):
    step = (d * pct) / 100.0
    passes = math.ceil((width - d) / step) + 1
    return round(step, 2), passes

@app.route('/api')
def api():
    try:
        d = float(request.args.get('fresa'))
        w = float(request.args.get('cava'))
        p = float(request.args.get('impegno'))
    except (TypeError, ValueError):
        return jsonify({"error": "Parametri errati"}), 400

    step, passes = calcolo_trocoidale(d, w, p)
    return jsonify({"step_mm": step, "passate": passes})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
