from flask import Flask, render_template
from flask import url_for
from flask import request
from markupsafe import escape
from webScraper import WebScraper

STATIC_FOLDER = './frontend/static'
TEMPLATE_FOLDER = './frontend/templates'
app = Flask(__name__,template_folder=TEMPLATE_FOLDER,static_folder=STATIC_FOLDER)

def do_the_login():
	return 'Post method'

def show_the_login_form():
	return 'Get method'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/scraped', methods=['POST'])
def scraped():
    print('scraped has been called')
    try:
        url = request.form["url"]
        price = request.form["price"]
        email = request.form["email"]
        if not url or not price or not email:
            raise ValueError('empty value')
    except:
        print('except')
        return render_template('unsuccesfulScrape.html')
    webScraper = WebScraper(price, url, email)
    return render_template('scraped.html')

@app.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    print('Unsubscribe has been called')
    #implement some interaction between database and user.
    return render_template('unsubscribe.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return do_the_login()
	else:
		return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return f'Post with post id: {post_id}'

with app.test_request_context():
    print(url_for('home'))
    print(url_for('scraped'))

if __name__ == '__main__':
    app.run(debug=True)