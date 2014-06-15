import sqlite3
import MySQLdb

#gets bookmarks from Firefox sqlite3 database
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
  

#sends bookmarks to MySQL database using python MySQLDB api 	
def sendBMs():
    bmz = getBookmarks()
    db = MySQLdb.connect("localhost", "1z", "ummie", "practice2")
    cursor2 = db.cursor()
    for bookmark in bmz: 
      cursor2.execute("INSERT INTO %s values('%s')"%('',bookmark))
    db.commit()
    db.close() 
  

if __name__ == '__main__':
    getBookmarks() 	
    sendBMs()
