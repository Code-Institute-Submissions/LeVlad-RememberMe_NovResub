# Remember Me #

# Design #
# User Stories #
# Purpose #
# Technologies #
# Frameworks #
# Tools #
# Testing #
# References #
# Deployment #
# Acknowledgements #

---
**RemembeMe**
![ReminderApp DesktopView](https://user-images.githubusercontent.com/88729876/190986183-6e1447f8-6a13-4d1f-b367-ad060e64cd0f.jpg)

*RemmeberMe* is meant to be a site where anyone can create their own profiles and use the build in app that aims to be a location based reminder. Anyone will be able to create their own task list, set up reminders and never forget about shopping to pick up, dry cleaning to drop off or important messages to deliver.

## Design ##

Having a minimal design the site will focus more on functionality.

# Wireframes #

## Site map ##
![Site Map Wireframe](https://user-images.githubusercontent.com/88729876/190978319-4349250f-55b0-4777-9585-9b2038a69c9b.png)

---

## Mobile ##
![Mobile View](https://user-images.githubusercontent.com/88729876/190970214-b668f6f3-29c3-428e-893c-32950c72ad48.png)



## Desktop ##
![Desktop View](https://user-images.githubusercontent.com/88729876/190970166-71cad197-0463-4166-97ac-e49014b61aaf.png)


## Tablet ##
![Tablet View](https://user-images.githubusercontent.com/88729876/190970185-ca593dd2-956a-49ac-85c6-8ae3014708b5.png)




## User Stories ##

Admin

As an Admin I want to be able to access the back end so that I can repair/maintain/approve requests

As an Admin I can login so that I can update lists and tick off completed reminders

As an Admin I want to create and edit a database so that I can delete or recover any important information requested by users

As an Admin I can login so that I can check and update the account details

As an Admin I want to use geolocation so that I can triangulate user's position and alert them of their set reminders for the specified location


User

As a User I want to create an account so that I can save all my reminders

As a User I can receive an e-mail so that I can confirm my account has been created.

As a user I can login so that I can view my account.

As a User I can create a profile so that I can view my reminders

As a User I want to be able to set a reminder for a specific location so that I can remember to do the task

As a User I want to be able to modify a reminder in case I make a mistake so that I can correct the mistake and be accurate





## Purpose ##

The main purpose of the website is to be a virtual space where users can set reminders with details of **what**, **where** and **priority**.



## Technologies ##

1.HTML
2.CSS
3.JavaScript
4.Python


## Frameworks ##

1.Django  
2.Bootstrap 
3.Libraries 
4.jQuery  


## Tools ##
Heroku
Git
Postgres


## Tests ##

I have not undertaken any automated testing and I chose to manually test the site functionality and layout.

Idea 💡: After creating all the templates I wanted to ensure their linkeage and functionality

Test 📝: To test this, I went through each and made sure they were loading correctly.

Result 👷: All templates loaded as expected in development but one issue appeared after deployment.

Verdict ✅: This test passed in it's basic form, amendments are required to the "remnider" template as it is not loading correctly.

---

Idea 💡: Once the functionality of the sign up and login were done I wanted to test and see if they work correctly.

Test 📝: To test this, I went through using a different device, created an account and managed to access the rest of the pages.

Result 👷: Everything worked as expected.

Verdict ✅: This test passed but further improvements can be made by ensuring the security aspect is kept and the design is more appealing.

---

Idea 💡: A good UX experience is given by interactions with the pages on a website, that's why messages have been implemented in the site.

Test 📝: Testing has been done by confirming every action that should send a message, is doing so.

Result 👷: Users are receiving success messages for loggin in and out and error messages for incorrect forms.

Verdict ✅: This test passed and no further corrections are required.

---



## Issues ##

Issue 🐛: Heroku Deployment failed.
Cause🔧: The Cloudinary environmental variable isn't configured correctly.
Resolution✅: Removing the variable name from the variable key resolved the issue.

---

Issue 🐛: Heroku CSS file not found while deploying
Cause🔧: The static files path was missing the app name.
Resolution✅: Adding the app name to the path resolved the issue.



# Unresolved Issues #

1. Sign Up and Login templates do not extend "base.html" and although I have found several solutions online, none worked.
2. The main app functionality has stopped working and can't be accessed at the moment until a fix can be found. **Access** can be gained in the admin section using the  admin credentials.


## Deployment ##

Deploying to Heroku #

This project was produced in GitPod and is deployed on Heroku. This is how to make a copy of this project and deploy it accordingly. The images are hosted on AWS, so you will need to sign up for a AWS account in order to get an API key. I opted to use a gmail account, the settings for which are in the settings.py file. The payment system used is Stripe, which you will need to set up an account for in order to collect the PUBLIC_KEY, PRIVATE_KEY and WebHook keys.

To set it up locally 1 - download the repository using the link at the top of the page, alternatively you can clone it using the following command:

git clone https://github.com/LeVlad/

2 - Set up a virtual environment:

py -m venv venv 3 - Activate the virtual environment:

venv\Scripts\activate Create a project by entering the command: django-admin startproject YOURPROJECTNAMEHERE

Create a new app by entering the comand: py manage.py startapp YOURAPPNAMEHERE

You are now ready to install the packages required to run this program. You can do this by installing the requirements in the requirements.txt file:

pip install -r requirements.txt Next we need to add the following to the list of installed apps in settings.py:

-'cloudinary_storage', -'crispy_forms', -'allauth', -'allauth.account', -'allauth.socialaccount', -'django.contrib.staticfiles', -'django_countries', -'home', -'bag', -'checkout', -'profiles', -'contact', -'yourappname'

You will need to create an env.py file which will contain the following:

os.environ["DATABASE_URL"] = "your postgresql url which you will find in heroku (see below)" 
os.environ["SECRET_KEY"] = "your secret key which will added to heroku" 
os.environ["CLOUDINARY_URL"] = "your cloudinary api"


Setting up on Heroku:

1 - Set up a (or log into an existing) Heroku account.

2 - Select add new app and give it a unique name

3 - Select 'Resources' and search for/install the Heroku Postgres add-on.

4 - Select 'Settings' and click 'Reveal Config Vars'

5 - You will find the DATABASE URL already added, copy this to the env.py file mentioned previously.

6 - You will need the following config vars:

CLOUDINARY_URL = your API url from cloudinary 
SECRET_KEY = your secret key must match the secret key in your env.py file 
DATABASE_URL = heroku link to your postgres database

Migrate and Run in Gitpod
Finally, all that remains is to makemigration by entering the following command:

python3 manage.py makemigrations Then migrate using the following:

python3 manage.py migrate And run the app locally:

python3 manage.py runserver


## Acknowledgements ##

1. Code Institute Courses
2. Richard Wells - CI mentor
3. StackOverflow
4. Django Documentation
5. https://hackernoon.com/a-simple-python-reminder-app-m3k42wk
6. https://towardsdatascience.com/pythons-geocoding-convert-a-list-of-addresses-into-a-map-f522ef513fd6#3128
7. https://www.w3schools.com/html/html5_geolocation.asp
8. https://github.com/earthcomfy/Django-registration-and-login-system
9. https://favicon.io/favicon-converter/


