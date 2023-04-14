from flask_app import app, render_template, redirect, request 


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/register", methods=['post'])
def register():
    print(request.form)
    
    return redirect('/dashboard')




@app.route("/dashboard")
def dashbaord():
    return "success"