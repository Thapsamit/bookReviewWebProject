# bookReviewWebProject

## Project Overview/Introduction:-

This project **“Book Review Website”** is a full stack website covering the front end and back end technologies. In this project we provided the user a platform where they are able to register for our website and then log in using their Email and password.
Once the user logged in they can search  for a particular book from the handpicked 5000 books database through book’s ISBN, Author Name and Title. They will be able to give their reviews and star rating to the book they like and can also checks the ratings and reviews by other users of the website so that they can know the feedbacks of the books by the other users. Added with these the user can also make changes to their profiles, can edit the review any time and delete it too.
The project also includes an API. When calls to the API are made, using an ISBN number, users will be able to access details about the relevant book.

## Objectives:-

-	To create a full stack website.
-	To gain experience with web technologies like html, css, js, python,mySql
-	To perform all CRUD i.e Create, Read,Update and Delete operations in a website.
-	To give users a platform to share their feedbacks with others.
-	To create an API that allows others to use our book’s data in json format.

# Target Audience:-
This application aims to attract people that like to read, look for next book to read, like to share their thoughts on books they have read, and interact with other readers. The website provides user with information about various books and reviews, and enables them to share their own reviews and interact with other users. Users are also able to edit and delete their reviews at any time
The main objective of the website is to provide a user with a tool that will enable them to **read / add / comment / rate for reviews.**

# Technologies/Tools Used:-

# Programming Languages:-
-	HTML - the project used HTML to define structure and layout of the web page;
-	CSS - the project used CSS stylesheets to specify style of the web document elements;
-	JavaScript - the project used JavaScript to implement some dynamicity in the website like to perform some button clicks, reponsivness etc.
-	Python - the project back-end functions are written using Python. 

# Frameworks:-
-	Flask - web application framework used to create functions with Python that are injected into html templates. Various flask extensions were used to validate login / register form, create routes, paginate reviews, manage login and logout.
Databases:-
-	MySQL – A relational database for storing the data in structured format.

# Libraries/CDNs:-
-	Google Fonts - Google Fonts library is used to set up font type for the document.
-	Font Awesome – Font awesome is used to use different icons in the website.
-	Open Library – API for displaying images of book of specific ISBN.

# Others:-
-	Jinja Template - A Jinja template is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc.). This contains variables and/or expressions, which get replaced with values when a template is rendered  and tags, which control the logic of the template.
-	pip – It is package manager for installing external libraries, extensions and additional packages.
-	Visual studio – Code editor for development.
-	Chrome/firefox


# Databases:-
-	In this project MySQl relational database is used for creating, storing, updating and deleting the data related to website.
-	The database for this project consists of three collection or tables namely Users, Books, Reviews.
## Tables/Schemas:-
-	Users – It contains all the necessary information about the users like Name, Username, Email, Password.
-	Books – It contains the complete collection of  5000 books that include details of ISBN, Book Title, Author Name, Year.
-	Reviews – It contains the Review and ratings given by different users.
## Relationships between tables:-
-	Users and Reviews – One to many relationship as one user can be associated with many records in review table.
-	Books and Reviews – One to many relationship as one book can be associated with many records in review table.


# Features/File Structure:-
 Static:-
     img:-
-	It contains all the images that are used in project.
script.js:-
-	It contains all the function that performed dynamically like during a button click.
style.css:-
-	It contains all the basic style of the website.
utilities.css:-
-	It containes all the styles that are used more often like btn styling, modals, responsiveness etc.

Templates:-
This folder contains all the html files that are used in the project.
     includes:-
-	This folder contains all the navbars or footers that are used throughout the project like dashboardnavbar, homenavbar, registernavbar, loginnavbar etc.
layout.html:-
-	This page contains the basic html structure including all the links of stylesheet and external cdns.This page extended to all the other html pages.
index.html:-
-	This file contains the homepage or landing page of website with links to register or login page.
register.html:-
-	This page contains a form that allows the user for registering in the website to create a profile with details like username, email, password, name. If all the details are filled and correct then it will create an account.
login.html:-
-	The application.py file automatically routes to the login page when user is registered or not logged in. Login is a simple form that posts information to the login route. After checking the information entered is correct and matches the users table in the database, user is routed to the dashboard otherwise an error message will be flashed.
dashboard.html:-
-	The dashboard page is shown up once a user has logged in. The page mainly has a search panel where user can search for books using the title, author or ISBN. 
-	Once a user has logged in, they should be taken to a page where they can search for a book. Users should be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page should find matches for those as well!
search.html:-
-	This page shows up all the books with basic details like Title, Author Name, ISBN and a button to go to the info section of the book based on the search query given by the user.
info.html:-
-	 When users click on a book from the results of the search page, they will be directed to this page, with details about the books Such as its title, author publication year, ISBN number, and any reviews that other users have left regarding the book on this website. 
-	It also contains the average rating and no. of reviews a book has received.
-	In  addition users are able to submit a review with rating on scale 1 to 5 and can submit it only 1 time as the submit button will not be displayed if the user already submitted the review although edit button will be there to edit the existing review.
profile.html:-
-	This contains the basic details about the users and we have given a provision of editing the profile at any time or can “Delete  the account” as well to teminate all his reviews from the website.
myreviews.html:-
-	This page contains all the reviews or ratings submitted by the user with his id.
-	This page helps the user to directly go to a book of which he wanted to change his review or delete it  and also a direct delete button is also available as well.

books.csv:-
-	It contains all the 5000 books available.

import.py:-
-	This contains the code that import all the books details in the database.

app.py:-
-	The main flask application. This file initializes and configures the web application, links to the database hosted locally in the system , and handles all sites routing. 

Routes in app.py:-
-	route(‘/’) or route(‘/index’) – for displaying the index page.
-	route(‘/register’,methods=[‘GET’,’POST’]) –  it displays the register page for new user
-	route(‘/login’,methods=[‘GET’,’POST’]) –  it allows the logging in of the user.
-	route(‘/dashboard’,methods=[‘GET’,’POST’]) – It shows the dashboard that contains the search bar.
-	route(‘/dashboard/search’,methods=[’POST’]) – it gives all the search results.
-	route(‘/dashboard/profile’,methods=[‘GET’,’POST’])–  it displays the profile of the users.
-	route(‘/dashboard/myreviews’) – It shows all the reviews submitted by the logged in user for any book.
-	route(‘info//<string:isbn>’, methods=[‘GET’,’POST’])) – It shows the page that contains the book information and review box and review section.
-	route(‘/edit/<string:isbn>’) – It not shows any page whereas it allows the editing of the review and the redirect the logged in user in the same info page of the book.
-	route(‘/delrevmy/<string:isbn>’) – It has the code that is used to delete the review
-	route(‘/logout’) – it logs outs the user from session.
-	route(‘/delacc’) – This route deletes the user account compeletely and then redirects to the register page.
-	route(‘/api/<string:isbn>’) – This route shows the page that contains the API that means the data of particular book in json format.

