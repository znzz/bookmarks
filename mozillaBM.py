"""

This module retieves all bookmarks in Mozilla Firefox and 
sends them to MySQL using python MySQLdb 
 
"""

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
    return bmlist  
  
  
class BookmarksDb(object):
    def __init__(self, host = None, user = None, password = None, 
                 db = None, filename = None, tablename = None):
      self.host = host
      self.user = user
      self.password = password 
      self.db = db
      self.filename = filename
      self.tablename = tablename

#sends bookmarks to MySQL database using Python MySQLdb api
  def sendBMs(self, filename, tablename):
      bmz = getBookmarks(self.filename)
      Db = MySQLdb.connect(self.host, self.user, self.password, self.db)
      cursor2 = Db.cursor()
      for bookmark in bmz: 
          cursor2.execute("INSERT INTO %s values('%s')"%(self.tablename,bookmark))
      Db.commit()
      Db.close() 
