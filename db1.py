#db1.py
import sqlite3

#일단 메모리에서 연습
#영구적으로 파일에 저장
#r: row string notation
con = sqlite3.connect(r"c:\work\sample.db")
#커서 인스턴스 생성
cur = con.cursor()

#테이블 구조 생성
cur.execute("CREATE TABLE if not exists PhoneBook(name text, phoneNum text)")

#1건 데이터 입력
cur.execute("INSERT INTO PhoneBook VALUES('derick', '010-2222-3333')")

#입력 파라메터 처리
name = "gildong"
phoneNumber = "010-1234-5678"
cur.execute("INSERT INTO PhoneBook VALUES(?, ?)", (name, phoneNumber))

#여러건을 입력
datalist = (("tom", "010-3333-4444"), ("dsp", "010-5555-6666"))
cur.executemany("INSERT INTO PhoneBook VALUES(?, ?)", datalist)

#입력 데이터 확인
cur.execute("SELECT * FROM PhoneBook;")
# for row in cur:
#     print(row[0], row[1])
# print(cur.fetchall())
print(cur.fetchall())

#완료(입력, 수정, 삭제)
con.commit( )


