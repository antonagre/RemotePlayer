#!/bin/bash
export FLASK_APP=./main.py
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
flask run -h 0.0.0.0 -p 5550
