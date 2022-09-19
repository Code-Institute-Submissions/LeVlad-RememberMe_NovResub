# Remember Me #

# Design #
# User Stories #
# Purpose #
# Technologies #
# Frameworks #
# Tools #
# Testing #
# References #
# Acknowledgements #


## Design ##

Having a minimal design the site will focus more on functionality.

Mobile 
![Mobile View](https://user-images.githubusercontent.com/88729876/190950218-f747e8ae-cb36-42db-9e7a-de9b016eff22.png)


Desktop
![Desktop View](https://user-images.githubusercontent.com/88729876/190950146-c4da1f60-c6e0-48d5-bbc6-1a915cdc87db.png)


Tablet
![Tablet View](https://user-images.githubusercontent.com/88729876/190949967-22bbfdef-1f9a-4ce3-92d9-7965fba97801.png)



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

HTML
CSS
JavaScript
Python


## Frameworks ##
Django  
Bootstrap 
Libraries 
jQuery  



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



Unresolved Issues

1. Sign Up and Login templates do not extend "base.html".
2. The main app functionality has stopped working and can't be accessed at the moment until a fix can be found.


## Acknowledgements ##
1. Code Institute Courses
2. Richard Wells - CI mentor
3. StackOverflow
4. Django Documentation

