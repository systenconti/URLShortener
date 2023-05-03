# URLShortener
Paste long URL to create shorter URL.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Project Status](#project-status)
* [Contact](#contact)


## General Information
This app allows user to shorten their long links. The app uses Flask framework and
PostgreSQL database. App compares if a link passed by user exists in database and if not
it creates new shortened URL and flashes new URL to the user on the website. If the app
finds an existing link in the database it is only flashed on the app's website.


## Technologies Used
- Python - version 3.11
- Flask - version 2.3.2
- Flask-SQLAlchemy - version 3.0.3
- psycopg2-binary - version 2.9.6


## Features
- Paste long URL and get shortened version of it


## Project Status
Project is: _complete_ 


## Contact
Created by [@systenconti](https://github.com/systenconti) - feel free to contact me!
