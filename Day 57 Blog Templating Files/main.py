import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<blog_id>')
def get_blog(blog_id):
    all_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    post_title = all_posts[int(blog_id) -1]["title"]
    post_blog = all_posts[int(blog_id) - 1]["body"]
    return render_template('post.html', title=post_title, blog=post_blog)

if __name__ == "__main__":
    app.run(debug=True)
