# StravaScript: Bard-Powered Text

StravaScript is a small Flask project that interfaces with the unofficial Bard API. You can upload a GPX file, and the program outputs the raw longitude and latitude values of that activity. Bard then takes that as an input, and generates an activity title and description, for running social medias like Strava.

## Downloading

1. Download and unzip these project files
   
2. Open this project in your code editor
   
3. Enter: `pip install -r requirements.txt` into your terminal

4. Go to [https://bard.google.com/chat](https://bard.google.com/chat)

5. Use `Fn + F12`, and navigate to Application, and then Cookies

6. Copy the __Secure-1PSID cookie into `main.py` before running the program

7. Run: `python3 main.py` in your terminal, and access the Flask live [server](http://127.0.0.1:5000/)

8. Enjoy!

## Usage

1. Download GPX data from wherever your activity is stored (Make sure it has a .gpx tag, or the program won't work)
   
2. Upload that file into the website

3. Accept the second download of the longitude and latitude

4. Upload that second file into the website

5. Wait for Bard's response (5-10 Seconds)
   
6. Copy the title and description into your Strava Activity

7. Adjust, or rerun however many times you need

## Debugging Issues

Read the issues at the [Bard API Github:](https://github.com/dsdanielpark/Bard-API/issues)

Contact [jzambreno@gmail.com](jzambreno@gmail.com) for other issues
  
## Roadmap

- Add Strava API interfacing

- Automatically upload name and description

## Links

- Built for the [Congressional App Challenge](https://www.congressionalappchallenge.us/students/#prizes)
- [Unofficial Bard API](https://github.com/dsdanielpark/Bard-API/tree/alpha-release)
- [Google Bard](https://bard.google.com/chat/)
- [@JoeyZeee](https://www.github.com/joeyzeee)

