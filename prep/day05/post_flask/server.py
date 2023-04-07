from flask import Flask, render_template, redirect, request
app = Flask(__name__)    

@app.route('/')         
def index():
    return render_template('index.html')

@app.route('/handle_my_stuff', methods=['post'])
def handle():
    print(request.form['my_stuff'])
    return request.form['my_stuff']

if __name__=="__main__":  
    app.run(debug=True)  