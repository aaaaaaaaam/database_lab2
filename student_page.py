import sys
import time
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QGroupBox,
                             QToolButton, QSplitter, QVBoxLayout, QHBoxLayout,
                             QLabel, QTableWidget, QTableWidgetItem, QAbstractItemView,
                             QLineEdit, QFileDialog, QToolTip, QComboBox)
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
import function
import datetime
import change_reserve
# import func

class StudentPage(QWidget):
    def __init__(self, student_info):
        super().__init__()
        self.student_info = student_info
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
        self.title_text = QLabel()
        self.title_text.setText('欢迎使用图书管理系统')
        self.title_text.setFont(QFont("微软雅黑", 16, QFont.Bold))
        self.title_text.setStyleSheet("color: black; background-color: white;")
        self.title_text.setFixedHeight(40)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.student_info[0] + self.student_info[1] + '，欢迎！')
        self.user_id_name.setFont(QFont("微软雅黑", 16, QFont.Bold))
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(40)
        
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(QFont("微软雅黑", 16, QFont.Bold))
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
        self.menufont = QFont("微软雅黑", 15, QFont.Bold)
        
        self.bookSearch = QToolButton()
        self.bookSearch.setText('图书查询')
        self.bookSearch.setFont(self.menufont)
        self.bookSearch.setStyleSheet("color: black; background-color: white;")
        self.bookSearch.setFixedSize(250, 50)
        self.bookSearch.clicked.connect(lambda: self.switch(0))

        # 借阅信息
        self.borrow = QToolButton()
        self.borrow.setText('借阅信息')
        self.borrow.setFont(self.menufont)
        self.borrow.setStyleSheet("color: black; background-color: white;")
        self.borrow.setFixedSize(250, 50)
        self.borrow.clicked.connect(lambda: self.switch(1))

        # 预约历史
        self.reserve = QToolButton()
        self.reserve.setText('预约信息')
        self.reserve.setFont(self.menufont)
        self.reserve.setStyleSheet("color: black; background-color: white;")
        self.reserve.setFixedSize(250, 50)
        self.reserve.clicked.connect(lambda: self.switch(2))
    
        # 个人信息
        self.person = QToolButton()
        self.person.setText('个人信息')
        self.person.setFont(self.menufont)
        self.person.setStyleSheet("color: black; background-color: white;")
        self.person.setFixedSize(250, 50)
        self.person.clicked.connect(lambda: self.switch(3))

        book_pale = QLabel()
        book_pale.setFixedSize(250, 200)
        book_pixmap = QPixmap('icon/book.jpg')
        book_pale.setPixmap(book_pixmap)
        vbox1 = QVBoxLayout()
        vbox1.addStretch()
        vbox1.addWidget(book_pale)
        vbox1.addStretch()
        vbox1.addWidget(self.bookSearch)
        vbox1.addStretch()
        
        borrow_pale = QLabel()
        borrow_pale.setFixedSize(250, 200)
        borrow_pixmap = QPixmap('icon/borrow.jpg')
        borrow_pale.setPixmap(borrow_pixmap)
        vbox2 = QVBoxLayout()
        vbox2.addStretch()
        vbox2.addWidget(borrow_pale)
        vbox2.addStretch()
        vbox2.addWidget(self.borrow)
        vbox2.addStretch()
        
        reserve_pale = QLabel()
        reserve_pale.setFixedSize(250, 200)
        reserve_pixmap = QPixmap('icon/reserve.jpg')
        reserve_pale.setPixmap(reserve_pixmap)
        vbox3 = QVBoxLayout()
        vbox3.addStretch()
        vbox3.addWidget(reserve_pale)
        vbox3.addStretch()
        vbox3.addWidget(self.reserve)
        vbox3.addStretch()
        
        person_pale = QLabel()
        person_pale.setFixedSize(250, 200)
        person_pixmap = QPixmap('icon/student.jpg')
        person_pale.setPixmap(person_pixmap)
        vbox4 = QVBoxLayout()
        vbox4.addStretch()
        vbox4.addWidget(person_pale)
        vbox4.addStretch()
        vbox4.addWidget(self.person)
        vbox4.addStretch()
        
        self.munelayout = QVBoxLayout()
        self.munelayout.addStretch()
        hbox1 = QHBoxLayout()
        hbox1.addStretch()
        hbox1.addLayout(vbox1)
        hbox1.addStretch()
        hbox1.addLayout(vbox2)
        hbox1.addStretch()
        self.munelayout.addLayout(hbox1)
        self.munelayout.addStretch()
        hbox3 = QHBoxLayout()
        hbox3.addStretch()
        hbox3.addLayout(vbox3)
        hbox3.addStretch()
        hbox3.addLayout(vbox4)
        hbox3.addStretch()
        self.munelayout.addLayout(hbox3)
        self.munelayout.addStretch()
        self.munelayout.setContentsMargins(0, 0, 0, 0)
        self.munelayout.setSpacing(0)

        self.menu.setFixedSize(1250, 500)
        self.menu.setLayout(self.munelayout)
        self.menu.setContentsMargins(0, 0, 0, 0)

    def switch(self, index:int):
        print('switch 1')
        self.page_index = index
        if index == 0:
            print('switch 2')
            self.bookSearch.setStyleSheet("color: white; background-color: blue;")
            self.borrow.setStyleSheet("color: black; background-color: white;")
            self.reserve.setStyleSheet("color: black; background-color: white;")
            self.person.setStyleSheet("color: black; background-color: white;")
        elif index == 1:
            print('switch 3')
            self.bookSearch.setStyleSheet("color: black; background-color: white;")
            self.borrow.setStyleSheet("color: white; background-color: blue;")
            self.reserve.setStyleSheet("color: black; background-color: white;")
            self.person.setStyleSheet("color: black; background-color: white;")
        elif index == 2:
            print('switch 4')
            self.bookSearch.setStyleSheet("color: black; background-color: white;")
            self.borrow.setStyleSheet("color: black; background-color: white;")
            self.reserve.setStyleSheet("color: white; background-color: blue;")
            self.person.setStyleSheet("color: black; background-color: white;")
        elif index == 3:
            print('switch 5')
            self.bookSearch.setStyleSheet("color: black; background-color: white;")
            self.borrow.setStyleSheet("color: black; background-color: white;")
            self.reserve.setStyleSheet("color: black; background-color: white;")
            self.person.setStyleSheet("color: white; background-color: blue;")
        self.set_page()
        
    def set_page(self):
        if self.page_index == 0:
            self.page = Book(self.student_info)
        elif self.page_index == 1:
            self.page = Borrow(self.student_info)
        elif self.page_index == 2:
            self.page = Reserve(self.student_info)
        else:
            self.page = Person(self.student_info)
        self.title.setVisible(False)
        self.menu.setVisible(False)
        self.body.addWidget(self.page)
        self.page.out.clicked.connect(self.back)
        
    def back(self):
        self.page.deleteLater()
        
        self.title.setVisible(True)
        self.menu.setVisible(True)
            
class Book(QWidget):
    def __init__(self, student_info):
        super().__init__()
        self.student_info = student_info
        print('borrow test 1')
        self.init_page()
        
    def init_page(self):
        self.title = QWidget()
        print('borrow test 2')
        self.set_title()
        self.menu = QWidget()
        print('borrow test 3')
        self.set_menu()
        
        self.body = QVBoxLayout()
        self.body.addStretch()
        self.body.addWidget(self.title)
        self.body.addWidget(self.menu)
        self.table = None
        print('borrow test 4')
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
        self.title_text.setText('图书信息查阅')
        self.title_text.setFont(self.title_font)
        self.title_text.setStyleSheet("color: black;")
        self.title_text.setFixedHeight(50)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.student_info[0] + self.student_info[1] + '，欢迎！')
        self.user_id_name.setFont(QFont("微软雅黑", 16, QFont.Bold))
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(50)
        
        print('title test 3')
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(QFont("微软雅黑", 16, QFont.Bold))
        self.out.setStyleSheet("color: black; background-color: white;")
        self.out.setFixedHeight(50)
        
        
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
        self.title.setStyleSheet("background-color: rgba(216, 216, 216, 1);")
        self.title.setContentsMargins(0, 0, 0, 0)
        
    def set_menu(self):
        print('menu test 1')
        self.select = QComboBox()
        self.select.addItems(['书号', '分类', '出版社', '作者', '书名'])
        font = QFont("微软雅黑", 15, QFont.Bold)
        self.select.setFixedSize(60,30)
        
        self.prom = QLineEdit()
        self.prom.setText('')
        self.prom.setClearButtonEnabled(True)
        self.prom.setFixedSize(400, 40)
        
        self.search = QToolButton()
        self.search.setText('查询')
        self.search.setFixedSize(100, 40)
        font = QFont("微软雅黑", 20, QFont.Bold)
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
        convert = {'书号': 'bno', '分类': 'class', '出版社': 'press', '作者': 'author', '书名': 'bname'}
        self.book_list = function.search_book(self.prom.text(), convert[self.select.currentText()], self.student_info[0])
        if self.book_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        self.set_table()
        
    def set_table(self):
        self.table = QTableWidget(0, 10)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['书号', '书名', '作者','出版日期', '出版社', '分类', '语言', '总数', '剩余', '操作'])  # 设置表头
        self.table.horizontalHeader().setStyleSheet("color: black;")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.horizontalHeader().setFont(QFont("微软雅黑", 15, QFont.Bold))
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.setMaximumHeight(40 * 10)
        
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 100)
        self.table.setColumnWidth(4, 100)
        self.table.setColumnWidth(5, 100)
        self.table.setColumnWidth(6, 100)
        self.table.setColumnWidth(7, 100)
        self.table.setColumnWidth(8, 100)
        self.table.setColumnWidth(9, 100)
        
        for val in self.book_list:
            row = self.table.rowCount()
            print(row)
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
            self.opreate_func(val, row)
            
        self.body.addWidget(self.table)
        
    def opreate_func(self, val, row):
        oprate_item = QToolButton()
        oprate_item.setFixedSize(70, 35)
        if val[-1] == '借书':
            oprate_item.setText('借书')
            oprate_item.clicked.connect(lambda: self.borrowBook(val[0]))
            oprate_item.setStyleSheet("color: white; background: green;")
            oprate_item.setFont(QFont("微软雅黑", 15))
        elif val[-1] == '预约':
            oprate_item.setText('预约')
            print(val[0])
            oprate_item.clicked.connect(lambda: self.reserveBook(val[0]))
            oprate_item.setStyleSheet("color: white; background: yellow;")
            oprate_item.setFont(QFont("微软雅黑", 15))
        else:
            oprate_item.setText('不能借')
            oprate_item.setEnabled(False)
            oprate_item.setStyleSheet("color: white; background: red;")
            oprate_item.setFont(QFont("微软雅黑", 15))
                
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(oprate_item)
        hbox.addStretch()
        table_wid = QWidget()
        table_wid.setLayout(hbox)
        self.table.setCellWidget(row, 9, table_wid)
            
            
    def borrowBook(self, bno: str):
        ans = function.borrow_book(bno, self.student_info[0])
        # 刷新表格
        if ans:
            self.searchFunction()
            
    def reserveBook(self, bno: str):
        ans = function.reserve_book(bno, self.student_info[0])
        # 刷新表格
        if ans:
            self.searchFunction()
            
        
class Borrow(QWidget):
    def __init__(self, student_info):
        super().__init__()
        self.student_info = student_info
        print('borrow 1')
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
        print('borrow 2')
        self.searchFunction()
        self.body.addStretch()
        
        self.wid = QWidget()
        self.wid.setLayout(self.body)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.wid)

        self.setStyleSheet("background-color: white;")
        self.setLayout(self.bodyLayout)
        
    def set_title(self):
        self.title_font = QFont("微软雅黑", 20, QFont.Bold)
        
        self.title_text = QLabel()
        self.title_text.setText('图书借阅信息')
        self.title_text.setFont(self.title_font)
        self.title_text.setStyleSheet("color: black;")
        self.title_text.setFixedHeight(50)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.student_info[0] + self.student_info[1] + '，欢迎！')
        self.user_id_name.setFont(QFont("微软雅黑", 16, QFont.Bold))
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(50)
        
        print('title test 3')
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(QFont("微软雅黑", 16, QFont.Bold))
        self.out.setStyleSheet("color: black; background-color: white;")
        self.out.setFixedHeight(50)
        
        
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
        self.title.setStyleSheet("background-color: rgba(216, 216, 216, 1);")
        self.title.setContentsMargins(0, 0, 0, 0)
        
    def set_menu(self):
        self.select = QComboBox()
        self.select.addItems(['书号', '书名', '借阅日期'])
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
        font = QFont("微软雅黑", 20, QFont.Bold)
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
        convert = {'书号': 'bno', '书名': 'bname', '借阅日期': 'borrow_date'}
        self.borrow_list = function.get_borrowing_books(self.prom.text(), convert[self.select.currentText()], self.student_info[0])
        if self.borrow_list == []:
            print('未找到')
        if self.table is not None:
            self.table.deleteLater()
        print("borrow 3")
        self.set_table()
        
    def set_table(self):
        print("borrow 4")
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setRowCount(0)
        self.table.setContentsMargins(10, 10, 10, 10)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['书号', '书名', '借阅日期','还书日期', '违期', '操作'])  # 设置表头
        self.table.horizontalHeader().setStyleSheet("color: black;")
        self.table.horizontalHeader().setFont(QFont("微软雅黑", 15, QFont.Bold))
        
        print("borrow 5")
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        
        print("borrow 6")
        for val in self.borrow_list:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setRowHeight(row, 45)

            for j in range(5):
                print(j)
                if val[j] is None:
                    string_item = 'NULL'
                else:
                    string_item = str(val[j])
                item = QTableWidgetItem(string_item)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFont(QFont("微软雅黑", 10))
                self.table.setItem(row, j, item)
            self.opearte_func(val, row)
            
        print("before")
        self.body.addWidget(self.table)
        print("finish")
        
    def opearte_func(self, val, row):
        print("borrow 7")
        oprate_item = QToolButton()
        oprate_item.setFixedSize(70, 35)
        if val[3] is None:
            print("borrow 8")
            oprate_item.setText('还书')
            oprate_item.clicked.connect(lambda: self.retrurnBook(val[0], val[2]))
            oprate_item.setStyleSheet("color: white; background: green;")
            oprate_item.setFont(QFont("微软雅黑", 15))
        else:
            print("borrow 9")
            oprate_item.setText('还书')
            oprate_item.setEnabled(False)
            oprate_item.setStyleSheet("color: white; background: red;")
            oprate_item.setFont(QFont("微软雅黑", 15))
                
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(oprate_item)
        hbox.addStretch()
        table_wid = QWidget()
        table_wid.setLayout(hbox)
        self.table.setCellWidget(row, 5, table_wid)
            
    def retrurnBook(self, bno: str, b_date:datetime.date):
        ans = function.return_book(bno, self.student_info[0], b_date)
        # 刷新表格
        if ans:
            self.searchFunction()

class Reserve(QWidget):
    def __init__(self, student_info):
        super().__init__()
        self.student_info = student_info
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
        
        self.wid = QWidget()
        self.wid.setLayout(self.body)
        self.bodyLayout = QGridLayout()#布局管理器
        self.bodyLayout.addWidget(self.wid)

        self.setStyleSheet("background-color: white;")
        self.setLayout(self.bodyLayout)

        
    def set_title(self):
        self.title_font = QFont("微软雅黑", 20, QFont.Bold)
        
        self.title_text = QLabel()
        self.title_text.setText('图书预约信息')
        self.title_text.setFont(self.title_font)
        self.title_text.setStyleSheet("color: black;")
        self.title_text.setFixedHeight(50)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.student_info[0] + self.student_info[1] + '，欢迎！')
        self.user_id_name.setFont(QFont("微软雅黑", 16, QFont.Bold))
        self.user_id_name.setStyleSheet("color: black; background-color: white;")
        self.user_id_name.setFixedHeight(50)
        
        print('title test 3')
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setFont(QFont("微软雅黑", 16, QFont.Bold))
        self.out.setStyleSheet("color: black; background-color: white;")
        self.out.setFixedHeight(50)
        
        
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
        self.title.setStyleSheet("background-color: rgba(216, 216, 216, 1);")
        self.title.setContentsMargins(0, 0, 0, 0)
        
    def set_menu(self):
        self.select = QComboBox()
        self.select.addItems(['书号', '书名', '预约日期'])
        font = QFont("Arial", 15, QFont.Bold)
        self.select.setFont(font)
        #self.search.setStyleSheet("color: black; background-color: white;")
        #self.select.setFixedSize(60,30)
        
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
        hbox.addWidget(self.fresh)
        hbox.addStretch()
        self.menu.setLayout(hbox)

    def searchFunction(self):
        convert = {'书号': 'bno', '书名': 'bname', '预约日期': 'reserve_date'}
        self.reserve_list = function.get_reserveing_books(self.prom.text(), convert[self.select.currentText()], self.student_info[0])
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
        self.table.setHorizontalHeaderLabels(['书号', '书名', '预约日期','取书日期', '操作1', '操作2'])  # 设置表头
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
            self.table.setRowHeight(row, 45)

            for j in range(4):
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
        oprate_item.setFixedSize(120, 35)
        oprate_item.setText('取消预约')
        oprate_item.clicked.connect(lambda: self.cancel_reserve(val[0]))
        oprate_item.setStyleSheet("color: white; background: green;")
        oprate_item.setFont(QFont("微软雅黑", 15))
                
        oprate_item1 = QToolButton()
        oprate_item1.setFixedSize(120, 35)
        oprate_item1.setText('更改取书日期')
        oprate_item1.clicked.connect(lambda: self.change_reserve(val[0]))
        oprate_item1.setStyleSheet("color: white; background: green;")
        oprate_item1.setFont(QFont("微软雅黑", 15))
                
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(oprate_item)
        hbox.addStretch()
        hbox1 = QHBoxLayout()
        hbox1.addStretch()
        hbox1.addWidget(oprate_item1)
        hbox1.addStretch()
        table_wid = QWidget()
        table_wid.setLayout(hbox)
        table_wid1 = QWidget()
        table_wid1.setLayout(hbox1)
        print('row = ' + str(row))
        self.table.setCellWidget(row, 4, table_wid)
        self.table.setCellWidget(row, 5, table_wid1)
            
    def cancel_reserve(self, bno: str):
        ans = function.cancel_reserve(bno, self.student_info[0])
        # 刷新表格
        if ans:
            self.searchFunction()
            
    def change_reserve(self, bno:str):
        self.updateDialog = change_reserve.Change(bno, self.student_info[0])
        self.updateDialog.show()
        
    def refresh(self):
        self.searchFunction()

class Person(QWidget):
    def __init__(self, student_info):
        super().__init__()
        self.student_info = function.get_student_info(student_info[0])
        
        self.title_text = QLabel()
        self.title_text.setText('学生个人信息')
        self.title_text.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        self.title_text.setFixedHeight(50)
        
        self.user_id_name = QLabel()
        self.user_id_name.setText(self.student_info[0] + self.student_info[1] + '，欢迎！')
        self.user_id_name.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        self.user_id_name.setFixedHeight(50)
        
        self.out = QToolButton()
        self.out.setText('退出')
        self.out.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        self.out.setFixedHeight(50)
        
        self.titlehbox = QHBoxLayout()
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.user_id_name)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.title_text)
        self.titlehbox.addStretch()
        self.titlehbox.addWidget(self.out)
        self.titlehbox.addStretch()
        
        
        # 学号输入框
        id = QLabel()
        id.setText('学号')
        #id.setFont(QFont("微软雅黑", 15, QFont.bold))
        id.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        self.student_id = QLineEdit()
        self.student_id.setFixedSize(400, 40)
        self.student_id.setText(self.student_info[0])
        self.student_id.setTextMargins(5, 5, 5, 5)
        self.student_id.setEnabled(False)
        idLayout = QHBoxLayout()
        idLayout.addStretch()
        idLayout.addWidget(id)
        idLayout.addStretch()
        idLayout.addWidget(self.student_id)
        idLayout.addStretch()

        name = QLabel()
        name.setText('姓名')
        name.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        #name.setFont(QFont("微软雅黑", 15, QFont.bold))
        #name.setStyleSheet("color: black; background: white;")
        self.student_name = QLineEdit()
        self.student_name.setFixedSize(400, 40)
        self.student_name.setText(self.student_info[1])
        self.student_name.setTextMargins(5, 5, 5, 5)
        self.student_name.setEnabled(False)
        nameLayout = QHBoxLayout()
        nameLayout.addStretch()
        nameLayout.addWidget(name)
        nameLayout.addStretch()
        nameLayout.addWidget(self.student_name)
        nameLayout.addStretch()

        password = QLabel()
        password.setText('密码')
        password.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        #password.setFont(QFont("微软雅黑", 15, QFont.bold))
        #password.setStyleSheet("color: black; background: white;")
        self.student_password = QLineEdit()
        self.student_password.setFixedSize(400, 40)
        self.student_password.setText(self.student_info[5])
        self.student_password.setTextMargins(5, 5, 5, 5)
        self.student_password.setEnabled(False)
        passwordLayout = QHBoxLayout()
        passwordLayout.addStretch()
        passwordLayout.addWidget(password)
        passwordLayout.addStretch()
        passwordLayout.addWidget(self.student_password)
        passwordLayout.addStretch()

        # 重复密码
        repPassword = QLabel()
        repPassword.setText('重复密码')
        repPassword.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        #repPassword.setFont(QFont("微软雅黑", 15, QFont.bold))
        #repPassword.setStyleSheet("color: black; background: white;")
        self.student_repPassword = QLineEdit()
        self.student_repPassword.setFixedSize(400, 40)
        self.student_repPassword.setText(self.student_info[5])
        self.student_repPassword.setTextMargins(5, 5, 5, 5)
        self.student_repPassword.setEnabled(False)
        repPasswordLayout = QHBoxLayout()
        repPasswordLayout.addStretch()
        repPasswordLayout.addWidget(repPassword)
        repPasswordLayout.addStretch()
        repPasswordLayout.addWidget(self.student_repPassword)
        repPasswordLayout.addStretch()

        # 年龄
        age = QLabel()
        age.setText('年龄')
        age.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        #age.setFont(QFont("微软雅黑", 15, QFont.bold))
        #age.setStyleSheet("color: black; background: white;")
        self.student_age = QLineEdit()
        self.student_age.setFixedSize(400, 40)
        self.student_age.setText(str(self.student_info[3]))
        self.student_age.setTextMargins(5, 5, 5, 5)
        self.student_age.setEnabled(False)
        ageLayout = QHBoxLayout()
        ageLayout.addStretch()
        ageLayout.addWidget(age)
        ageLayout.addStretch()
        ageLayout.addWidget(self.student_age)
        ageLayout.addStretch()

        # 学院
        dept = QLabel()
        dept.setText('学院')
        dept.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        #dept.setFont(QFont("微软雅黑", 15, QFont.bold))
        #dept.setStyleSheet("color: black; background: white;")
        self.student_dept = QLineEdit()
        self.student_dept.setFixedSize(400, 40)
        self.student_dept.setText(self.student_info[2])
        self.student_dept.setTextMargins(5, 5, 5, 5)
        self.student_dept.setEnabled(False)
        deptLayout = QHBoxLayout()
        deptLayout.addStretch()
        deptLayout.addWidget(dept)
        deptLayout.addStretch()
        deptLayout.addWidget(self.student_dept)
        deptLayout.addStretch()

        # 性别
        sex = QLabel()
        sex.setText('性别')
        sex.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: white;")
        #sex.setFont(QFont("微软雅黑", 15, QFont.bold))
        #sex.setStyleSheet("color: black; background: white;")
        self.student_sex = QLineEdit()
        self.student_sex.setFixedSize(400, 40)
        self.student_sex.setText(self.student_info[4])
        self.student_sex.setTextMargins(5, 5, 5, 5)
        self.student_sex.setEnabled(False)
        sexLayout = QHBoxLayout()
        sexLayout.addStretch()
        sexLayout.addWidget(sex)
        sexLayout.addStretch()
        sexLayout.addWidget(self.student_sex)
        sexLayout.addStretch()

        # 保存
        self.save = QToolButton()
        self.save.setText('保存')
        self.save.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: green;")
        #self.save.setFont(QFont("微软雅黑", 15, QFont.bold))
        #self.save.setStyleSheet("color: white; background: green;")
        self.save.setFixedSize(100, 40)
        self.save.setEnabled(False)
        self.save.clicked.connect(self.saveFunction)

        # 修改
        self.modify = QToolButton()
        self.modify.setText('修改')
        self.modify.setStyleSheet("color: black;font-size: 25px;font-family: 微软雅黑; background: blue;")
        #self.modify.setFont(QFont("微软雅黑", 15, QFont.bold))
        #self.modify.setStyleSheet("color: white; background: blue;")
        self.modify.setFixedSize(100, 40)
        self.modify.clicked.connect(self.modifyFunction)

        btnLayout = QHBoxLayout()
        btnLayout.addStretch()
        btnLayout.addWidget(self.modify)
        btnLayout.addStretch()
        btnLayout.addWidget(self.save)
        btnLayout.addStretch()

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addLayout(self.titlehbox)
        vbox.addLayout(idLayout)
        vbox.addLayout(nameLayout)
        vbox.addLayout(passwordLayout)
        vbox.addLayout(repPasswordLayout)
        vbox.addLayout(deptLayout)
        vbox.addLayout(ageLayout)
        vbox.addLayout(sexLayout)
        vbox.addLayout(btnLayout)
        vbox.addStretch()
        self.setStyleSheet("background: white;")
        self.setLayout(vbox)

    def saveFunction(self):
        if self.student_password.text() != self.student_repPassword.text():
            print('密码不一致')
            return
        self.student_info = list(self.student_info)
        self.student_info[5] = str(self.student_password.text())
        self.student_info[1] = self.student_name.text()
        self.student_info[2] = self.student_dept.text()
        self.student_info[4] = self.student_sex.text()
        self.student_info[3] = int(self.student_age.text())
        if not function.update_student(self.student_info):
            print('更新失败')
            return
        self.save.setEnabled(False)
        self.student_name.setEnabled(False)
        self.student_password.setEnabled(False)
        self.student_repPassword.setEnabled(False)
        self.student_dept.setEnabled(False)
        self.student_sex.setEnabled(False)
        self.student_age.setEnabled(False)
        self.modify.setStyleSheet("color: white; background: blue;")
        self.save.setStyleSheet("color: white; background: green;")

    def modifyFunction(self):
        self.save.setEnabled(True)
        self.student_name.setEnabled(True)
        self.student_password.setEnabled(True)
        self.student_repPassword.setEnabled(True)
        self.student_dept.setEnabled(True)
        self.student_sex.setEnabled(True)
        self.student_age.setEnabled(True)
        self.modify.setStyleSheet("color: white; background: green;")
        self.save.setStyleSheet("color: white; background: blue;")
        
        
        
        
        