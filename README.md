# Duewiger Projects Website

A full-stack website for **Duewiger Projects** built with Django, utilizing Django Template Language (DTL) for dynamic content rendering. This website showcases projects, services, and contact details, with an integrated contact form featuring Google reCAPTCHA to prevent spam. Hosted using Docker, AWS S3 for static and media file storage, and secured with environment variables.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Deployment](#deployment)
- [License](#license)

## Features
- **Dynamic Content:** Uses Django Template Language for rendering dynamic pages.
- **Contact Form:** A fully functional contact form with Google reCAPTCHA validation to prevent spam, integrated with email notifications.
- **Mobile-Responsive Design:** CSS and media queries ensure a responsive layout on mobile devices.
- **Navigation:** Smooth scrolling and navigation bar highlighting based on the active section.
- **AWS S3 Integration:** Static and media files are managed via Amazon S3, configured for performance and scalability.
- **Dockerized Application:** Docker and Docker Compose used for consistent deployment and development environments.
- **Custom Styling:** Custom CSS with a dark theme and animated elements for a modern look and feel.

## Tech Stack
- **Backend:** Django 5.1, Django Template Language
- **Frontend:** HTML, CSS, JavaScript (Boxicons for icons)
- **Form Handling:** Django Forms with Google reCAPTCHA
- **Styling:** Custom CSS, Bootstrap 5 (via `django-crispy-forms`)
- **Deployment:** Docker, Gunicorn, AWS S3 for static and media files
- **Database:** SQLite (for development)

## Setup and Installation

### Prerequisites
- Python 3.11+
- Docker and Docker Compose
- AWS Account (for S3 storage)
- SMTP Server for email (e.g., Gmail, SMTP2GO)

### Step 1: Clone the Repository
```bash
git clone https://github.com/YourUsername/duewiger-projects-website.git
cd duewiger-projects-website
```

### Step 2: Install Dependencies
Make sure to create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a `.env` file in the project root directory and populate it with your configuration:
```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=False
DJANGO_SECURE_SSL_REDIRECT=True
DJANGO_SECURE_HSTS_SECONDS=31536000
DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=True
DJANGO_SECURE_HSTS_PRELOAD=True
DJANGO_SESSION_COOKIE_SECURE=True
DJANGO_CSRF_COOKIE_SECURE=True
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key
DEFAULT_FROM_EMAIL=your-email@example.com
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email-user
EMAIL_HOST_PASSWORD=your-email-password
```

### Step 4: Collect Static Files
```bash
python manage.py collectstatic
```

## Running the Project

### Using Docker
1. **Build and Run:** Use Docker Compose to build and start the container.
   ```bash
   docker-compose up --build
   ```
2. **Access the Website:** Navigate to `http://localhost:8000` in your browser.

### Running Locally (Without Docker)
1. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```
2. **Run the Server:**
   ```bash
   python manage.py runserver
   ```
3. **Access the Website:** Navigate to `http://127.0.0.1:8000` in your browser.

## Deployment
This project is configured to run in a production environment using Docker, AWS S3, and Gunicorn. Follow these steps to deploy:
1. **Build Docker Image:** Use the provided `Dockerfile`.
2. **Upload Static and Media Files:** Collect static files and upload them to your AWS S3 bucket.
3. **Run Docker Compose:** Start the project using `docker-compose.yml`.
4. **Update DNS Settings:** Point your domain to the hosting server IP.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.