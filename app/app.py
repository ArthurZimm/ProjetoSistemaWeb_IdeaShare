
from flask import Flask, current_app, redirect, url_for, render_template, request, flash

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])  
def login():      
    error = None
        
    #LOGIN PADRÃO : admin
    #SENHA PADRÃO : admin
    if request.method == 'POST': 
        if request.form['username'] == 'admin' or request.form['password'] == 'admin': 
            return render_template('firstpage.html')
        else: 
            error = 'Invalid username or password. Please try again !'
    return render_template('login.html', error = error) 

if __name__ == "__main__":
    app.run()