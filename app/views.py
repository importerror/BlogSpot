from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user={'nickname':'Santosh'}
    posts=[
            {
                'author':{'nickname':'John'},
                'body': 'The text1 is working fine'
            },
            {
                'author':{'nickname':'Susan'},
                'body':'The text2 is working'
            }
          ]
    return render_template('index.html',
            title="Welcome",
            user=user,
            posts=posts
            )

