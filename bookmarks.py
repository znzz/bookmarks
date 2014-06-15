import sqlite3
import MySQLdb


#retrieves bookmarks from Firefox sqlite3 database
def getBookmarks(filename):
    bmlist = []
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute('select * from moz_places')
    table_info = cursor.fetchall()
    for bookmark in table_info:
      bm = bookmark[1]
      bmlist.append(bm)
    db.close()  
  

#sends bookmarks to MySQL database use Python MySQLdb api
def sendBMs():
    bmz = getBookmarks()
    db = MySQLdb.connect(host = None, user = None, password = None, db = None)
    cursor2 = db.cursor()
    for bookmark in bmz: 
      cursor2.execute("INSERT INTO %s values('%s')"%('',bookmark))
    db.commit()
    db.close() 
  

if __name__ == '__main__':
    getBookmarks() 	
    sendBMs()
