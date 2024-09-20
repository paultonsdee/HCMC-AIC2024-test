 FROM python:3.10-slim

# Set the working directory
RUN  echo "Setup the working directory ..."
WORKDIR /backend

# Copy files from local to container
RUN echo "Moving files from host to container ..."
# COPY /app /backend/
# COPY requirements.txt /backend
COPY . /backend/

# Setup environments
RUN echo "Setup environments"
RUN pip install --upgrade pip


# Setup libraries
RUN echo "Setup libraries and dependencies ..."
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip install -r requirements.txt --no-cache-dir
RUN echo "Done Setting ${PWD}"