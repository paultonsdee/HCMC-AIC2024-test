 FROM ubuntu:20.04

# Set the working directory
WORKDIR /backend

# Copy files from local to container
COPY /app .
COPY requirements.txt .

# Setup environments
RUN apt-get update && apt-get install -y python3.9 python3.9-dev
RUN pip install --upgrade pip


# Setup libraries
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip install -r requirements.txt --no-cache-dir