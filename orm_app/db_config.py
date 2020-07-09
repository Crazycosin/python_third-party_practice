DBNAME = 'test_db'
NAMELEN = 256
FIELDS = ['user', 'id']

def randName():
    return [('jane', 1), ('mike', 2)]

def setup():
    return 'mysql'

def tformat(a):
    return str(a)

def cformat(a):
    return a