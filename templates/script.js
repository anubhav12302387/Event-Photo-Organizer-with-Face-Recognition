const SERVER_URL = "http://127.0.0.1:5000/upload"; 

document.getElementById('uploadForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const responseDiv = document.getElementById('response');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const responseMessage = document.getElementById('responseMessage');

    responseDiv.classList.remove('error', 'success');
    responseMessage.textContent = ''; 

    if (!file) {
        alert("Please select a file to upload.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    loadingIndicator.classList.remove('hidden');
    responseDiv.classList.add('hidden');
    toggleFormState(true); 

    fetch(SERVER_URL, {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            loadingIndicator.classList.add('hidden');
            responseDiv.classList.remove('error', 'success', 'loading'); 

            if (data.error) {
                responseDiv.classList.add('error');
                responseMessage.textContent = `Error: ${data.error}`;
            } else {
                responseDiv.classList.add('success');
                responseMessage.innerHTML = `Success: ${data.message}<br>Matched with: ${data.matched_with || 'N/A'}`;
            }
            responseDiv.classList.remove('hidden');
        })
        .catch((error) => {
            console.error("Error uploading file:", error);
            loadingIndicator.classList.add('hidden');
            responseDiv.classList.add('error');
            responseMessage.textContent = "An error occurred during upload.";
            responseDiv.classList.remove('hidden');
        })
        .finally(() => {
            toggleFormState(false); 
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