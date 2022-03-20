# Nan n Gran's Scran - Testing Documentation

The Main README documentation can be found under [README.md](README.md)

# Table of contents

> 1.  [User Story Testing](#user-story-testing)
> 2.  [Home Page Testing](#home-page-testing)
> 3.  [Footer Testing](#footer-testing)
> 4.  [Register Testing](#register-testing)
> 5.  [Log In Testing](#log-in-testing)
> 6.  [Navigation Bar Testing](#navigation-bar-testing)
> 7.  [Log Out Testing](#log-out-testing)
> 8.  [Scullery Testing](#scullery-testing)
> 9.  [Browse Courses Testing](#browse-courses-testing)
> 10.  [Add New Recipe Testing](#add-new-recipe-testing)
> 11.  [Edit Recipe Testing](#edit-recipe-testing)
> 12.  [Delete Recipe Testing](#delete-recipe-testing)
> 13.  [Code Validation](#code-validation)
> 14.  [Significant Bugs](#significant-bugs)
> 15.  [Browser Testing](#browser-testing)

# User Story Testing

## As a family visitor to the website, I want to know what I can do on the website, navigate with ease using a clearly defined navigation bar, understand how to register an account and be able to see social media links to be able to contact & communicate with the developer (a family member).

**Acceptance Criteria:** Users must be able to understand the websites purpose on first visit and easily see where to register.

**Summary:**

- When the user visits the website, they are presented with a **Logo & Hero Image** containing a self-descriptive name and vintage image of an elderly lady holding a spoon.
- The **NavBar** is positioned at the top of the page, and is therefore familiar and easy to identify.
- When a user first visits the website, they are presented with a title and short description, an 'About section' which provides them with an understanding of the reason for the development of the site and awareness that they can also share their recipes on the site.
- The **NavBar** provides a clear indication of the next steps.
- The **Footer** provides social media icons as buttons to select. These open in a new page leaving the original URL available for the user to navigate back with ease/not lose the home page.
- It is therefore clear, from first visit, the name and purpose of the website.


**Outcome: Pass**

## As a user, I want the page to have an intuitive layout, so that I can interact with the site with ease without any dubiety of where to go next.

**Acceptance Criteria**: A user should be able to understand how to both navigate and interact with the website and its features, either through design, implementation or through instructions.

**Summary:**

- When the user clicks register, they are presented with a seperate **Register** page containing a self-explanatory form to complete **Username** and **Password** with a simple **Register Button** to complete their registration. 
- Should the user have forgotten they have already registered there's an available option provided at the bottom of the form **Already Registered?** & a **Log In** link for ease of use.
- The form fields have been made a 'requirement' therefore failing to complete each field provides feedback to the user that they must complete that field before they can select 'Register' keeping them on the right tracks. 
- Once registered the page automatically provides confirmation of this by a 'flash message' at the top of the page and displays a **Profile** page for the user.
- The Profile page also provides a link via a button which states 'Go to Scullery' which then takes the user to the Scullery to explore the recipes.
- Within the **Scullery** the user is able to select the type of dining **Course** they wish with a simple 'View' button taking them to the available recipes in that **Category**.
- Once the user has selected their choice of Course they can then see recipes and opt to view each individual recipe, with a button link to take them 'back to scullery'
- Once registered/logged in the user has more options on the NavBar including the **Scullery**, **Browse Courses** (taking them to the individual pages as an alternative to the visual Scullery page), go to their own **Profile**, **Add Recipe** and **Log Out**
- Within each recipe their is options to **Edit** or **Delete** the recipe or navigate back to the **Scullery** keeping it simple to use.
- Within the **Edit** and **Delete** pages these provide clear and self-explanatory forms which include **Placeholders** to keep the user on the right path, each field remains a requirement and therfore ensures each field has been provided wiht detail before it saves either the changes or saves the new recipe created. 
- The **Edit**, **Delete** and **Add Recipe** options, when complete, flash a message to the user to confirm they have either Edited, Deleted or Added a recipe.
- Considering all of the above, it is clear that there is an intuitive layout which is se;f-explanatory to the user with some hints, instructions and flash messages along the way to keep them on the right track.

**Outcome: Pass**

# Home Page Testing

- The Home page displays the intial options on the **NavBar** for a non-registered/not logged in user, as this has been created for the purposes of the developers family to use privately, the member has to create an account before they can log in and use the site: 

![Home Page NavBar Pre-Log In](static/assets/img/portfolio/HomePagePreRegLogInOptions.png "HomePagePreRegLogInOptions")

![Home Page to Log In](static/assets/img/portfolio/LogInFromHomePage.png "LogInFromHomePage")

![Home Page to Register](static/assets/img/portfolio/RegisterFromHomePage.png "RegisterFromHomePage")

# Footer Testing

- The footer bar clearly shows the social media icons with links taking to seperate pages:

![Footer](static/assets/img/portfolio/FooterSocialMedia.png "FooterSocialMedia")

- Each link was tested and work well opeining in a new page on the users browser.

# Register Testing

- The username & password fields are a requirement and was tested to ensure the user completes this and is unable to register without these, preventing a file saving with empty details on the database. It also provides the option at the bottom of the form to **Log In** if they are 'already registered?'.

![Register Required Fields Username](static/assets/img/portfolio/RegisterRequiredFieldsUsername.png "RegisterRequiredFieldsUsername")

![Register Required Fields Password](static/assets/img/portfolio/RegisterRequiredFieldsPasword.png "RegisterRequiredFieldsPassword")

- Upon registering the user is advised this was successful and automatically displays a profile page with option to 'go to Scullery':

![Register Success](static/assets/img/portfolio/RegTestSuccess.png "RegisterRequiredFieldsPassword")


# Log In Testing

- As with the Register function, the username & password fields are a requirement and these were tested to ensure the user has to complete this, they are unable to log in without the required details and this prevents saving a file with empty details on the database. It also provides the option at the bottom of the form to **Register** if they are 'new here'.

![Log In Required Username](static/assets/img/portfolio/LogInRequiredFieldsUsername.png "LogInRequiredFieldsUsername")

![Log In Required Password](static/assets/img/portfolio/LogInRequiredFieldsPassword.png "LogInRequiredFieldsPassword")

- Once logged in, the user recieves a welcome message and displays their profile page and option to go to the Scullery, which works well:

![Log In Welcome Message & Profile](static/assets/img/portfolio/WelcomeMessageProfile.png "WelcomeMessageProfile")


# Navigation Bar Testing

- Each option on the NavBar was selected and the user is taken to the desired routes succesfully.

![NavBar Options](static/assets/img/portfolio/NavBarOptions.png "NavBarOptions")

- For the same experience on a mobile view, the page NavBar is responsive and changes to a **Hamburger Icon** for dropdown menu, with all links continuing to work and take the user to their desired area on the site:

![Hamburger Icon](static/assets/img/portfolio/HamburgerIcon.png "Hamburger Icon")

![NavBar Options Mobile/Tablet View](static/assets/img/portfolio/NavBarResponsive.png "NavBarResponsive")

# Log Out Testing

- The user is given a message to confirm they have been logged out following selecting the **Log Out** option and returns them to the **Log In** page:

![Log Out Message](static/assets/img/portfolio/LoggedOutMessage.png "LoggedOutMessage")


# Scullery Testing

- The user is taken to a visual display of options to choose which course recipes they wish to view:

![Scullery Page Options](static/assets/img/portfolio/SculleryPageOptions.png "SculleryPageOptions")

# Browse Courses Testing

- The **Browse Courses** option on the NavBar also provides the available categories as an alternative to going to the **Scullery** page:

![Browse Courses Option on NavBar](static/assets/img/portfolio/BrowseCoursesOptionNavBar.png "BrowseCoursesOptionNavBar")


# Add New Recipe Testing

- Adding a recipe is accessed with ease via the **Add Recipe** option on the NavBar and displays a new add recipe form for the user to complete with clear instruction 'add your recipe here!'. All fields are required fields, including placeholders to keep the user right, and there is an option to upload an image of their recipe (*NOTE: Please see the significant bugs section regarding the upload image function*)
- A cancel button is also availble if the user changes their mind and is redirected abck to the Scullery section.
- Once the **Add to Scullery** option has been selected the form confirms to the user by **Flash Message** that this has been successful: 

![AddRecipeHere](static/assets/img/portfolio/AddRecipeHere.png "AddRecipeHere")

![Log Out Message](static/assets/img/portfolio/LoggedOutMessage.png "LoggedOutMessage")


# Delete Recipe Testing

![Log Out Message](static/assets/img/portfolio/LoggedOutMessage.png "LoggedOutMessage")


![Log Out Message](static/assets/img/portfolio/LoggedOutMessage.png "LoggedOutMessage")


![Log Out Message](static/assets/img/portfolio/LoggedOutMessage.png "LoggedOutMessage")



# Code Validation

