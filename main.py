from flask import Flask, render_template,flash,request,redirect
app = Flask(__name__)
config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ms.sdlite"
app.config["SECRET_KEY"] = "my_secret_key"
db=SQLAlchemy(app)

# User Class
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    fname=db.Column(db.String(255), nullable=False)
    lname=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(255), nullable=False)
    usernames=db.Column(db.String(255), nullable=False)
    edu=db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    status=db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f'User("{self.fname}","{self.lname}","{self.email}","{self.username}","{self.edu}","{self.password})'



# main index 
@app.route('/')
def index():
    return render_template('index.html', title='')

# admin login
@app.route('/admin/')
def adminIndex():
    return render_template('admin/index.html', title='Admin Login')

# ******************user area***********************
# user login
@app.route('/user/')
def userIndex():
    return render_template('user/index.html', title='User Login')

# user register
@app.route('/user/signup', methods=['POST','GET'])
def userSignup():
    if request.methods=='POST':
        #getting all inputs
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        username = request.form.get('username')
        edu = request.form.get('edu')
        password = request.form.get('password')

        # checking if all fields are filled or not.abs
        if fname=="" or lname=="" or email=="" or username=="" or password=="" or edu=="":
            flash('Please fill all the field','danger')
            return redirect('/user/signup')
        pass
    else:
        return render_template('user/signup.html', title='User Signup')




if __name__ == '__main__':
    app.run(debug=True)