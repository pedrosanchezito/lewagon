# Twitter API - Day 2

Go back to yesterday's repository:

```bash
cd ~/code/<github_username>/twitter-api
```

## Specifications

Re-using all your learnt yesterday about Flask and today about SQLAlchemy, implement the following API endpoints using a proper database. Don't forget to use feature branches (GitHub Flow) and push to Heroku regularly. You can skip TDD and test your endpoints directly in the browser or with [Postman](https://www.getpostman.com/)

1. List all tweets
1. Create a tweet
1. Update a tweet
1. Delete a tweet

Once you have basic CRUD for tweets, let's introduce a second model: `User`. There is a `1:n` association between `User` and `Tweet`, make sure it's correctly declared in the `models.py` file (cf [documentation](http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-many)). A `User` should have the following properties:

1. Username
1. API Token

The API token should be unique to each user and **auto-generated** at user creation.

Once you have this in place, update your previous `Tweet` endpoints so that a new tweet can be created if and only the request is logged in (you may use the `Authorization` HTTP request header for the API token). Using the same technique, protect the Update and Delete endpoints with a layer of authentication.

## Food for Thought

Yesterday, the `create_app` factory pattern is introduced. You will need to use `init_app` as explained on [this blog article](http://goonan.io/flask-application-factories/)

What about testing? Should you implement tests, how do you deal with the database? You will need a **separate** PostgreSQL database schema and use `setUp()` / `tearDown()` in the `TestCase`s to make sure each test is run on a clean database. More info on [this StackOverflow thread](https://stackoverflow.com/questions/17791571/testing-flask-sql-alchemy)

