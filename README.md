# FizzBuzz

A simple FizzBuzz generator application

the project was developed with:

* pip `9.0.1`
* virtualenv `15.1.0`

Setup:

* Clone this repo
* create a virtual environment `virtualenv virtualenv`
* run `source virtualenv/bin/activate` to activate your fresh virtual environment
* run `pip install -r requirements.txt` to install backend dependencies
* run `cd fizzbuzz/ && ./manage.py migrate` to run migrations
* `./manage.py runserver`
* `./manage.py createsuperuser`

* Visit http://localhost:8000/admin
* Create a basic Generator
* Create one or more Divisors for your fresh Generator. All of them will be used
  when generating string sequence using this Generator
* Create one or more Strings for your fresh Generator. All of them will be used
  when generating string sequence using this Generator

* Every generator displays its url in Django admin change form, so visit this
  url in order to use the Generator
