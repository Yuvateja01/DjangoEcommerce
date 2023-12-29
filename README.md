
# Django Ecommerce Backend with Swagger Documentation and Unit Tests (Pytest)

This repository contains a Django-based Ecommerce Backend with Swagger documentation and unit tests implemented using Pytest.

## Local Setup Instructions

```bash
# Clone the Repository
git clone https://github.com/Yuvateja01/DjangoEcommerce.git

# Create a Virtual Environment
python -m venv venv

# Activate the Virtual Environment (Windows)
venv\Scripts\activate

# Activate the Virtual Environment (macOS/Linux)
source venv/bin/activate

# Navigate to the Project Directory
cd drfecom

# Install Required Packages
pip install -r requirements.txt

# Run the Django Development Server
python manage.py runserver
```

## Swagger/API Documentation

Access the API documentation using the following endpoints:

- **API YAML File:** [127.0.0.1:8000/api/schema](http://127.0.0.1:8000/api/schema)
- **Swagger Documentation:** [127.0.0.1:8000/api/schema/docs](http://127.0.0.1:8000/api/schema/docs)

## Running Unit Tests

To run unit tests using Pytest:

```bash
pytest
```







