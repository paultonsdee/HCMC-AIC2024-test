#!/bin/bash

# Load the JSON file
JSON_FILE="kaggle.json"
if [ ! -f "$JSON_FILE" ]; then
  echo "Error: $JSON_FILE not found."
  exit 1
fi

# Load the JSON data and set the environment variables
KAGGLE_USERNAME=$(jq -r '.username' "$JSON_FILE")
KAGGLE_KEY=$(jq -r '.key' "$JSON_FILE")

# Install `kaggle` Python SDK for downloading dataset via kaggle command.
# Install kaggle SDK
pip install kaggle || {
  echo "Error installing kaggle SDK. Check your pip installation."
  exit 1
}

# Download dataset
kaggle datasets download pyetsvu/aic2024-extracted-data --path ./ --unzip || {
  echo "Error downloading dataset. Check your kaggle credentials and network connection."
  exit 1
}

# Remove .zip file
rm -f ./aic2024-extracted-data.zip || {
  echo "Error removing .zip file. Check your file system permissions."
  exit 1
}

# Uninstall kaggle SDK
pip uninstall kaggle || {
  echo "Error uninstalling kaggle SDK. Check your pip installation."
  exit 1
}