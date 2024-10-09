#!/bin/sh

# Check if keyframes.csv exists, skip download if found
if [ ! -f "keyframes.csv" ]; then
  echo "Start downloading and extracting files .... "

  # Download dataset from Google Drive
  gdown --id 18Fx1dmi_OJVdGE5ObU8NR08z7DNjCd9n --output dataset.zip

  # Check if download was successful
  if [ $? -eq 0 ]; then
    # Extract dataset
    unzip ./dataset.zip
    rm ./dataset.zip
    echo "Done!"
  else
    echo "Download failed!"
    exit 1
  fi
else
  echo "Found keyframes.csv, skipping download."
fi