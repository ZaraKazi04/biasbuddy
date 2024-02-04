from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

#app = Flask(__name__)

@app.route('/')
def template():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)





