requirements: (tested on OSX Sierra)
```
pip install requests
pip install peewee
pip install pymysql
pip install python-dotenv
```

Manually create a database for this app.  Create a .env file in the project root with the following items.  Replace the bracketed items with credentials from the database you set up.
```
DATABASE={database_name}
DB_USER={database_user}
DB_PASSWORD={database_password}
```

How to build an article URL:
ign.com/articles/{slug}
