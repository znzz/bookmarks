"""

This module retieves all bookmarks in Mozilla Firefox and 
sends them to MySQL using python MySQLdb 
 
"""

import sqlite3
import MySQLdb


"""retrieves bookmarks from Firefox sqlite3 database"""
def get_mozilla_bm(filename):
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


    """retrieves all bookmarks already stored in mysql"""
    def dbBookmarks(self, host, user, password, db, tablename):
        bmList = []
        Db = MySQLdb.connect(self.host, self.user, self.password, self.db)
        cursor1 = Db.cursor()
        cursor1.execute('SELECT * FROM %s' %(self.tablename))
        results = cursor1.fetchall()
        for row in results:
            bookmark = row[0]
            bmList.append(bookmark)
        Db.close()
        return bmList 
        
        
    #maybe return dict from dbBookmarks, retreival will be faster
    def send_new_bm(self, filename, host, user, password, db, tablename):
        new_bm_list = get_mozilla_bm(self.filename)
        bm_list = self.dbBookmarks(self.host, self.user, self.password, self.db, self.tablename)
        for newBM in new_bm_list:
            if not newBM in bm_list:
                #bm_list.append(newBM)
                print newBM



#sends bookmarks to MySQL database using Python MySQLdb api
  def sendBMs(self, filename, tablename):
      bmz = getBookmarks(self.filename)
      Db = MySQLdb.connect(self.host, self.user, self.password, self.db)
      cursor2 = Db.cursor()
      for bookmark in bmz: 
          cursor2.execute("INSERT INTO %s values('%s')"%(self.tablename,bookmark))
      Db.commit()
      Db.close() 
