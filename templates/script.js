const SERVER_URL = "http://127.0.0.1:5000/upload"; // Use a constant for server URL

document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const responseDiv = document.getElementById('response');

    // Reset response div
    responseDiv.classList.remove('error', 'success');
    responseDiv.textContent = ''; // Clear previous messages

    if (!file) {
        alert("Please select a file to upload.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    // Show loading feedback
    responseDiv.textContent = "Uploading... Please wait.";
    responseDiv.classList.add('loading'); // Add a class for potential spinner styling
    toggleFormState(true); // Disable form elements

    fetch(SERVER_URL, {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            responseDiv.classList.remove('error', 'success', 'loading'); // Reset classes

            if (data.error) {
                responseDiv.classList.add('error');
                responseDiv.textContent = `Error: ${data.error}`;
            } else {
                responseDiv.classList.add('success');
                responseDiv.innerHTML = `Success: ${data.message}<br>Matched with: ${data.matched_with || 'N/A'}`;
            }
        })
        .catch((error) => {
            console.error("Error uploading file:", error);
            responseDiv.classList.remove('loading');
            responseDiv.classList.add('error');
            responseDiv.textContent = "An error occurred during upload.";
        })
        .finally(() => {
            toggleFormState(false); // Re-enable form elements
        });
});

/**
 * Toggles the form state (disable/enable inputs and button).
 * @param {boolean} isDisabled - Whether to disable or enable the form.
 */
function toggleFormState(isDisabled) {
    const fileInput = document.getElementById('fileInput');
    const uploadButton = document.getElementById('uploadButton');
    fileInput.disabled = isDisabled;
    uploadButton.disabled = isDisabled;
}
