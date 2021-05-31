# Technologies and database:
Database: 
•sqlite

Back-end:  
•python >= 3.0  
•django    
•django-rest-framework  


	
# Steps to run the application

```

# Install virtualenv in your system
$ python3 -m pip install --user virtualenv (For macOS and Linux)
$ py -m pip install --user virtualenv (For Windows)


# Create virtual environment
$ python3 -m virtualenv env (For macOS and Linux)
$ py -m virtualenv env (For Windows)

# Activate virtual environment
$ source env/Scripts/activate (For macOS and Linux)
$ .\env\Scripts\activate (For Windows)

# Get project code form github
$ git clone https://github.com/SatishXceedance/weather-app.git

# Go to the project directory
$ cd weather_app

# Install project dependencies from requirements.txt file
$ pip install -r requirements.txt

# For getting database tables 
$ python manage.py migrate

# Runserver on your local system
$ python manage.py runserver

# Go to the postman and create get request for below url
 http://127.0.0.1:8000/weather?city=Delhi&country=In
 
 # To stop server press ctrl+C

# Run Test cases
$ python manage.py test

# to deactivate the virtual environment
$ deativate

```
