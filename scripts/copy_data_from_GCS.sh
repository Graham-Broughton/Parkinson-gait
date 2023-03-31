#!/usr/bin/env bash

echo "Starting the Download"

gsutil -m cp -r gs://parkinson-gait-data/data/* ../data
