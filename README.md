## Overview
This project is used for job site crawling by using python scrapy frame work.

## Why this project

The purpose of project to crawl data and store in database.

## Features
* python scrapy crawler
* store crawl data in database
* Before crawl sanitize data


## Using library( before run this project install those library)
* scrapy
* SQLAlchemy
* psycopg2
* beautiful soup


## Project Structure
        ├── jobsbot
        │   ├── __init__.py
        │   ├── __init__.pyc
        │   ├── items.py
        │   ├── middlewares.py
        │   ├── models.py
        │   ├── pipelines.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-35.pyc
        │   │   ├── items.cpython-35.pyc
        │   │   ├── models.cpython-35.pyc
        │   │   ├── pipelines.cpython-35.pyc
        │   │   └── settings.cpython-35.pyc
        │   ├── settings.py
        │   ├── settings.pyc
        │   └── spiders
        │       ├── allj.py
        │       ├── bdgovjob.py
        │       ├── govtjob.py
        │       ├── __init__.py
        │       ├── pvtjob.py
        │       └── __pycache__
        │           ├── allj.cpython-35.pyc
        │           ├── bdgovjob.cpython-35.pyc
        │           ├── govtjob.cpython-35.pyc
        │           ├── __init__.cpython-35.pyc
        │           └── pvtjob.cpython-35.pyc
        ├── README.md
        └── scrapy.cfg


