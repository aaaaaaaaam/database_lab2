import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import mysql.connector
from PyQt5.QtGui import QIcon
import function

class add_book(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        print('add book 1')
        self.setWindowTitle('书籍添加')
        self.setWindowIcon(QIcon('icon/book.png'))

        vbox = QVBoxLayout()

        print('add book 2')
        hbox1 = QHBoxLayout()
        label1 = QLabel('书籍号：')
        label1.setFixedSize(100, 40)
        self.id_edit = QLineEdit()
        self.id_edit.setFixedSize(200, 40)
        hbox1.addWidget(label1)
        hbox1.addWidget(self.id_edit)
        vbox.addLayout(hbox1)

        print('add book 3')
        hbox2 = QHBoxLayout()
        label2 = QLabel('书名：')
        label2.setFixedSize(100, 40)
        self.name_edit = QLineEdit()
        self.name_edit.setFixedSize(200, 40)
        hbox2.addWidget(label2)
        hbox2.addWidget(self.name_edit)
        vbox.addLayout(hbox2)

        print('add book 4')
        hbox3 = QHBoxLayout()
        label3 = QLabel('作者：')
        label3.setFixedSize(100,40)
        self.author_edit = QLineEdit()
        self.author_edit.setFixedSize(200,40)
        hbox3.addWidget(label3)
        hbox3.addWidget(self.author_edit)
        vbox.addLayout(hbox3)

        print('add book 5')
        hbox4 = QHBoxLayout()
        label4 = QLabel('分类：')
        label4.setFixedSize(100,40)
        self.class_edit = QLineEdit()
        self.class_edit.setFixedSize(200,40)
        hbox4.addWidget(label4)
        hbox4.addWidget(self.class_edit)
        vbox.addLayout(hbox4)

        print('add book 6')
        hbox5 = QHBoxLayout()
        label5 = QLabel('语言：')
        label5.setFixedSize(100,40)
        self.lang_edit = QLineEdit()
        self.lang_edit.setFixedSize(200,40)
        hbox5.addWidget(label5)
        hbox5.addWidget(self.lang_edit)
        vbox.addLayout(hbox5)

        print('add book 7')
        hbox6 = QHBoxLayout()
        label6 = QLabel('总量：')
        label6.setFixedSize(100,40)
        self.sum_edit = QLineEdit()
        self.sum_edit.setFixedSize(200,40)
        hbox6.addWidget(label6)
        hbox6.addWidget(self.sum_edit)
        vbox.addLayout(hbox6)
        
        print('add book 8')
        hbox7 = QHBoxLayout()
        label7 = QLabel('剩余：')
        label7.setFixedSize(100,40)
        self.rest_edit = QLineEdit()
        self.rest_edit.setFixedSize(200,40)
        hbox7.addWidget(label7)
        hbox7.addWidget(self.rest_edit)
        vbox.addLayout(hbox7)
        
        print('add book 9')
        hbox8 = QHBoxLayout()
        label8 = QLabel('出版商：')
        label8.setFixedSize(100,40)
        self.press_edit = QLineEdit()
        self.press_edit.setFixedSize(200,40)
        hbox8.addWidget(label8)
        hbox8.addWidget(self.press_edit)
        vbox.addLayout(hbox8)
        
        print('add book 10')
        hbox9 = QHBoxLayout()
        label9 = QLabel('出版日期：')
        label9.setFixedSize(100,40)
        self.date_edit = QLineEdit()
        self.date_edit.setFixedSize(200,40)
        hbox9.addWidget(label9)
        hbox9.addWidget(self.date_edit)
        vbox.addLayout(hbox9)
        
        print('add book 11')
        hbox10 = QHBoxLayout()
        self.register_button = QPushButton('提交')
        self.register_button.setFixedSize(400, 40)
        #register_button.clicked.connect(self.register)
        hbox10.addStretch()
        hbox10.addWidget(self.register_button)
        vbox.addLayout(hbox10)
        
        print('add book 12')
        hbox11 = QHBoxLayout()
        self.back_button = QPushButton('返回')
        self.back_button.setFixedSize(400, 40)
        hbox11.addStretch()
        hbox11.addWidget(self.back_button)
        vbox.addLayout(hbox11)
        
        print('add book 13')
        self.setLayout(vbox)
        print('add book 13')
        #self.setMyStyle()
        print('add book 13')
        
    def register(self):
        print('12')
        id = self.id_edit.text()
        print('13')
        name_ = self.name_edit.text()
        print('14')
        author = self.author_edit.text()
        print('15')
        class_ = self.class_edit.text()
        print('16')
        lang = self.lang_edit.text()
        sum = self.sum_edit.text()
        print('17')
        rest = self.rest_edit.text()
        print('18')
        press = self.press_edit.text()
        print('19')
        date_ = self.date_edit.text()

        if sum != rest:
            QMessageBox.warning(self, '警告', '剩余与总量不相等')
            return

        res = True
        print('13')
        conn = mysql.connector.connect(host = function.CONFIG['host'], user = function.CONFIG['user'], password = function.CONFIG['pwd'], database = function.CONFIG['db'], charset="utf8")
        try:
            print('14')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO book (bno, bname, author, date_press, press, class, laug, sun, rest) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s)",
                           (id, name_, author, date_, press, class_, lang, sum, rest))
            conn.commit()
        except Exception as e:
            print('Search error!')
            print(e)
            res = False
        finally:
           if conn:
                conn.close()
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = add_book()
    window.show()
    sys.exit(app.exec_())