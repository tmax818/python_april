

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

@app.route('/create_dojo', methods = ['post'])
def create_dojo():
    return redirect("/dojos")

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html', dojos = Dojo.get_all())

@app.route('/create_ninjas', methods=['post'])
def ninjas():
    return redirect(f"/dojos/{request.form['dojo_id']}")


@app.route('/dojos/<int:id>')
def show_dojo(id):
    return render_template('show.html')