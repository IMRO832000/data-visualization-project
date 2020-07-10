import xlrd as xl
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
l1=[]
def att1(f,c):
    if(c==1):
        i=7
        for i in range(7,f.nrows):
            l1.append(int(f.cell_value(i,2)))

    elif(c==2):
        i=7
        for i in range(7,f.nrows):
            l1.append(int(f.cell_value(i,5)))

    elif(c==3):
        i=7
        for i in range(7,f.nrows):
            l1.append(int(f.cell_value(i,3)))
    elif(c==4):
        i=7
        for i in range(7,f.nrows):
            l1.append(int(f.cell_value(i,6)))
    elif(c==5):
        i=7
        for i in range(7,f.nrows):
            l1.append(int(f.cell_value(i,4)))
    else:
        exit()
    return(l1)
l2=[]
def att2(g,d):
    if(d==1):
        i=7
        for i in range(7,g.nrows):
            l2.append(int(g.cell_value(i,2)))

    elif(d==2):
        i=7
        for i in range(7,g.nrows):
            l2.append(int(g.cell_value(i,5)))

    elif(d==3):
        i=7
        for i in range(7,g.nrows):
            l2.append(int(g.cell_value(i,3)))
    elif(d==4):
        i=7
        for i in range(7,g.nrows):
            l2.append(int(g.cell_value(i,6)))
    elif(d==5):
        i=7
        for i in range(7,g.nrows):
            l2.append(int(g.cell_value(i,4)))
    else:
        exit()
    return(l2)