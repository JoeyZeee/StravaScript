from flask import Flask, request, render_template
from bardapi import Bard
import os

app = Flask(__name__)

file_path = os.path.join('responses', 'BardAnswer.txt')
with open(file_path, 'w', encoding='utf-8') as f:  # Open the file in write mode with encoding
    f.write("")

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
        file_contents = txt_file.read().decode('utf-8')  # Decode bytes to string

        # Save the new file
        with open(file_path, 'w', encoding='utf-8') as f:  # Open the file in write mode with encoding
            f.write(file_contents)

        token = 'xxxxxxxx' # Change this to your __Secure-1PSID Token (See README.md) for more deatails...
        bard = Bard(token=token)
        question = file_contents
        answer = bard.get_answer("Generate a Strava Activity Name and Description from these coordinates: " + question + ". Don't ever include the distance of the activity, or the type of the activity. ALso never generate a google maps link for the activity.")['content']

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
        with open(answer_file_path, 'w', encoding='utf-8') as answer_file:  # Open the file with encoding
            answer_file.write(answer)
        
        return render_template('index.html', bard_answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
