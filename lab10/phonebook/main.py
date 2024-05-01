import psycopg2
import csv
from config import host, user, password, db_name, port

conn = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name,
    port = port
)
conn.autocommit = True
cursor = conn.cursor()

def insertdata():
    name = input("Name to insert ")
    number = input("Number to insert ")
    sql = f'''
   INSERT INTO users (username, phone) VALUES
   ('{name}', '{number}')
'''
    cursor.execute(sql)

def insertfromcsv():
    with open("contacts.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            sql = f'''
                INSERT INTO users(username, phone) VALUES
                ('{row[0]}', '{row[1]}')
                '''
            cursor.execute(sql)


def updatedatabyname():
    find = input("Enter a name to find ")
    update = input("Enter a new number ")
    sql = f'''
    UPDATE users SET phone = '{update}' WHERE username = '{find}'
    '''
    cursor.execute(sql)
    
def updatedatabynumber():
    find = input("Enter a number to find ")
    update = input("Enter a new name ")
    sql = f'''
    UPDATE users SET username = '{update}' WHERE phone = '{find}'
    '''
    cursor.execute(sql)    
    
def deletedatabyname():
    find = input("Enter a name to delete ")
    sql = f'''
    DELETE FROM users WHERE username = '{find}';
    '''
    cursor.execute(sql)
    
def deletedatabynumber():
    find = input("Enter a number to delete ")
    sql = f'''
    DELETE FROM users WHERE phone = '{find}';
    '''
    cursor.execute(sql)
    
def show():
    filter = input("What you need to find")
    sql = f'''
    SELECT * FROM users WHERE username LIKE '%{filter}%' OR phone LIKE '%{filter}%'
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        for i in result:
            print(i)
    else:
        print('There are none')
        

if __name__ == '__main__':
    intro = """
    Commands:
          insert
          delete by name
          delete by number
          show
          insert csv
          exit 
          """
    print(intro)
    run = True
    while run:
        enter = input(str("Enter what you want to do: "))
        if enter == 'insert':
            insertdata()
        elif enter == 'delete by name':
            deletedatabyname()
        elif enter == 'delete by number':
            deletedatabynumber()
        elif enter == 'update by name':
            updatedatabyname()
        elif enter == 'update by number':
            updatedatabynumber()
        elif enter == 'show':
            show()
        elif enter == 'insert csv':
            insertfromcsv()
        elif enter == 'exit':
            run = False
        else:
            print("Wrong input")

    conn.close()