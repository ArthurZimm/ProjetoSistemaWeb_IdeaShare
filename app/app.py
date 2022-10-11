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
        if password != passwordconfirm or name == "" or username == "":
            return render_template('error.html')
        else: 
            dictLog = {
                "name" : name,
                "username": username,
                "password" : password,
                "email" : email,
            }
            print(username)
            print(password)
            print(dictLog)
            return redirect('/login')
    return render_template('registerpage.html')



@app.route('/login' ,methods = ['GET','POST'])  
def login():      
    error = None
    
    if request.method == 'POST': 
        if request.form['username'] == 'admin' and request.form['password'] == 'admin': 
            return redirect('/home')
        else: 
            error = 'Invalid username or password. Please try again !'
    return render_template('login.html', error = error)

# @app.route('/home', methods = ['GET','POST'])
# def home():
#     if request.method == 'POST':

#     return render_template('homepage.html')

if __name__ == "__main__":
    app.run()