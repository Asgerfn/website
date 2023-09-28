from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify, make_response
from datetime import timedelta
from pythonTilWeb import *
import pyodbc 
import bcrypt
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm
from flask_bcrypt import Bcrypt
from flask_login import login_user, login_required, logout_user
from waitress import serve
from connectAzure import database_info



server = 'badmintonsql.database.windows.net'
database = database_info["name"]  # Use the database name from the JSON
username = 'Asgerfn'
password = 'Asger410'  # Replace with your actual Azure SQL Database password
driver = '{ODBC Driver 18 for SQL Server}'  # Use the appropriate driver version
conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

app = Flask(__name__)
app.secret_key = "fet96ksq!"
app.config['SECRET_KEY'] = 'fet96ksq!'
app.permanent_session_lifetime = timedelta(minutes=30)

bcrypt1 = Bcrypt(app)



"""sql = "DROP TABLE IF EXISTS link"
cursor.execute(sql)

conn.commit()"""

"""sql = '''
    CREATE TABLE hold (
        id INT IDENTITY(1,1) PRIMARY KEY,
        holdnavn VARCHAR(255),
        ejer VARCHAR(255),
        herre1 VARCHAR(255),
        herre2 VARCHAR(255),
        herre3 VARCHAR(255),
        herre4 VARCHAR(255),
        herre5 VARCHAR(255),
        herre6 VARCHAR(255),
        dame1 VARCHAR(255),
        dame2 VARCHAR(255),
        dame3 VARCHAR(255),
        dame4 VARCHAR(255),
        kaptajn VARCHAR(255),
        klub VARCHAR(255),
        point INT
    )
'''

cursor.execute(sql)
conn.commit()"""




"""create_table_sql = '''
CREATE TABLE link (
    id INT,
    name VARCHAR(500) NOT NULL,
    ude INT,
    klub VARCHAR(100)
)
'''
cursor.execute(create_table_sql)

# Commit the changes to the database
conn.commit()
"""

session = {"logged_in": False}


#print(printTable("hold",cursor,conn))



class RegisterForm(FlaskForm):
    navn = StringField(validators=[
                           InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Brugernavn"})
    klub = StringField(validators=[
                       InputRequired(), Length(min=5,max=50)], render_kw={"placeholder":"klub"})
    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Register')

    def validate_mail(self, navn):
        sql = "SELECT COUNT(*) FROM brugere WHERE navn = ?"
        cursor.execute(sql, navn.data)
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        if count != 0:
            raise ValidationError("Dette navn er taget")

class LoginForm(FlaskForm):
    navn = StringField(validators=[
                           InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Brugernavn"})
    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')
     

@app.route("/login", methods=["POST", "GET"])
def login():
  global login_success
  login_success = False
  if request.method == "POST":
    navn = request.form["navn"]
    kode = request.form["kode"]
    sql = "SELECT * FROM brugere WHERE navn = ?"
    cursor.execute(sql, navn)
    rows = cursor.fetchall()
    for row in rows:
        kode1 = row.kode
        klub = row.klub
    if rows and verify_password(kode, kode1):
      session['logged_in'] = True
      session['klub'] = klub
      session['login_success'] = True
      """token = jwt.encode({'mail' : id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
      """
      return redirect(url_for(("home")))
      
  return render_template('login.html')


def update_points(a, b):
    total_points = 0
    for player in a[:-1]:
        for name, points in b:
            if player == name:
                total_points += points
    return(total_points)



@app.route("/")
@app.route("/home")
def home():
    image_url = r"C:\Users\Asger Nielsen\Website\static\images\badmin.jpg"
    return render_template('index.html',image_url = image_url,login_success=session.get('login_success', False))
    #return(render_template("index.html",content = "Testing"))

"""@app.route("/view")
def view(): 
    if session['logged_in'] == True:
      #cursor.execute("SELECT * FROM brugere")
      #print(cursor,"c")
      lnks = "SELECT * FROM brugere"
      cursor.execute(lnks)
      rows = cursor.fetchall()
      print(rows)
      return(render_template("view.html",values = rows))
    return(redirect(url_for("login")))"""
  



@app.route("/spillere")
def spillere():
  try:
    if session['logged_in'] == True: 
      
      lst = []
      sql = "SELECT * FROM players WHERE klub = ?"
      cursor.execute(sql, session['klub'])
      for x in cursor:
          lst.append([x[1], x[3]])
          flash(f"spiller: {x[1]} har så mange point: {x[3]}")
      return render_template('spillere.html', lst=lst)
    else:
      return redirect(url_for("login"))
  except: 
    return redirect(url_for('login'))

def verify_password(user_password, stored_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), stored_password.encode('utf-8'))


@app.route("/statistik")
def statistik(): 
  try:
    if session['logged_in'] == True: 
      lst = []
      sql = "SELECT * FROM stats WHERE klub = ?"
      cursor.execute(sql, session['klub'])  
      for x in cursor:
        lst.append(x)
      
   
      return( render_template("statistik.html",lst = lst))
    else: 
      
      return redirect(url_for('login'))
  except: 
      return redirect(url_for('login'))
  redirect(url_for("login"))


@app.route("/oprethold", methods=["POST", "GET"])
def oprethold():
    
    
    try: 
      if session['logged_in'] == True:
        lst = []
        sql = "SELECT navn FROM players WHERE klub = ?"
        cursor.execute(sql, session['klub'])
        for x in cursor:
          lst.append(str(x)[2:-3])
        if request.method == "POST":
            
            
            holdnavn = request.form["holdnavn"]
            ejer = request.form["ejer"]
            herre1 = request.form["herre1"]
            herre2 = request.form["herre2"]
            herre3 = request.form["herre3"]
            herre4 = request.form["herre4"]
            herre5 = request.form["herre5"]
            herre6 = request.form["herre6"]
            dame1 = request.form["dame1"]
            dame2 = request.form["dame2"]
            dame3 = request.form["dame3"]
            dame4 = request.form["dame4"]
            kaptajn = request.form["Holdkaptajn"]
            
            cursor.execute("INSERT INTO hold (holdnavn, ejer, herre1, herre2, herre3, herre4, herre5, herre6, dame1, dame2, dame3, dame4, kaptajn, klub, point) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (holdnavn, ejer, herre1, herre2, herre3, herre4, herre5, herre6, dame1, dame2, dame3, dame4, kaptajn, session['klub'], 0))
            conn.commit()
            #print(lst)
            return render_template("oprethold.html", suggestions_herre=lst)
      else: 
        
        return redirect(url_for('login'))
    except: 
      return redirect(url_for('login'))


@app.route("/ændrepoint",methods =["POST","GET"])
def ændrepoint(): 
  try: 
    if session['logged_in'] == True: 
      if request.method == "POST":
        if "minus" in request.form:
          holdnavn = request.form["holdnavn"]
          point = request.form["point"]
          klub = session['klub']

          cursor.execute("UPDATE hold SET point = point-? WHERE holdnavn = ? AND klub = ?", (point, holdnavn,klub))
          conn.commit()
          sql = "SELECT * FROM hold WHERE klub = ?"
          cursor.execute(sql, session['klub'])    
          return(render_template('ændrepoint.html'))
        elif "plus" in request.form:
          holdnavn = request.form["holdnavn"]
          point = request.form["point"]
          klub = session['klub']
          cursor.execute("UPDATE hold SET point = point+? WHERE holdnavn = ? AND klub = ?", (point, holdnavn,klub))
          conn.commit()
          sql = "SELECT * FROM hold WHERE klub = ?"
          cursor.execute(sql, session['klub'])    
          return(render_template('ændrepoint.html'))
        
            
      
      return render_template('ændrepoint.html')
    else: 
      redirect(url_for("login"))
  except: 
    return redirect(url_for('login'))

@app.route("/sehold")
def sehold(): 
  try:
    if session['logged_in'] == True: 
      q = []
      sql = "SELECT * FROM hold WHERE klub = ?"
      cursor.execute(sql, session['klub'])
      for x in cursor:
        q.append([x[1],x[2],x[-1]])
      q = sorted(q, key=lambda x: x[-1], reverse=True)  
      return(render_template("sehold.html",lst = q))
    else:
      return redirect(url_for('login'))
  except: 
    return redirect(url_for('login'))


@app.route("/undersøghold")
def undersøghold():
    try:
        if session['logged_in'] == True:
            lst = []
            sql = "SELECT * FROM hold WHERE klub = ?"
            cursor.execute(sql, session['klub'])
            for x in cursor:
                lst.append([x[1],x[2], x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[-1]])
            return render_template("undersøghold.html", lst=lst)
        else:
            redirect(url_for('login'))
    except KeyError:
        return redirect(url_for('login'))

@app.route("/spil",methods = ["POST","GET"])
def spil(): 
  
    try:
      if session['logged_in'] == True:
        if request.method == "POST": 
          spiller = request.form["navn"]
          cursor.execute("INSERT INTO players (navn,point,klub) VALUES (?,?,?)",(spiller,0,session['klub']))
          conn.commit()
          cursor.execute("INSERT INTO stats (navn,klub) VALUES (?,?)",(spiller,session['klub']))
          conn.commit()
          flash(spiller)
          return(render_template("spil.html"))
        else:
          return(render_template("spil.html"))
      else: 
        return redirect(url_for('login'))
    except: 
      return redirect(url_for('login'))

@app.route("/register", methods=["POST", "GET"])
def register():

    if request.method == "POST":
        navn = request.form["navn"]
        klub = request.form["klub"]
        kode = request.form["kode"]
        hashed_password = bcrypt1.generate_password_hash(kode)
        sql = "INSERT INTO brugere (navn, kode, klub) VALUES (?,?,?)" 
        cursor.execute(sql, navn, hashed_password, klub)
        conn.commit()
        return redirect(url_for('login'))
    return render_template("register.html")


@app.route("/link",methods = ["POST","GET"])
def links():
  try:
    if session['logged_in'] == True:
      if request.method == "POST": 
        if "udebanelinknavn" in request.form:
          
          url = request.form["udebanelinknavn"]
          cursor.execute("SELECT * FROM link WHERE name = ? AND klub = ?", (url, session['klub']))
          if cursor.fetchone() is not None:
            flash("Linket er allerede brugt")
            return(render_template("links.html"))
          else:
            cursor.execute("INSERT INTO link (name,ude,id,klub) VALUES (?,?,?,?)",(url,1,0,session['klub']))
            conn.commit()
        elif "hjemmebanelinknavn" in request.form: 
          url = request.form["hjemmebanelinknavn"]
          cursor.execute("SELECT * FROM link WHERE name = ? AND klub = ?", (url, session['klub']))
          if cursor.fetchone() is not None:
            flash("Linket er allerede brugt")
            return(render_template("links.html"))
          else: 
            cursor.execute("INSERT INTO link (name,ude,id,klub) VALUES (?,?,?,?)",(url,0,0,session['klub']))
            conn.commit()
        sql = "SELECT * FROM link WHERE klub = ?"
        cursor.execute(sql, session['klub'])  
        
        
      return render_template("links.html")
    else:
      return redirect(url_for('login'))
  except KeyError:
    return redirect(url_for('login'))
@app.route("/allelinks")
def allelinks(): 
  try:
    if session['logged_in'] == True: 
        lnks = "SELECT * FROM link WHERE klub = ?"
        cursor.execute(lnks, session['klub'])
        rows = cursor.fetchall()
        for row in rows:
            k = 0 
            link = row[1]  
            ude = row[2]   
            if ude == 1: 
                k = "Udebane"
            else: 
                k = "Hjemmebane"
            flash(f"Link: {link}, {k}")

        return render_template("allelinks.html", values=lnks)
    else:
        return redirect(url_for("login"))
  except: 
    return redirect(url_for('login'))

@app.route("/logout")
def logout():  
  
  flash("you have been logged out","info")
  session.clear()
  
  return(redirect(url_for("login")))

@app.route("/job")
def job():
    return(render_template("job.html"))

@app.route("/resethold",methods = ["POST","GET"])
def resethold(): 
  try:
    if session['logged_in'] == True:
      if 'myButton' in request.form:
            print("cool")
            sql = "UPDATE hold SET point = 0 WHERE klub = ?"
            cursor.execute(sql,session['klub'])
            conn.commit()
            return(redirect(url_for("sehold")))
      return(render_template("resethold.html"))
    else:
      return(redirect(url_for("login")))
  except: 
    return redirect(url_for('login'))


@app.route("/kørspil",methods = ["POST","GET"])
def kørspil():
      if session['logged_in'] == True:
        udebanelinks = "SELECT * FROM link WHERE ude = 1 AND id = 0 AND klub = ?"
        cursor.execute(udebanelinks,session['klub'])
        udebaneliste = []
        rows1 = cursor.fetchall()
        for row in rows1:
                link1 = row[1]    
                udebaneliste.append(link1)
        hjemmebanelinks = "SELECT * FROM link WHERE ude = 0 AND id = 0 AND klub = ?"
        cursor.execute(hjemmebanelinks, session['klub'])
        hjemmebaneliste = []
        rows2 = cursor.fetchall()
        for row in rows2:
                link2 = row[1]  
                hjemmebaneliste.append(link2)          
        resultsNavne = "SELECT navn FROM players WHERE klub = ?"
        cursor.execute(resultsNavne,session['klub'])
        lstNavne = []
  
        for navne in cursor:
          lstNavne.append(str(navne[0]))
        if 'myButton' in request.form:
          if len(udebaneliste)+len(hjemmebaneliste) < 0:
              Point,statsss = (kørSpil(udebaneliste,hjemmebaneliste,lstNavne))
              statss = statsss[0]
              for i in range(len(Point)): 
                query1 = f"UPDATE stats SET point = point + {statss[i][1]}, sejre = sejre+ {statss[i][2]}, nederlag = nederlag+ {statss[i][3]}, kampe = kampe+ {statss[i][4]}, sæt = sæt+{statss[i][5]}, singlesejr = singlesejr+{statss[i][6]}, singlenederlag = singlenederlag+{statss[i][7]}, mixsejr = mixsejr+{statss[i][9]}, mixnederlag = mixnederlag+{statss[i][8]},doublesejr = doublesejr+{statss[i][10]},doublenederlag = doublenederlag+{statss[i][11]}, tosætsejr = tosætsejr+{statss[i][12]}, tresætsejr = tresætsejr+{statss[i][13]}, tosætnederlag = tosætnederlag+{statss[i][14]}, tresætnederlag = tresætnederlag+{statss[i][15]}, pointkamp = pointkamp+{statss[i][16]}, modstanderpointkamp = modstanderpointkamp+{statss[i][17]},vundet18 = vundet18+{statss[i][18]},vundet19 = vundet19+{statss[i][19]}, vundet20 = vundet20+{statss[i][20]},tabt18 = tabt18+{statss[i][21]},tabt19 = tabt19+{statss[i][22]}, tabt20 = tabt20+{statss[i][23]}, under10 = under10+{statss[i][24]}, under5 = under5+{statss[i][25]}, givet10 = givet10+{statss[i][26]}, givet5 = givet5+{statss[i][27]}, vundetfærrestpoint = vundetfærrestpoint+{statss[i][28]}, tabtflestpoint = tabtflestpoint+{statss[i][29]} WHERE klub = ?"
                cursor.execute(query1,session['klub'])
                conn.commit()
                query = f"UPDATE players SET Point = Point + {Point[i][1]} WHERE navn = '{Point[i][0]}' AND klub = ?"
                cursor.execute(query,session['klub'])
                conn.commit()
                flash(f"{Point[i][0]} har fået så mange point: {Point[i][1]}")
              holdnavne = "SELECT * FROM hold WHERE klub = ?"
              cursor.execute(resultsNavne,session['klub'])
              for j in range(len(udebanelinks)):
             
                cursor.execute("UPDATE link SET id = 1")
                conn.commit()
              for j in range(len(hjemmebanelinks)):
                    cursor.execute("UPDATE link SET id = 1")
                    conn.commit()
              lst = []
              sql = "SELECT * FROM hold WHERE klub = ?"
              cursor.execute(sql, session['klub'])  
              for x in cursor:
                  lst.append([x[1],x[3], x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[-1]])
              sql = "SELECT navn,point FROM players WHERE klub = ?"
              cursor.execute(sql,session['klub'])
              spillerlst = []
              for x in cursor: 
                spillerlst.append([x[0],x[1]])
              for i in range(len(lst)): 
                poi = update_points(lst[i][1:],spillerlst)
                cursor.execute("UPDATE hold SET point = ? WHERE holdnavn = ?", (poi, lst[i][0]))
                conn.commit()
              sql = "SELECT * FROM hold WHERE klub = ?"
              cursor.execute(sql, session['klub'])
              q = []
              for x in cursor:
                  q.append([x[1],x[2], x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[1],x[-1]])
              q = sorted(q, key=lambda x: x[-1], reverse=True)
              
              return (redirect(url_for("sehold")) )
          else:
            return(render_template("kørspil.html"))
        else:
          return render_template("kørspil.html")

      else:
        return redirect(url_for('login'))
      
    
    #except Exception as e: 
      #print(4,e)
      #return redirect(url_for('login'))
@app.route("/sletspiller",methods=["POST","GET"])
def sletspiller(): 
  try:
    if session['logged_in'] == True:
      holdlst = []
      sql = "SELECT holdnavn FROM hold WHERE klub = ?"
      cursor.execute(sql, session['klub'])
      for xy in cursor:
          holdlst.append(str(xy)[2:-3])
      linklst = []
      sql = "SELECT name FROM link WHERE klub = ?"
      cursor.execute(sql, session['klub'])
      for xi in cursor:
        linklst.append(str(xi)[2:-3])
      navnlst = []
      sql = "SELECT navn FROM players WHERE klub = ?"
      cursor.execute(sql, session['klub'])
      for x in cursor:
        navnlst.append(str(x)[2:-3])
      if "navn" in request.form: 
        name = request.form["navn"]
        query = f"DELETE FROM players WHERE navn = '{name}' AND klub = ?"
        cursor.execute(query,session['klub'])
        conn.commit()
        query = f"DELETE FROM stats WHERE navn = '{name}' AND klub = ?"
        cursor.execute(query,session['klub'])
        conn.commit()
        flash(f"Hvis {name} fandtes, er den nu blevet fjernet")
      if "links" in request.form: 
        links = request.form["links"]
        query = f"DELETE FROM link WHERE name = '{links}'"
        cursor.execute(query)
        conn.commit()
        flash(f"Hvis {links} fandtes, er den nu blevet fjernet")
      if "hold" in request.form: 
        hold = request.form["hold"]
        query = f"DELETE FROM hold WHERE holdnavn = '{hold}'"
        cursor.execute(query)
        conn.commit()
        flash(f"Hvis {hold} fandtes, er den nu blevet fjernet")
      
        
      return(render_template("sletspiller.html",navnlst = navnlst, linklst = linklst, holdlst = holdlst))
    else:
      return(redirect(url_for("login")))
  except: 
    return redirect(url_for('login'))

@app.route("/slette",methods=["POST","GET"])
def slette(): 
  try:
    if session['logged_in'] == True:
      if "SletSpiller" in request.form: 
        sql = "DELETE FROM players WHERE klub = ?"
        cursor.execute(sql, session['klub'])
        conn.commit()
        sql = "DELETE FROM stats WHERE klub = ?"
        cursor.execute(sql, session['klub'])
        conn.commit()
        
      if "SletLink" in request.form: 
        cursor.execute("DELETE FROM link")
        conn.commit()
      if "SletHold" in request.form: 
        cursor.execute("DELETE FROM hold")
        conn.commit()
      return(render_template("slette.html"))
    else:
      return(redirect(url_for("login")))
  except: 
    return redirect(url_for('login'))


@app.route("/brugtelinks")
def brugt(): 
  try:

    if session.get('logged_in'):

      sql = "SELECT * FROM link WHERE id = ? AND klub = ?"
      #sql = "SELECT * FROM link WHERE klub = ?"
      cursor.execute(sql, (session['klub']))
      for x in cursor:
        flash(x)
        
      return render_template("brugt.html")
  except: 
    return redirect(url_for('login'))


@app.route("/resetpoint",methods= ["POST","GET"])
def resetpoint(): 
  try:
    if session['logged_in'] == True:
      if 'myButton' in request.form:
            sql = "UPDATE players SET Point = 0 WHERE klub = ?"
            cursor.execute(sql,session['klub'])
            conn.commit()
            return ( redirect(url_for("spillere")))
      return(render_template("resetpoint.html"))
    else:
      return(redirect(url_for("login")))
  except: 
    return redirect(url_for('login'))

if __name__ == "__main__":
    #with app.app_context():
        #db.create_all()
    #serve(app, host = "127.0.0.1", port = 5000, threads = 4)
    app.run(debug=True)
    

