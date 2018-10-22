from flask import Flask, jsonify
from flask.views import MethodView

app = Flask(__name__)

class UserAPI(MethodView):
    def get(self):
        return jsonify({
            'username': 'fake',
            'avatar': 'http://lorempixel.com/100/100/nature'
        })

    def post(self):
        return 'UNSUPPORTED!'

app.add_url_rule('/user', view_func=UserAPI.as_view('userview'))

def user_required(f):
    def decorator(*args, **kwargs):
        if not g.user:
            abort(401)
        return f(*args, **kwargs)
    return decorator

view = user_required(UserAPI.as_view('users'))
app.add_url_rule('/users/', view_func=view)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)