document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file to upload.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        const responseDiv = document.getElementById('response');
        responseDiv.classList.remove('error', 'success');

        if (data.error) {
            responseDiv.classList.add('error');
            responseDiv.textContent = `Error: ${data.error}`;
        } else {
            responseDiv.classList.add('success');
            responseDiv.innerHTML = `Success: ${data.message}<br>Matched with: ${data.matched_with || 'N/A'}`;
        }
    })
    .catch(error => {
        console.error("Error uploading file:", error);
        document.getElementById('response').classList.add('error');
        document.getElementById('response').textContent = "An error occurred during upload.";
    });
});
