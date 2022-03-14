from test import app

if __name__ == '__main__':
    app.run(debug=True)







































# @app.route('/')
# def index():
#     return 'Index Page'
#
# @app.route('/hello')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html',name=name)
#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'User %s' % username
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id
#
# @app.route('/projects/')
# def projects():
#     return 'The project page'
#
# @app.route('/about')
# def about():
#     return 'The about page'
#
# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#             # the code below is executed if the request method
#             # was GET or the credentials were invalid
#         return render_template('login.html', error=error)
#
#
# def valid_login(username,password):
#     return 'do_login'
#
# def log_the_user_in(username):
#     return 'show_login'
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',debug=True,)
    # with app.test_request_context('/hello', method='POST'):
    #     assert request.path == '/hello'
    #     assert request.method == 'POST'
    #     print(url_for('index'))
    #     print(url_for('login'))
    #     print(url_for('login',next='/'))
    #     print(url_for('profile',username = 'John Doe'))
    #     url_for('static', filename='style.css')