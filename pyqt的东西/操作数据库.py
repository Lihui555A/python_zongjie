import PyQt5.QtSql as sql

db=sql.QSqlDatabase.addDatabase('QMYSQL')
db.setDatabaseName('localhost')
db.setUserName('root')
db.setPassword('guoxin521@')
db.open()

query=sql.QSqlQuery('select * from a1')
query.first()
for i in range(query.size()):
    print(query.value(0),query.value(1))
    query.next()

db.close()