from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# Create database
db=SQLAlchemy(app)
# Decorator defining URL of page


class Todo(db.Model):
    # Adding relevant properties at the to do item level
    # Creating column for ID
    id = db.Column(db.Integer, primary_key=True)
    # Creating column for title
    title = db.Column(db.String(100))
    # Creating column for whether task is complete or not
    complete = db.Column(db.Boolean)
# Each function serves to provide a separat page
@app.route('/')
def home():
    # Show all todos by querying the db, by returning all to do items as a list
    todo_list = Todo.query.all()

    # pass todo list into html template
    return render_template('base.html', todo_list=todo_list)

# Post method allows the html form to send any data to the server in this case executing the add method
@app.route("/add", methods=["POST"])
def add():
    # Get the latest to do item 
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    # Add to do item to the database
    db.session.add(new_todo)
    db.session.commit()

    #refresh page and redirect to index page
    return redirect(url_for("home"))


# Query the db for todo_id and change states 
@app.route("/update/<int:todo_id>")
def update(todo_id):
    # Get todo item based on the id 
    todo = Todo.query.filter_by(id=todo_id).first()

    # Set complete to the opposite of what it is already 
    todo.complete = not todo.complete

    # Update the database
    db.session.commit()
    #refresh page and redirect to index page
    return redirect(url_for("home"))

# Query the db for todo_id and remove item 
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # Get todo item based on the id 
    todo = Todo.query.filter_by(id=todo_id).first()

    # Set complete to the opposite of what it is already 
    db.session.delete(todo)

    # Update the database
    db.session.commit()
    #refresh page and redirect to index page
    return redirect(url_for("home"))



if __name__ == "__main__":
    # Create databse 
    with app.app_context():
        db.create_all() 
        db.session.commit()
    app.run(debug=True)