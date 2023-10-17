from flask import Flask, request, redirect, render_template, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong secret key

# Sample user data (in practice, use a database)
users = {'user1': 'password1', 'user2': 'password2'}


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('You need to log in first.', 'danger')
            return redirect(url_for('login'))
        return func(*args, **kwargs)

    return decorated_function


@app.route('/')
def home():
    return render_template("register.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists. Please choose another.', 'danger')
        else:
            users[username] = password
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')


@app.route('/profile')
@login_required
def profile():
    username = session['username']
    return f"Welcome to your profile, {username}!"


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
