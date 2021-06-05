from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
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
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)



if __name__ == '__main__':
    app.run(debug=True)

