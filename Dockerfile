# Pull official Python Docker image
FROM --platform=linux/amd64 python:3.11.7-slim

# Set the working directory
WORKDIR /code

# Install unix dependecies
RUN apt-get update

# Install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Copy all files
COPY ./src ./src

# Copy start script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Run start script
CMD ["/start.sh"]
