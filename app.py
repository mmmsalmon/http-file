"""
Relevant commands:
sudo firewall-cmd --zone=public --add-port=5000/tcp
sudo firewall-cmd --reload
python app.py
python -m http.server -d uploads 5000 # send file from computer to device
"""

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the folder to save uploaded files
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_files():
    # Check if the post request has the file part
    if "files[]" not in request.files:
        return "No file part"

    files = request.files.getlist("files[]")

    for file in files:
        if file.filename == "":
            continue  # Skip if no file is selected
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

    return redirect(url_for("index"))


if __name__ == "__main__":
    # Run the app on all available IPs (0.0.0.0) and port 5000
    app.run(host="0.0.0.0", port=5000)
