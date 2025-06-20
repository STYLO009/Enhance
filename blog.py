# A beautiful and functional personal blog site using Flask

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory database (can be replaced with a real DB like SQLite)
posts = []

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', post=posts[post_id], post_id=post_id)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = {
            'title': title,
            'content': content,
            'date': datetime.now().strftime("%B %d, %Y")
        }
        posts.append(post)
        return redirect(url_for('home'))
    return render_template('create.html')

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = posts[post_id]
    if request.method == 'POST':
        post['title'] = request.form['title']
        post['content'] = request.form['content']
        return redirect(url_for('post', post_id=post_id))
    return render_template('edit.html', post=post, post_id=post_id)

if __name__ == '__main__':
    app.run(debug=True)
