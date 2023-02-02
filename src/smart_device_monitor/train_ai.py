import os

def find_model_folders():
    model_folder = 'data/model_files/'
    model_folders = []
    for subdir, dirs, files in os.walk(model_folder):
        for dir in dirs:
            model_folders.append(subdir + '/' + dir)
    return model_folders
