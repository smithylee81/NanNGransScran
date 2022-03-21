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

- Database Test **(MongoDB)**: When a user successfully registers, a document is successfully written to the 'Users' collection in the Database, in the following format:
_id: Unique object ID generated by MongoDB
Username: A lowercase version of the username provided by the user.
Password: A hashed version of the password provided by the user.

# Log In Testing

- As with the Register function, the username & password fields are a requirement and these were tested to ensure the user has to complete this, they are unable to log in without the required details and this prevents saving a file with empty details on the database. It also provides the option at the bottom of the form to **Register** if they are 'new here'.

![Log In Required Username](static/assets/img/portfolio/LogInRequiredFieldsUsername.png "LogInRequiredFieldsUsername")

![Log In Required Password](static/assets/img/portfolio/LogInRequiredFieldsPassword.png "LogInRequiredFieldsPassword")

- Once logged in, the user recieves a welcome message and displays their profile page and option to go to the Scullery, which works well:

![Log In Welcome Message & Profile](static/assets/img/portfolio/WelcomeMessageProfile.png "WelcomeMessageProfile")


# Navigation Bar Testing

- Each option on the NavBar was selected and the user is taken to the desired routes succesfully.

![NavBar Options](static/assets/img/portfolio/NavBarOptions.png "NavBarOptions")

- For the same experience on a mobile view, the page NavBar is responsive **(Bootstrap 5)** and changes to a **Hamburger Icon** for dropdown menu, with all links continuing to work and take the user to their desired area on the site:

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
- A cancel button is also availble if the user changes their mind and is redirected back to the Scullery section.
- Once the **Add to Scullery** option has been selected the form confirms to the user by **Flash Message** that this has been successful: 

![Add Recipe Here](static/assets/img/portfolio/AddRecipeHere.png "Add Recipe Here")

![Recipe Add Success](static/assets/img/portfolio/RecipeAddSuccess.png "RecipeAddSuccess")

# Edit Recipe Testing

- After completing the edit recipe form and clicking 'edit recipe' a flash message is returned to the user confirming the edit success: 

![Edit Recipe Success](static/assets/img/portfolio/EditRecipeSuccess.png "EditRecipeSuccess")


# Delete Recipe Testing

- The option to delete a recipe is on all cards (*NOTE: Please see the 'Nice to Have' section in the README.md file on this option only being available to the users who created the recipe- impacted on due to time constraints*)

![Delete Option All Recipes](static/assets/img/portfolio/DeleteOptionAllRecipes.png "DeleteOptionAllRecipes")


![Recipe Deleted Message](static/assets/img/portfolio/RecipeDeletedMessage.png "RecipeDeletedMessage")


## Responsive Layout and Design

The features detailed above were re-tested for use on all viewports, including the user interface for responsive layout and design.

### Browser Based Testing

Using Chrome Development tools, either via the pre-set mobile device resolutions or via the manual responsive tool (using `Google Lighthouse Inspection Tool`), the following was completed:

- Manual responsive testing via Chrome Development Tools, selecting `Inspect`.
- Cycling through each available device, and performing the tests as detailed above:
  - iPhone SE
  - iPhone 12 Pro
  - iPhone XR
  - Pixel 5
  - Samsung Galaxy S8+
  - Samsung Galaxy S20 ULtra
  - iPad Air
  - iPad Mini
  - Surface Pro 7
  - Surface Duo
  - Galaxy Fold
  - Samsung Galaxy A51/71
  - Nest Hub
  - Nest Hub Max
- Ensure all Features function and appear correctly from at least 320px wide.
- Ensure Cards and Modals **(Bootstrap 5)** are presented appropriately on all viewports:
  - Interaction is enabled.
  - The Modal fits on device's screen.
  - The content is legible.
  - The user can dismiss the modal.
  - The user can select all available options.

### Mobile and Tablet Testing

The website was physically tested on an iPhone 11, and an iPad. The following tests were completed:

- Ensure all interactive **icons** are distinguishable, identifiable, and are correctly sized and placed to allow users to interact with each of them via touchscreen individually.
- Ensure all inputs within data entry fields and forms respond appropriately to touchscreen devices.
- Ensure all text input fields respond appropriately to on-screen keyboards.
- Ensure the **Dropdown Nav** can be selected to collapse or reveal.

## Additional Testing

## Basic Routing

Test 1: **get requests**

- **Overview** : Test the response from a **get** request to the appropriate`/` URL *('/soups', '/starters' etc)*.
- **Expected Result** : 200 response code, appropriate templates returned.
- **Outcome** : Pass

![Get Starters Request](static/assets/img/portfolio/GetStartersRequest.png "GetStartersRequest")

![Get Soups Request](static/assets/img/portfolio/GetSoupsRequest.png "GetSoupsRequest")

Test 2 **: post requests**

- **Overview** : Test the response from a **post** request to the appropriate `/` URL *('/new_recipe', '/edit_recipe' etc)*
- **Expected Result** : 200 response code, and appropriate templates returned.
- **Outcome** : Pass

![Get Soups Request](static/assets/img/portfolio/GetSoupsRequest.png "GetSoupsRequest")


## Database CRUD

Test 1: **test registration**

- **Overview** : Submit a **post** request to `/register`, and check a user has been added to the **users** collection within MongoDB.
- **Expected Result** : User added to the database, and username verified against that provided during the Post request for registration.
- **Outcome** : Pass

Test 2: **test new recipe creation**

- **Overview** : Submit a **post** request to `/new _recipe`, and check a new recipe has been added to the **recipes** collection within MongoDB.
- **Expected Result** : A new recipe is successfully written to the database, and subsequently retrieved from the database for verification.
- **Outcome** : Pass

Test 3: **test update/edit recipe**

- **Overview** : Submit a **post** request to `/edit_recipe`, and verify the details on MongoDB for full contents and ID comparison.
- **Expected Result** : Recipe is successfully edited and updated within the database.
- **Outcome** : Pass

Test 4: **test delete recipe**

- **Overview** : Delete a recipe on the website, this is deleted from the Database collection 'recipes'.
- **Expected Result** : Recipe is successfully deleted from website and database respectively.
- **Outcome** : Pass

## Chrome/Firefox/Edge/Safari (iOS)

All functionality worked as intended.

# Code Validation

## HTML

- The project's HTML was validated using the automated [W3 Markup Validator](https://validator.w3.org/) at intervals throughout the development process.
- All HTML files were assessed:
  - base.html
  - edit_recipe.html
  - home.html
  - login.html
  - mains.html
  - new_recipe.html
  - profile.html
  - puddings.html
  - register.html
  - scullery.html
  - soups.html
  - starters.html
  - view_recipe.html

### Errors:
- 'Error: Bad value' highlighted in most pages due to the presence of the Jinja templating {} syntax.
- 'Error: No space between attributes': Same fixed.
- 'Error: The value of the for attribute of the label element must be the ID of a non-hidden form control': Same fixed; spelling error on the word summary (written as 'summmary').
- 'Error: Non-space characters found without seeing a doctype first. Expected <!DOCTYPE html>': Same not fixed as throwing due to Jinja templating ({% extends "base.html" %}).
- 'Error: Element head is missing a required instance of child element title': Same not fixed as throwing due to Jinja templating ({% extends "base.html" %}).


## CSS

- The project's CSS was validated using the automated [W3 Jigsaw Validator](https://jigsaw.w3.org/css-validator/) at intervals throughout the development process.
- At time of deployment, there is 1 warning and 1 error:
  - Warning (3): ` Imported style sheets are not checked in direct input and file upload modes`.
    - Satisfied this is informational to confirm imported style sheet is not being validated.
  - Error (79): `Value Error : text-shadow Too many values or values are not recognized : #959596`
    - Satisfied these can be dismissed.

# Significant Bugs

## 

**Fixed: Yes**

When initially implementing an Expiry Date/Time for MongoDB to index TTL from, Time Zones were not considered. As my Time Zone matched UTC (the standard time format [MongoDB uses](https://docs.mongodb.com/manual/tutorial/model-time-data/)), at the time of initial implementation, I did not encounter any issues. However, following the change to Daylight Savings, I realised that the Expiry Date/Time a user was inputting into the database was being stored as pure UTC. As such, when storing an expiry of 15:00 (as a GMT+1 user), this was being stored directly into the Database as 15:00 (UTC), and was therefore not expiring until 16:00 (the GMT+1 representation of 15:00 UTC).

Many solutions were explored to try and implement Time Zone conversion, and consideration was given as to **how** a Time Zone could be obtained from the user, given the user, server, and database could all potentially be in different Time Zones at any given time.

Given any logic within python would be calculating a DateTime depending on the Time Zone of the server it was being hosted on, the first step was to obtain the user's Time Zone via the browser, before attempting to handle and process this data in the server. The following JavaScript code snippet taken from [StackOverflow](https://stackoverflow.com/a/34602679/13810970) obtains a user's [IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) Time Zone.

```javascript
Intl.DateTimeFormat().resolvedOptions().timeZone;
```

With a user's Time Zone now accessible, a decision had to be made as to how to store this information. The following solution was considered:

- Storing the user's Time Zone in an additional parameter in the **expiry** field within a document in the **messages** collection.
  - Considering the PEP8 warnings regarding the complexity of the existing **Wyspa** class, it was decided not to proceed with adding additional attributes to the class.

Ultimately, the decision was made to create hidden form fields within the Login and Register forms, which are automatically populated with the user's Time Zone (using the aforementioned code snippet). This is then passed to the server when a user Registers/Logs In, and is stored in the Session, under the **timezone** key. This results in the user's Time Zone being accessible at any time within Python.

When a user **Creates** or **Edits** a **Wyspa,** the time is converted to a DateTime object, and assigned the Time Zone of the current user before being submitted to MongoDB. A helpful discussion on this topic was found on [StackOverflow](https://stackoverflow.com/a/4771733/13810970). As this DateTime object is now Time Zone aware, when submitted to MongoDB it is automatically converted to UTC based on this information.

The next step was to decide how to convert this UTC Date Time back to a User's Time Zone whenever it was to be displayed back to the user. The following solution was considered:

- Utilising MongoDB's aggregate functions such as [toDate](https://docs.mongodb.com/manual/reference/operator/aggregation/toDate/) or [dateToString](https://docs.mongodb.com/manual/reference/operator/aggregation/dateToString/), combined with a [Time Zone Offset](https://docs.mongodb.com/manual/reference/operator/aggregation/hour/).
  - Unfortunately, these features are only available for paid databases.

The decision was made to make a standard query from the database, and replace the Expiry attribute of each returned Wyspa object with a Time Zone converted version of the UTC time object retrieved from the database. Once this is complete, it can then be converted to the appropriate string value to be presented to a user.

In order to test this fully, a user in Spain (UTC+2) created a Wyspa, and shared their **My Voice** page (which displays Wyspas' expiry dates), for me to compare against the relative document stored in the MongoDB collection:

![spain_my_voice](https://res.cloudinary.com/bak2k3/image/upload/v1619531109/WYSPA/Spain_Wyspa_Page_f354d8.png)

![spain_mongoDB](https://res.cloudinary.com/bak2k3/image/upload/v1619531108/WYSPA/Spain_DB_Entry_mjrfx0.png)

This solution means a user can submit a Wyspa whilst in one Time Zone, and be presented with its relative Expiry date if viewing the website in a country with a different Time Zone.

**Assigning Expiry Date the user's Time Zone**

```python
user_timezone = tz.gettz(session["timezone"])
formatted_expiry = formatted_expiry.replace(tzinfo=user_timezone)
```

**Converting Expiry Date from UTC to user's Time Zone**

```python
user_timezone = tz.gettz(session["timezone"])
formatted_expiry = formatted_expiry.astimezone(user_timezone)
```

## Double Form Submission

**Fixed: Yes**

When initially implementing and testing the **Wyspa: Comment** feature, I accidentally clicked the **Add** button within the comment form after inputting a comment. This resulted in two identical comments being added to the **Wyspa**. This brought to light the fact that forms were capable of rapidly being submitted.

![Double Comment](https://res.cloudinary.com/bak2k3/image/upload/v1619531106/WYSPA/empty_comment_oqhsru.jpg)

After researching a [potential workaround](https://www.bram.us/2020/11/04/preventing-double-form-submissions/) to this, I implemented an **is-submitting** class, which is attached to forms (via a custom JavaScript function) following submission, and all forms are prevented from being submitted if they contain this class. As such, after a form has been submitted, it will be blocked from being submitted on subsequent attempts.

However, this had an unintended effect on the Registration Form. If a user attempted to register with an invalid Username, Password, or Confirmation Password, they were prevented from subsequent attempts to register until the browser had been refreshed or the user navigated to a different page.

In order to rectify this, the registration form was excluded from the global form function discussed above, which applied **is-submitting** to all forms on submission. Instead, the addition of the **is-submitting** class was added to custom form-validation script, as part of the final checks when all other fields are valid. As a result of this, the registration form is still subject to the **is-submitting** submission exclusion, but the class is only added when all fields within the form are valid.

## Login and Register Modals

**Fixed: Yes**

When implementing the Login and Register Modals, I was keen to ensure that a user was never redirected away from any content in order to perform these actions. However, due to the size of the on-screen keyboard on physical mobile devices, and due to the implementation of modals in Materialize CSS, I identified that when attempting to log in or register on physical devices, the on screen keyboard would cause the respective modal to shrink, causing a user to have to scroll through the respective interface to log in or register. As you can see from the examples below, this resulted in validation errors or buttons being hidden from the user.

![Old login mobile](https://res.cloudinary.com/bak2k3/image/upload/c_scale,h_765/v1619531061/WYSPA/LoginMobile2_lx9gdj.jpg)

![Old Register](https://res.cloudinary.com/bak2k3/image/upload/c_scale,h_765/v1619531062/WYSPA/RegisterMobile2_qjdq6p.jpg)

The solution to this was to replace these modals with **slide-up** modals. I found that these inherently utilised space on the device more efficiently and effectively, and obfuscated less of the user's view when initially interacted with. The **help** modal still uses normal modals, as the variation of interfaces produces a much more dynamic website as a whole.

![New Mobile Login](https://res.cloudinary.com/bak2k3/image/upload/c_scale,h_765/v1619531061/WYSPA/loginnewmobile_pkd5vh.jpg)

![New Mobile Register](https://res.cloudinary.com/bak2k3/image/upload/c_scale,h_765/v1619531061/WYSPA/registernewmobile_tzetti.jpg)

## Unexpected Date Picker Behaviour

**Fixed: Yes**

When initially implementing the **Date and Time Pickers** for **Wyspa: Create** and **Wyspa: Edit**, the features were tested on a physical mobile device. While these features appeared to work fine on Chrome Developer Tools, when using a mobile browser (tested on Chrome and Firefox), the **Year** and **Month** drop-downs within the **Date Picker** was automatically disappearing on the first interaction every time. This provided a very poor user experience, so I attempted to research what was causing it.

After reaching a dead end with the specific nature of this particular issue, I looked into the Materialize CSS [issues](https://github.com/Dogfalo/materialize/issues) to find 616 open issues, with the last commit being in June 2020. A discussion on one of the issues stated the repository was [no longer being supported](https://github.com/Dogfalo/materialize/issues/6615), and that a group of contributors had forked the project and have been producing nightly builds of a _"community enhanced"_ [Materialize CSS](https://github.com/materializecss/materialize).

I created a new branch within my project (called nightly-css), and attempted to integrate a [nightly build](https://nightly.link/materializecss/materialize/workflows/nightly/v1-dev/build) of the community enhanced Materialize CSS on the off chance that this would resolve the Date Picker behaviour. After hosting the source code locally, and removing the CDN links to the old Materialize, I tested all features of the website thoroughly, and while there did not appear to be any substantial differences to the framework (other than a [deprecated component](https://github.com/materializecss/materialize/pull/49) of the Toast that I needed to update), everything worked as intended, and the Date Picker dropdowns no longer dismissed on first interaction; this is the reason the project uses the open sourced, community driven, version of Materialize CSS.

The deployed version of this project uses the first full [Alpha](https://github.com/materializecss/materialize/releases) release of the community enhanced Materialize CSS.

## Changing Layout in Chrome Dev Tools Breaks Page Layout

**Fixed: No**

When using Chrome Development Tools, when switching between a Responsive Layout and a Mobile-Specific layout, the page's structure will **sometimes** not update to the new screen size. While the background of the website remains full screen, all other components, whilst appearing to maintain the correct aspect ratio for the given device, do not fill the screen.

![Chrome Mobile Dev Tools](https://res.cloudinary.com/bak2k3/image/upload/v1619531062/WYSPA/chrome-dev-mobile_jbkgaa.jpg)

I have been unable to pinpoint the reason why this happens, and it doesn't appear to happen every time, however I am aware this is a development bug only, and would never have an impact on user experience. The website has been tested extensively on physical devices, and while using browsers (without inspector/development tools open) and this bug cannot be recreated in these instances.

## Korea Uses Default Map Style

**Fixed: N/A**

While testing the **Map** feature, I identified that when zooming into South Korea, all **Map** styles are reverted to default.

![Korea Google Maps](https://res.cloudinary.com/bak2k3/image/upload/v1619531106/WYSPA/Korea_Google_Maps_stumu2.jpg)

However, having [researched this issue](https://support.google.com/maps/forum/AAAABJRTXHEAI_0FslsAs4/?hl=ko&gpf=%23!topic%2Fmaps-ko%2FAI_0FslsAs4), it appears that South Korea has restrictions on the ability to export **Map** data to overseas data centres, and as such some **Map** stylings do not apply. Accordingly, there is no fix for this bug, and the issue remains.

---

[Click here](README.md) to return to the main README.md.