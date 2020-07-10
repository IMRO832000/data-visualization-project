import xlrd as xl
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, jsonify, request, render_template, Markup, json, session, redirect, url_for,session
import io
import base64
from  funf import ds1,ds2
from dc import att1,att2
import json

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"]=True

@app.route('/')
def data():
   return render_template('data.html')
   

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      global result
      result = request.form
      global a
      global b
      global c
      global d
      a=int(result["dataset-1"])
      b=int(result["dataset-2"])
      c=int(result["Attribute-1"])
      d=int(result["Attribute-2"])
      global l
      global k 
      f=ds1(a)
      g=ds2(b)
      k=att1(f,c)
      l=att2(g,d)
      global p
      global k1
      global k2
      k1=l.copy()
      k2=k.copy()
      k1=np.array(k1)
      k2=np.array(k2)
      p=np.subtract(k1,k2)
      p=list(p)
      global label
      label=['Jammu and Kashmir','Himachal Pradesh','Punjab','Chandigarh','Uttarakhand','Haryana','NCT of Delhi', 'Rajasthan','Uttar Pradesh','Bihar','Sikkim','Arunachal Pradesh','Nagaland','Manipur','Mizoram','Tripura','Meghalaya','Assam','West Bengal','Jharkhand','Orissa','Chhatisgarh','Madhya Pradesh','Gujarat','Daman and Diu','Dadra and Nagar Haveli','Maharashtra','Andhra Pradesh','Karnataka','Goa','Lakshadweep','Kerala','Tamil Nadu','Pondicherry','Andaman and Nicobar Islands']
      global at1,at2
      if(c==1):
         at1="male literate  population"
      elif(c==2):
         at1="male literacy rate"
      
      elif(c==3):
         at1="female literate population"
      
      elif(c==4):
         at1="female literacy rate"
      
      elif(c==5):
         at1="total literate population"
      
      if(d==1):
         at2="male literate  population"
      
      elif(d==2):
         at2="male literacy rate"
      
      elif(d==3):
         at2="female literate population"
      
      elif(d==4):
         at2="female literacy rate"
      
      elif(d==5):
         at2="total literate population"
      

      return render_template('result.html',result = result,a=a,b=b,c=c,d=d,p=p,k=k1,l=k2,label=label)



@app.route('/lc')
def lc():
   return render_template("gr.html",k=k,l=l,p=p,label=label,a=a,b=b,c=c,d=d,at1=at1,at2=at2)

@app.route('/pie')
def hst():
   return render_template("pie.html",k=k,l=l,label=label,p=p,at1=at1,at2=at2,a=a,b=b,c=c,d=d)

@app.route('/bplot')
def bplot():
   return render_template("bplot.html",k=k,l=l,p=p,label=label,at1=at1,at2=at2,a=a,b=b,c=c,d=d)
   
@app.route('/mlc')
def mlc():
   return render_template("mlc.html",k=k,l=l,p=p,label=label,at1=at1,at2=at2,a=a,b=b,c=c,d=d)

@app.route('/scplt')   
def scplt():
   return render_template("scplt.html",k=k,l=l,p=p,label=label,at1=at1,at2=at2,a=a,b=b,c=c,d=d)
if __name__ == '__main__':
   app.run(debug=True)
   

