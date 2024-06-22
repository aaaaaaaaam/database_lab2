import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox
import mysql.connector
import function
from PyQt5.QtGui import QIcon

KEY_LIST = ['bno', 'bname', 'author',
            'date', 'press', 'position', 'sum', 'class']


class BookInfo(QWidget):
    def __init__(self, bno:str):
        super().__init__()
        self.bno = bno
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('书籍更新')
        self.setWindowIcon(QIcon('icon/book.png'))

        vbox = QVBoxLayout()

        self.selectBox = QComboBox()
        self.selectBox.addItems(['分类', '出版社', '作者', '书名', '语言', '最大量'])
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
        convert = {'分类': 'class', '出版社': 'press', '作者': 'author', '书名': 'bname', '语言': 'laug', '最大量':'sum'}
        self.book_update = function.update_book(self.searchInput.text(), convert[self.selectBox.currentText()], self.bno)



if __name__ == '__main__':
    book_msg = {
        'bno': '4',
        'bname': 'Java',
        'author': 'kak',
        'date': '2009-05',
        'press': '电子出版社',
        'position': 'C05',
        'sum': 5,
        'class': 'aasd asd asd ad '
    }
    app = QApplication(sys.argv)
    ex = BookInfo(book_msg)
    ex.show()
    sys.exit(app.exec_())
