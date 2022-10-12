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

@app.route('/home', methods = ['GET','POST'])
def home():
    errors = []
    try:
        if request.method == 'POST':
            if request.form['curso_python_link']:
                return redirect('/cursopython')
            elif request.form['curso_Java_link']:
                return redirect('/cursopython')
            elif request.form['curso_C++_link']:
                return redirect('/cursocplusplus')
            elif request.form['curso_JavaScript_link']:
                return redirect('/cursojavascript')
            elif request.form['curso_git_link']:
                return redirect('/cursogit')
            elif request.form['curso_c#_link']:
                return redirect('/cursocsharpie')
    except: 
        errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
    return render_template('homepage.html')

@app.route('/cursopython', methods = ['GET','POST'])
def pythonroute():
    return render_template('pythoncurso.html')

@app.route('/python_aula_01', methods = ['GET','POST'])
def aula_um():
    if request.method == 'POST':
        if request.form['btn_back_to_home_python']:
            return redirect('/cursopython')
    return render_template('./cursopythonvideos/videoUM.html')

@app.route('/python_aula_02', methods = ['GET','POST'])
def aula_dois():
    return render_template('./cursopythonvideos/videoDOIS.html')

@app.route('/python_aula_03', methods = ['GET','POST'])
def aula_tres():
    return render_template('./cursopythonvideos/videoTRES.html')

@app.route('/python_aula_04', methods = ['GET','POST'])
def aula_quatro():
    return render_template('./cursopythonvideos/videoQUATRO.html')

@app.route('/python_aula_05', methods = ['GET','POST'])
def aula_cinco():
    return render_template('./cursopythonvideos/videoCINCO.html')

@app.route('/python_aula_06', methods = ['GET','POST'])
def aula_seis():
    return render_template('./cursopythonvideos/videoSEIS.html')

if __name__ == "__main__":
    app.run()