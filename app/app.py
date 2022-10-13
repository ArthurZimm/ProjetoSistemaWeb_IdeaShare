from flask import Flask, current_app, redirect, url_for, render_template, request, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'usbw'
app.config['MYSQL_DB'] = 'idea_share'

mysql = MySQL(app)

class registration:
    @app.route('/', methods = ['GET','POST'])
    def register():
        if request.method == 'POST':
            name = request.form['nameregister']
            username = request.form['usernameregister']
            password = request.form['passwordregister']
            passwordconfirm = request.form['passwordregisterconfirm']
            email = request.form['emailregister']
            if password != passwordconfirm or name == "" or username == "":
                return render_template('./login/error.html')
            else: 
                cursor = mysql.connection.cursor()
                cursor.execute("INSERT INTO users(nome, username, senha, email) VALUES (%s, %s, %s, %s)", (name, username, password, email))
                mysql.connection.commit()
                cursor.close()
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
        return render_template('./login/registerpage.html')



    @app.route('/login' ,methods = ['GET','POST'])  
    def login():      
        error = None
        
        if request.method == 'POST': 
            if request.form['username'] == 'admin' and request.form['password'] == 'admin': 
                return redirect('/home')
            else: 
                error = 'Invalid username or password. Please try again !'
        return render_template('./login/login.html', error = error)

class home_page:
    @app.route('/home', methods = ['GET','POST'])
    def home():
        return render_template('homepage.html')

class routes_redirect_course:
    @app.route('/cursopython', methods = ['GET','POST'])
    def python_route():
        return render_template('./homecursos/pythoncurso.html')

    @app.route('/cursojava', methods = ['GET','POST'])
    def java_route():
        return render_template('./homecursos/pythoncurso.html')

    @app.route('/cursocpluplus', methods = ['GET','POST'])
    def cplusplus_route():
        return render_template('./homecursos/pythoncurso.html')

    @app.route('/cursojavascript', methods = ['GET','POST'])
    def javascript_route():
        return render_template('./homecursos/pythoncurso.html')

    @app.route('/cursogit', methods = ['GET','POST'])
    def git_route():
        return render_template('./homecursos/pythoncurso.html')

    @app.route('/cursocsharpie', methods = ['GET','POST'])
    def csharpie_route():
        return render_template('./homecursos/pythoncurso.html')

class python_course_classes:
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