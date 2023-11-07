from flask import Flask, render_template, request, redirect, url_for, flash
import pyrebase

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Firebase configuration
config = {
    "apiKey": "AIzaSyABvlgpz7TBuvA3HQQUJS4wY4tTRtiLOco",
    "authDomain": "data-collection-509ec.firebaseapp.com",
    "databaseURL": "YOUR_DATABASE_URL",
    "storageBucket": "data-collection-509ec.appspot.com"
}
config = {
  "apiKey": "AIzaSyABvlgpz7TBuvA3HQQUJS4wY4tTRtiLOco",
  "authDomain": "data-collection-509ec.firebaseapp.com",
  #"databaseURL": "https://data-collection-509ec-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "projectId": "data-collection-509ec",
  "storageBucket": "data-collection-509ec.appspot.com",
  "messagingSenderId": "117519028614",
  "appId": "1:117519028614:web:7af8e4cc44677b66159c07",
  "measurementId": "G-M7Y1TKWJP1"
};

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    contact_number = request.form['contact_number']
    email = request.form['email']
    tags = request.form.getlist('tags')
    comments = request.form['comments']

    if not name or not contact_number:
        flash('Name and Contact Number are mandatory fields.')
    else:
        data = {
            'name': name,
            'contact_number': contact_number,
            'email': email,
            'tags': tags,
            'comments': comments
        }
        db.child('entries').push(data)
        flash('Data added successfully!')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
