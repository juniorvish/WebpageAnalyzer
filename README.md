# WebpageAnalyzer

WebpageAnalyzer is a web application that allows users to enter a URL of any webpage and displays a paragraph explaining what the company actually does.

## Installation

1. Clone the repository:

```
git clone https://github.com/juniorvish/WebpageAnalyzer.git
```

2. Change directory to the project folder:

```
cd WebpageAnalyzer
```

3. Install the required Python packages:

```
pip install -r backend/requirements.txt
```

## Usage

1. Start the backend server:

```
python backend/server.py
```

2. Open the `frontend/index.html` file in your web browser.

3. Enter a URL in the input field and click the "Analyze" button to get the company description.

## Project Structure

- `frontend/index.html`: The main HTML file containing the structure of the web application.
- `frontend/css/styles.css`: The CSS file containing the styles for the web application.
- `frontend/js/main.js`: The JavaScript file containing the logic for handling user input and displaying the result.
- `backend/server.py`: The Python file containing the backend logic for processing the URL and returning the company description.
- `backend/requirements.txt`: The file containing the required Python packages for the backend.

## Dependencies

- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask, BeautifulSoup, OpenAI API
- UI: Tailwind CSS (if required)