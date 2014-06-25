import sqlite3
import MySQLdb
import mozilla
import string

""" subjects.py matches and assigns subjects from subject_dict to bookmarks"""


def get_mozilla_bm(filename):
    bmlist = []
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute('select * from moz_places')
    table_info = cursor.fetchall()
    for bookmark in table_info:
        bm = bookmark[1]
        bmlist.append(bm)
    return bmlist
        
    
def split_list(text):
    text = text.lower()
    text = text.rstrip('/')
    for punc in string.punctuation:
      text = text.replace(punc, " ")
      splittext = text.split(" ")
    del(splittext[1:3])
    return splittext


def word_dict():
    bmz = get_mozilla_bm(filename)
    subject_dict = {'backend': ['webservices', 'webservice', 'api', 'rest', 'server', 'backend', 'json', 'node-js'],
                  'startup': ['startup', 'acquired', 'funding'],
                  'ios': ['ios', 'iphones', 'ipad'],
                  'android': 'android',
                  'mobile': ['app', 'smartphones'],
                  'languages': ['python', 'php', 'java', 'c', 'c++', 'scripting', 'object-oriented'],
                  'functional programming': ['clojure', 'scala', 'haskell'],
                  'database': ['database', 'mysql', 'nosql', 'sqlite'],
                  'operating systems': ['macosx', 'mac', 'linux'],
                  'cloud': 'cloud',
                  'programming': ['web scraping', 'software', 'computing', 'programmer', 'programming'],
                  'jobs': ['job', 'indeed'],
                  'github': 'github',
                  'architecture': 'memory',
                  'distributed systems': ['distributed', 'cluster'],
                  'apache': 'mesos',
                  'data processing': ['hadoop', 'storm', 'backtype'],
                  'open source': ['opensource', 'open-source']}


    new_list = []
    for values in subject_dict.values():
        if isinstance(values, str):
            new_list.append(values)
        else:
            for i in values:
                new_list.append(i)


    for bookmark in bmz:
        bookmark_list = split_list(bookmark)
        for bm in bookmark_list:
            for value in new_list:
                if bm == value:
                    print bookmark
                    print key
                    

if __name__ == '__main__':	
  print word_dict()
