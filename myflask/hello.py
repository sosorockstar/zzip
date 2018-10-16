# coding: utf-8

from flask import Flask

app = Flask(__name__)

# 开启debug
app.debug=True
app.run()
# app.run(debug=True)


@app.route('/item/<int:id>')
def print_item(id):
    return 'The item {}'.format(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)