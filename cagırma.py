from flask import Flask, request, render_template
from views.main1 import app1
app = Flask(__name__)
app.register_blueprint(app1)
if __name__ == '__main__':
    app.run(debug=True)