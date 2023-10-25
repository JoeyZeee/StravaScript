document.getElementById("upload-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    const gpxFileInput = document.getElementById("gpx-file");
    const outputElement = document.getElementById("output");
    const bardElement = document.getElementById("bard");

    outputElement.textContent = "Loading...";
    bardElement.textContent = "Loading...";

    const file = gpxFileInput.files[0];

    if (file) {
        const text = await file.text();
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(text, "text/xml");

        let coordinatesString = 'Longitude and Latitude Coordinates:';

        const trkptElements = xmlDoc.querySelectorAll('trkpt');
        for (const trkpt of trkptElements) {
            const lat = trkpt.getAttribute('lat');
            const lon = trkpt.getAttribute('lon');
            coordinatesString += `\n${lat},${lon}`;
        }

        coordinatesString = coordinatesString.trim();

        outputElement.textContent = coordinatesString;
        bardElement.textContent = "Bard Response: ";
    } else {
        outputElement.textContent = "Please select a GPX file.";
        bardElement.textContent = "NA";
    }
});
