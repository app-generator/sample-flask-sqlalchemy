# Flask Database Sample

**Flask** Sample project that provides an integration of **SQLAlchemy** ORM on top of a simple Flask Codebase. **[Flask Database](https://blog.appseed.us/flask-database-how-to-create-sqlite/)** project might help beginners to code a `real` project on top of Flask. For newcomers, Flask is a lightweight web application framework written in Python. By using a database in our project, we can have a persistent data layer that can be reused and updated according to application requirements.  

<br />

> Features

- Simple Flask codebase built with `simplicity` in mind
- DBMS: `SQLite` Storage
- DB Tools: `SQLAlchemy` ORM, `Flask-Migrate` (schema migrations)
- Permissive MIT License - allows unlimited copies for hobby and commercial products
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).

<br />

> Implementation 

- Add `SQLAlchemy` ORM to the `requirements.txt`
    - [SqlAlchemy](https://pypi.org/project/SQLAlchemy/) - v1.4.5     
    - [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/) - v2.5.1      
- `Update codebase` to use `SQLAlchemy`
- Define a `new model`
- `Populate` the new table with `new data`
- Visualize the information using `SQLiteBrowser` tool
- Use a `migration` to update the model (add new field)
    - Integrate/Use [Flask-Migrate](https://pypi.org/project/Flask-Migrate/) v2.7.0
- Visualize the information using `SQLiteBrowser` tool

<br />

> Links

- [Atlantis Lite Flask](https://appseed.us/admin-dashboards/flask-dashboard-atlantis-dark) - Free Starter with more features:
    - Authentication, Blueprints, Dual Config (dev & production), Deploy scripts.
- [Atlantis Lite Flask - Demo](https://flask-atlantis-dark.appseed-srv1.com/) - LIVE Deployment

<br />

![Flask Database Sample - App main screen.](https://raw.githubusercontent.com/app-generator/flask-database-sample/master/media/flask-database-sample-screen.png)

<br />

## Build from sources

```bash
$ # Clone the sources
$ git clone https://github.com/app-generator/flask-database-sample.git
$ cd flask-database-sample
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the Jinja Template
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the UI in browser: http://127.0.0.1:5000/
```

<br />

## Codebase structure

The project has a simple structure, represented as bellow:

```bash
< PROJECT ROOT >
   |
   |-- app/__init__.py
   |-- app/
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/
   |    |    |
   |    |    |-- includes/                 # Page chunks, components
   |    |    |    |
   |    |    |    |-- navigation.html      # Top bar
   |    |    |    |-- sidebar.html         # Left sidebar
   |    |    |    |-- scripts.html         # JS scripts common to all pages
   |    |    |    |-- footer.html          # The common footer
   |    |    |
   |    |    |-- layouts/                  # App Layouts (the master pages)
   |    |    |    |
   |    |    |    |-- base.html            # Used by the common pages like index, UI
   |    |    |    |-- base-fullscreen.html # Used by auth pages (login, register)
   |    |    |
   |    |  index.html                      # The default page
   |    |  login.html                      # Auth Login Page
   |    |  register.html                   # Auth Registration Page
   |    |  page-404.html                   # Error 404 page (page not found)
   |    |  page-500.html                   # Error 500 page (server error)
   |    |    *.html                        # All other pages provided by the UI Kit
   |
   |-- requirements.txt
   |
   |-- run.py
   |
   |-- ************************************************************************
```

<br />

## Phase#1 - Initial Codebase

The project is forked from a [simple Flask template](https://github.com/app-generator/jinja-atlantis-dark), without database or other hard dependencies. The design was translated to Jinja template and ... that's all. 

<br />

## Phase#2 - Update `requirements`

Added libraries required by the project: 

- sqlalchemy, version 1.4.5
- flask_sqlalchemy, version 2.5.1
- flask_migrate, version 2.7.0

<br />

## Phase#3 - Integrate SqlAlchemy

The changes required by this phase:

- Update `requirements.txt`: added `sqlalchemy` and `flask_sqlalchemy`
- Update `app/__init__.py` to use SqlAlchemy
    - import `SQLAlchemy` library
    - define the configuration: `SQLALCHEMY_DATABASE_URI` and `SQLALCHEMY_TRACK_MODIFICATIONS`
    - Bind SqlAlchemy to `app` object
    - SqlAlchemy interface is exposed via `db` object

> Note: we don't have any tables yet    

<br />

**Test the set up via Flask CLI**

```bash
$ flask shell
Python 3.8.4 ...
App: app [development]
>>> from app import db
>>> db.create_all()   
```

The above code will invoke `SQLAlchemy` **db** object and create all defined tables. At this moment we don't have any tables but the `db.sqlite3` (SQLite) file is created inside the `app` folder.
The Location of the file is determined by this code snippet used in `app/__init__.py`:

```python
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
...
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
...
```

<br />

## Phase#4 - Configuration Update

Optional phase - Configuration variables defined in `app/__init__.py` file will be moved to a separate file for a cleaner design.  

The changes required by this phase:

- Create `config.py` file in `app` folder
- Move all configuration variables used in `app/__init__.py` to `app/config.py`
    - `SECRET_KEY` - used by Flask for security purposes
    - `SQLALCHEMY_DATABASE_URI` - defines SQLite database path
    - `SQLALCHEMY_TRACK_MODIFICATIONS` - used by SqlAlchemy core 
- Remove variable `basedir` from `__init__.py` (no longer needed)
- Update `__init__.py` to load the configuration from `config.py` 

<br />

**Test the set up via Flask CLI**

```bash
$ flask shell
Python 3.8.4 ...
App: app [development]
>>> app.config['SECRET_KEY'] # access a configiguration variable
'VALUE_FROM_CONFIG_HERE'
```

Using `Flask CLI` to print the variables defined in `app/config.py` we should see the values used in the file.

<br />

## Phase#5 - New Table

In this phase we will define and integrate a simple table called `Stats` with three columns: Id, Month (unique string), Sold_units (Integer)

The changes required by this phase:

- Define the new table in `app/models.py`
- Update `__init__.py` to use it
- Delete `app/db.sqlite3` to recreate the database with the new table

<br />

**Test the set up via Flask CLI**

```bash
$ flask shell
Python 3.8.4 ...
App: app [development]
>>> from app import db
>>> db.create_all()   
>>>
>>> from app.models import Stats
>>> Stats.query.all()
[]
```

Above code snippet does the following: 

- Invoke `db` object (SqlAlchemy interface)
- Call `create_all()` SqlAlchemy helper to create all tables
- Import into the CLI context `Stats` ORM object
- List all **rows**  via helper `query.all()` 

Obviously, we have an empty list - no rows defined so far. Let's create new records using the `CLI`:

```python
>>> from app.models import Stats
>>> Stats.query.all()
[] # No rows yet
>>> 
>>> # Define a new object
>>> ian = Stats(id=1, month='Jan', sold_units=540) 
>>> db.session.add(ian) # Add the new object to the DB Session
>>> db.session.commit() # Save changes in the database
>>> 
>>> Stats.query.all()
[Jan - 540] # we have an object now
```

<br />

**Code a DB helper** for lazy devs

Add the following snippet to `Stats` model to speed up the saving.

```python
# Contents of `app/models.py`
...
class Stats(db.Model):
...
    def save(self):
        # inject self into db session    
        db.session.add ( self )
        # commit change and save the object
        db.session.commit( )

        return self 
...        
```

Now we can save the new objects by calling the `save()` helper: 

```python
>>> from app.models import Stats
>>> # Define a new objects
>>> febr = Stats(id=2, month='Feb', sold_units=480) 
>>> febr.save() 
>>> 
>>> Stats.query.all()
[Jan - 540, Feb - 480]
```

In the same way we can save the information for all months: 

```python
>>> feb = Stats(id=2,  month='Feb', sold_units=480)
>>> mar = Stats(id=3,  month='Mar', sold_units=430)
>>> apr = Stats(id=4,  month='Apr', sold_units=550)
>>> may = Stats(id=5,  month='May', sold_units=530)
>>> jun = Stats(id=6,  month='Jun', sold_units=453)
>>> jul = Stats(id=7,  month='Jul', sold_units=380)
>>> aug = Stats(id=8,  month='Aug', sold_units=434)
>>> sep = Stats(id=9,  month='Sep', sold_units=568)
>>> oct = Stats(id=10, month='Oct', sold_units=610)
>>> nov = Stats(id=11, month='Nov', sold_units=700)
>>> dec = Stats(id=12, month='Dec', sold_units=900)
>>>
>>> Stats.query.all() 
[Jan - 540, Feb - 480, Mar - 430, Apr - 550, May - 530, Jun - 453, Jul - 380, Aug - 434, Sep - 568, Oct - 610, Nov - 700, Dec - 900]
```

> Hint: to visualize the information we can use [SQLiteBrowser](https://sqlitebrowser.org/) an open-source and free editor for SQLite. If we download the tool and open `app/db.sqlite3` we should see something like this: 

<br />

![Flask Database Sample - SQL view of decalred information.](https://raw.githubusercontent.com/app-generator/flask-database-sample/master/media/flask-database-sample-sqlite-view.png)

<br />

## Phase#6 - Migrations

In this phase, we will update the `Stats` with a new column: `total sales` (Integer)

The changes required by this phase:

- Add [flask_migrate](https://flask-migrate.readthedocs.io/en/latest/) to the `requirements.txt` file 
- Update `app/__init__.py` to integrate the migrations
    - Import `flask_migrate`
    - Inject `Migrate` constructor in our app

<br />

**How it works**

After `Flask-Migrate` is properly integrated we should run `db init` and `db migrate` to generate the **initial state** for our database.

```bash
$ # This command will create a migrations folder
$ flask db init
$ flask db migrate -m "Initial migration."
```

<br />

After this step is complete, we will add the new field (`total_sales`) to the `Stats` table and apply the new changes on the database. 

```bash
$ flask db migrate -m "Stats - Added Total_Sales Column"
Generating ... migrations\versions\d26f9f5f6e4f_stats_added_total_sales_column.py ...  done
$ flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> d26f9f5f6e4f, Stats - Added Total_Sales Column
```

At this point, we can use the new structure. Let's update an object via Flask CLI:

```python
>>> from app.models import Stats
>>> ian = Stats.query.all()[0]
>>> ian.total_sales = 1000
>>> ian.save()
```

By inspecting the `app/db.sqlite3` (SQLite database) we should see the new changes: 

<br />

![Flask Database Sample - SQL view of declared information.](https://raw.githubusercontent.com/app-generator/flask-database-sample/master/media/flask-database-sample-sqlite-view.png)

<br />

## Bonus: Deployment

The project comes with a basic configuration for [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

<br />

### [Docker](https://www.docker.com/) execution
---

The steps to start the template using Docker:

> Get the code

```bash
$ git clone https://github.com/app-generator/flask-database-sample.git
$ cd flask-database-sample
```

> Start the app in Docker

```bash
$ sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

<br />

## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website

<br />

---
Flask Database Sample - Open-source sample provided by **AppSeed** [App Generator](https://appseed.us/app-generator).
