Feature: flaskr is secure in that users must log in and log out to
access certain features

Scenario: successful login
Given flaskr is set up
When we log in with "admin" and "admin"
Then we should see the alert "You were logged in"

Scenario: incorrect username
Given flaskr is set up
When we log in with "notright" and "admin"
Then we should see the alert "Invalid username"

Scenario: incorrect password
Given flaskr is set up
When we log in with "admin" and "notright"
Then we should see the alert "Invalid password"

Scenario: successful logout
Given flaskr is set up
and we log in with "admin" and "admin"
When we log out
Then we should see the alert "You were logged out"