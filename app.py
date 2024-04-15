from flask import Flask, render_template, request, redirect, url_for, flash, session
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Essential for session management

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['datafile']
    delimiter = request.form.get('delimiter', ',')  # Default to comma if not specified
    if not file:
        flash('No file part')
        return redirect(request.url)
    try:
        # Assuming the file is a plain text file with a specified delimiter
        df = pd.read_csv(file, delimiter=delimiter)
        # Convert DataFrame to CSV format in-memory (could save to disk if needed)
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)
        session['dataframe'] = csv_buffer.getvalue()  # Storing CSV data in session
        columns = df.columns.tolist()
        return render_template('select_columns.html', columns=columns)
    except Exception as e:
        flash('Failed to process file: ' + str(e))
        return redirect(url_for('index'))

@app.route('/plot', methods=['POST'])
def plot():
    selected_columns = request.form.getlist('columns')
    csv_data = session.get('dataframe')
    df = pd.read_csv(io.StringIO(csv_data))
    
    img = io.BytesIO()
    df[selected_columns].hist()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf-8')
    
    return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)

