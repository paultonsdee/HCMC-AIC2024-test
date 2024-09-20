# Download data
echo "Downloading data ..."
cd /db
bash download_file.sh
cd ../

# Run backend
echo "Moving to backend, then run backend"
cd /backend
uvicorn main:app --host=0.0.0.0 --port=8000 --reload