from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/4af156202f984d3464c3"
response = requests.get(url=url)
all_posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:post_id>')
def read_post(post_id):
    request_post = {}
    for blog_post in all_posts:
        if blog_post['id'] == post_id:
            request_post = blog_post
    return render_template("post.html", post=request_post)


if __name__ == "__main__":
    app.run(debug=True)
