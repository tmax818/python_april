from flask_app import app, render_template, redirect, request, session, bcrypt
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/register", methods=['post'])
def register():
    print(request.form)
    
    # TODO validate user
    if not User.validate_user(request.form):
        return redirect('/')
    
    # TODO hash the password
    
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])    
    print(hashed_pw)
    print(bcrypt.check_password_hash(hashed_pw, 'password'))
    # TODO save the user to the DB
    temp_user = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw
    }
    user = User.save(temp_user)
    print(user)
    
    # TODO log them in
    session['user_id'] = user
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    
    
    return redirect('/dashboard')




@app.route('/login', methods=['post'])
def login():
    
    # TODO see if the email is in the DB
    user = User.find_by_email(request.form['email'])
    # TODO see if the provided password matches the hash in DB
    
    # TODO log them in
    session['user_id'] = user.id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


