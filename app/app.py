from flask import Flask, current_app, redirect, url_for, render_template, request, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'usbw'
app.config['MYSQL_DB'] = 'idea_share'

mysql = MySQL(app)

@app.route('/', methods = ['GET','POST'])
def main_page():
    return render_template('./paginaPrincipal/principal.html')

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
        return render_template('./homecursos/javacurso.html')

    @app.route('/cursocpluplus', methods = ['GET','POST'])
    def cplusplus_route():
        return render_template('./homecursos/cplusplus.html')

    @app.route('/cursojavascript', methods = ['GET','POST'])
    def javascript_route():
        return render_template('./homecursos/javaScriptCurso.html')

    @app.route('/cursogit', methods = ['GET','POST'])
    def git_route():
        return render_template('./homecursos/Gitcurso.html')

    @app.route('/cursocsharpie', methods = ['GET','POST'])
    def csharpie_route():
        return render_template('./homecursos/cscurso.html')

class python_course_classes:
    @app.route('/python_aula_01', methods = ['GET','POST'])
    def aula_um_python():
        return render_template('./cursos/cursopythonvideos/videoUM.html')

    @app.route('/python_aula_02', methods = ['GET','POST'])
    def aula_dois_python():
        return render_template('./cursos/cursopythonvideos/videoDOIS.html')

    @app.route('/python_aula_03', methods = ['GET','POST'])
    def aula_tres_python():
        return render_template('./cursos/cursopythonvideos/videoTRES.html')

    @app.route('/python_aula_04', methods = ['GET','POST'])
    def aula_quatro_python():
        return render_template('./cursos/cursopythonvideos/videoQUATRO.html')

    @app.route('/python_aula_05', methods = ['GET','POST'])
    def aula_cinco_python():
        return render_template('./cursos/cursopythonvideos/videoCINCO.html')

    @app.route('/python_aula_06', methods = ['GET','POST'])
    def aula_seis_python():
        return render_template('./cursos/cursopythonvideos/videoSEIS.html')

class java_course_classes:
    @app.route('/java_aula_01', methods = ['GET','POST'])
    def aula_um_java():
        return render_template('./cursos/cursoJavaVideos/videoUM.html')

    @app.route('/java_aula_02', methods = ['GET','POST'])
    def aula_dois_java():
        return render_template('./cursos/cursoJavaVideos/videoDOIS.html')

    @app.route('/java_aula_03', methods = ['GET','POST'])
    def aula_tres_java():
        return render_template('./cursos/cursoJavaVideos/videoTRES.html')

    @app.route('/java_aula_04', methods = ['GET','POST'])
    def aula_quatro_java():
        return render_template('./cursos/cursoJavaVideos/videoQUATRO.html')

    @app.route('/java_aula_05', methods = ['GET','POST'])
    def aula_cinco_java():
        return render_template('./cursos/cursoJavaVideos/videoCINCO.html')

    @app.route('/java_aula_06', methods = ['GET','POST'])
    def aula_seis_java():
        return render_template('./cursos/cursoJavaVideos/videoSEIS.html')


if __name__ == "__main__":
    app.run()