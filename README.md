# Backend
Part of my application for Code Foo 7.  The rest of my application can be found [here](https://github.com/thomas-j-sell/codefoo7).

## Requirements:
Taken from: http://www.ign.com/code-foo/2017/

a. Using [this API](http://ign-apis.herokuapp.com/), pull a list of both articles and videos.

b. Build an app to store at least 10 articles and 10 videos from the API in a MySQL 5.6.X database. Alternatively, submit this as a set of SQL setup, table creation, and insertion commands.

c. Build a service that can read in the articles and videos from the MySQL database instance in the previous step and serve a valid MRSS feed. Use the official RSS 2.0 and MRSS 1.5.1 specifications from the [RSS Advisory Board](http://www.rssboard.org/)

## Implementation:

#### Prereqs:
Run the following commands to insure all necessary libraries are installed:
```
pip install requests
pip install peewee
pip install pymysql
pip install python-dotenv
pip install feedgen
```

Manually create a database for this app.  Create a .env file in the project root with the following items.  (Replace the bracketed items with credentials from the database you set up.)
```
DATABASE={database_name}
DB_USER={database_user}
DB_PASSWORD={database_password}
```

### Use
You can start the feed generator and server with the following command:
```
python backend.py
```

This will populate the database with items from the API, generate an RSS feed from the items in the database, and serve the feed on port 8080.  The the feed will be available at {root_url}/rss (on your local machine this will look something like localhost:8080/rss).


###### (tested on OSX Sierra)
