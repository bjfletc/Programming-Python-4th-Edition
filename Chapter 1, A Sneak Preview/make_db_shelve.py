from initdata import bob, sue, brandon
import shelve

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db['brandon'] = brandon

db.close()
