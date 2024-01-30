![Picture of the website on different devices](static/images/responsive_img.png)

# The Jetsetter Journal

The Jetsetter Journal is a website for frequent travellers to search for inspiration for their upcoming holidys. Users are also able to share and manage their own recommendations via their profile page.

The functions to build this application were written in Python and using the Flask framework. All data was stored in a Mongodb non-relational database and was deployed via Heroku. 

The [live website is here](https://the-jetsetters-journal-834f32dcb176.herokuapp.com/).

## Table of Contents

### User Experience (UX)
- Strategy
- Scope
- Structure
- Skeleton
- Surface

### Features
### Technologies
### Testing
- Test Results and Bugs
### Future Improvements
### Deployment
### Credits

-----

## Strategy

### Site goals
- To give travellers the opportunity to share their travel experiences and recommendations for specific destinations.
- To provide information to travellers planning an upcoming holiday and looking to put together an itinerary.

### User Stories

#### As a first-time user:
- I want to understand the purpose of the website as soon as I land on it.
- I want the site to be fully responsive and viewable on any device.
- I want to easily return to the homepage if any errors occur.

#### As a user without an account:
- I want to find what I need easily with intuitive navigation.
- I want to view information about the destination I plan to travel to.
- I want the opportunity to create an account.

#### As a user with an account:
- I want to sign in to my account.
- I want to log out successfully.
- I want to search and filter destination information.
- I want to add my own recommendations.
- I want to view, edit, and delete my recommendations.

------

## Scope

The table below shows all planned features of the site, detailing the user type, difficulty, and importance ratings. Prioritization will be based on these ratings during the build phase.

| User               | Feature                                                       | Difficulty | Importance |
|--------------------|---------------------------------------------------------------|------------|------------|
| All users          | Responsive Design                                              |     3     |      4   |
| All users          | MongoDB database creation to store data                        |      5      |        5    |
| All users          | Navigation                                                    |       1    |      4      |
| All users          | Home page - branding and about section                         |       1     |      2      |
| All users          | Home page - travel destination on map with clickable markers |      5      |       3     |
| Users with an account | Travel destination information page with ability to view user recommendations |       3       |      4      |
| All users          | Log-in functionality                                          |     5       |       5    |
| All users          | Registration functionality                                     |      5      |      5      |
| All users          | Error pages providing home page links                          |       2     |     3       |
| Users with an account | Logout functionality                                        |       5     |       5     |
| Users with an account | Profile page                                                   |    4        |     4       |
| Users with an account | Add recommendation functionality                              |      5      |       5     |
| Users with an account | Edit/ delete functionality for user’s own recommendations     |       4     |        5    |

------

## Structure

![Flow diagram of how the app will function](static/images/flow_chart.png)

The site will consist of 9 pages, including:

### Home page and search page
- An about section explaining the purpose of the app
- Search bar that enables the user to view all recommendations made on the app and filter the results by user, category, city name and comment

### Registration page
- User sign-up form

### Login page
- User login form

### Profile page
- Interactive map with clickable markers that signals to the user what countries they can get information on 

### Location/recommendations page
- Loads the user recommendations and location information based on the country that was selected on the interactive map
- Users are able to view the recommendations they've created and choose to edit or delete their recommendations

### Add recommendations page
- Form to add recommendations

### Edit recommendations page
- Form to edit a recommendation

### Delete recommendations page
- Confirmation page asking if the user is sure they want to delete a particular recommendation

### Logout page
- Logout confirmation page

-----

## Database Structure

All data was stored in a Mongodb non-relational database. The database itself was made up of 3 collections: 

- Users
- Locations 
- Recommendations 

Each user was structured in a document consisting of the following information:

![Example of a document in Users collection](static/images/users.png)

Users signed up with a username and a password which was hashed by Werkzeug before being stored in Mongodb. All recommendations added to the platform were assigned with the corresponding username who created them. 


Each location available to view and add recommendations to was structured like so: 

![Example of a document in Locations collection](static/images/location.png)

The location information was dynamically rendered to the view_recommendations page depending on which location was clicked on the interactive map. 


Each recommendation added to the application was structured in the following way: 

![Example of a document in Recommendations collection](static/images/recommendations.png)

All recommendations were assigned a city_id which corresponds to the object_id of the location that each recommendation was for. For example, a recommendation for Bangkok contained the object_Id for the location of Bangkok. This was stored under the field city_id. This was useful when adding recommendations or searching for specific recommendations under a specific city name. 

Recommendations were grouped into 3 categories: 

- Things to do
- Where to eat
- Where to stay

All recommendations had an objectID that enabled specific recommendations to be queried and rendered to the application interface. This made it possible for editing and deletion of recommendations on the site.

## Skeleton

[Wireframes for Desktop, Tablet, and Mobile.]

## Surface

### Images
- Background hero image

### Colors
- Darker and lighter shades of green

### Fonts
- Lobster (hero image text overlay, brand text)
- Roboto (main font across the site)

Text consistency across pages:
- Centered title and small summary
- Remaining content aligned to the left
