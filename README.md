:warning: v1.0 is not longer working due to the changes in the Coinmarketcap API.

# 1. Starting Position

Many crypto portfolio apps either need a lot of storage or do not have the most up-to-date prices. Furthermore, I do not want to make my confidential data available to an app provider. An individual solution should remedy this.

# 2. Functions

The user is able to create his own cryptocurrency portfolio. To do this, he can add or delete cryptocurrencies from the portfolio himself. In addition, the amount of the respective currencies can be specified. The function should take the current rate of the cryptocurrencies from the API of the website https://coinmarketcap.com and display it live to the user. This data is updated automatically when the price changes. The total value of the portfolio and the minute changes to it should be displayed to the user. In addition, a diagram could be displayed showing the weekly change in the total value of the portfolio.

# 3. Workflow

## Data Entry

The user can add or delete cryptocurrencies from the portfolio. He can also specify the amount of the respective currency.

## Data Processing / Storage

The course data are taken from the API of the website https://coinmarketcap.com. The data should update automatically when the price changes. The user's portfolio entries are saved in a .json file.

## Data Output

The web application shows the current prices and the total value of the individual portfolio entries. The following is calculated (example):\
`bitcoin_portfoliovalue = bitcoin_amount * bitcoin_price`<br><br>
In addition, the total value of the portfolio should be output. The following is calculated (example):\
`all_portfoliovalue = (bitcoin_amount * bitcoin_price) + (ethereum_amount * ethereum_price)...`

# 4. Modules

## Overview

The App is built with the following Python modules:

1. Flask\
   Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.
2. SQLAlchemy\
   SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
3. Bcyrpt-Flask\
   Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application.
4. Flask-Login\
   Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users' sessions over extended periods of time.
5. Pillow-PIL\
   Pillow wrapper for PIL compatibility
6. Flask-WTF\
   Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.
7. Requests\
   Requests is a simple, yet elegant HTTP library.

## Installation

Ensure that you are in your main directory (Normally: C:\).\
You can install all modules all at once with the following command:

```
py -m pip install Flask Flask-SQLAlchemy Bcrypt-Flask Flask-Login Pillow-PIL Flask-WTF requests

```

### Flask

```
py -m pip install Flask

```

### Flask-SQLAlchemy

```
py -m pip install -U Flask-SQLAlchemy
```

### Bcyrpt-Flask

```
py -m pip install -U Bcrypt-Flask
```

### Flask-Login

```
py -m pip install -U Flask-Login
```

### Pillow-PIL

```
py -m pip install -U Pillow-PIL
```

### Flask-WTF

```
py -m pip install -U Flask-WTF
```

### Requests

```
py -m pip install -U requests
```

# 5. Running the project

1. Ensure that you are in the project home directory. Start the app by running the following command:

```
python run.py
```

2. Navigate to URL http://localhost:5000 (By default, flask will run on port 5000.)

# 6. Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
