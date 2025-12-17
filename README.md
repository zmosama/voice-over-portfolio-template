# Basma Portfolio

A portfolio website for Voice Over artist **Basma**, built with Django, Unfold Admin, and Tailwind CSS.

## Features
- **Portfolio Showcase**: Listen to audio clips with a custom player.
- **Modern UI**: Dark themed, high-contrast design (Deep Navy + Neon Pink).
- **Admin Panel**: customized using `django-unfold`.

## Setup

1.  **Clone the repository**
2.  **Create Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run Migrations**:
    ```bash
    python manage.py migrate
    ```
5.  **Create Superuser**:
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run Server**:
    ```bash
    python manage.py runserver
    ```

## Technolgies
- Django 5.x
- Tailwind CSS
- SQLite
