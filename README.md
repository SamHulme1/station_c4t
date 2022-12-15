# Station C4t
To see the live version of the site click [here!](https://stationc4t.herokuapp.com/)

![mockup-image](/static/readme-img/station-mockup-img.jpg)

---
## Contents

### [UX](#ux-1)
### [User Requirements and Expectations](#user-requirements-and-expectations-1) 
### [Developer goals](#developer-goals-1) 
### [User Stories](#user-stories-1)
### [Design Choices](#design-choices-1) 
### [Wireframes](#wireframes-1)
### [Features](#features-1)
### [Database](#database)
### [Technologies Used](#technologies-used-1)
### [Depolyment](#deployment) 
### [Testing](#testing-1) 
### [Bugs](#bugs-1)
### [Credits](#credits-1)
---
## UX:

### Project goals: 

- To create a website were users can create, read, upadte and delete data 
- To experiment with the relationship between python and other languages

---
### Target Audience: 

- The website is targeted at people of all ages who enjoy the scifi genre and like cats

---
### Target Audience goals: 

- To be able to navigate around the site
- To be able to create, read, update and delete data
---
## User Requirements and Expectations

The website features visual and written content with clear methods for the user to create, read, update and delete information. The user is given clear feedback from the site whenever they create, read, update and delte information. through the use of flash messages and javascript alerts. The user is also given feedback when something doesn't go as expected on the site. The website is structured in a way that is easy to navigate and protects user data. 

---
## Developer goals: 

- To create a fun site for users to visit
- To create a website that has both front end and backend functinaloty 
- To develop my understanding of python

---
## User Stories: 

### First-Time Users:

- As a first-time user, I need to be able to create my own account on the site and create my own ship on the database
- I need to be able to see how the data I enter into the site creates information that I can read, update and delete

- I need to be able to navigate around the site easily and recieve feedback from the site 

- When im finised with the site I need to be able to logout 

### Returning users:

- I want to be able to log back into the site
- manage my account on the site, changing my password or deleting my account if needed 

## Design Choices 

---

### Colors:

![colours-blue](/static/readme-img/color-palette-blue.jpg)
![colours-purple](/static/readme-img/color-palette-purple.jpg)

The colour pallete for the site came from images I generated in an Ai art generator. Other colours such as blacks and white were used to create contrast. for the forms and inputs I used a purple colour palette, for the rest of the site I decided to use a muted blue colour palette

---
### Fonts

![fonts](/static/readme-img/station-fonts.jpg)

I used the font Audiowide across the site, this was because I thought the font was easiy to read and fitted in well with the space like theme I was creating. I also used font awesome to create the icons. If the Audiowide font doesn't load in I added a default san-serif font.

---
### Imagery

All the images on the site were created using the AI art generation tool NightCafe and help to create the space theme. I styled the images on the site to have a border radius of 50% to look like windows on a spaceship. For the background images, I created a css parallax effect to play on the sense of weightlessness someone might feel if they are in space, it almost creates an orbital effect. The images used were also of spacestations and planets to help build the enviroment for the site. I used different images to identify different sections and gave each citizen from the database a unique image so that the user can differantiate them from others.

---
### Styling 

The site is designed to be responsive accross all screen sizes, Where there is lots of written information such as on the citiens page, information is hidden behind collapsable buttons. The site makes good use or imagery to break up written information. Colours remain consistent accross the site. On smaller screen size, the site makes good use of a materialize side navigation. The site has also been designed so that if a user insn't logged in, they can only see login and signup in the nav. 



---
## WireFrames: 

![wireframe](/static/readme-img/station-wf.jpg)

---
## Features: 

### Current Features:

### Navbar 

![navbar](/static/readme-img/navbar.jpg)
- Includes links to all the different pages accross the site
- Is responsive on smaller screens turning into a side nav on small devices
- Only displays all content to users who are logged in, otherwise displays signup or login
- Allows a signed in user to signout, create a newship or manage their account 

### Footer 

![footer](/static/readme-img/footer.jpg)
- Includes links to external sources which open in seperate tabs

### Hero Image

![hero-image](/static/readme-img/hero-img.jpg)
- Is responsive accross all devices
- When the user first lands on the page is relivent to what the website is all about, building spaceships for cats in space

### User Forms

#### Create Account form
![create-account-form](/static/readme-img/create-account-form.jpg)
- Allows a new user to create an account on the database
- used flask-wtf to validate the form infomation 
#### Login form
![login-form](/static/readme-img/login-form.jpg)
- Allows a returning user to log back into their account 
- used flask-wtf to validate the form infomation 
#### Delete Account form
![delete-account-form](/static/readme-img/delete-account-form.jpg)
- Allows a user to delete their account, any ships connected to the account are also deleted to prevent 
new users inheriting a previous users ships if only the user is deleted on the database.
- used flask-wtf to validate the form infomation 
#### Change Password form
![change-password-form](/static/readme-img/change-password-form.jpg)
- Allows a returning user to change their password on the database
- used flask-wtf to validate the form infomation 
#### Create crew form
![create-crew-form](/static/readme-img/create-crew-form.jpg)
- Allows a user to create a new ship
- used flask-wtf to validate the form infomation 
- uses javascrit to turn user input information into a string which is then turned into an object on the backend and passed to the database.

### Manage account page 
![my-account](/static/readme-img/my-account.jpg)
- Gives the user a space where they can manage their account, sections include: logout, change password and delete account.

### Manage ships page
![my-ships](/static/readme-img/my-ships.jpg)
- Allows the users to see the ships they have created in the database
---
### Future Features:

Because of the time restraint I had when developing this site there are a number of features that I want to add in the near future that i've listed below:

- A way for the users to change the ships they're already created
- A page to display all ships created to all users so that diffenet users can compare and interact with them
- building on the interaction, Id like to make it so that the users can launch ships from their ships which will send messages to other users, like a chat function

### Naming Conventions and Structure of Files 

- All the files on the site have been named with consistency and structured into their appropriate sections
- Names contain lowercase and no special characters
- Javascript variables follow the format of camelsCase
- Python variables follow the format of CamelCase for classes and use underscore and lowercase to define methods and variables. All python is indented correctly
- Separate Javascript files have been created for the different webpages
- static files have been added to static folder
- html templates for python routes are included in templates folder
- Site includes a procfile for heroku deployment
- dependentsies are stored in requirement.txt
- enviroment variables are stored in env.py

---

## Database
The site was designed using a non-relational database structure, the data is structured into three different tables, users, ships and citizens. The ships table holds all the information for the users ships that are created. The users can access the ships they create via their username which is stored in session and has a realtionship with the ship captain field in the database. The citizens data is used to store information on the cat citizens. Which are used to build the users crew for their ships, this creates another relationship within the database. The user collection stores the users that have created accounts. The website uses this data to allow users to login, change their passwords and delete their accounts. 

## Technologies used: 

### Languages: 

1. [HTML5](https://www.w3schools.com/html/default.asp) To create the structure and the content of the website
2. [CSS3](https://www.w3schools.com/css/) To create the style for the website and its content
3. [Javascript](https://www.w3schools.com/js/) creates the functionality for the website
4. [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) creates the backend for the website
---
### Tools and libraries:

1. [Gitpod](https://www.gitpod.io/) To create and code the site
2. [Heroku](https://dashboard.heroku.com/) To host, deploy and store the site
6. [Google Fonts](https://fonts.google.com/about) To import fonts to the site
7. [Grammarly](https://app.grammarly.com/) To correct spelling, punctuation and grammar
8. [Font Awesome](https://fontawesome.com/) To create the icons used on the site in the nav, footer and for the spaceship visual representation in ships.html
9. [Adobe Colourwheel](https://color.adobe.com/create/color-wheel) To create the colour scheme for the website
10. [Jigsaw](https://jigsaw.w3.org/css-validator/validator) To validate CSS
11. [nu Html Checker](https://validator.w3.org/) To validate HTML 
13. [Jshint](https://jshint.com/) To validate Javascript 
14. [NightCafe](https://nightcafe.studio/) To create the images used on the site
15. [MongoDB](https://www.mongodb.com/) To create the database for the site
16. [Flask](https://flask.palletsprojects.com/en/2.2.x/) To render the webpages
17. [WTF-forms](https://wtforms.readthedocs.io/en/3.0.x/) To create the forms used on the site and to validate
18. [jinja](https://jinja.palletsprojects.com/en/3.1.x/) To display database information in html
19. [PyMongo](https://pymongo.readthedocs.io/en/stable/) To allow interaction with the database
20. [Werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/) To generate and process passwords adding extra security
21. [Materialize](https://materializecss.com/) To create site responsiveness and to create the navbar

---
## Deployment


### This site was developed using Git. Here is the development lifecycle:

1. I created a new repository by using Code Institutes template
2. In the terminal, I typed git init to initialise
3. I created all the files and folders for the project
4. For each change that I made I used the git add . and commit commands
5. I used git push to push the changes in Git to Github


## Testing 

### Testing User's Stories 

#### First Time User

As a first time user, when I first land on the site, I can clearly see what the site is about through the use of imagery and text descriptions on the index page. I can then go onto create an account and create my own ship by following the routes to signup and buildship. I can read the information I have created on the database for the ship I created by visiting the my ships section of the site. If i need to update or delete my account information I can do this through the my account section of the site. I can also logout of the site.  

#### Returning User

As a returning user I can log back into my account by entering my created username and password. When I have logged back in, I can see the information that I have already created on the site and if I need to I can manage my account, deleting my account and its stored ships and I can also change my accounts password if needed.

---
### Developer goals have been met by

- I have created a website where the user can create, read, update and delete data
- I have experimented with passing data from javascript to python and developed my understand of how backend data can interact with the front end. 

---
### Site responsiveness and compatibility

The site has been tested for responsiveness on the following devices using Google Developer tools:
- Blackberry Z30
- Blackberry PlayBook
- Galaxy Note 3
- Galaxy Note 2
- Galaxy S3 
- Galaxy S8
- Galaxy S9 Plus
- Galaxy Tab S4 
- Galaxy S20 Ultra
- Galaxy Fold
- Galaxy A51
- Kindle Fire HDX
- LG Optimus L70
- Microsoft Lumia 550
- Microsoft Lumia 950
- Moto G4 
- Nexus 10, 4, 5, 5X, 6, 6P, 7, 
- Nokia Lumia 520
- Nokia N9
- Pixel 3, 4, 3 XL, 5
- Ipad mini, Ipad, Ipad Pro
- iPhone 4, SE, XR, 12 Pro
- JioPhone 2
- Ipad air, mini
- Surface Pro 7, Duo
- Nest Hub, Hub Max
- iPhone 5, SE, 6, 7, 8, X
- larger screen sizes such as 4k have also been tested
I used Materialize to build the basis for my site responsiveness, I have added media queries to achieve the desired responsiveness on elements that I didn't use materialize for such as fonts and images.

---
#### LightHouse 
Lighthouse scores:

##### Index
![index-mobile](/static/readme-img/idex-lighthouse-mobile.jpg)
![index-desktop](/static/readme-img/index-lighthouse-desktop.jpg)

##### Changepassword
![changepassword-mobile](/static/readme-img/change-password-lighthouse-mobile.jpg)
![changepassword-desktop](/static/readme-img/change-password-lighthouse-desktop.jpg)

##### Citizens
![citizens-mobile](/static/readme-img/buildships-lighthouse-mobile.jpg)
![citizens-desktop](/static/readme-img/buildships-lighthouse-desktop.jpg)

##### Delete-account
![delete-account-mobile](/static/readme-img/delete-account-lightouse-mobile.jpg)
![delete-account-desktop](/static/readme-img/delete-account-lighthouse-desktop.jpg)

##### Login
![signin-mobile](/static/readme-img/signin-lighthouse-mobile.jpg)
![signin-desktop](/static/readme-img/signin-lighhouse-desktop.jpg)

##### Myaccount
![myaccount-mobile](/static/readme-img/my-account-lighthouse-mobile.jpg)
![myaccount-desktop](/static/readme-img/my-account-lighthouse-desktop.jpg)

##### Ships
![ships-mobile](/static/readme-img/myships-lighthouse-mobile.jpg)
![ships-desktop](/static/readme-img/myships-lighthouse-desktop.jpg)

##### Signup
![signup-mobile](/static/readme-img/signup-lighthouse-mobile.png)
![signup-desktop](/static/readme-img/signup-lighthouse-desktop.jpg)
---
### Online validators 

The final validator results:

---
### Javascript Validation

#### Game const and game-start 
![]()



---
### CSS Validation
![]()

---
### HTML Validation

#### Game-start
![]()

#### index
![]()

---
### Manual Tests run on site

Below are a number of manual tests I've run towards the end of devlopment
1. Do all the nav links work?
- result: all the nav links work
2. Do the footer links open in seperate tabs?
- result: all the links open in seperate tabs
3. Can I create an account?
- result: I can create an account on the website, the user appears in the db
4. Can I create a ship?
- result: I can create a ship on the website, the ship appears in the db
5. Can I change my password?
- result: I can change my password on the db
6. Can I delete my account: 
- result: I can delete my account, however my ships arn't deleted
- action: added python code to remove the users ships from the db when the user is deleted
7. Can I view the data I create on the db?
- result: I can view all the data I have created on the db


---

### Browser testing 

The site has been tested on Chrome, Firefox and Microsoft Edge 

---
## Bugs 

1. flask validators arn't validating correctly on forms when validate_on_submit is used 
- originally I thought the bug might have been caused by an incorrect instiallion of flask wtf. I was correct, after pip freezing requirements it installed correctly. However I had a number of issues with the validation in my forms. So I had to just use data required and use if POST and validate in my app.py file instead.

2. Heroku doesn't connect to database correctly resulting in errors when on the deployed site, the error doesn't occur if I host the site locally in github.
- I the issue was cause by a misscopied url to fix the issue I simply copied and pasted my url again and the site worked fine afterwards.

---
### Bugs Left in Code:

1. On some of the forms you can sometimes submit them without all the data being entered. This occurs for the password field where I wanted to use the flask wtf equal to validation. However, to login you still have to have the correct username and password.

---
## Credits 

### Code

---
### Content 

- All written content for the site came from me the developer

---
### Media

- The images for the site were created using an online AI image generator [NightCafe](https://nightcafe.studio/)
- The favicon was created using [Favicon Io](https://favicon.io/favicon-converter/)
### Acknowledgements

- My mentor for the amazing help and support
- Other students on slack for their support 
- Code Institute for the helpful materials and support
- W3C for their library of information when I needed a quick refresher on the content I'd learnt about during the course