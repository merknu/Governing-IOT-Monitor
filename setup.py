from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Cogz',
    version='0.1.0',
    author='Author Name',
    author_email='author@email.com',
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
