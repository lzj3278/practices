from flask import Flask, url_for, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    with app.test_request_context():
        return url_for('hello_someone', username='lzj')


@app.route('/user/<username>/')
def hello_someone(username):
    return url_for('hello_someone', username=username)


@app.route('/post/<int:post_id>/')
def show_post(post_id):
    return 'post {}'.format(post_id)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == ' POSt':
        return '1111'
    else:
        return '2222'


if __name__ == '__main__':
    app.run(debug=True)
