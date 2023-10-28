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

        let coordinatesString = 'Longitude and Latitude Coordinates:\n';

        const trkptElements = xmlDoc.querySelectorAll('trkpt');
        const maxCoordinates = 100; // Set the maximum number of coordinates you want to include

        for (let i = 0; i < Math.min(maxCoordinates, trkptElements.length); i++) {
            const trkpt = trkptElements[i];
            const lat = trkpt.getAttribute('lat');
            const lon = trkpt.getAttribute('lon');
            coordinatesString += `\n${lat},${lon}`;
        }

        coordinatesString = coordinatesString.trim();

        outputElement.textContent = coordinatesString;

        // Create a Blob with the coordinates string
        const blob = new Blob([coordinatesString], { type: 'text/plain' });

        // Create a temporary anchor element for the download
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'coordinates.txt';

        // Trigger a click event on the anchor to initiate the download
        a.style.display = 'none';
        document.body.appendChild(a);
        a.click();

        // Remove the temporary anchor
        document.body.removeChild(a);
        
    } else {
        outputElement.textContent = "Please select a GPX file.";
        bardElement.textContent = "NA";
    }
});
