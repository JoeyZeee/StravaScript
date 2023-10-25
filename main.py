from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Define the directory where uploaded GPX files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
		os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
		return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_gpx():
		if 'gpx_file' not in request.files:
				return 'No file part'

		gpx_file = request.files['gpx_file']

		if gpx_file.filename == '':
				return 'No selected file'

		if gpx_file:
				file_path = os.path.join(app.config['UPLOAD_FOLDER'], gpx_file.filename)
				gpx_file.save(file_path)
				return 'GPX file uploaded successfully'

if __name__ == '__main__':
		app.run(debug=True)
