# Pull base image
FROM python:3.14.7-bookworm

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY srcs/backend/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

# Copy project
COPY srcs/backend .

