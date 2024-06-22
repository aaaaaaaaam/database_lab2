import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QGridLayout
import mysql.connector
from PyQt5.QtGui import QIcon, QFont
import function

class Signup(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('学生注册')
        self.setWindowIcon(QIcon('icon/person.png'))

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        label1 = QLabel('学号：')
        label1.setFont(QFont("Arial", 16, QFont.Bold))
        label1.setStyleSheet("color: black; background-color: white;")
        label1.setFixedSize(100, 40)
        self.id_edit = QLineEdit()
        self.id_edit.setFixedSize(200, 40)
        hbox1.addWidget(label1)
        hbox1.addWidget(self.id_edit)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        label2 = QLabel('姓名：')
        label2.setFont(QFont("Arial", 16, QFont.Bold))
        label2.setStyleSheet("color: black; background-color: white;")
        label2.setFixedSize(100, 40)
        self.name_edit = QLineEdit()
        self.name_edit.setFixedSize(200, 40)
        hbox2.addWidget(label2)
        hbox2.addWidget(self.name_edit)
        vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        label3 = QLabel('学院：')
        label3.setFont(QFont("Arial", 16, QFont.Bold))
        label3.setStyleSheet("color: black; background-color: white;")
        label3.setFixedSize(100,40)
        self.dept_edit = QLineEdit()
        self.dept_edit.setFixedSize(200,40)
        hbox3.addWidget(label3)
        hbox3.addWidget(self.dept_edit)
        vbox.addLayout(hbox3)

        hbox4 = QHBoxLayout()
        label4 = QLabel('年龄：')
        label4.setFont(QFont("Arial", 16, QFont.Bold))
        label4.setStyleSheet("color: black; background-color: white;")
        label4.setFixedSize(100,40)
        self.age_edit = QLineEdit()
        self.age_edit.setFixedSize(200,40)
        hbox4.addWidget(label4)
        hbox4.addWidget(self.age_edit)
        vbox.addLayout(hbox4)

        hbox5 = QHBoxLayout()
        label5 = QLabel('性别：')
        label5.setFont(QFont("Arial", 16, QFont.Bold))
        label5.setStyleSheet("color: black; background-color: white;")
        label5.setFixedSize(100,40)
        self.sex_edit = QLineEdit()
        self.sex_edit.setFixedSize(200,40)
        hbox5.addWidget(label5)
        hbox5.addWidget(self.sex_edit)
        vbox.addLayout(hbox5)


        hbox6 = QHBoxLayout()
        label6 = QLabel('密码：')
        label6.setFont(QFont("Arial", 16, QFont.Bold))
        label6.setStyleSheet("color: black; background-color: white;")
        label6.setFixedSize(100,40)
        self.password_edit = QLineEdit()
        self.password_edit.setFixedSize(200,40)
        hbox6.addWidget(label6)
        hbox6.addWidget(self.password_edit)
        vbox.addLayout(hbox6)
        
        hbox7 = QHBoxLayout()
        label7 = QLabel('重复密码：')
        label7.setFont(QFont("Arial", 16, QFont.Bold))
        label7.setStyleSheet("color: black; background-color: white;")
        label7.setFixedSize(100,40)
        self.repassword_edit = QLineEdit()
        self.repassword_edit.setFixedSize(200,40)
        hbox7.addWidget(label7)
        hbox7.addWidget(self.repassword_edit)
        vbox.addLayout(hbox7)
        
        hbox10 = QHBoxLayout()
        self.register_button = QPushButton('提交')
        self.register_button.setFont(QFont("Arial", 19, QFont.Bold))
        self.register_button.setStyleSheet("color: black; background-color: white;")
        self.register_button.setFixedSize(400, 40)
        #self.register_button.clicked.connect(self.register)
        hbox10.addStretch()
        hbox10.addWidget(self.register_button)
        vbox.addLayout(hbox10)
        
        hbox11 = QHBoxLayout()
        self.back_button = QPushButton('返回')
        self.back_button.setFont(QFont("Arial", 19, QFont.Bold))
        self.back_button.setStyleSheet("color: black; background-color: white;")
        self.back_button.setFixedSize(400, 40)
        #back_button.clicked.connect(self.close)
        hbox11.addStretch()
        hbox11.addWidget(self.back_button)
        vbox.addLayout(hbox11)

        self.inputBox = QWidget()
        self.inputBox.setLayout(vbox)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.inputBox)


        self.setLayout(self.bodyLayout)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Signup()
    window.show()
    sys.exit(app.exec_())