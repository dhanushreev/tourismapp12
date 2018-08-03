from flask import Flask, render_template, request,redirect,url_for,session,g
import sqlite3


app=Flask(__name__)


DATABASE = 'myapp.db'


def connect_db():
   return sqlite3.connect(DATABASE)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/getsession')
def getsession():
   if 'user' in session:
      return session['user']
   return 'not logedin'

@app.route('/dropsession')
def dropsession():
   session.pop('user',None)
   return 'Dropped!!!'

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/places')
def places():
   return render_template('places.html')

@app.route('/packages')
def packages():
   return render_template('packages.html')

@app.route('/pack')
def pack():
   return render_template('pack.html')

@app.route('/pack2')
def pack2():
   return render_template('pack2.html')

@app.route('/pack3')
def pack3():
   return render_template('pack3.html')

@app.route('/pack4')
def pack4():
   return render_template('pack4.html')

@app.route('/karnataka')
def karnataka():
   return render_template('karnataka.html')

@app.route('/kerala')
def kerala():
   return render_template('kerala.html')

@app.route('/andhrapradhesh')
def andhrapradhesh():
   return render_template('andhrapradhesh.html')

@app.route('/Tamilnadu')
def Tamilnadu():
   return render_template('Tamilnadu.html')

@app.route('/a')
def a():
   return render_template('a.html')

@app.route('/a1')
def a1():
   return render_template('a1.html')

@app.route('/a2')
def a2():
   return render_template('a2.html')

@app.route('/a3')
def a3():
   return render_template('a3.html')

@app.route('/a4')
def a4():
   return render_template('a4.html')

@app.route('/a5')
def a5():
   return render_template('a5.html')

@app.route('/a6')
def a6():
   return render_template('a6.html')

@app.route('/a7')
def a7():
   return render_template('a7.html')

@app.route('/a8')
def a8():
   return render_template('a8.html')

@app.route('/a9')
def a9():
   return render_template('a9.html')

@app.route('/a10')
def a10():
   return render_template('a10.html')

@app.route('/a11')
def a11():
   return render_template('a11.html')

@app.route('/k')
def k():
   return render_template('k.html')

@app.route('/k1')
def k1():
   return render_template('k1.html')

@app.route('/k2')
def k2():
   return render_template('k2.html')

@app.route('/k3')
def k3():
   return render_template('k3.html')

@app.route('/k4')
def k4():
   return render_template('k4.html')

@app.route('/k5')
def k5():
   return render_template('k5.html')

@app.route('/k6')
def k6():
   return render_template('k6.html')

@app.route('/k7')
def k7():
   return render_template('k7.html')

@app.route('/k8')
def k8():
   return render_template('k8.html')

@app.route('/k9')
def k9():
   return render_template('k9.html')

@app.route('/k10')
def k10():
   return render_template('k10.html')

@app.route('/k11')
def k11():
   return render_template('k11.html')

@app.route('/ke1')
def ke1():
   return render_template('ke1.html')

@app.route('/ke2')
def ke2():
   return render_template('ke2.html')

@app.route('/ke3')
def ke3():
   return render_template('ke3.html')

@app.route('/ke4')
def ke4():
   return render_template('ke4.html')

@app.route('/ke5')
def ke5():
   return render_template('ke5.html')

@app.route('/ke6')
def ke6():
   return render_template('ke6.html')

@app.route('/ke7')
def ke7():
   return render_template('ke7.html')

@app.route('/ke8')
def ke8():
   return render_template('ke8.html')

@app.route('/ke9')
def ke9():
   return render_template('ke9.html')

@app.route('/ke10')
def ke10():
   return render_template('ke10.html')

@app.route('/ke11')
def ke11():
   return render_template('ke11.html')

@app.route('/ke12')
def ke12():
   return render_template('ke12.html')

@app.route('/te1')
def te1():
   return render_template('te1.html')

@app.route('/te2')
def te2():
   return render_template('te2.html')

@app.route('/te3')
def te3():
   return render_template('te3.html')

@app.route('/te4')
def te4():
   return render_template('te4.html')

@app.route('/te5')
def te5():
   return render_template('te5.html')

@app.route('/te6')
def te6():
   return render_template('te6.html')

@app.route('/te7')
def te7():
   return render_template('te7.html')

@app.route('/te8')
def te8():
   return render_template('te8.html')

@app.route('/te9')
def te9():
   return render_template('te9.html')

@app.route('/te10')
def te10():
   return render_template('te10.html')

@app.route('/te11')
def te11():
   return render_template('te11.html')

@app.route('/te12')
def te12():
   return render_template('te12.html')

@app.route('/login',methods=['GET','POST'])
def login():
   return render_template('booking.html')

@app.route('/checkuser',methods=['GET','POST'])
def checkuser():
   username = request.form['username']
   password = request.form['password']
   db = connect_db()
   cur = db.execute("select * from login112 where username=? and password=? ",(username,password))
   entries5 = [dict(username=row[0],password=row[1]) for row in cur.fetchall()]
   if int(len(entries5))>0:
      return render_template('booking2.html')
   else:
      return "failed"

@app.route('/booking')
def booking():
   return render_template('booking.html')

@app.route('/myProfile',methods=['POST','GET'])
def showmyprofile():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      email = request.form['email']
      db = connect_db()
      sql = "insert into login112 (username,password,email) values (?,?,?)"
      db.execute(sql, [username,password,email])
      db.commit()
      db.close()
      return render_template('myProfile.html',html_page_name=username)   

@app.route('/bookinglist')
def bookinglist():
   db = connect_db()
   cur = db.execute("select username,password,email from login112")
   entries = [dict(username=row[0],password=row[1],email=row[2]) for row in cur.fetchall()]
   print(entries)
   db.close()
   return render_template('users.html',entries=entries)  

@app.route('/booking2')
def booking1():
      return render_template('booking2.html')

@app.route('/myProfile2',methods=['GET','POST'])
def showmyprofile1():
   if request.method == 'POST':
      username = request.form['username']
      email = request.form['email']
      phonenumber = request.form['phonenumber']
      password = request.form['password']
      confirmpassword = request.form['confirmpassword']
      db = connect_db()
      sql = "insert into cpass (username,email,phonenumber,password,confirmpassword) values (?,?,?,?,?)"
      db.execute(sql, [username,email,phonenumber,password,confirmpassword])
      db.commit()
      db.close()
      return render_template('myprofile2.html',html_page_name=username)   

@app.route('/cpasslist1')
def bookinglist1():
   db = connect_db()
   cur = db.execute("select username,email,phonenumber,password,confirmpassword from cpass")
   entries1 = [dict(username=row[0],email=row[1],phonenumber=row[2],password=row[3], confirmpassword=row[4]) for row in cur.fetchall()]
   print(entries1)
   db.close()
   return render_template('user1.html',entries1=entries1)  

@app.route('/booking3')
def booking3():
   return render_template('booking3.html')

@app.route('/myProfile3',methods=['GET','POST'])
def showmyprofile3():
   if request.method == 'POST':
      username = request.form['username']
      email = request.form['email']
      password = request.form['password']
      reenterpassword = request.form['reenterpassword']
      db = connect_db()
      sql = "insert into pass (username,email,password,reenterpassword) values (?,?,?,?)"
      db.execute(sql, [username,email,password,reenterpassword])
      db.commit()
      db.close()
      return render_template('myprofile3.html',html_page_name=username)   

@app.route('/cpasslist3')
def bookinglist3():
   db = connect_db()
   cur = db.execute("select username,email,password,reenterpassword from pass")
   entries2 = [dict(username=row[0],email=row[1],password=row[2],reenterpassword=row[3]) for row in cur.fetchall()]
   print(entries2)
   db.close()
   return render_template('user2.html',entries2=entries2)  

if __name__=='__main__':
    app.run(debug=True)
