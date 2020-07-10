# - * - coding: utf-8 - * -
import threading, apsw
import queue
import sys

class TestThr(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.IQ = queue.Queue()
        self.OQ = queue.Queue()

    def run(self):
        try:
            print("*THREAD: Thread started ")
            while self.IQ.empty():
                pass
            self.IQ.get()
            print("*THREAD: <<< Prepare database")
            conn = apsw.Connection('test.db')
            cursor = conn.cursor()
            try:
                cursor.execute("create table a(a integer)")
                cursor.execute("end")
            except:
                pass
            cursor.execute('begin')
            cursor.execute('delete from a')
            cursor.execute('end')
            print("*THREAD: >>> Prepare database")

            self.OQ.put(1)
            while self.IQ.empty():
                pass
            self.IQ.get()
            print("*THREAD: <<< Fillup 1000 values")
            cursor.execute('begin')
            print("*THREAD: Trans. started")
            for i in range(1000):
                cursor.execute('insert into a values(%d)'%i)
            print("*THREAD: >>> Fillup 1000 values")
            self.OQ.put(1)

            while self.IQ.empty():
                pass
            self.IQ.get()
            cursor.execute('end')
            print("*THREAD: Trans. finished")

            self.OQ.put(1)
            while self.IQ.empty():
                pass
            self.IQ.get()
            print("*THREAD: <<< Fillup 1000 values")
            cursor.execute('begin')
            print("*THREAD: Trans. started")
            for i in range(1000, 2000):
                cursor.execute('insert into a values(%d)' % i)
            print("*THREAD: >>> Fillup 1000 values")
            cursor.execute('end')
            print("*THREAD: Trans. finished")
            self.OQ.put(1)
            while self.IQ.empty():
                pass
            self.IQ.get()
            print(" Thread end")
            self.OQ.put(1)
        except:
            print(sys.exc_info())
            sys.exit()


conn = apsw.Connection('test.db')
cursor = conn.cursor()
t = TestThr()
t.IQ.put(1)
t.start()
while t.OQ.empty(): pass
t.OQ.get()

def ReadLastRec():
    rec = None
    for rec in cursor.execute("select * from a"):
        pass
    print("- MAIN: Read last record", rec)

ReadLastRec()
t.IQ.put(1)
print(" - MAIN : Finished")