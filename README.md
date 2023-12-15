# Pop-up Restaurant

## Purpose

* The external user goal is to 
* The internal user goal is to 
* The site is targeted at 

* The live version can be accessed here: ADD LIVE URL HERE


## AGILE Methodology

### MILESTONES - EPICS - SPRINTS

* An Agile approach was taken. Possible features were listed and evaluated based on the value they could provide to the user, and their feasibility in terms of time and resources.
* An initial milestone was set on Github for target of minimum functionality.
* Due to the limited time available for completion of the project, only one sprint was completed. 
* Work items that were not listed as part of the first sprint, deemed not being crucial for minimum functionality, were moved to a Product Backlog also on Github.
* All items that were part of the completed sprint were converted into User Stories and managed on the Github Kanban board.  
* User Stories that could not be achieved during the sprint were moved back to the Product Backlog, to be evaluated and prioritised before any next sprint begins.

### USER STORIES

* Github Kanban board: User Stories were moved from 'To-do' to 'In Progress' to 'Complete' as work progressed.

## UX

### Wireframes

#### Home Page

![DESCRIPTION](static/images/FILE_NAME.png)


#### Log In and Sign up Pages

#### 
#### PAGE NAME

### Typography and Color

ADD HERE

### Accessibility

ADD HERE


## Features

* Features were added to provide the user with CRUD (Create, Read, Update, Delete) functionality. After logging in, the user can create a booking, read/view it, update it and delete it. 
* The admin user can create, read/view, update and delete both products and orders after logging in to the admin dashboard.

Key features are described below.

### Home Page

* The home page 

### Navigation Bar

* The navigation bar is located at the top of every page.
* Logged-out users can 
* 'Home' returns the user to the home page.
* 

### Sign In, Log in and Log out

* The sign in, log in and log out pages use the templates provided by Django with a little modification.
* The navigation bar options shown to the user change depending on whether a user is logged-in or logged-out. Users must be authenticated in order to make, view, edit or cancel bookings.
* The sign in and log in form inputs use built-in Django validation to check that the user enters a suitable password and username. 
 
### FEATURE

* The 

### FEATURE

* The 

### FEATURE

* 


## Additional Features

DESCRIPTION IN BRIEF

* A


## Future Features

ADD HERE


## Data Model

Unique data models were created as described below.

### MODEL 1: 

* Attributes

### MODEL 2

* Attribute

### MODEL 3

### Entity Relationship Diagram (ERD)

The Models used in this project were mapped out as in the Entity Relationship Diagram below.

![entity relationship diagram](static/images/FILE NAME HERE.png)

ADD FILE ABOVE SHOWING ERD

## Django MVT Structure

* The website was built using the model-view-template structure in Django.
* Views are function-based.

## Templates

* A base template was created to store the navigation bar and footer which appears on each page. All other templates extend this base template.
* All Allauth account templates use modified versions of the original allauth templates. The templates 
were modified to fit the style of the website while keeping their original functionality.

## Technology

* Heroku was used to deploy the program.
* Gitpod was used for editing.
* Github was used for storing, sharing the repository and version control. Github Boards
were used to store and plan user story, sprint, milestone and other required information
as part of the Agile method and approach to workflow.
* LucidChart was used to create the Entity Relationship Diagram (ERD). MAY CHANGE THIS
* Bootstrap classes and styles were used throughout the application with some modification.
* ElephantSQL was used to store the database once deployed.
* AWS was used to store static files after deployment.
* Mockplus was used to create wireframes. MAY CHANGE THIS
* Allauth was used for log-in, log-out, and sign-up authentication. 


## Testing

### Code Validation MUST COMPLETE VALIDATION OF ALL

* Python code was passed through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/). No issues were found.

* HTML code in the template files was validated using the [W3 Validator](https://validator.w3.org/nu/). No errors were found. 

* CSS code was validated using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator).

### Other Testing

* This app was tested for responsiveness using the Google Chrome browser and Chrome DevTools. It has not yet been tested on other browsers.

### Test Cases

#### Test Case 1

COMPLETE ONE OR MORE TEST CASES

1. Open the live app. The user is shown a home page with a large 'Pop-up Restaurant' heading and a card showing the details of an upcoming event. The user notices that there is a 'Book now' button.
2. Click 'Book now'. The user has not logged in so they are directed to a 'Log In' page. The user is not yet registered on the app. The user notices a 'Sign Up' link above the form.
3. C


### Fixed Bugs

ADD FIXED BUGS

* O

### Remaining Bugs

ADD REMAINING BUGS

## Deployment

### Via Gitpod

1. Go to http://github.com.
2. Open the 'SiobhanP1/art-shop-ecommerce-store' repository.
3. Click on 'Gitpod' to open a Gitpod workspace.
4. Enter the command `python3 manage.py runserver` in the terminal to run the program.

### Via Heroku

The program was deployed using Heroku by doing the following:

1. Go to http://github.com.
2. Open the 'SiobhanP1/art-shop-ecommerce-store' repository.
3. Go to https://www.heroku.com.
4. Select 'Create app'.
5. Give the app a unique name.
6. Go to 'Settings'.
7. Click 'Reveal Config Vars' and add the following keys and their
corresponding values:
* AWS_ACCESS_KEY_ID: from the AWS storage bucket
* AWS_SECRET_ACCESS_KEY: from the AWS storage bucket
* DATABASE_URL: add ElephantSQL database URL here
* SECRET_KEY
* USE_AWS: True
9. Go to 'Deploy' and then 'Deployment Method'.
10. Select 'Connect to Github'.
11. Enter the repository name.
12. Select 'Manual Deploy'. 
13. Click 'Deploy'.

## Credits

* The initial template used to build the project was the ci-full-template provided for project use by Code Institute.
* Much of the process followed in the building of the application were those steps provided in the 
Code Institute Boutique Ado project.
* The Order and LineItem models are modified versions of those in the Boutique Ado project.
* The images used are copyright-free images from [Unsplash](https://unsplash.com/). In particular, the 
following images are featured: 

ADD IMAGE LINKS IF POSSIBLE
