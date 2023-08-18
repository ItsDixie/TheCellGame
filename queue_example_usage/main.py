import threading
import foo
import bababa
from collections import deque

test = "que pro"
q = deque()
q.append(test)

threading.Thread(target=bababa.run, args=(q,), name='Test2').start()
threading.Thread(target=foo.run, args=(q,), name='Test1').start()

print(q)

