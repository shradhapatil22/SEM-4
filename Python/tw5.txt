import sqlite3
from contextlib import closing


def dbConnect(file):
    try:
        conn = sqlite3.connect(file)
        return conn
    except:
        print("Dbconnect error")


def dbInsert(conn):
    n = int(input("Enter n:"))
    with closing(conn.cursor()) as C:
        for i in range(n):
            pid, n, q, p = input("Enter id,name,qty and price: ").split()
            pid = int(pid)
            q = int(q)
            p = float(p)
            query = "insert into products values(?,?,?,?)"
            try:
                C.execute(query, (pid, n, q, p))
            except:
                print("DbInsert error")
        conn.commit()


def dbDisplay(conn):
    with closing(conn.cursor()) as C:
        query = "Select * from products"
        try:
            C.execute(query)
            result =  C.fetchall()
            print("Products:")
            for line in result:
                print(line[0], line[1], line[2], line[3])
        except:
            print("DbDisplay error")


def dbDelete(conn):
    pid = int(input("Enter prodId to delete: "))
    with closing(conn.cursor()) as C:
        query = "delete from products where productid=?"
        try:
            C.execute(query,(pid,))
            conn.commit()
        except:
            print("Dbdelete error")


def dbUpdate(conn):
    with closing(conn.cursor()) as C:
        query = "Update products set price=price+(price*0.1) where price<50"
        try:
            C.execute(query)
            conn.commit()
        except:
            print("DbUpdate error")


def dbDispLTforty(conn):
    with closing(conn.cursor()) as C:
        query = "select * from where quantity<40"
        try:
            C.execute(query)
            result =  C.fetchall()
            for line in result:
                print(line[0], line[1], line[2], line[3])

        except:
            print("DbDisplay less than 40 error")


def main():
    conn = dbConnect("D:\\Srushti\\GIT\\4th sem\\Python\\PROGRAMS\\products.sqlite")
    dbInsert(conn)
    dbDisplay(conn)
    dbDelete(conn)
    print("Products after deleting")
    dbDisplay(conn)
    dbUpdate(conn)
    print("Products after update")
    dbDisplay(conn)
    print("Products whose qty<40:")
    dbDispLTforty(conn)


if __name__ == '__main__':
    main()