from flask import Flask, url_for, request, render_template, redirect
from werkzeug import exceptions
app = Flask(__name__)


@app.route('/<user>')
@app.route('/')
def index(user=None):
    return render_template("user.html", user=user)


@app.route('/login')
def login():
    print("In login function")
    return '<h4>Login Page</h4>, Request:%s' %request.method


@app.route('/profile/<username>')

def users_page(username):
    return render_template("profile.html", username = username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    try:
        return redirect(url_for('login'))
    except:
        return 'Show post ID: %s' % post_id

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))


@app.errorhandler(exceptions.BadRequestKeyError)
def handle_bad_request(e):
    return 'bad request!'

app.register_error_handler(404, lambda e: 'bad request!')


if __name__ == '__main__':
    app.run(host='127.0.0.4', port=5000)

