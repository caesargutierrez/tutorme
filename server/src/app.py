from flask import Flask,request,render_template, make_response
import os
import time
app = Flask(__name__,static_folder='../../static')

@app.route('/')
def index():
    context = { 'server_time': format_server_time() }
    template = render_template('index.html', context=context)
    response = make_response(template)
    response.headers['cache-Control'] = 'public, max-age=300, s-maxage=600'
    return template

def format_server_time():
    server_time = time.localtime()
    return time.strftime("%I:%M:%S %p", server_time)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))