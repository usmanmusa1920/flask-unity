#!/bin/sh

flaskunity db makemigrations

flaskunity db migrate

python3 run.py boot --port 7000 --debug True --host 0.0.0.0
