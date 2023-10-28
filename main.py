from flask import Flask, request, render_template
from bardapi import Bard
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Read the contents of the "BardAnswer.txt" file
    answer_file_path = os.path.join('responses', 'BardAnswer.txt')
    with open(answer_file_path, 'r') as answer_file:
        bard_answer = answer_file.read()

    return render_template('index.html', bard_answer=bard_answer)

@app.route('/upload', methods=['POST'])
def upload_txt():
    txt_file = request.files['txt_file']

    if 'txt_file' not in request.files:
        return 'No file part'

    if txt_file.filename == '':
        return 'No selected file'

    # Define the path where you want to save the file
    file_path = os.path.join('uploads', txt_file.filename)

    # Delete any existing files in the "uploads" folder
    existing_files = os.listdir('uploads')
    for existing_file in existing_files:
        existing_file_path = os.path.join('uploads', existing_file)
        try:
            os.remove(existing_file_path)
        except Exception as e:
            print("Error deleting existing file:", str(e))

    if txt_file:
        # Get the contents of the uploaded file
        file_contents = txt_file.read()

        # Save the new file
        with open(file_path, 'wb') as f:
            f.write(file_contents)

        token = 'cgiPsMSxouMUxto8TTqyhgXvrDU8TTZHQnptASvJN3G4XKDgDLDkRNGOyzfaVbBQuvlXvg.'
        bard = Bard(token=token)
        answer = bard.get_answer("How you doing?")['content']

        # Delete any existing files in the "responses" folder
        existing_files = os.listdir('responses')
        for existing_file in existing_files:
            existing_file_path = os.path.join('responses', existing_file)
            try:
                os.remove(existing_file_path)
            except Exception as e:
                print("Error deleting existing file:", str(e))

        # Save the BARD API answer into a text file
        answer_file_path = os.path.join('responses', 'BardAnswer.txt')
        with open(answer_file_path, 'w') as answer_file:
            answer_file.write(answer)
        
        return render_template('index.html', bard_answer=answer)  # Fix the indentation here

if __name__ == '__main__':
    app.run(debug=True)
