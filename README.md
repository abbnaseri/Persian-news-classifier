# Persian News Classifier

## Introduction
This project aims to create a model and system for classifying and perdicting categories of persian news. The classifying part is developed in OOP manners which can be used in any project by adding the module into your code. 

## Reqirements
For this project, it is used programming languages and libraries including:
- Python3
- scikit-learn
- numpy
- pandas
- nltk
- hazm: [You can see it here](https://github.com/sobhe/hazm)
- requests
- beautifulsoup4
- flask

##Performance

| Category      | precision | recall | f1-score | support |
| ------------- | --------- | ------ | -------- | ------- |
| 0             |      0.99 |   0.99 |     0.99 |     299 |
| 1             |      0.93 |   0.93 |     0.93 |     295 |
| 2             |      0.93 |   0.94 |     0.93 |     291 |
| 3             |      0.99 |   0.99 |     0.99 |     307 |
| 4             |      0.99 |   0.98 |     0.98 |     308 |

accuracy: 0.9653333333333334

## Dataset
Dataset has been retrieved from ISNA News Agency in five category:
- cinema
- economy
- politic
- sport
- tech and science

## Aditional parts
The code exports a csv file which includes normalized texts with their labels in each row.
It also saves the model into a pickle file.

## Scraper
Scraper's python code is added into scraper directory. If you want to add new texts, you should give a valid url like: [url](https://www.isna.ir/page/archive.xhtml?mn=4&wide=0&dy=17&ms=0&pi=1&yr=1398&tp=24)

## Install
You can install libararies by running the command `pip install -r reqirements.txt` in cmd-windows or if you are using linux, use pip3 instead of pip.

## Running the code
You can run the code by executing `python3/python app.py`.