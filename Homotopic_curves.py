# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:09:44 2020

@author: Unnat Antani

Homotopic curves visualization
"""


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter
import numpy as np


class MyClass:
    
    # def get_constants(self,points):
    #     point1 = points[0]
    #     point2 = points[1]
        
    #     #Quadratic (Please complete it man)
    #     c1 = np.array([[0+point1[1]],[0]]) #for f(x)
    #     c2 = np.array([[100],[100]])#for g(x)

    #     X_1 = np.array([[point1[0]**2,point1[0]],[point2[0]**2,point2[0]]])
        
    def __init__(self, frame):
        self.frame = frame
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)
        self.slider = tkinter.Scale(master=root,from_=-500 , to=500,troughcolor = 'cyan',length = 500, orient='horizontal', command=self.plot_graph)
        self.slider.pack()

    def plot_graph(self,sldr):
        t = float(sldr)/500
        x = np.linspace(2,20,50,True)
        y = (1-t)*((5/36)*(x**2) +(20/9)*x) + t*((95/36)*(x**2) + (-950/18)*x + 100) #Use constant values automatically so dont have to manually calculate the constants for any two points
        a = (1-t)*(5/36) + t*(95/36)#make before by calling get constants
        b = (1-t)*(20/9) - t*(950/18)#same
        c = (t*100)#same
        # print(a,b,c)
        lbl = "{0:.2f}x^2".format(a) + "+ {0:.2f}x".format(b) + " + {0:.2f}".format(c)
    
       
        self.ax.cla()
        self.ax.set_xlim(0,25)
        
        clr = "red"
        
        self.ax.plot(x, y,color = clr, label = lbl)
        self.ax.legend(loc='upper left', bbox_to_anchor=(0.2, 1.00), shadow=True, ncol=1)
        self.ax.scatter([2,20],[5,100])
        self.ax.set_ylim(-200,300)
        self.canvas.draw()


root = tkinter.Tk()
root.title("Homotopy of two curves")
MyFrame = tkinter.Frame(root)
MyClass(MyFrame)
MyFrame.pack()
root.mainloop()


