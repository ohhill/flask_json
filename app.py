import os

from flask import Flask, Blueprint, render_template, request, redirect
from user import user
from get_all_users import all_user



app = Flask(__name__)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(all_user, url_prefix='/all_users')



if __name__=="__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='127.0.0.1', port=port)
