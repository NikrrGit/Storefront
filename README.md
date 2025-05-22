# Django E-commerce Store

A full-featured e-commerce application built with Django, featuring a robust product catalog, customer management, shopping cart functionality, and order processing system.

## 🚀 Features

### Product Management
- Product catalog with collections and categories
- Product promotions and discounts
- Inventory tracking
- Product search and filtering

### Customer Management
- Customer profiles with membership levels (Bronze, Silver, Gold)
- Address management
- Order history
- Customer authentication

### Shopping Experience
- Shopping cart functionality
- Wishlist
- Order processing
- Payment status tracking

### Admin Features
- Admin dashboard
- Product management
- Order management
- Customer management
- Sales analytics

## 🛠️ Technical Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (development)
- **Frontend**: HTML, CSS, JavaScript
- **Additional Tools**: 
  - Python 3.13+
  - Pillow for image processing
  - python-dotenv for environment management

## 📋 Project Structure

```
storefront/
├── store/                 # Main app for e-commerce functionality
│   ├── models.py         # Database models
│   ├── views.py          # View logic
│   ├── urls.py           # URL routing
│   └── migrations/       # Database migrations
├── storefront/           # Project configuration
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py          # WSGI configuration
└── manage.py             # Django management script
```

## 🚀 Getting Started

### Prerequisites
- Python 3.13 or higher
- pip (Python package manager)
- Git

### Installation

1. Clone the repository
```bash
git clone https://github.com/NikrrGit/Storefront.git
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

5. Create superuser (admin account)
```bash
python manage.py createsuperuser
```

6. Start development server
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## 📝 Database Models

### Core Models
- **Collection**: Product categories
- **Product**: Product information and inventory
- **Promotion**: Discount and promotional offers
- **Customer**: Customer profiles and membership
- **Order**: Order processing and tracking
- **OrderItem**: Individual items in orders
- **Address**: Customer shipping/billing addresses
- **Cart**: Shopping cart management
- **CartItem**: Items in shopping cart

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Author

- **NikrrGit** - [GitHub Profile](https://github.com/NikrrGit)

## 🙏 Acknowledgments

- Django Documentation
- Django REST Framework
- Python Community 