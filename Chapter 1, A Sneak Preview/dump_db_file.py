# To test further, Example 1-3 reloads the database from a file each time it is run.

from make_db_file import loadDbase
db = loadDbase()
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
