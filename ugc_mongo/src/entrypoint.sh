#!/bin/bash

cd /app

gunicorn main:app --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker
