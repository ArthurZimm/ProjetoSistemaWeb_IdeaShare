from flask import Flask, current_app, redirect, url_for, render_template, request, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'usbw'
app.config['MYSQL_DB'] = 'idea_share'

mysql = MySQL(app)

class registration:
    @app.route('/registro', methods = ['GET','POST'])
    def register():
        if request.method == 'POST':
            name = request.form['nameregister']
            password = request.form['passwordregister']
            email = request.form['emailregister']
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO users(nome, senha, email) VALUES (%s, %s, %s)", (name, password, email))
            mysql.connection.commit()
            cursor.close()
            return redirect('/login')
        return render_template('./registrar/registro.html')



    @app.route('/login' ,methods = ['GET','POST'])  
    def login():             
        if request.method == 'POST':
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT nome, senha FROM users")
            myresult = cursor.fetchall()
            for x in myresult:
                if request.form['username'] == x[0] and request.form['password'] == x[1]:
                    cursor.close()
                    return redirect('/home')
                
            cursor.close()
        return render_template('./login/login.html')

class home_page:
    @app.route('/home', methods = ['GET','POST'])
    def home():
        return render_template('./homepage/homepage.html')

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