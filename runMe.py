# Author: Albert Luna
# Copying of this code is prohibited.
# Github: https://github.com/A-Luna05

import GUI
import threading
root = GUI.newsAggregate()
x = threading.Thread(target = root.loadRest,args= ())
x.start()
root.geometry("1100x625")
root.mainloop()