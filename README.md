# Welcome to the Flower Shop

You have been tasked to build an app that will allow the employees of the flower shop to manage the different bouquets that the shop builds for it's customers.

## Project Setup

* Clone down the repo and `cd` into it

* Change this from a git repo to a regular directory:
  * `rm -rf .git`

* Create a new repository on Github and make your first commit with this boilerplate code:
  * Create a brand new repository under your account on Github
  * `git init`
  * `git add .`
  * `git commit -m "First commit with boilerplate code"`
  * `git remote add origin your-new-repos-ssh-remote-url`
  * `git push -u origin master`

* Create your OSX/Linux OS virtual environment in Terminal:

  * `python -m venv flowershopenv`
  * `source ./flowershopenv/bin/activate`

* Install the app's dependencies:

  * `pip install -r requirements.txt`

* All your models and migrations have already been created, so ahead and run migrations:

  * `python manage.py migrate`

* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`

* Populate your database with initial data from fixtures files: (_NOTE: every time you run this it will remove existing data and repopulate the tables_)

  * `python manage.py loaddata flowers`
  * `python manage.py loaddata bouquets`
  * `python manage.py loaddata bouquet_flowers`

* Make a copy of `bouquetapp/views/connection.py.example` and remove the `.example` extension and change the path to the database 

* Fire up your dev server and get to work!

  * `python manage.py runserver`


## Requirements

You need to meet the following requirements in the order they are listed since they build on each other. After each requirement has been met, please make sure you make a commit with a detailed commit message explaining what feature has been completed. You **do not** need to worry about authentication for this application.

1. When a user navigates to the root URL of the application (`/`), they should see a list of all the bouquets in alphabetical order.

1. Above the list of bouquets, provide a link that presents the user with a form to add a new bouquet by providing the name and occasion. When the form is submitted, the user should be directed to `/` and should see the newly added bouquet in the list.

1. Add a link to view the details of each bouquet for every item on the list of bouquets. When the user clicks on this link, they should see the name of the bouquet, the occasion, the names of the many flowers that make up that bouquet and the quantity of each flower needed for that bouquet.

1. Add a DELETE button next to each flower listed on the details page for a bouquet. When the user clicks this button, the flower should be removed from that bouquet. **This action should not delete the flower itself!**

1. Add an EDIT button at the bottom of the bouquet details page. When the user clicks on the button, they should be presented with a form that lets them edit only the occasion of the bouquet. 
