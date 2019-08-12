from socket import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql,socket,sys,time
from threading import Thread 
from socketserver import ThreadingMixIn
import sys
client=None
global uname,psw
server_address='localhost'
server_port=1234
print("Server connected")
db_address='localhost'
db_port=3306
db_name='chatdb'
db_user='root'
db_psw=''
print("Db connected")
class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(373, 444)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.tab_5 = QtWidgets.QTabWidget(self.centralwidget)
		self.tab_5.setEnabled(True)
		self.tab_5.setGeometry(QtCore.QRect(20, 10, 341, 401))
		self.tab_5.setStyleSheet("QTabWidget::pane\n"
		"{\n"
		"    border-top: 2px solid #1B1B1B;\n"
		"    background-color: #FFFFFF;\n"
		"}\n"
		"\n"
		"QTabWidget::tab-bar\n"
		"{\n"
		"    left: 5px;\n"
		"    alignment: left;\n"
		"    background: #3E3E3E;\n"
		"}\n"
		"\n"
		"QTabBar::tab\n"
		"{\n"
		"    background: transparent;\n"
		"    color: #000000;\n"
		"    padding: 15px 5px 15px 5px;\n"
		"}\n"
		"\n"
		"QTabBar::tab:hover\n"
		"{\n"
		"    text-decoration: underline;\n"
		"}\n"
		"\n"
		"QTabBar::tab:selected\n"
		"{\n"
		"    color: #FFFFFF;\n"
		"    background: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #262626, stop: 1.0 #3D3D3D );\n"
		"}\n"
		"QWidget {\n"
		"    background-color:#00800;\n"
		"}\n"
		"\n"
		"")
		self.tab_5.setObjectName("tab_5")
		self.tablogin = QtWidgets.QWidget()
		self.tablogin.setObjectName("tablogin")
		self.txtlname = QtWidgets.QTextEdit(self.tablogin)
		self.txtlname.setGeometry(QtCore.QRect(80, 50, 161, 21))
		self.txtlname.setObjectName("txtlname")
		self.label_3 = QtWidgets.QLabel(self.tablogin)
		self.label_3.setGeometry(QtCore.QRect(10, 50, 81, 20))
		self.label_3.setObjectName("label_3")
		self.txtlpassword = QtWidgets.QTextEdit(self.tablogin)
		self.txtlpassword.setGeometry(QtCore.QRect(80, 110, 161, 21))
		self.txtlpassword.setObjectName("txtlpassword")
		self.label_6 = QtWidgets.QLabel(self.tablogin)
		self.label_6.setGeometry(QtCore.QRect(10, 110, 81, 20))
		self.label_6.setObjectName("label_6")
		self.btnlogin = QtWidgets.QPushButton(self.tablogin)
		self.btnlogin.setGeometry(QtCore.QRect(80, 160, 87, 29))
		self.btnlogin.setObjectName("btnlogin")
		self.btnlogin.clicked.connect(self.signin)
		self.lblstatus_2 = QtWidgets.QLabel(self.tablogin)
		self.lblstatus_2.setGeometry(QtCore.QRect(100, 220, 171, 16))
		self.lblstatus_2.setObjectName("lblstatus_2")
		self.tab_5.addTab(self.tablogin, "")
		self.tabsignup = QtWidgets.QWidget()
		self.tabsignup.setObjectName("tabsignup")
		self.label_2 = QtWidgets.QLabel(self.tabsignup)
		self.label_2.setGeometry(QtCore.QRect(140, 60, 54, 17))
		self.label_2.setText("")
		self.label_2.setObjectName("label_2")
		self.btnsignup = QtWidgets.QPushButton(self.tabsignup)
		self.btnsignup.setGeometry(QtCore.QRect(100, 310, 87, 29))
		self.btnsignup.setObjectName("btnsignup")
		self.btnsignup.clicked.connect(self.signup)
		self.txtusername = QtWidgets.QTextEdit(self.tabsignup)
		self.txtusername.setGeometry(QtCore.QRect(100, 40, 161, 21))
		self.txtusername.setObjectName("txtusername")
		self.txtpassword = QtWidgets.QTextEdit(self.tabsignup)
		self.txtpassword.setGeometry(QtCore.QRect(100, 80, 161, 21))
		self.txtpassword.setObjectName("txtpassword")
		self.txtemail = QtWidgets.QTextEdit(self.tabsignup)
		self.txtemail.setGeometry(QtCore.QRect(100, 120, 161, 21))
		self.txtemail.setObjectName("txtemail")
		self.txtphone = QtWidgets.QTextEdit(self.tabsignup)
		self.txtphone.setGeometry(QtCore.QRect(100, 160, 161, 21))
		self.txtphone.setObjectName("txtphone")
		self.rmale = QtWidgets.QRadioButton(self.tabsignup)
		self.rmale.setGeometry(QtCore.QRect(100, 200, 100, 22))
		self.rmale.setObjectName("rmale")
		self.rfemale = QtWidgets.QRadioButton(self.tabsignup)
		self.rfemale.setGeometry(QtCore.QRect(160, 200, 100, 22))
		self.rfemale.setObjectName("rfemale")
		self.txtage = QtWidgets.QTextEdit(self.tabsignup)
		self.txtage.setGeometry(QtCore.QRect(100, 240, 104, 21))
		self.txtage.setObjectName("txtage")
		self.label = QtWidgets.QLabel(self.tabsignup)
		self.label.setGeometry(QtCore.QRect(10, 40, 61, 17))
		self.label.setObjectName("label")
		self.label_7 = QtWidgets.QLabel(self.tabsignup)
		self.label_7.setGeometry(QtCore.QRect(10, 80, 54, 17))
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self.tabsignup)
		self.label_8.setGeometry(QtCore.QRect(10, 120, 54, 17))
		self.label_8.setObjectName("label_8")
		self.label_9 = QtWidgets.QLabel(self.tabsignup)
		self.label_9.setGeometry(QtCore.QRect(10, 160, 54, 17))
		self.label_9.setObjectName("label_9")
		self.label_10 = QtWidgets.QLabel(self.tabsignup)
		self.label_10.setGeometry(QtCore.QRect(10, 200, 54, 17))
		self.label_10.setObjectName("label_10")
		self.label_11 = QtWidgets.QLabel(self.tabsignup)
		self.label_11.setGeometry(QtCore.QRect(10, 240, 54, 17))
		self.label_11.setObjectName("label_11")
		self.lblstatus = QtWidgets.QLabel(self.tabsignup)
		self.lblstatus.setGeometry(QtCore.QRect(100, 280, 171, 16))
		self.lblstatus.setObjectName("lblstatus")
		self.tab_5.addTab(self.tabsignup, "")
		MainWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		
		self.retranslateUi(MainWindow)
		self.tab_5.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label_3.setText(_translate("MainWindow", "Username"))
		self.label_6.setText(_translate("MainWindow", "Password"))
		self.btnlogin.setText(_translate("MainWindow", "Login"))
		self.lblstatus_2.setText(_translate("MainWindow", "popup"))
		self.tab_5.setTabText(self.tab_5.indexOf(self.tablogin), _translate("MainWindow", "Login"))
		self.btnsignup.setText(_translate("MainWindow", "SignUP"))
		self.rmale.setText(_translate("MainWindow", "Male"))
		self.rfemale.setText(_translate("MainWindow", "Female"))
		self.label.setText(_translate("MainWindow", "Username"))
		self.label_7.setText(_translate("MainWindow", "Password"))
		self.label_8.setText(_translate("MainWindow", "Email"))
		self.label_9.setText(_translate("MainWindow", "Phone"))
		self.label_10.setText(_translate("MainWindow", "Gender"))
		self.label_11.setText(_translate("MainWindow", "Age"))
		self.lblstatus.setText(_translate("MainWindow", "popup"))
		self.label_9.setText(_translate("MainWindow", "Phone"))
		self.label_10.setText(_translate("MainWindow", "Gender"))
		self.label_11.setText(_translate("MainWindow", "Age"))
		self.lblstatus.setText(_translate("MainWindow", "popup"))
		self.tab_5.setTabText(self.tab_5.indexOf(self.tabsignup), _translate("MainWindow", "Sign Up"))
	def signin(self):
		
		uname=self.txtlname.toPlainText()
		psw=self.txtlpassword.toPlainText()
		db = pymysql.connect(db_address,db_user,db_psw,db_name)
		cursor=db.cursor()
		cursor.execute("Select * from user where user_name='"+uname+"' and user_psw='"+psw+"'")
		data=cursor.fetchone()
		if data:
			client_socket.send(bytes(uname.encode("utf8")))
			global publicchat
			publicchat = QtWidgets.QMainWindow()
			self.ui=Ui_publicchatform()
			self.ui.setupUi(publicchat)
			publicchat.show()
			db = pymysql.connect(db_address,db_user,db_psw,db_name)
			cursor=db.cursor()
			cursor.execute("Select user_name from user where status='active'")
			data=cursor.fetchall()
			for item in data:
				self.ui.lstonline.addItem(str(item).strip("'[](),"))
			cursor.close()
			sql="UPDATE `user` set status=('%s') where user_name='%s'"%("active",uname)
			cursor=db.cursor()
			self.ui.lblcurrentuser.setText("User : "+uname)
			cursor.execute(sql)
			db.commit()
			cursor.close()
			db.close
			MainWindow.show()
		else:
			self.lblstatus_2.setText("NOT FOUND")
		db.close
	def signup(self):
		uname=self.txtusername.toPlainText()
		psw=self.txtpassword.toPlainText()
		email=self.txtemail.toPlainText()
		phn=int(self.txtphone.toPlainText())
		if(self.rmale.isChecked()):
			gender='male'
		elif(self.rfemale.isChecked()):
			gender='female'
		else:
			self.lblstatus_2.setTexr("Select Gender")
		age=int(self.txtage.toPlainText())
		
		db = pymysql.connect(db_address,db_user,db_psw,db_name)
		cursor=db.cursor()
		sql="INSERT INTO `user`(user_name,user_psw,user_email,user_phn,user_gender,user_age,status) VALUES ('%s','%s','%s','%d','%s','%d','inactive')" % (uname,psw,email,phn,gender,age)
		data=cursor.execute(sql)
		db.commit()
		if data:
			self.lblstatus.setText("Signed Up-Please login")
			self.txtusername.clear()
			self.txtpassword.clear()
			self.txtemail.clear()
			self.txtphone.clear()
			self.txtage.clear()
		else:
			self.lblstatus.setText("SIGNUP FAILED")
		db.close


BUFSIZ = 1024
ADDR = (server_address, server_port)
print(socket)
client_socket = socket.socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
		
class Ui_publicchatform(object):
	def __init__(self):
		receive_thread = Thread(target=self.receive)
		receive_thread.start()	
		
	def setupUi(self, publicchatform):
		publicchatform.setObjectName("publicchatform")
		publicchatform.resize(485, 397)
		publicchatform.setTabShape(QtWidgets.QTabWidget.Rounded)
		self.centralwidget = QtWidgets.QWidget(publicchatform)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 311, 231))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.lstchatbox = QtWidgets.QListWidget(self.gridLayoutWidget)
		self.lstchatbox.setObjectName("lstchatbox")
		self.gridLayout.addWidget(self.lstchatbox, 0, 0, 1, 1)
		self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
		self.gridLayoutWidget_2.setGeometry(QtCore.QRect(329, 70, 151, 291))
		self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
		self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.btnpm = QtWidgets.QPushButton(self.gridLayoutWidget_2)
		self.btnpm.setObjectName("btnpm")
		self.gridLayout_2.addWidget(self.btnpm, 1, 0, 1, 1)
		self.lstonline = QtWidgets.QListWidget(self.gridLayoutWidget_2)
		self.lstonline.setObjectName("lstonline")
		self.gridLayout_2.addWidget(self.lstonline, 0, 0, 1, 1)
		self.btnsend = QtWidgets.QPushButton(self.centralwidget)
		self.btnsend.setGeometry(QtCore.QRect(140, 340, 181, 21))
		self.btnsend.setObjectName("btnsend")
		self.btnsend.clicked.connect(self.send)
		self.btnleave = QtWidgets.QPushButton(self.centralwidget)
		self.btnleave.setGeometry(QtCore.QRect(10, 340, 131, 21))
		self.btnleave.setObjectName("btnleave")
		self.btnleave.clicked.connect(self.signout)
		self.txtsendmsg = QtWidgets.QTextEdit(self.centralwidget)
		self.txtsendmsg.setGeometry(QtCore.QRect(10, 310, 311, 21))
		self.txtsendmsg.setObjectName("txtsendmsg")
		self.lblcurrentuser = QtWidgets.QLabel(self.centralwidget)
		self.lblcurrentuser.setGeometry(QtCore.QRect(120, 40, 131, 17))
		self.lblcurrentuser.setObjectName("lblcurrentuser")
		publicchatform.setCentralWidget(self.centralwidget)
		self.statusbar = QtWidgets.QStatusBar(publicchatform)
		self.statusbar.setObjectName("statusbar")
		publicchatform.setStatusBar(self.statusbar)
	
		self.retranslateUi(publicchatform)
		QtCore.QMetaObject.connectSlotsByName(publicchatform)
	def retranslateUi(self, publicchatform):
		_translate = QtCore.QCoreApplication.translate
		publicchatform.setWindowTitle(_translate("publicchatform", "PUBLIC CHAT"))
		self.btnpm.setText(_translate("publicchatform", "Personal Message"))
		self.btnsend.setText(_translate("publicchatform", "SEND"))
		self.btnleave.setText(_translate("publicchatform", "LEAVE"))
		self.lblcurrentuser.setText(_translate("publicchatform", "USERNAME"))
	def signout(self):
		uname=self.lblcurrentuser.text()
		uname=uname.replace('User : ','')
		db = pymysql.connect(db_address,db_user,db_psw,db_name)
		cursor=db.cursor()
		print(cursor)
		sql="UPDATE `user` set status=('%s') where user_name='%s'"%("inactive",uname)
		print(sql)
		cursor.execute(sql)
		db.commit()
		db.close
		self.lblcurrentuser.setText("")
		self.on_closing()
		app2 = QtWidgets.QApplication(sys.argv)
		publicchat = QtWidgets.QMainWindow()
		ui = Ui_publicchatform()
		ui.setupUi(publicchat)
		publicchat.close()
		sys.exit(app2.exec_())
	def receive(self):
		"""Handles receiving of messages."""
		while True:
			try:
				msg = client_socket.recv(BUFSIZ).decode("utf8")
				self.lstchatbox.addItem(msg)
			except OSError:  # Possibly client has left the chat.
				self.lstchatbox.addItem(uname+"has left chat")
				break
	            
	            
	def send(self,event=None):  # event is passed by binders.
		"""Handles sending of messages."""
		msg = self.txtsendmsg.toPlainText()
		self.txtsendmsg.setText("")  # Clears input field.
		client_socket.send(bytes(msg.encode("utf8")))
		if msg == "{quit}":
			client_socket.close()
	def on_closing(self,event=None):
	    """This function is to be called when the window is closed."""
	    msg="{quit}"
	    self.send()

if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
