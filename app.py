from flask import Flask, render_template, request, redirect, jsonify
import language_tool_python
import markdown
import os

app=Flask(__name__)
tool = language_tool_python.LanguageToolPublicAPI('en-US')
NOTES_DIR = 'notes'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error":"No file part"}), 400
    
    file=request.files['file']
    if file.filename == '':
        return jsonify({"error":"No selected file"}), 400
    if not file.filename.endswith('.md'):
        return jsonify({"error":"Invalid file format"}), 400

    file.save(f'{NOTES_DIR}/{file.filename}')
    try:
        with open(f'{NOTES_DIR}/{file.filename}', 'r') as f:
            content = f.read()
            matches = tool.check(content)
            corrected= tool.correct(content)
            return jsonify({
                "message":"File upload successfully",
                "corrections": matches,
                "corrected_content": corrected
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/save", methods=['POST'])
def save():
    data = request.get_json()
    filename= data.get('filename')
    content = data.get('content')
    
    try:
        with open(f"{NOTES_DIR}/{filename}", 'w') as f:
            f.write(content)
        return jsonify({'message': 'notes successfully saved'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route("/list")
def list():
    try:
        notes=os.listdir(NOTES_DIR)
        return jsonify({'notes': notes})
    except Exception as e:
        return jsonify({'error': str(e)}),500
    
@app.route("/render/<filename>")
def render(filename):
    try:
        with open(f'{NOTES_DIR}/{filename}', 'r') as f:
            content = f.read()
            html_content = markdown.markdown(content)
            return render_template('render.html', content= html_content)
    except FileNotFoundError:
        return jsonify({'error': 'file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__== "__main_":
    app.run(debug=True)