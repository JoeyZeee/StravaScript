from flask import Flask, request, render_template
from bardapi import Bard
import os

app = Flask(__name__)

token = 'cQiPsFSGiWDV4J_Oh9EPUI03XQRb_Tnnc6n5H_DkfuT3pgCp06FnZ6J6cnWHvp8SxRcKwA.'
question = "Hi! How are you today?"

print(Bard(token, timeout=10).get_answer(question)['content'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_gpx():
    if 'gpx_file' not in request.files:
        return 'No file part'

    #gpx_file = request.files['gpx_file']

    if gpx_file.filename == '':
        return 'No selected file'

    if gpx_file:
        return 'GPX file uploaded successfully'

        return 'File uploaded and saved as coordinates.txt'

if __name__ == '__main__':
    app.run(debug=True)
