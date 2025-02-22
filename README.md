# Kiratech Inventory System

A Django-based inventory management system with REST API support.

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/kiratech-inventory-system.git
cd kiratech-inventory-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

### 5. Access the Application

Open your web browser and navigate to `http://127.0.0.1:8000/inventory/`.

### 6. Test the API

You can test the API endpoints using tools like `curl` or `Postman`.

### 7. Test the Application

You can test the application using the test cases in the `tests.py` file.

```bash
python manage.py test
```

### 8. Test the Admin Page

You can test the admin page using the test cases in the `tests.py` file.

```bash
python manage.py test
```

### 9. Test the Admin Page

You can test the admin page using the test cases in the `tests.py` file.

```bash
python manage.py test
```

## Available Endpoints

### Template Views
- **Admin Interface**: http://127.0.0.1:8000/admin/
- **Inventory List**: http://127.0.0.1:8000/inventory/
- **Inventory Detail**: http://127.0.0.1:8000/inventory/detail/<id>/

### API Endpoints
- **API Root**: http://127.0.0.1:8000/api/
- **Inventory List**: http://127.0.0.1:8000/api/inventory/
- **Inventory Detail**: http://127.0.0.1:8000/api/inventory/<id>/

### API Features
- Search inventory by name: `/api/inventory/?search=<query>`
- Filter by availability: `/api/inventory/?inventory_availability=true`
- Order by name: `/api/inventory/?ordering=inventory_name`

## Running Tests

To ensure everything is working correctly, run the tests:

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test inventory
```

## Troubleshooting

Common Issues:
- **Missing Dependencies**: Ensure all packages are installed via `pip install -r requirements.txt`
- **Database Errors**: Verify migrations are up to date with `python manage.py migrate`
- **Server Not Starting**: Check if port 8000 is available
- **Static Files Not Loading**: Run `python manage.py collectstatic`
- **Admin Access Issues**: Verify superuser credentials

---





