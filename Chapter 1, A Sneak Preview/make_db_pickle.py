from initdata import db
import pickle

dbfile = open('people-pickle', 'wb')  # # use binary mode files in 3.X
pickle.dump(db, dbfile)
dbfile.close()
