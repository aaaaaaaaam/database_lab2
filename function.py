import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import mysql.connector
import datetime

CONFIG = {
    "host": '127.0.0.1',
    "user": 'root',
    "pwd": 'hgw622811',
    'db': 'lab2'}
    
#该函数仅仅查询图书部分
def search_book(info:str, restrict:str, sno:str):
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    res = []
    print(info + ' ' + restrict + ' ' + sno)
    try:
        cursor = conn.cursor()
        if info == '':
            cursor.execute("SELECT * FROM book")
            res = cursor.fetchall()
        elif restrict == 'bno':
            cursor.execute("SELECT * FROM book WHERE bno = %s", (info,))
            res = cursor.fetchall()
        elif restrict == 'class':
            cursor.execute("SELECT * FROM book WHERE class = %s", (info,))
            res = cursor.fetchall()
        elif restrict == 'press':
            cursor.execute("SELECT * FROM book WHERE press = %s", (info,))
            res = cursor.fetchall()
        elif restrict == 'author':
            cursor.execute("SELECT * FROM book WHERE author = %s", (info,))
            res = cursor.fetchall()
        elif restrict == 'bname':
            cursor.execute("SELECT * FROM book WHERE bname = %s", (info,))
            res = cursor.fetchall()
            
        res_temp = []
        if sno != '':
            for book in res:
                book = list(book)
                bno = book[0]
                print("here")
                cursor.execute("SELECT is_or_not_borrowbook(%s, %s)", (sno, bno))
                result = cursor.fetchone()
                integer_value = result[0]
                print('integer_value = ' + str(integer_value))
                if integer_value == 3:
                    book.append('预约')
                elif integer_value == 4:
                    cursor.execute("SELECT borrow_date FROM borrow WHERE sno = %s AND bno = %s", (sno, bno,))
                    ans = cursor.fetchall()
                    current_time = datetime.datetime.now()
                    current_date = current_time.strftime('%Y-%m-%d')
                    flag = 1
                    for an in ans:
                        if str(an[0]) == current_date:
                            flag = 0
                    if flag == 1:
                        book.append('借书')
                    else:
                        book.append('不可借')
                else:
                    book.append('不可借')
                    print(book)
                res_temp.append(book)
        else:
            for book in res:
                res_temp.append(book)
    except Exception as e:
        print('Search error!')
        print(e)
        res_temp = []
    finally:
        if conn:
            conn.close()
        return res_temp
            
    
def borrow_book(bno:str, sno:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        current_time = datetime.datetime.now()
        current_date = current_time.strftime('%Y-%m-%d')
        cursor.execute("INSERT INTO borrow(bno, sno, borrow_date) VALUES(%s, %s, %s)", (bno, sno, current_date,))
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
    
#这个函数需要用到借阅表、图书表以及罚金表。
#这个函数接受一个学号sno
#返回书号、书名、借书日期、还书日期以及罚金
def get_borrowing_books(info:str, restrict:str, sno:str):
    res = []
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        if info == '':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.borrow_date, borrow.return_date FROM borrow, book where borrow.sno = %s and borrow.bno = book.bno", (sno,))
        elif restrict == 'bno':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.borrow_date, borrow.return_date FROM borrow, book where borrow.sno = %s and borrow.bno = book.bno and borrow.bno = %s", (sno, info,))
        elif restrict == 'bname':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.borrow_date, borrow.return_date FROM borrow, book where borrow.sno = %s and book.bname = %s and borrow.bno = book.bno", (sno, info,))
        elif restrict == 'borrow_date':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.borrow_date, borrow.return_date FROM borrow, book where borrow.sno = %s and borrow.borrow_date = %s and borrow.bno = book.bno", (sno, info,))
        res = cursor.fetchall()
        print('1')
        res_temp = []
        for borrow in res:
            borrow = list(borrow)
            cursor.execute("SELECT COUNT(*) FROM over_due WHERE sno = %s AND bno = %s and borrow_date = %s", (sno, borrow[0], str(borrow[2])))
            is_over = cursor.fetchall()[0][0]
            if is_over:
                borrow.append('违期')
            else:
                cursor.execute("SELECT is_or_not_nore_over(%s, %s, %s)", (sno, borrow[0], borrow[2]))
                result = cursor.fetchone()
                integer_value = result[0]
                if integer_value == 1:
                    borrow.append('不违期')
                else:
                    borrow.append('违期')
            res_temp.append(borrow)
        print('2')
    except Exception as e:
        print('Search error!')
        print(e)
        res_temp = []
    finally:
        if conn:
            conn.close()
        return res_temp
                
    
def return_book(bno:str, sno:str, b_date:datetime.date):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        cursor.callproc("UpdateReturnDate", args = (bno, sno, b_date))
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
    
def get_student_info(sno:str):
    print("get_stu_info")
    res = []
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        print("get_stu_info")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE sno = %s", (sno,))
        res = cursor.fetchall()[0]
        print(len(res))
    except Exception as e:
        print('Search error!')
        print(e)
        res = []
    finally:
        if conn:
            conn.close()
        return res
    
def get_administrator_info(sno:str):
    print("get_adm_info")
    res = []
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        print("get_stu_info")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM administrator WHERE ano = %s", (sno,))
        res = cursor.fetchall()[0]
        print(len(res))
    except Exception as e:
        print('Search error!')
        print(e)
        res = []
    finally:
        if conn:
            conn.close()
        return res
    
def update_student(stu_mes):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        # 编写UPDATE语句WHERE sno=%s", (
        print("de 3")
        cursor.execute("UPDATE student SET sname=%s, dept=%s, age=%s, sex=%s, code_stu = %s WHERE student.sno = %s",(
                stu_mes[1],
                stu_mes[2],
                stu_mes[3],
                stu_mes[4],
                stu_mes[5],
                stu_mes[0]
            ))
        # 提交更改
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
    
            
def update_book(info:str, restrict:str, bno:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        if restrict == 'class':
            cursor.execute("UPDATE book SET class=%s WHERE book.bno = %s", (info, bno))
        elif restrict == 'press':
            cursor.execute("UPDATE book SET press=%s WHERE book.bno = %s", (info, bno))
        elif restrict == 'author':
            cursor.execute("UPDATE book SET author=%s WHERE book.bno = %s", (info, bno))
        elif restrict == 'bname':
            cursor.execute("UPDATE book SET bname=%s WHERE book.bno = %s", (info, bno))
        elif restrict == 'lang':
            cursor.execute("UPDATE book SET lang=%s WHERE book.bno = %s", (info, bno))
        elif restrict == 'sum':
            cursor.execute("SELECT sun FROM book WHERE book.bno = %s", (bno,))
            sum = cursor.fetchall()[0][0]
            sum_new = int(info)
            cursor.execute("SELECT rest FROM book WHERE book.bno = %s", (bno,))
            rest = cursor.fetchall()[0][0]
            rest_new = int(rest) + (sum_new - int(sum))
            if rest_new < 0:
                print("借出的书籍数量超过存在的书籍总数")
                return False
            cursor.execute("UPDATE book SET sun=%s WHERE book.bno = %s", (info, bno))
            cursor.execute("UPDATE book SET rest=%s WHERE book.bno = %s", (str(rest_new), bno))
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
            
def delete_book(bno:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        # 编写UPDATE语句WHERE sno=%s", (
        cursor.callproc('delete_book', (bno,))
        # 提交更改
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
    
    
#管理员部分查找学生信息
def search_student(info:str, restrict:str):
    res = []
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        print('student 2')
        cursor = conn.cursor()
        if info == '':
            cursor.execute("SELECT * FROM student")
        elif restrict == 'sno':
            cursor.execute("SELECT * FROM student WHERE student.sno = %s", (info,))
        elif restrict == 'sname':
            cursor.execute("SELECT * FROM student WHERE student.sname = %s", (info,))
        elif restrict == 'dept':
            cursor.execute("SELECT * FROM student WHERE student.dept = %s", (info,))
        elif restrict == 'age':
            cursor.execute("SELECT * FROM student WHERE student.age = %d", (info,))
        elif restrict == 'sex':
            cursor.execute("SELECT * FROM student WHERE student.sex = %s", (info,))
        res = cursor.fetchall()
        print('student 3')
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = []
    finally:
        if conn:
            conn.close()
        return res
    
#管理员部分查找借阅记录
def borrow_log(info:str, restrict:str):
    res = []
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        if info == '':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM borrow, book, student where borrow.bno = book.bno and borrow.sno = student.sno")
        elif restrict == 'bno':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM book, borrow, student WHERE borrow.bno = book.bno and borrow.sno = student.sno and borrow.bno = %s", (info,))
        elif restrict == 'sno':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM book, borrow, student WHERE borrow.bno = book.bno and borrow.sno = student.sno and borrow.sno = %s", (info,))
        elif restrict == 'bname':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM book, borrow, student WHERE borrow.bno = book.bno and borrow.sno = student.sno and book.bname = %s", (info,))
        elif restrict == 'sname':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM book, borrow, student WHERE borrow.bno = book.bno and borrow.sno = student.sno and student.sname = %s", (info,))
        res = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = []
    finally:
        if conn:
            conn.close()
        return res
    
#该函数接受一个学号或者姓名或者书籍号来查找预约记录,管理员查找预约记录
def reserve_log(info:str, restrict:str):
    res = []
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        if info == '':
            cursor.execute("SELECT reserve.bno, book.bname, reserve.sno, student.sname, reserve.reserve_date, reserve.take_date FROM reserve, book, student where reserve.bno = book.bno and reserve.sno = student.sno")
        elif restrict == 'bno':
            cursor.execute("SELECT reserve.bno, book.bname, reserve.sno, student.sname, reserve.reserve_date, reserve.take_date FROM reserve, book, student where reserve.bno = book.bno and reserve.sno = student.sno and reserve.bno = %s", (info,))
        elif restrict == 'sno':
            cursor.execute("SELECT reserve.bno, book.bname, reserve.sno, student.sname, reserve.reserve_date, reserve.take_date FROM reserve, book, student where reserve.bno = book.bno and reserve.sno = student.sno and reserve.sno = %s", (info,))
        elif restrict == 'bname':
            cursor.execute("SELECT reserve.bno, book.bname, reserve.sno, student.sname, reserve.reserve_date, reserve.take_date FROM reserve, book, student where reserve.bno = book.bno and reserve.sno = student.sno and book.bname= %s", (info,))
        elif restrict == 'sname':
            cursor.execute("SELECT reserve.bno, book.bname, reserve.sno, student.sname, reserve.reserve_date, reserve.take_date FROM reserve, book, student where reserve.bno = book.bno and reserve.sno = student.sno and student.sname = %s", (info,))
        res = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = []
    finally:
        if conn:
            conn.close()
        return res
    
    
#学生自己查找自己的预约记录
def get_reserveing_books(info:str, restrict:str, sno:str):
    res = []
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        if info == '':
            cursor.execute("SELECT reserve.bno, book.bname, reserve.reserve_date, reserve.take_date FROM reserve, book where reserve.sno = %s and reserve.bno = book.bno", (sno,))
        elif restrict == 'bno':
            cursor.execute("SELECT reserve.bno, book.bname, reserve.reserve_date, reserve.take_date FROM reserve, book where reserve.sno = %s and reserve.bno = book.bno and reserve.bno = %s", (sno, info,))
        elif restrict == 'bname':
            cursor.execute("SELECT reserve.bno, book.bname, reserve.reserve_date, reserve.take_date FROM reserve, book where reserve.sno = %s and reserve.bno = book.bno and book.bname = %s", (sno, info,))
        elif restrict == 'reserve_date':
            cursor.execute("SELECT reserve.bno, book.bname, reserve.reserve_date, reserve.take_date FROM reserve, book where reserve.sno = %s and reserve.bno = book.bno and reserve.reserve_date = %s", (sno, info,))
        res = cursor.fetchall()
        res = list(res)
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = []
    finally:
        if conn:
            conn.close()
        return res
    
    
    
#学生自己取消预约记录
def cancel_reserve(bno:str, sno:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reserve WHERE bno = %s AND sno = %s", (bno, sno))
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
    
def reserve_book(bno:str, sno:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        current_time = datetime.datetime.now()

        # 创建一个表示十天的时间间隔
        ten_days = datetime.timedelta(days=10)
        # 计算十天后的日期
        ten_days_later = current_time + ten_days
        current_date = ten_days_later.strftime('%Y-%m-%d')
        cursor = conn.cursor()
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("INSERT INTO reserve(bno, sno, take_date) VALUES(%s, %s, %s)", (bno, sno, current_date))
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
    
    
def stu_check(sno:str, password:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        print(sno)
        print(password)
        cursor.execute("SELECT * FROM student WHERE sno = %s AND code_stu = %s", (sno, password))
        res = cursor.fetchall()
        if res is None:
            print("没有这个人")
            res = False
        else:
            res = True
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res


def administrator_check(sno:str, password:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        print(sno)
        print(password)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM administrator WHERE ano = %s and code_adm = %s", (sno, password))
        res = cursor.fetchall()
        if res is None:
            print("没有这个人")
            res = False
        else:
            res = True
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
    
def overdue_log(info:str, restrict:str):
    res = []
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        if info == '':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM borrow, book, student where borrow.bno = book.bno and borrow.sno = student.sno")
        elif restrict == 'bno':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM book, borrow, student WHERE borrow.bno = book.bno and borrow.sno = student.sno and borrow.bno = %s", (info,))
        elif restrict == 'sno':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM book, borrow, student WHERE borrow.bno = book.bno and borrow.sno = student.sno and borrow.sno = %s", (info,))
        elif restrict == 'bname':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM book, borrow, student WHERE borrow.bno = book.bno and borrow.sno = student.sno and book.bname = %s", (info,))
        elif restrict == 'sname':
            cursor.execute("SELECT borrow.bno, book.bname, borrow.sno, student.sname, borrow.borrow_date, borrow.return_date FROM book, borrow, student WHERE borrow.bno = book.bno and borrow.sno = student.sno and student.sname = %s", (info,))
        res = cursor.fetchall()
        res_temp = []
        for borrow in res:
            borrow = list(borrow)
            cursor.execute("SELECT COUNT(*) FROM over_due WHERE sno = %s AND bno = %s and borrow_date = %s", (borrow[2], borrow[0], str(borrow[4])))
            is_over = cursor.fetchall()[0][0]
            if is_over:
                res_temp.append(borrow)
            else:
                cursor.execute("SELECT is_or_not_nore_over(%s, %s, %s)", (borrow[2], borrow[0], borrow[4]))
                result = cursor.fetchone()
                integer_value = result[0]
                if integer_value == 2:
                    res_temp.append(borrow)
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res_temp = []
    finally:
        if conn:
            conn.close()
        return res_temp
    
def delete_student(sno:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        # 编写UPDATE语句WHERE sno=%s", (
        cursor.callproc('delete_student', (sno,))
        # 提交更改
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
    
def update_student_adm(info:str, restrict:str, sno:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        if restrict == 'sname':
            cursor.execute("UPDATE student SET sname=%s WHERE student.sno = %s", (info, sno))
        elif restrict == 'dept':
            cursor.execute("UPDATE student SET dept=%s WHERE student.sno = %s", (info, sno))
        elif restrict == 'age':
            cursor.execute("UPDATE student SET age=%s WHERE student.sno = %s", (info, sno))
        elif restrict == 'sex':
            cursor.execute("UPDATE student SET sex=%s WHERE student.sno = %s", (info, sno))
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res
    
def change_reserve(info:str, sno:str, bno:str):
    res = True
    conn = mysql.connector.connect(host = CONFIG['host'], user = CONFIG['user'], password = CONFIG['pwd'], database = CONFIG['db'], charset="utf8")
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE reserve SET take_date=%s WHERE reserve.sno = %s and reserve.bno= %s", (info, sno, bno))
        conn.commit()
    except Exception as e:
        print('Search error!')
        print(e)
        res = False
    finally:
        if conn:
            conn.close()
        return res