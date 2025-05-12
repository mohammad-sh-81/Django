# 🛒 Django Online Shop

This is a Django-based online shopping project that includes core e-commerce features such as product browsing, adding items to a basket, user authentication, password reset via email, and AJAX-based comment submission.

## 🚀 Features

- ✅ User registration, login, and logout
- ✅ Password reset via email
- ✅ Product listing and detail views
- ✅ Add products to shopping basket/cart
- ✅ AJAX-based comment submission on products
- ✅ Basic admin panel to manage products and users

## 🛠️ Technologies Used

- Python 3
- Django
- SQLite (default, can be changed)
- HTML/CSS + JavaScript (with AJAX)
- Bootstrap (optional for UI)
- Django's built-in authentication system

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/mohammad-sh-81/Django.git
cd Django
```
2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional):

```bash
python manage.py createsuperuser
```
6. Run the development server:
 
```bash
python manage.py runserver
```

Then open your browser and go to: http://127.0.0.1:8000/


## 📬 Email Configuration

To enable password reset via email, configure your email settings in settings.py:

```bash
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

