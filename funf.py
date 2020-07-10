import xlrd as xl
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


def ds1(a):
    if(a==1):
        d1=xl.open_workbook('l1.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==2):
        d1=xl.open_workbook('l2.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==3):
        d1=xl.open_workbook('l3.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==4):
        d1=xl.open_workbook('l4.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==5):
        d1=xl.open_workbook('l5.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==6):
        d1=xl.open_workbook('l6.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==7):
        d1=xl.open_workbook('l7.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==8):
        d1=xl.open_workbook('l8.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==9):
        d1=xl.open_workbook('l9.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==10):
        d1=xl.open_workbook('l10.xlsx')
        a1=d1.sheet_by_index(0)
    elif(a==11):
        d1=xl.open_workbook('l11.xlsx')
        a1=d1.sheet_by_index(0)
    else:
        exit()
    return(a1)    

def ds2(b):
    if(b==1):
        d2=xl.open_workbook('l1.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==2):
        d2=xl.open_workbook('l2.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==3):
        d2=xl.open_workbook('l3.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==4):
        d2=xl.open_workbook('l4.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==5):
        d2=xl.open_workbook('l5.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==6):
        d2=xl.open_workbook('l6.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==7):
        d2=xl.open_workbook('l7.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==8):
        d2=xl.open_workbook('l8.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==9):
        d2=xl.open_workbook('l9.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==10):
        d2=xl.open_workbook('l10.xlsx')
        a2=d2.sheet_by_index(0)
    elif(b==11):
        d2=xl.open_workbook('l11.xlsx')
        a2=d2.sheet_by_index(0)
    else:
        exit()
    return(a2)


   
    