# Art Shop E-Commerce Application

## Purpose

* The external user goal is to view and purchase local art online.
* The internal user goal is to sell local art online.
* The site is targeted at those interested in buying art particularly from artists based in 
the West of Ireland.

* The live version can be accessed here: [Art Shop](https://art-shop-ecommerce-71a1569e3f02.herokuapp.com/)


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

* The font 'Merriweather' was used throughout the site. 
* #3c4142 (charcoal grey) was used for all key text, both headings and body.

### Accessibility

The following measures were taken to help ensure accessibility:
* All images include an 'alt' description.
* Where appropriate, HTML elements include 'aria-label' or 'aria-labelledby' attributes.
* There is a high level of contrast between the background and any text through the site to help
ensure readability.

## Features

* Features were added to provide the user with CRUD (Create, Read, Update, Delete) functionality. After logging in, the user can create a booking, read/view it, update it and delete it. 
* The admin user can create, read/view, update and delete both products and orders after logging in to the admin dashboard.

Key features are described below.

### Home Page

* The home page 

### Navigation Bar

* The navigation bar is located at the top of every page.
* The 'Artshop' icon/button in the top-left of the screen provides a link back to the 
home page.
* The 'Art' button brings the users directly to the product display page.
* The search bar in the center of the navigation bar allows the users to search for 
products using keywords.
* The 'person' icon in the top right of the screen provides a quick link to account
information. Logged-in users can click on 'My Profile' to be brought to their profile
and order history page. Logged-out users are brought to the sign in page when they click
on 'My Profile'. 
* At the very right of the screen, there is a basket icon. Clicking this icon brings 
the users to the basket page.
* The navigation bar is visible on all pages, providing quick links to all parts of 
the site.

### Sign Up, Log in and Log out

* The sign in, log in and log out pages are modified versions of the templates provided by
Allauth for user account and authentication.
* Logged-in users can access their profile page, view previous orders and edit or delete 
their information.
* The sign in and log in form inputs use built-in Django validation to check that the user 
enters a suitable password and username. 
* Logged-in admin users can access the admin dashboard and view, edit, add and delete product,
user and order information.
 
### Home Page / Index.html

* When a user first arrives on the website, they see the main heading inviting them to view
art by local artists. There is a large button which links to the main product page.

### Products Page

* The main products page displays basic information about all available products including an
image, the title, the artist and the price.
* There is a button under each product linking the user to a detailed information page for 
that product.

### Detailed Product Page

* Clicking on any product on the products page will bring the user to a detailed page for
that product.
* The user will see a large image of the product and detailed information. 
* There is an 'Add to Basket' button under the product information.

### My Basket Page

### The Checkout Page

### The Checkout Success Page

### The User Profile Page


## Future Features

* Order confirmation emails to be sent to users after successfully completing a user.
* An 'About page.
* A footer containing important links such as to detailed delivery information and 
social media pages.
* An order summary to be displayed on the checkout page.
* Alternative payment options to be provided when checking out.
* A hero image on the home page.
* A more extensive collection of artwork, each with relevant data.

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
* All views created are function-based.

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
* Stripe was used to handle secure checkout and payment by credit card.


## Testing

### Code Validation 

MUST COMPLETE VALIDATION OF ALL

* Python code was passed through the [Code Institute Python Linter](https://pep8ci.herokuapp.com/). No issues were found.

* HTML code in the template files was validated using the [W3 Validator](https://validator.w3.org/nu/). No errors were found. NOT COMPLETE

* CSS code was validated using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator).
NOT COMPLETE

### Other Testing

* This app was tested for responsiveness using the Google Chrome browser and Chrome DevTools. It has not yet been tested on other browsers.

### Test Cases

#### Test Case 1

1. Open the live app. The user is shown a home page with a large heading inviting the user to view local art. The user notices that there is a 'View Gallery' button.
2. Click 'View Gallery'. The user is brought to the gallery/products page. The user notices that there are more products further down the page.
3. Scroll down the page. The user sees a piece of art that they like. The user notices the 'View Details' button under the piece of art.
4. Click the 'View Details' button. The user sees the detailed information page for that piece of art. 
The user notices the 'Add to Basket' button.
5. Click the 'Add to Basket' button.  The user notices a success message in the top right of the screen 
with an 'x' in the corner.
6. Click the 'x'. The success message disappears. The user notices the basket icon in the top-right of 
the screen.
7. Click the basket icon. The user sees the basket page with their item details in the 
basket. The user notices the 'Secure Checkout' button.
8. Click 'Secure Checkout'. The user sees the checkout form page. The user notices that the first 
field is active.
9. Type in personal details. The user notices the delivery information section.
10. Type in delivery details. The user notices the payment information section.
11. Type in payment details. The user notice the 'Complete Payment' button.
12. Click 'Complete Payment'. The user sees the loading icon and then the successful checkout page.


### Fixed Bugs

ADD FIXED BUGS

* 

### Remaining Bugs

* It is possible to purchase the same piece of art multiple times in different orders.
* Stripe webhooks are not yet functioning correctly. In the event that a user closes the payment
window before an order is created but after payment has been processed, there is no 
back-up system in place to ensure the order is created. 
* While the app is responsive on medium to large screens, on very small screens the checkout and 
basket pages do not display correctly.

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
* The images used are copyright-free images from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/). In particular, the 
following images are featured: 
  * [sheep in field](https://www.pexels.com/photo/five-sheeps-on-pasture-during-golden-hour-1650919/)
  * [graffit portrait](https://unsplash.com/photos/floral-persons-portrait-graffiti-fT49QnFucQ8)
  * [hands](https://unsplash.com/photos/two-human-hands-painting-k39RGHmLoV8)
