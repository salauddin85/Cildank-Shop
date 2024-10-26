
# Cildank-Shop

Cildank-Shop  an online clothing shop built using Django 5.1 and Django Rest Framework. This application provides a platform for users and admins to manage and interact with products seamlessly.

## Features

### User Features
- Users can register, log in, and log out.
- Users can view products.
- Users can purchase products.
- Users can leave reviews for products.
- Users can view their purchase history.

### Admin Features
- Admins can manage product listings.
- Admins can add new products.
- Admins can view existing products.
- Admins can update product information.
- Admins can delete products.

## API Endpoints

### For Authentication
- **Register:** `POST https://cildank-shop-deploy-versel.vercel.app/auth/register/`
- **Login:** `POST https://cildank-shop-deploy-versel.vercel.app/auth/login/`
- **Logout:** `POST https://cildank-shop-deploy-versel.vercel.app/auth/logout/`

### For Products
- **All Products:** `GET https://cildank-shop-deploy-versel.vercel.app/products/product/`
- **Product Pagination:** `GET https://cildank-shop-deploy-versel.vercel.app/products/product/?page=2`
- **Sort by Price Ascending:** `GET https://cildank-shop-deploy-versel.vercel.app/products/product/sorted_by_price/?order=asc`
- **Sort by Price Descending:** `GET https://cildank-shop-deploy-versel.vercel.app/products/product/sorted_by_price/?order=desc`
- **Sort by Size:** `GET https://cildank-shop-deploy-versel.vercel.app/products/product/sorted_by_size/M/`
- **Add to Wishlist:** `POST https://cildank-shop-deploy-versel.vercel.app/products/wishlist/add_product/1/`
- **Remove from Wishlist:** `POST https://cildank-shop-deploy-versel.vercel.app/products/wishlist/remove_product/1/`
- **All Wishlist Items:** `GET https://cildank-shop-deploy-versel.vercel.app/products/wishlist/`
- **Reviews:** `GET https://cildank-shop-deploy-versel.vercel.app/products/review/`

### For Purchases
- **Purchase Product:** `GET https://cildank-shop-deploy-versel.vercel.app/purchases/list/1`

### For Transactions
- **Deposit:** `POST https://cildank-shop-deploy-versel.vercel.app/transactions/deposit/`

### For Categories
- **All Categories:** `GET https://cildank-shop-deploy-versel.vercel.app/categories/category_list/`
- **All Subcategories:** `GET https://cildank-shop-deploy-versel.vercel.app/categories/subcategory_list/`

### Show Products by Category or Subcategory
- **Show Products by Subcategory:** `GET https://cildank-shop-deploy-versel.vercel.app/category_products/?sub_category_id=3`
- **Show Products by Category:** `GET https://cildank-shop-deploy-versel.vercel.app/category_products/?category_id=3`


## Getting Started

### Prerequisites

- Python 3.12.1
- Django 5.1
- Django Rest Framework

### Installation


### Setting Up the Django Environment on Windows

1. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```

2. Navigate to the virtual environment directory:
   ```bash
   cd myenv
   ```

3. Activate the virtual environment:
   ```bash
   Scripts\Activate\myenv
   ```

4. To deactivate the virtual environment, use:
   ```bash
   deactivate
   ```

5. Install Django:
   ```bash
   pip install django
   ```

6. Create migrations:
   ```bash
   python manage.py makemigrations
   ```

7. Apply migrations:
   ```bash
   python manage.py migrate
   ```

8. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

9. Start the development server:
   ```bash
   python manage.py runserver
   ```


## Usage

- Access the API endpoints to interact with products, reviews, and user accounts.
- Use the provided functionality to manage product listings and user accounts effectively.


