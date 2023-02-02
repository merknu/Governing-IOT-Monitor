# setup.py
from setuptools import setup, find_packages

import model_updater

if name == "main":
    model_folders = [
    ("data/model_files/avatar", "https://example.com/avatar_models"),
    ("data/model_files/lip_sync", "https://example.com/lip_sync_models"),
    ("data/model_files/voice_recognition", "https://github.com/mozilla/DeepSpeech/releases/download/v0.9.4/deepspeech-0.9.4-models.pbmm", "https://github.com/mozilla/DeepSpeech/releases/download/v0.9.4/deepspeech-0.9.4-models.scorer")    ]
for folder, url in model_folders:
model_updater.update_models(folder, url)


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Cogz',
    version='0.1.0',
    author='Knut Ingmar Merødningen',
    author_email='merodningen.design@gmail.com',
    description='A smart device monitor program that works like a personal assistant',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/author/Cogz',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'influxdb',
        'paho-mqtt',
        'python-snmp',
        'pygame',
        'gTTS',
        'SpeechRecognition',
        'numpy',
        'opencv-python'
    ],
    entry_points={
        'console_scripts': [
            'cogz=cogz.__main__:main',
        ],
    }
)
