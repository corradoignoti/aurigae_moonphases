FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app/ ./app

# Expose the port the app runs on
EXPOSE 5050

# Set the environment variable for Flask
ENV FLASK_APP=app/main.py

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5050"]