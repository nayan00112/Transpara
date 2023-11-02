
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

Creation of virtualenvironment:
- Install virtualenv:
```bash
pip install virtualenv
```

- Create a virtual environment now,
```bash
virtualenv -p /usr/bin/python3.9 virtualenv_name
```

- Activate virtualenvironment:
```bash
cd virtualenv_name
cd Scripts
activate
cd ../..
```
- Now, goto Transpara project root folder, and install all requirements:

```bash
pip install -r requirements.txt
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

Done!