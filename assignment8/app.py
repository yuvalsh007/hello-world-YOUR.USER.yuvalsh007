from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('cv_yuval.html ')


@app.route('/my_peoplecontact')
def contacts():
    return render_template('my_peoplecontact.html')

@app.route('/assignment8')
def hobbies():
    return render_template('assignment8.html',hobbies={'camping,running,swimming'})


if __name__ == '__main__':
    app.run()
