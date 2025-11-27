# Homework TODO List Application

A simple and interactive TODO list web application built with Django, featuring add, toggle completion, and visual status indicators.

## Features

- ✅ Add new TODO items
- 🔘 Toggle completion status with a single click
- 📝 Visual indicators (strikethrough for completed items)
- 🎨 Clean, minimal user interface

## Project Structure

```
01-overview/
├── homework/           # Django project configuration
│   ├── settings.py    # Project settings
│   ├── urls.py        # Main URL configuration
│   └── wsgi.py        # WSGI configuration
├── todo/              # TODO app
│   ├── models.py      # Todo model definition
│   ├── views.py       # View functions (list, add, toggle)
│   ├── urls.py        # App URL patterns
│   ├── templates/     # HTML templates
│   │   ├── base.html
│   │   └── todo/
│   │       └── home.html
│   └── migrations/    # Database migrations
├── manage.py          # Django management script
├── pyproject.toml     # Project dependencies
└── db.sqlite3         # SQLite database
```

## How It Was Made

This project was created using:
- **Django 5.2.8** - Python web framework
- **SQLite** - Database backend
- **uv** - Python package manager

The TODO app includes:
1. A `Todo` model with fields: title, due_date, and completed status
2. Three views: `todo_list` (display), `add_todo` (create), and `toggle_todo` (update)
3. URL routing for each action
4. HTML templates with inline CSS for styling
5. Form handling with CSRF protection

## Prerequisites

- Python 3.12 or higher
- uv (Python package manager)

## Installation & Setup

1. **Clone or navigate to the project directory:**
   ```bash
   cd /ai-dev-tools-zoomcamp/cohorts/2025/01-overview
   ```

2. **Create and activate a virtual environment:**
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   uv sync
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your browser and navigate to: `http://127.0.0.1:8000/`

## Usage

### Adding a TODO Item
1. Type your task in the input field
2. Click the "Add" button
3. The new item appears in the list

### Toggling Completion Status
1. Click the button next to any TODO item
2. ○ (circle) = incomplete
3. ✓ (checkmark) = completed
4. Completed items are shown with strikethrough text

## Development

### Creating a Superuser (for Django Admin)
```bash
python manage.py createsuperuser
```

### Accessing the Admin Panel
Navigate to `http://127.0.0.1:8000/admin/` after creating a superuser.

### Running in Production
For production deployment, use a WSGI server like Gunicorn:
```bash
uv sync --group prod
gunicorn homework.wsgi:application
```

## Technologies Used

- Django 5.2.8
- Python 3.12
- SQLite
- HTML/CSS
- Django Template Language

## License

This project is part of the AI Dev Tools Zoomcamp coursework.
