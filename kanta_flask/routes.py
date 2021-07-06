from flask import render_template, url_for, flash, redirect
from kanta_flask import app
from kanta_flask.models import User, Post   
from kanta_flask.forms import RegistrationForm, LoginForm

posts = [
   
   { 
    'author': 'Shaad Hussain',
    'title': 'Post 1',
    'content': "I like apples",
    'date_posted': "3/3/2021"
   },

   { 
    'author': 'Syed Hussain',
    'title': 'Post 2',
    'content': 'No I like apples',
    'date_posted': '5/20/2021'
   }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') #"success" here is what's called a Bootstrap category, see layout.html, 28:38 at vid 3
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your credentials.', 'danger')
    return render_template('login.html', title="Login", form=form)

