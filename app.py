from flask import Flask,redirect,url_for,request,render_template;

app=Flask(__name__);

# The jinja2 template engine uses the following delimiters for escaping from HTML.
# {% ... %} for Statements
# {{ ... }} for Expressions to print to the template output
# {# ... #} for Comments not included in the template output
# ... ## for Line Statements

@app.route('/login',methods=['GET','POST'])
def login():
   if request.method=='POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      return render_template('login.html')
   
@app.route('/success/<name>')
def success(name):
   return render_template('success.html',name=name)

@app.route('/result')
def result():
   dict={
      'math':34,
      'science':24,
      'english':56
   }
   return render_template('result.html',score=dict)

if __name__=='__main__':
   app.run(debug=True)