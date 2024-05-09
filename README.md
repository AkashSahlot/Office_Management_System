# **Office Management System (Django Project)**

This Django project is designed to manage employee data for an office environment. It provides basic CRUD functionality to add, filter, display, and delete employee records.

**Features**
Add Employee: Add new employee details to the system.
Filter Employee: Filter employees based on certain criteria (e.g., department, role).
Show Employee: Display employee details.
Delete Employee: Remove an employee from the system.

**Setup Instructions**

**Prerequisites**
Python (3.x recommended)
Django (3.x recommended)

**Installation**
Clone the repository:

git clone https://github.com/AkashSahlot/Office_Management_System.git

**Navigate to the project directory**:

cd Office_Management_System

**Create a virtual environment (optional but recommended):**

python3 -m venv .venv
source .venv/bin/activate  # Activate virtual environment (Linux/macOS)
**or**
.venv\Scripts\activate  # Activate virtual environment (Windows)

**Install dependencies:**
pip install -r requirements.txt

**Apply database migrations:**
python manage.py migrate
**Create a superuser (admin user) to access the Django admin interface:**
python manage.py createsuperuser

**Start the development server:**

python manage.py runserver
Access the application in your web browser at http://127.0.0.1:8000/.

**To access the Django admin interface (for managing employees):**
Navigate to http://127.0.0.1:8000/admin/ in your browser.
Log in using the superuser credentials created earlier.

**Project Structure**
/employees: Django app for managing employee-related functionality.
/templates: HTML templates for rendering views.
/static: Static files (e.g., CSS, JavaScript).

**Contributing**
Contributions are welcome! If you find a bug or want to enhance this project, feel free to submit a pull request.
