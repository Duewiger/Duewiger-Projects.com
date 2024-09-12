FROM python:3.11.7-slim-bullseye

# Set the working directory in the container
WORKDIR /duewiger-projects.com

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Install Gunicorn
RUN pip install gunicorn

# Expose port 8000
EXPOSE 8000

# Default command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "projects_website.wsgi:application"]