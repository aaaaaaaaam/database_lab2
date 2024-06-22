import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, \
    QToolButton, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('学生/管理员登录')
        self.setWindowIcon(QIcon('icon/person.png'))

        self.vbox = QVBoxLayout()

        label = QLabel()
        label.setText('欢迎登录图书管理系统')
        label.setFont(QFont("微软雅黑", 20, QFont.Bold))
        label.setStyleSheet("color: black; background-color: white;")
        label.setAlignment(Qt.AlignVCenter)  # 居中对齐
        label.setFixedSize(520, 50)
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        self.vbox.addLayout(hbox)

        hbox1 = QHBoxLayout()
        account = QLabel()
        account.setText('读者证号(学工号)')
        account.setAlignment(Qt.AlignVCenter)  # 居中对齐
        account.setFont(QFont("微软雅黑", 16))
        account.setStyleSheet("color: black; background-color: white;")
        account.setFixedSize(190, 50)
        self.account_edit = QLineEdit()
        self.account_edit.setFixedSize(320, 50)  # 框的大小
        hbox1.addWidget(account)
        hbox1.addWidget(self.account_edit)
        self.vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        password = QLabel()
        password.setText('图书馆密码')
        password.setAlignment(Qt.AlignVCenter)  # 居中对齐
        password.setFont(QFont("微软雅黑", 16))
        password.setStyleSheet("color: black; background-color: white;")
        password.setFixedSize(190, 50)
        self.password_edit = QLineEdit()
        self.password_edit.setFixedSize(320, 50)  # 框的大小
        hbox2.addWidget(password)
        hbox2.addWidget(self.password_edit)
        self.vbox.addLayout(hbox2)

        # 注册按钮
        hbox3 = QHBoxLayout()
        self.signup = QToolButton()
        self.signup.setText('注册')
        self.signup.setFont(QFont("微软雅黑", 16))
        self.signup.setStyleSheet("color: black; background-color: white;")
        self.signup.setFixedSize(100, 40)

        # 登录按钮
        self.loginButton = QToolButton()
        self.loginButton.setText('登录')
        self.loginButton.setFont(QFont("微软雅黑", 16))
        self.loginButton.setStyleSheet("color: black; background-color: white;")
        self.loginButton.setFixedSize(100, 40)
        hbox3.addWidget(self.signup)
        hbox3.addWidget(self.loginButton)
        self.vbox.addLayout(hbox3)
        
        self.inputBox = QWidget()
        self.inputBox.setLayout(self.vbox)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.inputBox)
        self.setLayout(self.bodyLayout)
        
        self.setStyleSheet('''
                background-color:white;
        ''')

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec_())