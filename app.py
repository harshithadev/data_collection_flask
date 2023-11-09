from flask import Flask, render_template, request, redirect, url_for
import pyrebase

app = Flask(__name__)

firebaseConfig = {
  "apiKey": "AIzaSyBwxFg6_v5cgq-s5PVDuF0KDQ89TgfBldc",
  "authDomain": "data-collection-a96d1.firebaseapp.com",
  "databaseURL": "https://data-collection-a96d1-default-rtdb.firebaseio.com",
  "projectId": "data-collection-a96d1",
  "storageBucket": "data-collection-a96d1.appspot.com",
  "messagingSenderId": "199940641896",
  "appId": "1:199940641896:web:c0bdc4a5fd8a987ee157dd",
  "measurementId": "G-4Q73Z756E8"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


# Define form fields and their labels
form_fields = {
    'name': 'Name',
    'phone_number': 'Phone Number',
    'email': 'Email',
    'tags': 'Tags',
    'comments': 'Comments'
}
# Define tag options
tag_options = ['Client', 'EduProgram', 'Investor']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {}
        for field, label in form_fields.items():
            if field == 'tags':
                #data[field] = request.form[field].split(',')
                data[field] = request.form.getlist(field)
            else :
                data[field] = request.form[field]
        # db.child("uberstall").push({"name":"Harshithaaa", "number":9907512656})
        db.child("uberstall").push(data)
        return redirect(url_for('index'))
    return render_template('index.html', form_fields=form_fields, tag_options=tag_options)

if __name__ == '__main__':
    app.run(debug=True)

# data_ref = "your_data_node"  # Replace 'your_data_node' with the actual node name

# # Get the data at the specified reference
# snapshot = db.child(data_ref).get()

# if snapshot.val() is not None:
#     num_children = len(snapshot.each())
#     print(f'Number of children: {num_children}')
# else:
#     print('No data found at the specified reference')

#####################################

# @app.route("/")
# def home():
#   result = firebase.get('/uberStall', None)
#   print(result)
#   return str(result)
