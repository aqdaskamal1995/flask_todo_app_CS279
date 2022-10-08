Simple Flask Todo App using SQLAlchemy and SQLite database.
(Adapated from: https://www.python-engineer.com/posts/flask-todo-app/)

For styling [semantic-ui](https://semantic-ui.com/) is used.

### Setup
Create project with virtual environment

```console
$ mkdir flask_todo_app
$ cd flask_todo_app
$ python3 -m venv venv
```

Activate it
```console
$ . venv/bin/activate
```

or on Windows
```console
venv\Scripts\activate
```

Install Flask
```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
```

Set environment variables in terminal
```console
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

or on Windows
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

Run the app
```console
$ flask run
```

### Functionality 

The to do app allows the user to:
1. Add a to do task 
2. Update status - complete/incomplete
3. Delete task 
4. The tasks are locally stored on an sqlite database 