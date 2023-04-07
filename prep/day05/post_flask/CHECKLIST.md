# checklist

- [x] create a new directory
- [ ] inside the directory run:

```bash
[python -m] pipenv install flask
```

- [ ] activate the virtual env:

```bash
[python -m] pipenv shell 
```

- [ ] create [server.py](server.py)

```py
from flask import Flask, render_template, redirect, request
app = Flask(__name__)    

@app.route('/')         
def index():
    return render_template('index.html') 


if __name__=="__main__":  
    app.run(debug=True)    
```


- [ ] go to [localhost:5000](http://localhost:5000/)

- [ ] create a [templates](templates/index.html) folder that contains our HTML