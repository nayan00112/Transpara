
# Transpara

Expand your vocabulary!


## Documentation

<!-- [Documentation](https://linktodocumentation) -->

Greetings everyone,

Transpara is an innovative language tool designed to enhance your linguistic experience. This document outlines the comprehensive set of specifications that will guide the development of this remarkable application.

Transpara aims to bridge linguistic barriers by offering users a platform to effortlessly explore the meanings of individual words from diverse languages. Users can submit paragraphs, and the application will seamlessly break down the text into unique words, providing their meanings in other languages.
## Features

- Multiple Languages (Hindi, Gujarati, Tamil, Telugu, German, Italian, Arabic, Russian, Korean, French, Spanish, and Japanese)
- Print (pdf)
- Authentication
- Edit user profile
- History 
- Responsive


## Installation
python libraries:

- Creation of virtualenvironment:
```bash
python -m venv myenv
```
(Replace myenv with the name you want to give your virtual environment and wait for the virtual environment to be created.)

Once you have created the virtual environment, you can activate it by running the appropriate command based on your operating system:

- On Linux and macOS, run:

```bash
source myenv/bin/activate
```
- On Windows, run:
```bash
myenv\Scripts\activate.bat
```
Install all requirement libraries for django project.

```bash
pip install -r requirement.txt
```


- For database:
```bash
cd Transpara
python manage.py makemigrations
python manage.py migrate
```
    
- Run django project:
```bash
python manage.py runserver
```

