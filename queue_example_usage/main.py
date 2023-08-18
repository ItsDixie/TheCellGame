import threading
import foo
import bababa
from queue import Queue

test = "que pro"
q = Queue()
q.put(test)

threading.Thread(target=foo.run, args=(q,), name='Test1').start()
threading.Thread(target=bababa.run, args=(q,), name='Test2').start()

