from flask import Blueprint
from flask import Flask, url_for, redirect, render_template
from flask import request, session
import mysql.connector

assignment10 = Blueprint('assignment10', __name__, static_folder='static',
                         static_url_path="/assignment10",
                         template_folder='templates')

@assignment10.route('/assignment10', methods=['GET', 'POST'])
def assignment10_f():
    if request.method == 'POST':
        firstName = request.form['firstName']
        email = request.form['email']
        age = request.form['age']
        city= request.form['city']
        favoriteHobby = request.form['favoriteHobby']

        query = "INSERT INTO users(firstName, email, age, city, favoriteHobby) VALUES ('%s', '%s', '%s', '%s','%s')" % (firstName, email, age, city, favoriteHobby)
        return_value = interact_db(query, 'commit')
        requestQuery ="SELECT * FROM users WHERE email='%s'" % email
        backUser = interact_db(requestQuery, 'fetch')
        usersListQuery = "SELECT * FROM users"
        usersList = interact_db(usersListQuery, 'fetch')
        return render_template('assignment10.HTML', backUser=backUser[0], users=usersList)
    else:
        query = "SELECT * FROM users"
        query_result = interact_db(query, 'fetch')
        return render_template('assignment10.HTML', users=query_result)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='YAssignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
    return_value = True

    if query_type == 'fetch':
        query_result= cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/assignment10/update', methods=['GET', 'POST'])
def assignment10Update_func():

    if request.method == 'POST':
        ID = request.form['ID']

        setQuery = ""

        for key in request.form:
           value = request.form[key]
           if key != 'ID' and value != '':
               setQuery += key + "='" + value + "' ,"

        setQuery = setQuery[:-1]

        query = "UPDATE users SET " + setQuery + " WHERE ID='%s';" % ID
        interact_db(query, query_type='commit')

    return redirect('/assignment10')


@assignment10.route('/assignment10/delete', methods=['GET', 'POST'])
def delete_f():
    ID = request.args['ID']
    query = "DELETE FROM users WHERE ID='%s'" % ID
    query_result = interact_db(query, query_type='commit')
    return redirect('/assignment10')
