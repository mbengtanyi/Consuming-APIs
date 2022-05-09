#!/bin/bash

#This script is a basic setup of a virtual environment and a few dependency installs when starting a new python project

#Uncomment next line to be sure you're setting up the correct directory
#pwd

#create virtual environment
python3 -m venv .venv

#activate virtual environment
source .venv/bin/activate

#flask install (if necessary)
python3 -m pip install flask
pip install flask-sqlalchemy

#Putting all project dependencies in a file named requirements.txt
python3 -m pip3 freeze >> requirements.txt