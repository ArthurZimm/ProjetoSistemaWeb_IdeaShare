
from flask import Flask, current_app, redirect, url_for, render_template, request, flash

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        
        
        name = request.form['nameregister']
        username = request.form['usernameregister']
        password = request.form['passwordregister']
        passwordconfirm = request.form['passwordregisterconfirm']
        email = request.form['emailregister']
        dictLog = {
            "name" : name,
            "username": username,
            "password" : password,
            "email" : email,
        }
        print(username)
        print(password)
        print(dictLog)
        if password != passwordconfirm:
            return render_template('error.html')
        else: 
            return render_template('login.html')
    return render_template('registerpage.html')



@app.route('/login' ,methods = ['GET','POST'])  
def login(self):      
    error = None
    
    if request.method == 'POST': 
        for v in self.dictLog.values():
            if self.dictLog['username'] == request.form['username'] and self.dictLog['password'] == request.form['username']: 
                return render_template('firstpage.html')
            else: 
                error = 'Invalid username or password. Please try again !'
    return render_template('login.html', error = error) 

    #LOGIN PADRÃO : admin
    #SENHA PADRÃO : admin

if __name__ == "__main__":
    app.run()