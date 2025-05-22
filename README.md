# Django E-commerce Store

A full-featured e-commerce application built with Django.

## Features

- Product catalog with collections and promotions
- Customer management with membership levels
- Shopping cart functionality
- Order processing system
- Address management
- Admin interface

## Models

- Collection
- Product
- Promotion
- Customer
- Order
- OrderItem
- Address
- Cart
- CartItem

## Setup

1. Clone the repository
```bash
git clone <your-repo-url>
cd storefront
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Start development server
```bash
python manage.py runserver
```

## Technologies Used

- Django
- Python
- SQLite (development)
- HTML/CSS/JavaScript (frontend)

## License

MIT 