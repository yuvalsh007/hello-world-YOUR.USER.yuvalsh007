from flask import Flask, redirect, url_for, render_template
from flask import request, session
app = Flask(__name__)

app.secret_key = '9876'

@app.route('/')
def hello_world():
    return render_template('cv_yuval.html ', UserFirstName=session.get('FirstName'))


@app.route('/my_peoplecontact')
def contacts():
    return render_template('my_peoplecontact.html', UserFirstName=session.get('FirstName'))

@app.route('/assignment8')
def hobbies():
    return render_template('assignment8.html',hobbies={'camping,running,swimming'}, UserFirstName=session.get('FirstName'))

@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    #I'm defining a array for the total users. I've created 4 users for the assignment, with the following relevant fields.
    users=[{'firstname':'Yuval', 'email':'Yuval@gmail.com', 'age':'18', 'city':'tel aviv', 'favorite_hobby':'swimming'},
           {'firstname':'Dor', 'email':'Dor@gmail.com', 'age':'54', 'city':'beer sheva', 'favorite_hobby':'netflix'},
           {'firstname':'Shmuel', 'email':'Shmulik@gmail.com', 'age':'23', 'city':'Haifa', 'favorite_hobby':'chilling'},
           {'firstname':'Yakov', 'email':'Yaki@gmail.com', 'age':'22', 'city':'Jerusalem', 'favorite_hobby':'drinking wine'}]

    #I've created a new array only for the relevant users to show in the frond end.
    wantedUsers=[]

    if request.method == "POST":
        #This is the use of a POST form.
        Email = request.form['Email']
        UserName = request.form['UserName']
        Password = request.form['Password']
        Age = request.form['Age']
        session['FirstName'] = request.form['FirstName']

    else:
        #This is the use of a GET form.
        wantedEmail = request.args.get('email')
        if wantedEmail == '':
            wantedUsers = users
        else:
            for user in users:
                if user['email'] == wantedEmail:
                    wantedUsers.append(user)

    return render_template('Assignment9.html', users=wantedUsers,method=request.method, UserFirstName=session.get('FirstName'))

@app.route('/logout')
def logout():
    session['FirstName'] = None
    return render_template('Assignment9.html',method=request.method, UserFirstName=session.get('FirstName'))

if __name__ == '__main__':
    app.run()
