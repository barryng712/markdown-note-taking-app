# markdown-note-taking-app
A Simple Markdown Note-Taking App
=====================================

The markdown-note-taking-app is a web-based application designed to facilitate the creation, editing, and rendering of markdown notes. This app provides a user-friendly interface for users to upload markdown files, check the grammar and spelling of the content, save the note, and render it in HTML format for easy reading.

Features
--------

### Markdown File Upload

The app allows users to upload markdown files directly from their local machine. This feature is particularly useful for users who prefer to write their notes in markdown format and want to manage them in a centralized location.

### Grammar and Spelling Check

The app integrates a grammar and spelling check tool that analyzes the uploaded markdown content and suggests corrections. This feature ensures that the notes are error-free and easy to read.

### Note Saving

Once the markdown content is uploaded and corrected, the app saves the note securely. Users can access their saved notes at any time and make further edits as needed.

### HTML Rendering

The app renders the markdown content in HTML format, making it easy to read and share with others. The HTML rendering feature allows users to view their notes in a visually appealing format, complete with headings, bold text, italics, and other markdown syntax elements.

Technical Details
-----------------

The markdown-note-taking-app is built using Flask, a lightweight Python web framework. The app utilizes the following technologies:

* Flask: For building the web application and handling HTTP requests and responses.
* LanguageTool: For grammar and spelling checks.
* Markdown: For converting markdown content to HTML.
* Flask-JSONify: For handling JSON data exchange between the client and server.

Directory Structure
-------------------

The project directory structure is organized as follows:

* `app.py`: The Flask application file that handles HTTP requests and responses.
* `templates/`: A directory containing HTML templates for the app's user interface.
* `static/`: A directory containing static assets such as CSS, JavaScript, and images.
* `notes/`: A directory where uploaded markdown files are stored.
* `requirements.txt`: A file listing the project's dependencies.
* `README.md`: This file, which provides an overview of the project.

Getting Started
---------------

To use the markdown-note-taking-app, follow these steps:

1. Clone the project repository to your local machine.
2. Install the project dependencies by running `pip install -r requirements.txt`.
3. Run the app by executing `python app.py`.
4. Open a web browser and navigate to `http://localhost:5000` to access the app.

src: https://roadmap.sh/projects/markdown-note-taking-app

