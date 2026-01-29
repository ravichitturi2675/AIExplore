from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "codellama"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status', methods=['GET'])
def check_status():
    """Checks connections to critical services (Ollama)."""
    status = {"ollama": "disconnected", "model": MODEL_NAME}
    try:
        # Check if Ollama is up (using tags endpoint as a lightweight check)
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            status["ollama"] = "connected"
    except Exception as e:
        status["error"] = str(e)
    return jsonify(status)

@app.route('/api/convert', methods=['POST'])
def convert_code():
    data = request.json
    java_code = data.get('java_code', '')
    
    if not java_code:
        return jsonify({"error": "No code provided"}), 400

    from converter import JavaToPlaywrightConverter
    converter = JavaToPlaywrightConverter()
    result = converter.convert(java_code)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

