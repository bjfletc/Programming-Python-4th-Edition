from initdata import db
import pickle

dbfile = open('people-file', 'wb')  # # use binary mode files in 3.X
pickle.dump(db, dbfile)
dbfile.close()
