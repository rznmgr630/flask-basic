from flask import Flask,render_template;

app=Flask(__name__)

# Note: The route /flask can only handle the url /path but /python/ can handle both  /python and /python/
@app.route('/')
def hello_world():
   return 'Hello world'

@app.route('/<int:userId>')
def get_user(userId):
   # return f'User id is {userId}'
   return 'User id is %d' % userId

@app.route('/html')
def get_html():
   return render_template('index.html')

if __name__=='__main__':
   app.run(debug=True)