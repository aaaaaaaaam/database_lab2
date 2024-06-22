import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5 import QtGui
import login
import function
import signup
import student_page
import administrator_page
import mysql.connector


class BookManage_Window(QWidget):

    def __init__(self):
        super().__init__()
        self.login = login.Login()
        self.login.setParent(self)
        self.login.move(390, 120)
        self.login.loginButton.clicked.connect(self.login_button)
        self.login.signup.clicked.connect(self.signup_button)
        self.setGeometry(200, 200, 1280, 720)
        self.setFixedSize(1280, 720)
        self.setMyStyle()
        self.user = 'stu'
        # 创建登录菜单

    def login_button(self):
        self.id = self.login.account_edit.text()
        self.password = self.login.password_edit.text()
        res = True
        if self.id[0] == 'S':
            self.user = 'stu'
            res = function.stu_check(self.id, self.password)
        elif self.id[0] == 'G':
            self.user = 'adm'
            res = function.administrator_check(self.id, self.password)
        
        if res == True:
            self.login.setVisible(False)
            self.display()
        else:
            print('登录失败!')
            

# 显示注册界面
    def signup_button(self):
        self.login.setVisible(False)
        self.signup = signup.Signup()
        self.signup.setParent(self)
        self.signup.setVisible(True)
        self.signup.move(425, 110)
        self.signup.back_button.clicked.connect(self.back)
        self.signup.register_button.clicked.connect(self.register)

# 后退按钮
    def back(self):
        self.signup.setVisible(False)
        self.login.setVisible(True)
        
    def register(self):
        id = self.signup.id_edit.text()
        name_ = self.signup.name_edit.text()
        dept = self.signup.dept_edit.text()
        age_ = self.signup.age_edit.text()
        sex = self.signup.sex_edit.text()
        password = self.signup.password_edit.text()
        rep_pass = self.signup.repassword_edit.text()

        if password != rep_pass:
            QMessageBox.warning(self, '警告', '密码前后不相同')
            return

        res = True
        conn = mysql.connector.connect(host = function.CONFIG['host'], user = function.CONFIG['user'], password = function.CONFIG['pwd'], database = function.CONFIG['db'], charset="utf8")
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO student (sno, sname, dept, age, sex, code_stu) VALUES (%s, %s, %s, %s, %s, %s)",
                           (id, name_, dept, age_, sex, password))
            conn.commit()
        except Exception as e:
            print('Search error!')
            print(e)
            res = False
        finally:
            if conn:
                conn.close()
            self.user = 'stu' 
        if res:
            self.signup.setVisible(False)
            self.id = id
            self.display()
        else:
            self.errorBox('注册失败')

    def display(self):
        # 显示学生信息
        if self.user == 'stu':
            stu = function.get_student_info(self.id)
            self.body = student_page.StudentPage(stu)
            self.body.setParent(self)
            self.body.setVisible(True)
            self.body.out.clicked.connect(self.logout)
        else:
            adm = function.get_administrator_info(self.id)
            self.body = administrator_page.AdministratorPage(adm)
            self.body.setParent(self)
            self.body.setVisible(True)
            self.body.out.clicked.connect(self.logout)


    def logout(self):
        self.body.close()
        self.login.setVisible(True)

    def errorBox(self, mes: str):
        msgBox = QMessageBox(
            QMessageBox.Warning,
            "警告!",
            mes,
            QMessageBox.NoButton,
            self
        )
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.exec_()

    def setMyStyle(self):
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("icon/back.jpg").scaled(1280, 720)))
        self.setPalette(window_pale)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = BookManage_Window()
    mainwindow.show()
    sys.exit(app.exec_())

