import sys
import time
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QGroupBox, QMessageBox, 
                             QToolButton, QSplitter, QVBoxLayout, QHBoxLayout,
                             QLabel, QTableWidget, QTableWidgetItem, QAbstractItemView,
                             QLineEdit, QFileDialog, QToolTip, QComboBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize
import function
import datetime
import book_information
import add_book
from PyQt5.QtGui import QPixmap
import add_student
import mod_student

# import func

class AdministratorPage(QWidget):
    def __init__(self, adm_info):
        super().__init__()
        self.adm_info = adm_info
        self.init_page()
        
    def init_page(self):
        self.title = QWidget()
        self.set_title()
        self.menu = QWidget()
        self.set_menu()
        
        self.body = QVBoxLayout()
        self.body.addStretch()
        self.body.addWidget(self.title)
        self.body.addWidget(self.menu)
        self.body.addStretch()
        
        self.page_index = 0
        self.page = QWidget()
        self.page.setFixedSize(1250, 600)
        self.page.setStyleSheet('background-color: white;')
        
        #self.body.addLayout(self.page)
        self.wid = QWidget()
        self.wid.setLayout(self.body)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.wid)

        self.setLayout(self.bodyLayout)

    def set_title(self):
        self.title_font = QFont("微软雅黑", 20, QFont.Bold)
        
        self.title_text = QLabel()
        self.title_text.setText('欢迎使用图书管理系统')
        self.title_text.setFont(self.title_font)
        self.title_text.setStyleSheet("color: black; background-color: white;")
        self.title_text.setFixedHeight(40)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.adm_info[0] + self.adm_info[1] + '，欢迎！')
        self.user_id_name.setFont(self.title_font)
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(40)
        
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(self.title_font)
        self.out.setStyleSheet("color: black; background-color: white;")
        self.out.setFixedHeight(40)
        

        self.titlehbox = QHBoxLayout()
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.user_id_name)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.title_text)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.out)
        self.titlehbox.addStretch()
        
        self.title.setFixedSize(1250, 50)
        self.title.setLayout(self.titlehbox)
        self.title.setContentsMargins(0, 0, 0, 0)
    
    def set_menu(self):
        # 查询按钮
        print('menu test 1')
        self.menufont = QFont("微软雅黑", 15, QFont.Bold)
        
        self.bookSearch = QToolButton()
        self.bookSearch.setText('图书查询')
        self.bookSearch.setFont(self.menufont)
        self.bookSearch.setStyleSheet("color: black; background-color: white;")
        self.bookSearch.setFixedSize(200, 50)
        self.bookSearch.clicked.connect(lambda: self.switch(0))

        # 借阅信息
        self.student = QToolButton()
        self.student.setText('学生查询')
        self.student.setFont(self.menufont)
        self.student.setStyleSheet("color: black; background-color: white;")
        self.student.setFixedSize(200, 50)
        self.student.clicked.connect(lambda: self.switch(1))
        
        self.borrow = QToolButton()
        self.borrow.setText('借阅查询')
        self.borrow.setFont(self.menufont)
        self.borrow.setStyleSheet("color: black; background-color: white;")
        self.borrow.setFixedSize(200, 50)
        self.borrow.clicked.connect(lambda: self.switch(2))

        # 预约历史
        self.reserve = QToolButton()
        self.reserve.setText('预约信息')
        self.reserve.setFont(self.menufont)
        self.reserve.setStyleSheet("color: black; background-color: white;")
        self.reserve.setFixedSize(200, 50)
        self.reserve.setIconSize(QSize(30, 30))
        self.reserve.clicked.connect(lambda: self.switch(3))

        # 违期信息
        self.overdue = QToolButton()
        self.overdue.setText('违期信息')
        self.overdue.setFont(self.menufont)
        self.overdue.setStyleSheet("color: black; background-color: white;")
        self.overdue.setFixedSize(200, 50)
        self.overdue.clicked.connect(lambda: self.switch(4))


        book_pale = QLabel()
        book_pale.setFixedSize(200, 200)
        book_pixmap = QPixmap('icon/book.jpg')
        book_pale.setPixmap(book_pixmap)
        vbox1 = QVBoxLayout()
        vbox1.addStretch()
        vbox1.addWidget(book_pale)
        vbox1.addStretch()
        vbox1.addWidget(self.bookSearch)
        vbox1.addStretch()
        
        borrow_pale = QLabel()
        borrow_pale.setFixedSize(200, 200)
        borrow_pixmap = QPixmap('icon/borrow.jpg')
        borrow_pale.setPixmap(borrow_pixmap)
        vbox2 = QVBoxLayout()
        vbox2.addStretch()
        vbox2.addWidget(borrow_pale)
        vbox2.addStretch()
        vbox2.addWidget(self.borrow)
        vbox2.addStretch()
        
        reserve_pale = QLabel()
        reserve_pale.setFixedSize(200, 200)
        reserve_pixmap = QPixmap('icon/reserve.jpg')
        reserve_pale.setPixmap(reserve_pixmap)
        vbox3 = QVBoxLayout()
        vbox3.addStretch()
        vbox3.addWidget(reserve_pale)
        vbox3.addStretch()
        vbox3.addWidget(self.reserve)
        vbox3.addStretch()
        
        student_pale = QLabel()
        student_pale.setFixedSize(200, 200)
        student_pixmap = QPixmap('icon/student.jpg')
        student_pale.setPixmap(student_pixmap)
        vbox4 = QVBoxLayout()
        vbox4.addStretch()
        vbox4.addWidget(student_pale)
        vbox4.addStretch()
        vbox4.addWidget(self.student)
        vbox4.addStretch()
        
        overdue_pale = QLabel()
        overdue_pale.setFixedSize(250, 200)
        overdue_pixmap = QPixmap('icon/overdue.jpg')
        overdue_pale.setPixmap(overdue_pixmap)
        vbox5 = QVBoxLayout()
        vbox5.addStretch()
        vbox5.addWidget(overdue_pale)
        vbox5.addStretch()
        vbox5.addWidget(self.overdue)
        vbox5.addStretch()
        
        self.munelayout = QVBoxLayout()
        self.munelayout.addStretch()
        hbox1 = QHBoxLayout()
        hbox1.addStretch()
        hbox1.addLayout(vbox1)
        hbox1.addStretch()
        hbox1.addLayout(vbox2)
        hbox1.addStretch()
        hbox1.addLayout(vbox3)
        hbox1.addStretch()
        self.munelayout.addLayout(hbox1)
        self.munelayout.addStretch()
        hbox3 = QHBoxLayout()
        hbox3.addStretch()
        hbox3.addLayout(vbox4)
        hbox3.addStretch()
        hbox3.addLayout(vbox5)
        hbox3.addStretch()
        self.munelayout.addLayout(hbox3)
        self.munelayout.addStretch()
        self.munelayout.setContentsMargins(0, 0, 0, 0)
        self.munelayout.setSpacing(0)

       
        self.menu.setFixedSize(1250, 500)
        self.menu.setLayout(self.munelayout)
        self.menu.setContentsMargins(0, 0, 0, 0)

    def switch(self, index:int):
        self.page_index = index
        if index == 0:
            self.bookSearch.setStyleSheet("color: white; background-color: blue;")
            self.student.setStyleSheet("color: black; background-color: white;")
            self.borrow.setStyleSheet("color: black; background-color: white;")
            self.reserve.setStyleSheet("color: black; background-color: white;")
            self.overdue.setStyleSheet("color: black; background-color: white;")
        elif index == 1:
            self.bookSearch.setStyleSheet("color: black; background-color: white;")
            self.student.setStyleSheet("color: white; background-color: blue;")
            self.borrow.setStyleSheet("color: black; background-color: white;")
            self.reserve.setStyleSheet("color: black; background-color: white;")
            self.overdue.setStyleSheet("color: black; background-color: white;")
        elif index == 2:
            self.bookSearch.setStyleSheet("color: black; background-color: white;")
            self.student.setStyleSheet("color: black; background-color: white;")
            self.borrow.setStyleSheet("color: white; background-color: blue;")
            self.reserve.setStyleSheet("color: black; background-color: white;")
            self.overdue.setStyleSheet("color: black; background-color: white;")
        elif index == 3:
            self.bookSearch.setStyleSheet("color: black; background-color: white;")
            self.student.setStyleSheet("color: black; background-color: white;")
            self.borrow.setStyleSheet("color: black; background-color: white;")
            self.reserve.setStyleSheet("color: white; background-color: blue;")
            self.overdue.setStyleSheet("color: black; background-color: white;")
        elif index == 4:
            self.bookSearch.setStyleSheet("color: black; background-color: white;")
            self.student.setStyleSheet("color: black; background-color: white;")
            self.borrow.setStyleSheet("color: black; background-color: white;")
            self.reserve.setStyleSheet("color: black; background-color: white;")
            self.overdue.setStyleSheet("color: white; background-color: blue;")
        self.set_page()
        
    
    def set_page(self):
        if self.page_index == 0:
            self.page = Book(self.adm_info)
        elif self.page_index == 1:
            self.page = Student(self.adm_info)
        elif self.page_index == 2:
            self.page = Borrow(self.adm_info)
        elif self.page_index == 3:
            self.page = Reserve(self.adm_info)
        else:
            self.page = Overdue(self.adm_info)
        self.title.setVisible(False)
        self.menu.setVisible(False)
        self.body.addWidget(self.page)
        self.page.out.clicked.connect(self.back)
        
    def back(self):
        self.page.deleteLater()
        
        self.title.setVisible(True)
        self.menu.setVisible(True)
            
class Book(QWidget):
    def __init__(self, adm_info):
        super().__init__()
        print('book test 1')
        self.adm_info = adm_info
        self.init_page()
        
    def init_page(self):
        self.title = QWidget()
        self.set_title()
        self.menu = QWidget()
        self.set_menu()
        
        self.body = QVBoxLayout()
        self.body.addStretch()
        self.body.addWidget(self.title)
        self.body.addWidget(self.menu)
        self.table = None
        self.searchFunction()
        self.body.addStretch()
        
        #self.body.addLayout(self.table)
        self.wid = QWidget()
        self.wid.setLayout(self.body)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.wid)

        self.setStyleSheet("background-color: white;")
        self.setLayout(self.bodyLayout)
        
    def set_title(self):
        self.title_font = QFont("微软雅黑", 20, QFont.Bold)
        
        self.title_text = QLabel()
        self.title_text.setText('管理员图书信息查询')
        self.title_text.setFont(self.title_font)
        self.title_text.setStyleSheet("color: black; background-color: white;")
        self.title_text.setFixedHeight(40)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.adm_info[0] + self.adm_info[1] + '，欢迎！')
        self.user_id_name.setFont(self.title_font)
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(40)
        
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(self.title_font)
        self.out.setStyleSheet("color: black; background-color: white;")
        self.out.setFixedHeight(40)
        

        self.titlehbox = QHBoxLayout()
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.user_id_name)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.title_text)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.out)
        self.titlehbox.addStretch()
        
        self.title.setFixedSize(1250, 50)
        self.title.setLayout(self.titlehbox)
        self.title.setContentsMargins(0, 0, 0, 0)
        
    def set_menu(self):
        print('title test 2')
        self.select = QComboBox()
        self.select.addItems(['书号', '分类', '出版社', '作者', '书名'])
        #font = QFont("Arial", 15, QFont.Bold)
        #self.select.setFont(font)
        #self.search.setStyleSheet("color: black; background-color: white;")
        self.select.setFixedSize(60,30)
        
        self.prom = QLineEdit()
        self.prom.setText('')
        self.prom.setClearButtonEnabled(True)
        self.prom.setFixedSize(400, 40)
        
        self.search = QToolButton()
        self.search.setText('查询')
        self.search.setFixedSize(100, 40)
        font = QFont("Arial", 20, QFont.Bold)
        self.search.setFont(font)
        self.search.setStyleSheet("color: white; background-color: blue;")
        self.search.clicked.connect(self.searchFunction)
        
        self.addbook = QToolButton()
        self.addbook.setText('添加图书')
        self.addbook.setFixedSize(120, 40)
        font = QFont("Arial", 20, QFont.Bold)
        self.addbook.setFont(font)
        self.addbook.setStyleSheet("color: white; background-color: blue;")
        self.addbook.clicked.connect(lambda: self.addNewBookFunction())
        
        self.fresh = QToolButton()
        self.fresh.setText('刷新')
        self.fresh.setFixedSize(100, 40)
        font = QFont("Arial", 20, QFont.Bold)
        self.fresh.setFont(font)
        self.fresh.setStyleSheet("color: white; background-color: blue;")
        self.fresh.clicked.connect(self.refresh)
        
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.select)
        hbox.addWidget(self.prom)
        hbox.addWidget(self.search)
        hbox.addWidget(self.addbook)
        hbox.addWidget(self.fresh)
        hbox.addStretch()
        self.menu.setLayout(hbox)

    def searchFunction(self):
        print('search test 1')
        convert = {'书号': 'bno', '分类': 'class', '出版社': 'press', '作者': 'author', '书名': 'bname'}
        self.book_list = function.search_book(self.prom.text(), convert[self.select.currentText()], '')
        if self.book_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.set_table()
        
    def set_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.table.setRowCount(0)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['书号', '书名', '作者','出版日期', '出版社', '分类', '语言', '总数', '剩余', '操作'])  # 设置表头
        self.table.horizontalHeader().setStyleSheet("color: black;")
        self.table.horizontalHeader().setFont(QFont("微软雅黑", 15, QFont.Bold))
        
        self.table.setColumnWidth(0, 110)
        self.table.setColumnWidth(1, 110)
        self.table.setColumnWidth(2, 110)
        self.table.setColumnWidth(3, 110)
        self.table.setColumnWidth(4, 110)
        self.table.setColumnWidth(5, 110)
        self.table.setColumnWidth(6, 110)
        self.table.setColumnWidth(7, 110)
        self.table.setColumnWidth(8, 110)
        self.table.setColumnWidth(9, 110)
        
        for val in self.book_list:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setRowHeight(row, 45)

            for j in range(9):
                string_item = str(val[j])
                if j == 1:
                    string_item = "《" + str(val[j]) + "》"
                item = QTableWidgetItem(string_item)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("微软雅黑", 10))
                self.table.setItem(row, j, item)
            self.oprate_func(val, row)
            
        self.body.addWidget(self.table)
            
    def oprate_func(self,val, row):
        mod_item = QToolButton()
        mod_item.setFixedSize(50, 35)
        mod_item.setText('修改')
        mod_item.setStyleSheet("color: white; background: blue;")
        mod_item.clicked.connect(lambda: self.updateBookFunction(val[0]))
        mod_item.setFont(QFont("微软雅黑", 15))
            
        del_item = QToolButton()
        del_item.setFixedSize(50, 35)
        del_item.setText('删除')
        del_item.setStyleSheet("color: white; background: red;")
        del_item.clicked.connect(lambda: self.deleteBookFunction(val[0]))
        del_item.setFont(QFont("微软雅黑", 15))
                
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(mod_item)
        hbox.addWidget(del_item)
        hbox.addStretch()
        table_wid = QWidget()
        table_wid.setLayout(hbox)
        self.table.setCellWidget(row, 9, table_wid)
            
    def updateBookFunction(self, bno: str):
        self.updateBookDialog = book_information.BookInfo(bno)
        self.updateBookDialog.show()
        self.updateBookDialog.register_button.clicked.connect(self.updateBookDialog.register)

    def addNewBookFunction(self):
        self.newBookDialog = add_book.add_book()
        self.newBookDialog.show()
        self.newBookDialog.register_button.clicked.connect(self.newBookDialog.register)
        self.newBookDialog.back_button.clicked.connect(self.newBookDialog.close)

    def deleteBookFunction(self, bno: str):
        msgBox = QMessageBox(QMessageBox.Warning, "警告!", '您将会永久删除这本书以及相关信息!',
                             QMessageBox.NoButton, self)
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.addButton("取消", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.AcceptRole:
            ans = function.delete_book(bno)
            if ans:
                self.searchFunction()
                
    def refresh(self):
        self.searchFunction()
        
class Student(QWidget):
    def __init__(self, adm_info):
        super().__init__()
        self.adm_info = adm_info
        self.init_page()
        
    def init_page(self):
        print("student page test 1")
        self.title = QWidget()
        self.set_title()
        self.menu = QWidget()
        self.set_menu()
        
        self.body = QVBoxLayout()
        self.body.addStretch()
        self.body.addWidget(self.title)
        self.body.addWidget(self.menu)
        self.table = None
        self.searchFunction()
        self.body.addStretch()
        
        #self.body.addLayout(self.table)
        self.wid = QWidget()
        self.wid.setLayout(self.body)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.wid)

        self.setStyleSheet("background-color: white;")
        self.setLayout(self.bodyLayout)
        
    def set_title(self):
        self.title_font = QFont("微软雅黑", 20, QFont.Bold)
        
        self.title_text = QLabel()
        self.title_text.setText('管理员学生信息查询')
        self.title_text.setFont(self.title_font)
        self.title_text.setStyleSheet("color: black; background-color: white;")
        self.title_text.setFixedHeight(40)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.adm_info[0] + self.adm_info[1] + '，欢迎！')
        self.user_id_name.setFont(self.title_font)
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(40)
        
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(self.title_font)
        self.out.setStyleSheet("color: black; background-color: white;")
        self.out.setFixedHeight(40)
        

        self.titlehbox = QHBoxLayout()
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.user_id_name)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.title_text)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.out)
        self.titlehbox.addStretch()
        
        self.title.setFixedSize(1250, 50)
        self.title.setLayout(self.titlehbox)
        self.title.setContentsMargins(0, 0, 0, 0)
        
    def set_menu(self):
        print("student menu test 1")
        self.select = QComboBox()
        self.select.addItems(['学号', '姓名', '学院', '年龄', '性别'])
        font = QFont("Arial", 15, QFont.Bold)
        #self.select.setFont(font)
        #self.search.setStyleSheet("color: black; background-color: white;")
        self.select.setFixedSize(60,30)
        
        self.prom = QLineEdit()
        self.prom.setText('')
        self.prom.setClearButtonEnabled(True)
        self.prom.setFixedSize(400, 40)
        
        self.addstudent = QToolButton()
        self.addstudent.setText('添加学生')
        self.addstudent.setFixedSize(120, 40)
        font = QFont("Arial", 20, QFont.Bold)
        self.addstudent.setFont(font)
        self.addstudent.setStyleSheet("color: white; background-color: blue;")
        self.addstudent.clicked.connect(lambda: self.addNewStudentFunction())
        
        self.fresh = QToolButton()
        self.fresh.setText('刷新')
        self.fresh.setFixedSize(100, 40)
        font = QFont("Arial", 20, QFont.Bold)
        self.fresh.setFont(font)
        self.fresh.setStyleSheet("color: white; background-color: blue;")
        self.fresh.clicked.connect(self.refresh)
        
        self.search = QToolButton()
        self.search.setText('查询')
        self.search.setFixedSize(100, 40)
        font = QFont("Arial", 20, QFont.Bold)
        self.search.setFont(font)
        self.search.setStyleSheet("color: white; background-color: blue;")
        self.search.clicked.connect(self.searchFunction)
        
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.select)
        hbox.addWidget(self.prom)
        hbox.addWidget(self.addstudent)
        hbox.addWidget(self.fresh)
        hbox.addWidget(self.search)
        hbox.addStretch()
        self.menu.setLayout(hbox)

    def searchFunction(self):
        convert = {'学号': 'sno', '姓名': 'sname', '学院': 'dept', '年龄':'age', '性别':'sex'}
        self.stu_list = function.search_student(self.prom.text(), convert[self.select.currentText()])
        if self.stu_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.set_table()
        
    def set_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['学号', '姓名', '学院','年龄', '性别', '操作'])  # 设置表头
        self.table.horizontalHeader().setStyleSheet("color: black;")
        self.table.horizontalHeader().setFont(QFont("微软雅黑", 20, QFont.Bold))
        
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 175)
        self.table.setColumnWidth(4, 175)
        self.table.setColumnWidth(5, 175)
        
        for val in self.stu_list:
            row = self.table.rowCount()
            self.table.insertRow(row)

            for j in range(5):
                if val[j] is None:
                    string_item = 'NULL'
                else:
                    string_item = str(val[j])
                item = QTableWidgetItem(string_item)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("微软雅黑", 15))
                self.table.setItem(row, j, item)
            self.oprate_func(val, row)
                
        self.body.addWidget(self.table)
        
    def oprate_func(self,val, row):
        mod_item = QToolButton()
        mod_item.setFixedSize(50, 35)
        mod_item.setText('修改')
        mod_item.setStyleSheet("color: white; background: blue;")
        mod_item.clicked.connect(lambda: self.updateFunction(val[0]))
        mod_item.setFont(QFont("微软雅黑", 15))
            
        del_item = QToolButton()
        del_item.setFixedSize(50, 35)
        del_item.setText('删除')
        del_item.setStyleSheet("color: white; background: red;")
        del_item.clicked.connect(lambda: self.deleteFunction(val[0]))
        del_item.setFont(QFont("微软雅黑", 15))
                
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(mod_item)
        hbox.addWidget(del_item)
        hbox.addStretch()
        table_wid = QWidget()
        table_wid.setLayout(hbox)
        self.table.setCellWidget(row, 5, table_wid)
        
    def updateFunction(self, sno: str):
        self.updateDialog = mod_student.mod_stu(sno)
        self.updateDialog.show()
        self.updateDialog.register_button.clicked.connect(self.updateDialog.register)

    def deleteFunction(self, sno: str):
        msgBox = QMessageBox(QMessageBox.Warning, "警告!", '您将会永久删除这位学生以及相关信息!',
                             QMessageBox.NoButton, self)
        msgBox.addButton("确认", QMessageBox.AcceptRole)
        msgBox.addButton("取消", QMessageBox.RejectRole)
        if msgBox.exec_() == QMessageBox.AcceptRole:
            ans = function.delete_student(sno)
            if ans:
                self.searchFunction()
        
    def addNewStudentFunction(self):
        self.newStudentDialog = add_student.Signup()
        self.newStudentDialog.show()
        self.newStudentDialog.register_button.clicked.connect(self.newStudentDialog.register)
        self.newStudentDialog.back_button.clicked.connect(self.newStudentDialog.close)
        
    def refresh(self):
        self.searchFunction()
        
    
                

class Borrow(QWidget):
    def __init__(self, adm_info):
        super().__init__()
        self.adm_info = adm_info
        self.init_page()
        
    def init_page(self):
        self.title = QWidget()
        self.set_title()
        self.menu = QWidget()
        self.set_menu()
        
        self.body = QVBoxLayout()
        self.body.addStretch()
        self.body.addWidget(self.title)
        self.body.addWidget(self.menu)
        self.table = None
        self.searchFunction()
        self.body.addStretch()
        
        #self.body.addLayout(self.table)
        self.wid = QWidget()
        self.wid.setLayout(self.body)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.wid)

        self.setStyleSheet("background-color: white;")
        self.setLayout(self.bodyLayout)
        
    def set_title(self):
        self.title_font = QFont("微软雅黑", 20, QFont.Bold)
        
        self.title_text = QLabel()
        self.title_text.setText('管理员借阅信息查询')
        self.title_text.setFont(self.title_font)
        self.title_text.setStyleSheet("color: black; background-color: white;")
        self.title_text.setFixedHeight(40)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.adm_info[0] + self.adm_info[1] + '，欢迎！')
        self.user_id_name.setFont(self.title_font)
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(40)
        
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(self.title_font)
        self.out.setStyleSheet("color: black; background-color: white;")
        self.out.setFixedHeight(40)
        

        self.titlehbox = QHBoxLayout()
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.user_id_name)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.title_text)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.out)
        self.titlehbox.addStretch()
        
        self.title.setFixedSize(1250, 50)
        self.title.setLayout(self.titlehbox)
        self.title.setContentsMargins(0, 0, 0, 0)
        
    def set_menu(self):
        print("adm borrow 2")
        self.select = QComboBox()
        self.select.addItems(['书号','学号', '书名', '姓名'])
        font = QFont("Arial", 15, QFont.Bold)
        #self.select.setFont(font)
        #self.search.setStyleSheet("color: black; background-color: white;")
        self.select.setFixedSize(60,30)
        
        self.prom = QLineEdit()
        self.prom.setText('')
        self.prom.setClearButtonEnabled(True)
        self.prom.setFixedSize(400, 40)
        
        self.search = QToolButton()
        self.search.setText('查询')
        self.search.setFixedSize(100, 40)
        font = QFont("Arial", 20, QFont.Bold)
        self.search.setFont(font)
        self.search.setStyleSheet("color: white; background-color: blue;")
        self.search.clicked.connect(self.searchFunction)
        
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.select)
        hbox.addWidget(self.prom)
        hbox.addWidget(self.search)
        hbox.addStretch()
        self.menu.setLayout(hbox)

    def searchFunction(self):
        print("adm borrow test 1")
        convert = {'书号': 'bno', '学号': 'sno', '书名': 'bname', '姓名': 'sname'}
        self.borrow_list = function.borrow_log(self.prom.text(), convert[self.select.currentText()])
        if self.borrow_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.set_table()
        
    def set_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['书号', '书名', '学号','姓名', '借阅日期', '还书日期'])  # 设置表头
        self.table.horizontalHeader().setStyleSheet("color: black;")
        self.table.horizontalHeader().setFont(QFont("微软雅黑", 15, QFont.Bold))
        
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 175)
        self.table.setColumnWidth(4, 175)
        self.table.setColumnWidth(5, 175)
        
        for val in self.borrow_list:
            row = self.table.rowCount()
            self.table.insertRow(row)

            for j in range(6):
                if val[j] is None:
                    string_item = 'NULL'
                else:
                    string_item = str(val[j])
                item = QTableWidgetItem(string_item)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("微软雅黑", 10))
                self.table.setItem(row, j, item)
                
        self.body.addWidget(self.table)

class Reserve(QWidget):
    def __init__(self, adm_info):
        super().__init__()
        self.adm_info = adm_info
        self.init_page()
        
    def init_page(self):
        self.title = QWidget()
        self.set_title()
        self.menu = QWidget()
        self.set_menu()
        
        self.body = QVBoxLayout()
        self.body.addStretch()
        self.body.addWidget(self.title)
        self.body.addWidget(self.menu)
        self.table = None
        self.searchFunction()
        self.body.addStretch()
        
        #self.body.addLayout(self.table)
        self.wid = QWidget()
        self.wid.setLayout(self.body)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.wid)

        self.setStyleSheet("background-color: white;")
        self.setLayout(self.bodyLayout)
        
    def set_title(self):
        self.title_font = QFont("微软雅黑", 20, QFont.Bold)
        
        self.title_text = QLabel()
        self.title_text.setText('管理员预约信息查询')
        self.title_text.setFont(self.title_font)
        self.title_text.setStyleSheet("color: black; background-color: white;")
        self.title_text.setFixedHeight(40)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.adm_info[0] + self.adm_info[1] + '，欢迎！')
        self.user_id_name.setFont(self.title_font)
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(40)
        
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(self.title_font)
        self.out.setStyleSheet("color: black; background-color: white;")
        self.out.setFixedHeight(40)
        

        self.titlehbox = QHBoxLayout()
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.user_id_name)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.title_text)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.out)
        self.titlehbox.addStretch()
        
        self.title.setFixedSize(1250, 50)
        self.title.setLayout(self.titlehbox)
        self.title.setContentsMargins(0, 0, 0, 0)
        
    def set_menu(self):
        self.select = QComboBox()
        self.select.addItems(['书号','学号', '书名', '姓名'])
        font = QFont("Arial", 15, QFont.Bold)
        #self.select.setFont(font)
        #self.search.setStyleSheet("color: black; background-color: white;")
        self.select.setFixedSize(60,30)
        
        self.prom = QLineEdit()
        self.prom.setText('')
        self.prom.setClearButtonEnabled(True)
        self.prom.setFixedSize(400, 40)
        
        self.search = QToolButton()
        self.search.setText('查询')
        self.search.setFixedSize(100, 40)
        font = QFont("Arial", 20, QFont.Bold)
        self.search.setFont(font)
        self.search.setStyleSheet("color: white; background-color: blue;")
        self.search.clicked.connect(self.searchFunction)
        
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.select)
        hbox.addWidget(self.prom)
        hbox.addWidget(self.search)
        hbox.addStretch()
        self.menu.setLayout(hbox)

    def searchFunction(self):
        convert = {'书号': 'bno', '学号': 'sno', '书名': 'bname', '姓名': 'sname'}
        self.reserve_list = function.reserve_log(self.prom.text(), convert[self.select.currentText()])
        if self.reserve_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.set_table()
        
    def set_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['书号', '书名', '学号','姓名', '预约日期', '取书日期'])  # 设置表头
        self.table.horizontalHeader().setStyleSheet("color: black;")
        self.table.horizontalHeader().setFont(QFont("微软雅黑", 15, QFont.Bold))
        
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 175)
        self.table.setColumnWidth(4, 175)
        self.table.setColumnWidth(5, 175)
        
        for val in self.reserve_list:
            row = self.table.rowCount()
            self.table.insertRow(row)

            for j in range(6):
                if val[j] is None:
                    string_item = 'NULL'
                else:
                    string_item = str(val[j])
                item = QTableWidgetItem(string_item)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("微软雅黑", 10))
                self.table.setItem(row, j, item)
        
        self.body.addWidget(self.table)

class Overdue(QWidget):
    def __init__(self, adm_info):
        super().__init__()
        self.adm_info = adm_info
        self.init_page()
        
    def init_page(self):
        self.title = QWidget()
        self.set_title()
        self.menu = QWidget()
        self.set_menu()
        
        self.body = QVBoxLayout()
        self.body.addStretch()
        self.body.addWidget(self.title)
        self.body.addWidget(self.menu)
        self.table = None
        self.searchFunction()
        self.body.addStretch()
        
        #self.body.addLayout(self.table)
        self.wid = QWidget()
        self.wid.setLayout(self.body)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.wid)

        self.setStyleSheet("background-color: white;")
        self.setLayout(self.bodyLayout)
        
    def set_title(self):
        self.title_font = QFont("微软雅黑", 20, QFont.Bold)
        
        self.title_text = QLabel()
        self.title_text.setText('管理员违期信息查询')
        self.title_text.setFont(self.title_font)
        self.title_text.setStyleSheet("color: black; background-color: white;")
        self.title_text.setFixedHeight(40)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.adm_info[0] + self.adm_info[1] + '，欢迎！')
        self.user_id_name.setFont(self.title_font)
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(40)
        
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(self.title_font)
        self.out.setStyleSheet("color: black; background-color: white;")
        self.out.setFixedHeight(40)
        

        self.titlehbox = QHBoxLayout()
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.user_id_name)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.title_text)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.out)
        self.titlehbox.addStretch()
        
        self.title.setFixedSize(1250, 50)
        self.title.setLayout(self.titlehbox)
        self.title.setContentsMargins(0, 0, 0, 0)
        
    def set_menu(self):
        self.select = QComboBox()
        self.select.addItems(['书号','学号', '书名', '姓名'])
        font = QFont("Arial", 15, QFont.Bold)
        #self.select.setFont(font)
        #self.search.setStyleSheet("color: black; background-color: white;")
        self.select.setFixedSize(60,30)
        
        self.prom = QLineEdit()
        self.prom.setText('')
        self.prom.setClearButtonEnabled(True)
        self.prom.setFixedSize(400, 40)
        
        self.search = QToolButton()
        self.search.setText('查询')
        self.search.setFixedSize(100, 40)
        font = QFont("Arial", 20, QFont.Bold)
        self.search.setFont(font)
        self.search.setStyleSheet("color: white; background-color: blue;")
        self.search.clicked.connect(self.searchFunction)
        
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(self.select)
        hbox.addWidget(self.prom)
        hbox.addWidget(self.search)
        hbox.addStretch()
        self.menu.setLayout(hbox)

    def searchFunction(self):
        convert = {'书号': 'bno', '学号': 'sno', '书名': 'bname', '姓名': 'sname'}
        self.overdue_list = function.overdue_log(self.prom.text(), convert[self.select.currentText()])
        if self.overdue_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.set_table()
        
    def set_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['书号', '书名', '学号','姓名', '借阅日期', '还书日期', '违期显示'])  # 设置表头
        self.table.horizontalHeader().setStyleSheet("color: black;")
        self.table.horizontalHeader().setFont(QFont("微软雅黑", 15, QFont.Bold))
        
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 175)
        self.table.setColumnWidth(4, 175)
        self.table.setColumnWidth(5, 175)
        self.table.setColumnWidth(6, 175)
        
        for val in self.overdue_list:
            row = self.table.rowCount()
            self.table.insertRow(row)

            for j in range(6):
                if val[j] is None:
                    string_item = 'NULL'
                else:
                    string_item = str(val[j])
                item = QTableWidgetItem(string_item)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("微软雅黑", 10))
                self.table.setItem(row, j, item)
            self.opreate_func(val, row)
        
        self.body.addWidget(self.table)
        
    def opreate_func(self, val, row):
        oprate_item = QToolButton()
        oprate_item.setFixedSize(70, 35)
        oprate_item.setText('违期')
        oprate_item.setEnabled(False)
        oprate_item.setStyleSheet("color: white; background: red;")
        oprate_item.setFont(QFont("微软雅黑", 15))
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(oprate_item)
        hbox.addStretch()
        table_wid = QWidget()
        table_wid.setLayout(hbox)
        self.table.setCellWidget(row, 6, table_wid)