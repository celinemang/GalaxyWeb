# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import pandas as pd

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
@cross_origin(origins=['http://localhost:3000']) 
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # 파일을 불러와서 첫 5줄만 읽기
        try:
            data = pd.read_csv(file_path)
            file_data = data.head().to_json(orient='records')
            return jsonify({"fileData": file_data})
        except Exception as e:
            return jsonify({"error": f"Failed to read file: {str(e)}"}), 500
    return "File uploaded successfully", 200
    

def upload():
    return "Upload finish", 200

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
