# -*- coding:utf-8 -*-

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return 'Loging in as {}'.format(escape(session['username']))
    return 'logged'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        return '''
        <form action="" method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
            '''


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
