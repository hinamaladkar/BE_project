# Open database connection ( If database is not created don't give dbname)
db = MySQLdb.connect("localhost","yourusername","yourpassword","yourdbname" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

## INSERT DATA TO TABLE
for key,val in j_decoded["one-wire"].items():
    try:
        rom = key.encode('utf-8')
        temperatuur = val["temperatuur"]
        createsqltable = """CREATE TABLE IF NOT EXISTS `%s` (
                 id INT PRIMARY KEY AUTO_INCREMENT,
                 created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                 timestamp TIMESTAMP,
                 temp FLOAT)""" % (rom)
        cursor.execute(createsqltable)
        cursor.execute("""INSERT INTO %s (timestamp, temp) VALUES (%s,%s)"""%(rom,timestampdata,temperatuur))
        db.commit()
    except:     
        db.rollback()

## CLOSE THE DATABASE
db.close()
