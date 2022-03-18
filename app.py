from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contact.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/tenders')
def tenders():
    return render_template('tender.html')

@app.route('/A')
def a():
    return render_template('a.html')

@app.route('/B')
def b():
    return render_template('b.html')

@app.route('/C')
def c():
    return render_template('c.html')

@app.route('/D')
def d():
    return render_template('d.html')

@app.route('/E')
def e():
    return render_template('e.html')

@app.route('/F')
def f():
    return render_template('f.html')



if __name__ == "__main__":
    app.run(debug=True)