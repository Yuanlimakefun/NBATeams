# -*- encoding:utf-8 -*-

import tkinter as tk
from app_frame import AppFrame


root = tk.Tk()
root.title('NBA球队信息')
root.wm_state('zoomed')
#root.resizable(False, False)

AppFrame(root)

root.mainloop()
