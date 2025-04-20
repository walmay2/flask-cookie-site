import os
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    language = request.cookies.get('language', 'не встановлено')
    resp = make_response(render_template('index.html', language=language))
    if language == 'не встановлено':
        resp.set_cookie('language', 'uk', max_age=60*60*24*30)
    return resp

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)