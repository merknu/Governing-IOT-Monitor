import requests
import zipfile
import os

def update_models(model_folder, base_url):
    model_version_url = base_url + "/version.txt"
    response = requests.get(model_version_url)
    latest_version = response.text.strip()
    local_version_file = os.path.join(model_folder, "version.txt")
    if os.path.exists(local_version_file):
        with open(local_version_file, "r") as f:
            local_version = f.read().strip()
        if local_version == latest_version:
            print("Model files are already up to date.")
            return
    model_zip_url = base_url + "/model_files.zip"
    response = requests.get(model_zip_url)
    model_zip = zipfile.ZipFile(io.BytesIO(response.content))
    model_zip.extractall(model_folder)
    with open(local_version_file, "w") as f:
        f.write(latest_version)
    print("Model files updated successfully.")
