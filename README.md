![Picture of the website on different devices](static/images/responsive_img.png)

# The Jetsetter Journal

The Jetsetter Journal is a website for frequent travellers to share their recommendations for specific destinations or to pick up suggestions for upcoming holidays. The [live website is here](https://the-jetsetters-journal-834f32dcb176.herokuapp.com/).

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
### Deployment
### Credits

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



[Insert user flow diagram here.]

The site will consist of 10 pages, including:

### Home page
- Site branding, about section
- Navigation bar
- Location map (powered by Google Maps API)

### Registration page
- User sign-up form

### Login page
- User login form

### Profile page
- Summary of user recommendations

### Location/recommendations page
- All destinations and recommendations

### Add recommendations page
- Form to add recommendations

### Edit recommendations page
- Edit user's recommendations

### Add locations page
- Form for superusers to add locations

### Edit locations page
- Edit locations added by superusers

### Logout page
- Logout confirmation page

## Database Structure

[Link to database structure diagram.]
[Screenshots of example database records.]

The database structure includes collections:
- Users
- Recommendations

Posts have titles, content, author (username), date, and category name.

Recommendation Categories:
- Things to do
- Where to eat
- Where to stay

An index in MongoDB is used to query posts by location and category name.

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
