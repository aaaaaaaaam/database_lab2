import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox
import mysql.connector
import function
from PyQt5.QtGui import QIcon

KEY_LIST = ['bno', 'bname', 'author',
            'date', 'press', 'position', 'sum', 'class']


class mod_stu(QWidget):
    def __init__(self, sno:str):
        super().__init__()
        self.sno = sno
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('学生信息更新')

        vbox = QVBoxLayout()

        self.selectBox = QComboBox()
        self.selectBox.addItems(['姓名', '学院', '年龄', '性别'])
        self.selectBox.setFixedSize(60, 40)
        self.searchTitle = QLabel()
        self.searchTitle.setText('更新信息')
        self.searchTitle.setFixedSize(90, 40)
        self.searchInput = QLineEdit()
        self.searchInput.setText('')
        self.searchInput.setClearButtonEnabled(True)
        self.searchInput.setFixedSize(250, 40)
        searchLayout = QHBoxLayout()
        searchLayout.addStretch()
        searchLayout.addWidget(self.selectBox)
        searchLayout.addWidget(self.searchTitle)
        searchLayout.addWidget(self.searchInput)
        searchLayout.addStretch()
        vbox.addLayout(searchLayout)
        
        hbox5 = QHBoxLayout()
        self.register_button = QPushButton('提交')
        self.register_button.setFixedSize(400, 40)
        hbox5.addStretch()
        hbox5.addWidget(self.register_button)
        vbox.addLayout(hbox5)
        
        hbox6 = QHBoxLayout()
        back_button = QPushButton('返回')
        back_button.setFixedSize(400, 40)
        back_button.clicked.connect(self.close)
        hbox6.addStretch()
        hbox6.addWidget(back_button)
        vbox.addLayout(hbox6)

        self.setLayout(vbox)

    def register(self):
        convert = {'姓名': 'sname', '学院': 'dept', '年龄': 'age', '性别': 'sex'}
        self.book_update = function.update_student_adm(self.searchInput.text(), convert[self.selectBox.currentText()], self.sno)


    