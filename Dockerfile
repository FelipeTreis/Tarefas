# Base image
FROM python:3.8.10-slim

# Set directory
WORKDIR /app

# Enviroments
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFERED 1

ENV SECRET_KEY $SECRET_KEY 
ENV DEBUG $DEBUG
ENV ALLOWED_HOSTS $ALLOEWD_HOSTS

# Copy libs
COPY requirements.txt . 

# Upgrade pip and install requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project 
COPY . .

# Expose port 8000
EXPOSE 8000

# Run server
CMD python manage.py runserver 0.0.0.0:8000
