import threading
import queue

import graphics
import cells
import perceptron

threading.Thread(target=graphics.run, name='GraphicsRender').start()
threading.Thread(target=perceptron.run, name='PerceptroneCalc').start()
#threading.Thread(target=cells.run, name='GraphicsRender').start()
queue = queue.Queue
#queue.put(var) - добавить переменную