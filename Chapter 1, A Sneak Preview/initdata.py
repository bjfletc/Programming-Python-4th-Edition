# initialize data to be stored in files, pickles, shelves

# records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}
brandon = {'name': 'Brandon Fletcher', 'age': 24, 'pay': 20000, 'job': 'dev'}

# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db['brandon'] = brandon

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n ', db[key])
