FROM alpine:latest

# Set the working directory
RUN  echo "Setup the working directory ..."
WORKDIR /db

# Copy scripted download file
RUN echo "Moving files from host to container ..."
COPY download_file.sh /db/

# Download files
RUN echo "Setup dependencies, and instructions to download data ..."
RUN apk update && apk --no-cache add bash curl
RUN bash download_file.sh
RUN echo "Done Setting ${PWD}"