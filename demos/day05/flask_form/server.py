from flask import Flask, render_template, redirect, request, session  
app = Flask(__name__)   
app.secret_key = "any string you want"

@app.route('/')        
def index():
    return render_template('index.html') 


@app.route('/handle_form', method='post')
def handle_form():
    print(request.form)
    session['favorite_color'] = request.form['favorite_color']
    session['favorite_animal'] = request.form['favorite_animal']
    return redirect('/')

@app.route('/another_route')
def another():
    return session['favorite_color']


## MORE ROUTES HERE 


if __name__=="__main__":     
    app.run(debug=True) 