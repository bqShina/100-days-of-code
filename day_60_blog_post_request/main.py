from flask import Flask, render_template, request
import requests
import smtplib

POSTS_URL = "https://api.npoint.io/81bab482e62ce81face5"
response = requests.get(url=POSTS_URL)
all_posts = response.json()

MY_EMAIL = "bqshina1994@gmail.com"
PASSWORD = "***********"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=all_posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone-number']
        message = request.form['message']
        email_content = f"Name: {name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="764762555@qq.com",
                                msg=f"Subject: New Message \n\n{email_content}")

        return render_template('contact.html', msg_sent=True)
    else:
        return render_template('contact.html', msg_sent=False)


# @app.route('/form-entry', methods=['POST'])
# def receive_data():


@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = {}
    for post in all_posts:
        if post['id'] == post_id:
            requested_post = post
    return render_template('post.html', this_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
