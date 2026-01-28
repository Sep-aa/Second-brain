# Second Brain (Django)

A personal Second Brain built with Django for managing notes, school assignments, and deadlines in one place.
The project focuses on structure, clarity, and extensibility rather than complexity.

Features

📝 Notes

Create, edit, and organize text-based notes

Support for categories and tags

📚 Assignments

Track school assignments with subject, description, and status

Link assignments to relevant notes

⏰ Deadlines

Manage due dates with priority and visual overview

📊 Dashboard

Overview of active assignments, upcoming deadlines, and recent activity

Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript

Database: SQLite (development)

Other: Django Templates, Django ORM

Project Goals

Build a practical personal productivity system

Practice backend-driven web application design with Django

Emphasize clean data models and maintainable architecture

Keep the system lightweight and easy to extend

Status

🚧 Work in progress
This project is actively being developed and refined. Features and structure may change.

Planned Features

Search across notes and assignments

Improved tagging and filtering

Authentication and multi-user support

Better UI/UX for the dashboard

Optional Markdown support for notes

Getting Started
# Clone the repository
git clone https://github.com/yourusername/second-brain-django.git
cd second-brain-django

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver


Then open http://127.0.0.1:8000/ in your browser.

License

This project is for personal and educational use.
License to be defined.
