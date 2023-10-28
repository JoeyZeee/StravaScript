from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-page')
def upload_page():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_txt():
    txt_file = request.files['txt_file']

    if 'txt_file' not in request.files:
        return 'No file part'

    if txt_file.filename == '':
        return 'No selected file'

    # Define the path where you want to save the file
    file_path = os.path.join('uploads', txt_file.filename)

    # Debug: Print the file path before deleting
    #print("File path:", file_path)

    # Delete any existing files in the "uploads" folder
    existing_files = os.listdir('uploads')
    for existing_file in existing_files:
        existing_file_path = os.path.join('uploads', existing_file)
        try:
            os.remove(existing_file_path)
            #print("Deleted existing file:", existing_file_path)
        except Exception as e:
            print("Error deleting existing file:", str(e))

    if txt_file:
        # Get the contents of the uploaded file
        file_contents = txt_file.read()

        # Save the new file
        with open(file_path, 'wb') as f:
            f.write(file_contents)

        return 'Text file uploaded and saved successfully'

if __name__ == '__main__':
    app.run(debug=True)
