FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /backend

COPY . /backend/
# COPY .env /backend/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir