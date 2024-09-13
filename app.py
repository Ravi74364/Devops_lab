from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def home():
     return render_template('register.html')
@app.route('/success',methods=['GET','POST'])
def success():
     if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        password=request.form('password')
        return render_template('success.html')
    else:
        return render_template('register.html')
if__name__=='__main__':
    app.run(host='0.0.0.0')