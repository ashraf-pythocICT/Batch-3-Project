import sqlite3

db= sqlite3.connect('mirzapur.db')

db.execute('drop table if exists mirzapur')

db.execute('create table mirzapur(i int, j name, k int)')

db.execute('insert into mirzapur(i,j,k) values(?,?,?)',('roll', 'name', 'class'))
db.execute('insert into mirzapur(i,j,k) values(?,?,?)',('1', 'saima',   '9'))
db.execute('insert into mirzapur(i,j,k) values(?,?,?)',('2', 'naima',   '10'))
db.execute('insert into mirzapur(i,j,k) values(?,?,?)',('3', 'wazifa',  '8'))
db.execute('insert into mirzapur(i,j,k) values(?,?,?)',('4', 'priya',   '9'))
db.execute('insert into mirzapur(i,j,k) values(?,?,?)',('5', 'sanjida', '7'))

result= db.execute('select * from mirzapur')
print("Mirzapur girls high school")
for row in result:
           print(row)

db.execute('update mirzapur set j=? ,k=? where i=?',('tamanna',6,2))
db.commit()

print("\n \n after update:")
print("Mirzapur girls high school")
result= db.execute('select * from mirzapur')
for row in result:
           print(row)

db.execute('delete from mirzapur where i=4')
db.commit()

print("\n \n after delete:")
print("Mirzapur girls high school")
result= db.execute('select * from mirzapur')
for row in result:
           print(row)           
