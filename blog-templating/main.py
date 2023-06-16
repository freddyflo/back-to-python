from flask import Flask, render_template
import requests
from post import Post 
app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()
post_objects = []
for post in all_posts:
   new_post = Post(post.id, post.title, post.subtitle, post.body)
   post_objects.append(new_post)
   

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    return render_template("post.html", posts=all_posts, blog_id=blog_id)
    pass

if __name__ == "__main__":
    app.run(debug=True)
