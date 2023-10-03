
# Transpara

Expand your vocabulary!


## Documentation

[Documentation](https://linktodocumentation)

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

Install googletrans library:

```bash
pip install googletrans==3.1.0a0
```
    
Install PyDictionary library:

```bash
pip install PyDictionary
```

For database:
```bash
cd Transpara
python manage.py makemigrations
python manage.py migrate
```
    
Run django project:
```bash
python manage.py runserver
```

