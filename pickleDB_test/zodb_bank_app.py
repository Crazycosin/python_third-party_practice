# - * - coding: utf-8 - * -
from ZODB import (
    FileStorage as ZFS,
    DB)
import transaction
from zodb_bank_customer import  Account


class ZODBUtils:

    conn = None
    file_storage = None

    def open_connection(self, file_name):
        self.file_storage = ZFS.FileStorage(file_name)
        db = DB(self.file_storage)
        self.conn = db.open()
        return self.conn

    def close_connection(self):
        self.conn.close()
        self.file_storage.close()


def init_balance():
    zodb_utils = ZODBUtils()
    conn = zodb_utils.open_connection('./db_location/zodb_bank.db')
    root = conn.root()

    noah = Account('noah', 1000)
    print(noah)
    root['noah'] = noah

    jermy = Account('jermy', 2000)
    print(jermy)
    root['jermy'] = jermy

    transaction.commit()
    zodb_utils.close_connection()


def app():
    zodb_utils = ZODBUtils()
    conn = zodb_utils.open_connection('./db_location/zodb_bank.db')
    root = conn.root()
    noah = root['noah']
    print('Before Deposit Or Withdraw')
    print('-'*30)
    print(noah)
    jermy = root['jermy']
    print(jermy)
    print('-'*30)

    transaction.begin()
    noah.deposit(300)
    jermy.withdraw(300)
    transaction.commit()

    print('After Deposit Or Withdraw')
    print('-' * 30)
    print(noah)
    print(jermy)
    print('-' * 30)

if __name__ == "__main__":
    init_balance()
    app()