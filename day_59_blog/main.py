from flask import Flask, render_template
import requests

POSTS_URL = "https://api.npoint.io/81bab482e62ce81face5"
response = requests.get(url=POSTS_URL)
all_posts = response.json()
print(all_posts)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = {}
    for post in all_posts:
        if post['id'] == post_id:
            requested_post = post
    return render_template('post.html', this_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
