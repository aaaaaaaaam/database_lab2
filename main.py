import sys
from PyQt5.QtWidgets import QApplication
import widget


def main():
    # createDB.create_database()
    app = QApplication(sys.argv)
    mainwin = widget.BookManage_Window()
    mainwin.setWindowTitle("图书馆管理系统")
    mainwin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
