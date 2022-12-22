## Foodie

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/top.png?raw=true)

# Ecomerce Website

This project deals with developing a Virtual website ‘E-commerce Website’. It provides the user with a list of the various products available for purchase in the store. For the convenience of online shopping, a shopping cart is provided to the user. After the selection of the goods, it is sent for the order confirmation process. The system is implemented using Python’s web framework Django.

## Foodie
This is basic E-comerce web app using

### Frontend

[![python](https://img.shields.io/twitter/url?label=Python&logo=Python&style=for-the-badge&url=https%3A%2F%2Fwww.python.org%2F)](https://www.python.org/) 
[![html](https://img.shields.io/twitter/url?label=Html&logo=HTML5&style=for-the-badge&url=https%3A%2F%2Fwww.w3schools.com%2Fhtml%2F)](https://www.w3schools.com/html/)  [![css](https://img.shields.io/twitter/url?label=Css&logo=CSS3&logoColor=blue&style=for-the-badge&url=https%3A%2F%2Fwww.w3schools.com%2Fcss%2F)](https://www.w3schools.com/css/)  [![bootstrap](https://img.shields.io/twitter/url?label=bootstrap&logo=bootstrap&logoColor=white&style=for-the-badge&url=https%3A%2F%2Fgetbootstrap.com%2F)](https://getbootstrap.com/)
[![javascripts](https://img.shields.io/twitter/url?label=JavaScript&logo=JavaScript&style=for-the-badge&url=https%3A%2F%2Fwww.w3schools.com%2Fjs%2F)](https://getbootstrap.com/)








### Backend
[![linkedin](https://img.shields.io/twitter/url?label=django&logo=django&logoColor=white&style=for-the-badge&url=https%3A%2F%2Fwww.djangoproject.com%2F)](https://www.djangoproject.com/)   [![portfolio](https://img.shields.io/twitter/url?label=postgresql&logo=postgresql&logoColor=white&style=for-the-badge&url=https%3A%2F%2Fwww.postgresql.org%2F)](https://www.postgresql.org/)








## Project installation and setup

#### Create virtuelenv Cmd 

```bash
  virtualenv venv

```

#### To Activate the virtual environment
```bash
  venv/bin/activate

```
#### Install the requirements in the current environment
```bash
  pip install -r requirements

```

#### Install django on this virtualenv
```bash
  pip install django=<version>

```

#### After installed django create a project

```bash
  django-admin startproject ecomerce-project

```
#### Then cd to new directory newly created

```bash
  cd ecomerce-project

```
#### Next create apps ( accounts , shops , cart )

```bash
  python manage.py startapp accounts

```
#### Create directories (static and templates)

```bash
  mkdir static

```
#### Then makemigrations

```bash
  python manage.py makemigrations

```
#### Migrate 

```bash
  python manage.py migrate

```
#### To run a Starting development server at http://127.0.0.1:8000
```bash
  python manage.py runserver

```
### Django server

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/ia8jlkozut4uxwatnqwp.png?raw=true)

## Django administration creation

#### First Create a superuser id

```bash
   python manage.py createsuperuser

```
#### Enter the username choice
```bash
   Username: example

```
#### Enter email adress
```bash
   Email adress : example@gmail.com

```
#### Enter The password
```bash
   password : ******

```
#### Again Enter The password for confirmation
```bash
   password (again) : ******

```

#### Superuser created successfully if above fields are entered correctly

#### Next run the server
```bash
   python manage.py runserver

```
#### Open the django server page and now enter top url add /admin
http://127.0.0.1:8000/admin/


### Django Admin login page

#### Enter the superuser id and unique password

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/Screenshot%20(21).png?raw=true)

#### Login successfully entered django administration page
![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/Screenshot%20(30).png?raw=true)

## Project Screenshots


## Head home page

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/home.png?raw=true)


## Register page

#### User can fill the register form first.

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/register.png?raw=true)

## PostgreSQL database

#### User filled register form data collected on PostgreSQL Database auth user table.

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/Screenshot%20(34).png?raw=true)

## Login page

#### The colleted auth user data Username and Password type on login form. unautherised people doen't open login page .  autherised user can login foodie page successfully.

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/login.png?raw=true)



## Home items section

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/items%201.png?raw=true)


![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/items2.png?raw=true)

## Item details page

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/item%20details.png?raw=true)

## Item cart page

![App Screenshot](https://github.com/athulpython/foodie-/blob/master/screeshots/cart.png?raw=true)
