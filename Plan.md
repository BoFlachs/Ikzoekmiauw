# Plan for Ikzoekmiauw

## General structure
- Header
    - Ikzoekmiauw banner
    - With a picture of a cat
- Nav-bar 
    - Links to the pages
    - Login button
- Home page
    - Cute picture of a cat
    - Big button directing to Katalogus
    - Some general information
    - (Highlighted cats)
- Katalogus
    - List of available cats
    - Paginated (6, 12 or 24)
    - Search bar
    - Filter on many properties
    - Including thumbnail and summary of cat
- Ditjes en katjes
    - Tips for choosing the right cat
    - Tips for taking care of your cat
    - Tips for putting a cat up for adoption
- Mijn account
    - Only visible for logged-in users
    - Profile
    - Favorite cats
    - My adoptions (Information on current adoption)
    - Logout
- Contact 
    - Contact form for putting cat up for adoption
    - Information for other questions
- Footer
    - Contact information
    - Privacy statement
    - Copyright statement
    - (Links to important pages)



## Technical structure
### App structure
- Layout app
    - Contains the home page view
    - Contains the 
- Katalogus app
- Account app
- Contact app

### File structure
- static
    - contains images and css files
- templates
    - contains base.html
- templates/partials
    - contains header, footer files
- \<app\>/templates
    - contains the specific html files for that app


### Database structure
- User (built-in)
    - pk: id
- Cat
    - pk: id
    - All the properties a cat can have
- Contact form
    - pk: id
    - email
    - name
    - question
- Profile
    - https://dev.to/earthcomfy/django-user-profile-3hik
    - one-to-one: user
    - all the profile records
    - one-to-many: favorite cats
    - etc.



## To do list
- 