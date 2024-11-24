from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key'

# Simple user storage for demonstration purposes
users = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        if not username or not password:
            flash('Please fill out all fields', 'error')
            return redirect(url_for('register'))

        users[username] = password
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in users or users[username] != password:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))

        flash('Login successful!', 'success')
        return redirect(url_for('home'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
