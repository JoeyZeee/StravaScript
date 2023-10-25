# StravaScript: Bard-Powered Text

StravaScript is a small Flask project that interfaces with the unofficial Bard API. You can upload a GPX file, and the program outputs the raw longitude and latitude values of that activity. Bard then takes that as an input, and generates an activity title and description, for running social medias like Strava.

## For Joey...

Add this code into the main javascript file, so it puts the coordinates data into the file:

```
var fs = require("fs");

let fInput = "Test";
fs.writeFile('Coordinates.txt', fInput, (err) => {
	 if (err) throw err;
	 else{
			console.log("The file is updated with the coordinate data");
	 }
})
```

(Delete this from the README.md page after putting it in)

## Downloading

1. Download and unzip these project files
   
2. Open this project in your code editor
   
3. Enter: `pip install -r requirements.txt` into your terminal

4. Run: `python3 main.py` in your terminal, and access the Flask live [server](http://127.0.0.1:5000/)

5. Enjoy!

## Usage

1. Download GPX data from wherever your activity is stored (Make sure it has a .gpx tag, or the program won't work)
   
2. Upload that file into the website
   
3. Copy the title and description into your Strava Activity

4. Adjust however nessecary for you
  
## Roadmap

- Add Strava API interfacing

- Automatically upload name and description
  
- Better UI

## Links

- Built for the [Congressional App Challenge](https://www.congressionalappchallenge.us/students/#prizes)
- [Unofficial Bard API](https://github.com/dsdanielpark/Bard-API/tree/alpha-release)
- [Google Bard](https://bard.google.com/chat/)
- [@JoeyZeee](https://www.github.com/joeyzeee)

