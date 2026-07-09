from flask import Flask, render_template, request, jsonify, send_file
import os
from modules.data_extraction import extract_data_from_files
from modules.data_cleaning import clean_and_process_data
from modules.visualization import generate_dashboard
from modules.eda import perform_eda
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'output'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'docx', 'doc', 'txt', 'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        if 'files' not in request.files:
            return jsonify({'error': 'No files uploaded'}), 400
        
        files = request.files.getlist('files')
        theme = request.form.get('theme', 'plotly')
        
        if not files:
            return jsonify({'error': 'No files selected'}), 400
        
        uploaded_paths = []
        for file in files:
            if file and allowed_file(file.filename):
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                uploaded_paths.append(filepath)
        
        if not uploaded_paths:
            return jsonify({'error': 'No valid files uploaded'}), 400
        
        # Extract data from all files
        all_data = extract_data_from_files(uploaded_paths)
        
        if not all_data:
            return jsonify({'error': 'No data could be extracted from uploaded files'}), 400
        
        # Clean and process data
        processed_data = clean_and_process_data(all_data)
        
        # Perform EDA
        eda_results = perform_eda(processed_data)
        
        # Generate dashboard
        dashboard_path = generate_dashboard(processed_data, theme, app.config['OUTPUT_FOLDER'])
        
        return jsonify({
            'success': True,
            'dashboard_url': f'/view_dashboard/{os.path.basename(dashboard_path)}',
            'eda_summary': eda_results
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/view_dashboard/<filename>')
def view_dashboard(filename):
    return send_file(os.path.join(app.config['OUTPUT_FOLDER'], filename))

@app.route('/themes')
def get_themes():
    themes = [
        {'id': 'plotly', 'name': 'Plotly Default'},
        {'id': 'plotly_dark', 'name': 'Plotly Dark'},
        {'id': 'seaborn', 'name': 'Seaborn'},
        {'id': 'ggplot2', 'name': 'GGPlot2'},
        {'id': 'simple_white', 'name': 'Simple White'},
        {'id': 'presentation', 'name': 'Presentation'}
    ]
    return jsonify(themes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
