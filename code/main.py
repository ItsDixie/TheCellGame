import threading
from collections import deque
from time import sleep
import graphics
import perceptron

q = deque()
#queue.put(var) - добавить переменную

threading.Thread(target=graphics.run, name='GraphicsRender', args=(q,)).start()
sleep(1)
threading.Thread(target=perceptron.run, name='PerceptronCalc', args=(q,)).start()
#threading.Thread(target=cells.run, name='GraphicsRender').start()

