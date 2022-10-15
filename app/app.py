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
        return render_template('./homecursos/javascriptcurso.html')

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

class cs_course_classes:
    @app.route('/cs_aula_01', methods = ['GET','POST'])
    def aula_um_cs():
        return render_template('./cursos/cursocsvideos/videoUM.html')

    @app.route('/cs_aula_02', methods = ['GET','POST'])
    def aula_dois_cs():
        return render_template('./cursos/cursocsvideos/videoDOIS.html')

    @app.route('/cs_aula_03', methods = ['GET','POST'])
    def aula_tres_cs():
        return render_template('./cursos/cursocsvideos/videoTRES.html')

    @app.route('/cs_aula_04', methods = ['GET','POST'])
    def aula_quatro_cs():
        return render_template('./cursos/cursocsvideos/videoQUATRO.html')

    @app.route('/cs_aula_05', methods = ['GET','POST'])
    def aula_cinco_cs():
        return render_template('./cursos/cursocsvideos/videoCINCO.html')

    @app.route('/cs_aula_06', methods = ['GET','POST'])
    def aula_seis_cs():
        return render_template('./cursos/cursocsvideos/videoSEIS.html')

class javascript_course_classes:
    @app.route('/javascript_aula_01', methods = ['GET','POST'])
    def aula_um_javascript():
        return render_template('./cursos/cursojsvideos/videoUm.html')

    @app.route('/javascript_aula_02', methods = ['GET','POST'])
    def aula_dois_javascript():
        return render_template('./cursos/cursojsvideos/videoDois.html')

    @app.route('/javascript_aula_03', methods = ['GET','POST'])
    def aula_tres_javascript():
        return render_template('./cursos/cursojsvideos/videoTres.html')

    @app.route('/javascript_aula_04', methods = ['GET','POST'])
    def aula_quatro_javascript():
        return render_template('./cursos/cursojsvideos/videoQuatro.html')

    @app.route('/javascript_aula_05', methods = ['GET','POST'])
    def aula_cinco_javascript():
        return render_template('./cursos/cursojsvideos/videoCinco.html')

    @app.route('/javascript_aula_06', methods = ['GET','POST'])
    def aula_seis_javascript():
        return render_template('./cursos/cursojsvideos/videoSeis.html')

class git_course_classes:
    @app.route('/git_aula_01', methods = ['GET','POST'])
    def aula_um_git():
        return render_template('./cursos/cursoGitvideos/videoUM.html')

    @app.route('/git_aula_02', methods = ['GET','POST'])
    def aula_dois_git():
        return render_template('./cursos/cursoGitvideos/videoDOIS.html')

    @app.route('/git_aula_03', methods = ['GET','POST'])
    def aula_tres_git():
        return render_template('./cursos/cursoGitvideos/videoTRES.html')

    @app.route('/git_aula_04', methods = ['GET','POST'])
    def aula_quatro_git():
        return render_template('./cursos/cursoGitvideos/videoQUATRO.html')

    @app.route('/git_aula_05', methods = ['GET','POST'])
    def aula_cinco_git():
        return render_template('./cursos/cursoGitvideos/videoCINCO.html')

    @app.route('/git_aula_06', methods = ['GET','POST'])
    def aula_seis_git():
        return render_template('./cursos/cursoGitvideos/videoSEIS.html')

class cplusplus_course_classes:
    @app.route('/cplusplus_aula_01', methods = ['GET','POST'])
    def aula_um_cplusplus():
        return render_template('./cursos/cursocplusplusvideos/videoUM.html')

    @app.route('/cplusplus_aula_02', methods = ['GET','POST'])
    def aula_dois_cplusplus():
        return render_template('./cursos/cursocplusplusvideos/videoDOIS.html')

    @app.route('/cplusplus_aula_03', methods = ['GET','POST'])
    def aula_tres_cplusplus():
        return render_template('./cursos/cursocplusplusvideos/videoTRES.html')

    @app.route('/cplusplus_aula_04', methods = ['GET','POST'])
    def aula_quatro_cplusplus():
        return render_template('./cursos/cursocplusplusvideos/videoQUATRO.html')

    @app.route('/cplusplus_aula_05', methods = ['GET','POST'])
    def aula_cinco_cplusplus():
        return render_template('./cursos/cursocplusplusvideos/videoCINCO.html')

    @app.route('/cplusplus_aula_06', methods = ['GET','POST'])
    def aula_seis_cplusplus():
        return render_template('./cursos/cursocplusplusvideos/videoSEIS.html')


if __name__ == "__main__":
    app.run()