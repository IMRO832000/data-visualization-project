import xlrd as xl
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px                        


print("Comparative analysis")
a=int(input("select the year 1-11 for dataset-1"))
b=int(input("select the year 1-11 for dataset-2"))

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
    print('error\n')
    exit()

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
    print("error\n")
    exit()
z='y'
while(z=='y'):
    print("enter the attribute you want to compare from first dataset\n ")
    c=int(input("1.male literate  population\n2.male literacy rate\n3.female literate population\n4.female literacy rate\n5.total literate population\n"))
    print("enter the attribute you want to compare from second dataset\n ")
    d=int(input("1.male literate  population\n2.male literacy rate\n3.female literate population\n4.female literacy rate\n5.total literate population\n"))
    l1=[]
    l2=[]
    if(c==1):
        i=7
        for i in range(7,a1.nrows):
            l1.append(int(a1.cell_value(i,2)))

    elif(c==2):
        i=7
        for i in range(7,a1.nrows):
            l1.append(int(a1.cell_value(i,5)))

    elif(c==3):
        i=7
        for i in range(7,a1.nrows):
            l1.append(int(a1.cell_value(i,3)))
    elif(c==4):
        i=7
        for i in range(7,a1.nrows):
            l1.append(int(a1.cell_value(i,6)))
    elif(c==5):
        i=7
        for i in range(7,a1.nrows):
            l1.append(int(a1.cell_value(i,4)))
    else:
        print('no such option')


    if(d==1):
        i=7
        for i in range(7,a2.nrows):
            l2.append(int(a2.cell_value(i,2)))

    elif(d==2):
        i=7
        for i in range(7,a2.nrows):
            l2.append(int(a2.cell_value(i,5)))

    elif(d==3):
        i=7
        for i in range(7,a2.nrows):
            l2.append(int(a2.cell_value(i,3)))
    elif(d==4):
        i=7
        for i in range(7,a2.nrows):
            l2.append(int(a2.cell_value(i,6)))
    elif(d==5):
        i=7
        for i in range(7,a2.nrows):
            l2.append(int(a2.cell_value(i,4)))
    else:
        print('no such option')
       

    opt=int(input("1.Relative growth graph 2.comparative line graph 3. piechart  4.stacked chart"))
    if opt==1:
        k1=l1.copy()
        k2=l2.copy()
        k1=np.array(k1)
        k2=np.array(k2)
        p=np.subtract(k2,k1)
        l=list(p)
        l=np.array(l)
        yrs=np.array(['Jammu & Kashmir','Himachal Pradesh','Punjab','Chandigarh','Uttarakhand','Haryana','NCT of Delhi', 'Rajasthan','Uttar Pradesh','Bihar','Sikkim','Arunachal Pradesh','Nagaland','Manipur','Mizoram','Tripura','Meghalaya','Assam','West Bengal','Jharkhand','Orissa','Chhatisgarh','Madhya Pradesh','Gujarat','Daman & Diu','Dadra & Nagar Haveli','Maharashtra','Andhra Pradesh','Karnataka','Goa','Lakshadweep','Kerala','Tamil Nadu','Pondicherry','Andaman & Nicobar Islands'])
        print(l)
        plt.rc('font',family='arial',size=15)

        plt.plot(yrs,l,'s',color='blue')
        plt.xlabel('STATES')
        plt.ylabel('GROWTH')
        plt.title('Relative growth analysis')
        plt.show()
        
    elif opt==2:
        sts=np.array(['Jammu & Kashmir','Himachal Pradesh','Punjab','Chandigarh','Uttarakhand','Haryana','NCT of Delhi', 'Rajasthan','Uttar Pradesh','Bihar','Sikkim','Arunachal Pradesh','Nagaland','Manipur','Mizoram','Tripura','Meghalaya','Assam','West Bengal','Jharkhand','Orissa','Chhatisgarh','Madhya Pradesh','Gujarat','Daman & Diu','Dadra & Nagar Haveli','Maharashtra','Andhra Pradesh','Karnataka','Goa','Lakshadweep','Kerala','Tamil Nadu','Pondicherry','Andaman & Nicobar Islands'])
        m1=l1.copy()
        m2=l2.copy()
        m1=np.array(m1)
        m2=np.array(m2)
        plt.plot(sts,m1,label="Year 200{}\n".format(a))
        plt.plot(sts,m2,label="Year 200{}\n".format(b))
        plt.xlabel('States')
        plt.title('Comparative analysis')
        plt.legend()
        plt.show()
        

    elif opt==3:
        g1=l1.copy()
        g2=l2.copy()
        g1=np.array(g1)
        g2=np.array(g2)
        pg=np.subtract(g2,g1)
        lg=list(pg)
        lg=np.array(lg)
        st=['Jammu & Kashmir','Himachal Pradesh','Punjab','Chandigarh','Uttarakhand','Haryana','NCT of Delhi', 'Rajasthan','Uttar Pradesh','Bihar','Sikkim','Arunachal Pradesh','Nagaland','Manipur','Mizoram','Tripura','Meghalaya','Assam','West Bengal','Jharkhand','Orissa','Chhatisgarh','Madhya Pradesh','Gujarat','Daman & Diu','Dadra & Nagar Haveli','Maharashtra','Andhra Pradesh','Karnataka','Goa','Lakshadweep','Kerala','Tamil Nadu','Pondicherry','Andaman & Nicobar Islands']
        e=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        plt.pie(lg,explode=e,labels=st)
        plt.title("Literacy growth analysis chart")
        plt.show()

    elif opt==4:
        sts=['Jammu & Kashmir','Himachal Pradesh','Punjab','Chandigarh','Uttarakhand','Haryana','NCT of Delhi', 'Rajasthan','Uttar Pradesh','Bihar','Sikkim','Arunachal Pradesh','Nagaland','Manipur','Mizoram','Tripura','Meghalaya','Assam','West Bengal','Jharkhand','Orissa','Chhatisgarh','Madhya Pradesh','Gujarat','Daman & Diu','Dadra & Nagar Haveli','Maharashtra','Andhra Pradesh','Karnataka','Goa','Lakshadweep','Kerala','Tamil Nadu','Pondicherry','Andaman & Nicobar Islands']
        m1=l1.copy()
        m2=l2.copy()
        mk1=np.array(m1)
        mk2=np.array(m2)
        plt.bar(sts,m1,color='orange',label='200{}'.format(a),width=1)
        plt.bar(sts,m2,bottom=m1,color='blue',label='200{}'.format(b),width=1)
        plt.legend()
        plt.show()
    z=input('y for generating more graphs or n for moving to next analysis')

       

print("Detailed analysis of state")
q='y'
while(q=='y'):
    st=input("enter the state name")
    op=int(input("1.male literate population analysis\n2.female literate population analysis\n3.male literacy rate analysis\n4.female literacy rate analysis"))

    if op==1:
        h=[]
        f1=xl.open_workbook("l1.xlsx")
        q1=f1.sheet_by_index(0)
        i=7
        for i in range(7,q1.nrows):
            if(st==q1.cell_value(i,0)):
                pos=i
                h.append(q1.cell_value(pos,2))
                

        f2=xl.open_workbook("l2.xlsx")
        q2=f2.sheet_by_index(0)
        i=7
        for i in range(7,q2.nrows):
            if(st==q2.cell_value(i,0)):
                pos=i
                h.append(q2.cell_value(pos,2))


        f3=xl.open_workbook("l3.xlsx")
        q3=f3.sheet_by_index(0)
        i=7
        for i in range(7,q3.nrows):
            if(st==q3.cell_value(i,0)):
                pos=i
                h.append(q3.cell_value(pos,2))

        f4=xl.open_workbook("l4.xlsx")
        q4=f4.sheet_by_index(0)
        i=7
        for i in range(7,q4.nrows):
            if(st==q4.cell_value(i,0)):
                pos=i
                h.append(q4.cell_value(pos,2))

        f5=xl.open_workbook("l5.xlsx")
        q5=f5.sheet_by_index(0)
        i=7
        for i in range(7,q5.nrows):
            if(st==q5.cell_value(i,0)):
                pos=i
                h.append(q5.cell_value(pos,2))

        f6=xl.open_workbook("l6.xlsx")
        q6=f6.sheet_by_index(0)
        i=7
        for i in range(7,q6.nrows):
            if(st==q6.cell_value(i,0)):
                pos=i
                h.append(q6.cell_value(pos,2))

        f7=xl.open_workbook("l7.xlsx")
        q7=f7.sheet_by_index(0)
        i=7
        for i in range(7,q7.nrows):
            if(st==q7.cell_value(i,0)):
                pos=i
                h.append(q7.cell_value(pos,2))

        f8=xl.open_workbook("l8.xlsx")
        q8=f8.sheet_by_index(0)
        i=7
        for i in range(7,q8.nrows):
            if(st==q8.cell_value(i,0)):
                pos=i
                h.append(q8.cell_value(pos,2))


        f9=xl.open_workbook("l9.xlsx")
        q9=f9.sheet_by_index(0)
        i=7
        for i in range(7,q9.nrows):
            if(st==q9.cell_value(i,0)):
                pos=i
                h.append(q9.cell_value(pos,2))


        f10=xl.open_workbook("l10.xlsx")
        q10=f10.sheet_by_index(0)
        i=7
        for i in range(7,q10.nrows):
            if(st==q10.cell_value(i,0)):
                pos=i
                h.append(q10.cell_value(pos,2))

        f11=xl.open_workbook("l11.xlsx")
        q11=f11.sheet_by_index(0)
        i=7
        for i in range(7,q11.nrows):
            if(st==q11.cell_value(i,0)):
                pos=i
                h.append(q11.cell_value(pos,2))
                print(h)

        k=int(input("1.line graph 2.bar plot"))
        if k==1:
            x=[1,2,3,4,5,6,7,8,9,10,11]
            plt.plot(x,h,color='green')
            plt.xlabel("Years 1-11")
            plt.title("Detailed analysis of men of  {}".format(st))
            
            plt.show()



        elif k==2:
            x=[1,2,3,4,5,6,7,8,9,10,11]
            plt.bar(x,h,color="orange",edgecolor='black',width=1)
            plt.show()


    if op==2:
        h=[]
        f1=xl.open_workbook("l1.xlsx")
        q1=f1.sheet_by_index(0)
        i=7
        for i in range(7,q1.nrows):
            if(st==q1.cell_value(i,0)):
                pos=i
                h.append(q1.cell_value(pos,3))
                

        f2=xl.open_workbook("l2.xlsx")
        q2=f2.sheet_by_index(0)
        i=7
        for i in range(7,q2.nrows):
            if(st==q2.cell_value(i,0)):
                pos=i
                h.append(q2.cell_value(pos,3))


        f3=xl.open_workbook("l3.xlsx")
        q3=f3.sheet_by_index(0)
        i=7
        for i in range(7,q3.nrows):
            if(st==q3.cell_value(i,0)):
                pos=i
                h.append(q3.cell_value(pos,3))

        f4=xl.open_workbook("l4.xlsx")
        q4=f4.sheet_by_index(0)
        i=7
        for i in range(7,q4.nrows):
            if(st==q4.cell_value(i,0)):
                pos=i
                h.append(q4.cell_value(pos,3))

        f5=xl.open_workbook("l5.xlsx")
        q5=f5.sheet_by_index(0)
        i=7
        for i in range(7,q5.nrows):
            if(st==q5.cell_value(i,0)):
                pos=i
                h.append(q5.cell_value(pos,3))

        f6=xl.open_workbook("l6.xlsx")
        q6=f6.sheet_by_index(0)
        i=7
        for i in range(7,q6.nrows):
            if(st==q6.cell_value(i,0)):
                pos=i
                h.append(q6.cell_value(pos,3))

        f7=xl.open_workbook("l7.xlsx")
        q7=f7.sheet_by_index(0)
        i=7
        for i in range(7,q7.nrows):
            if(st==q7.cell_value(i,0)):
                pos=i
                h.append(q7.cell_value(pos,3))

        f8=xl.open_workbook("l8.xlsx")
        q8=f8.sheet_by_index(0)
        i=7
        for i in range(7,q8.nrows):
            if(st==q8.cell_value(i,0)):
                pos=i
                h.append(q8.cell_value(pos,3))


        f9=xl.open_workbook("l9.xlsx")
        q9=f9.sheet_by_index(0)
        i=7
        for i in range(7,q9.nrows):
            if(st==q9.cell_value(i,0)):
                pos=i
                h.append(q9.cell_value(pos,3))


        f10=xl.open_workbook("l10.xlsx")
        q10=f10.sheet_by_index(0)
        i=7
        for i in range(7,q10.nrows):
            if(st==q10.cell_value(i,0)):
                pos=i
                h.append(q10.cell_value(pos,3))

        f11=xl.open_workbook("l11.xlsx")
        q11=f11.sheet_by_index(0)
        i=7
        for i in range(7,q11.nrows):
            if(st==q11.cell_value(i,0)):

                pos=i
                h.append(q11.cell_value(pos,3))

        k=int(input("1.line graph 2.bar plot"))
        if k==1:
            x=[1,2,3,4,5,6,7,8,9,10,11]
            plt.plot(x,h,color='green')
            plt.xlabel("Years 1-11")
            plt.title("Detailed analysis of women of{}".format(st))
            
            plt.show()



        elif k==2:
            x=[1,2,3,4,5,6,7,8,9,10,11]
            plt.bar(x,h,color="orange",edgecolor='black',width=1)
            
            plt.show()



    if op==3:
        h=[]
        f1=xl.open_workbook("l1.xlsx")
        q1=f1.sheet_by_index(0)
        i=7
        for i in range(7,q1.nrows):
            if(st==q1.cell_value(i,0)):
                pos=i
                h.append(q1.cell_value(pos,5))
                

        f2=xl.open_workbook("l2.xlsx")
        q2=f2.sheet_by_index(0)
        i=7
        for i in range(7,q2.nrows):
            if(st==q2.cell_value(i,0)):
                pos=i
                h.append(q2.cell_value(pos,5))


        f3=xl.open_workbook("l3.xlsx")
        q3=f3.sheet_by_index(0)
        i=7
        for i in range(7,q3.nrows):
            if(st==q3.cell_value(i,0)):
                pos=i
                h.append(q3.cell_value(pos,5))

        f4=xl.open_workbook("l4.xlsx")
        q4=f4.sheet_by_index(0)
        i=7
        for i in range(7,q4.nrows):
            if(st==q4.cell_value(i,0)):
                pos=i
                h.append(q4.cell_value(pos,5))

        f5=xl.open_workbook("l5.xlsx")
        q5=f5.sheet_by_index(0)
        i=7
        for i in range(7,q5.nrows):
            if(st==q5.cell_value(i,0)):
                pos=i
                h.append(q5.cell_value(pos,5))

        f6=xl.open_workbook("l6.xlsx")
        q6=f6.sheet_by_index(0)
        i=7
        for i in range(7,q6.nrows):
            if(st==q6.cell_value(i,0)):
                pos=i
                h.append(q6.cell_value(pos,5))

        f7=xl.open_workbook("l7.xlsx")
        q7=f7.sheet_by_index(0)
        i=7
        for i in range(7,q7.nrows):
            if(st==q7.cell_value(i,0)):
                pos=i
                h.append(q7.cell_value(pos,5))

        f8=xl.open_workbook("l8.xlsx")
        q8=f8.sheet_by_index(0)
        i=7
        for i in range(7,q8.nrows):
            if(st==q8.cell_value(i,0)):
                pos=i
                h.append(q8.cell_value(pos,5))


        f9=xl.open_workbook("l9.xlsx")
        q9=f9.sheet_by_index(0)
        i=7
        for i in range(7,q9.nrows):
            if(st==q9.cell_value(i,0)):
                pos=i
                h.append(q9.cell_value(pos,5))


        f10=xl.open_workbook("l10.xlsx")
        q10=f10.sheet_by_index(0)
        i=7
        for i in range(7,q10.nrows):
            if(st==q10.cell_value(i,0)):
                pos=i
                h.append(q10.cell_value(pos,5))

        f11=xl.open_workbook("l11.xlsx")
        q11=f11.sheet_by_index(0)
        i=7
        for i in range(7,q11.nrows):
            if(st==q11.cell_value(i,0)):
                pos=i
                h.append(q11.cell_value(pos,5))

        k=int(input("1.line graph 2.bar plot"))
        if k==1:
            x=[1,2,3,4,5,6,7,8,9,10,11]
            plt.plot(x,h,color='green')
            plt.xlabel("Years 1-11")
            plt.title("analysis of effective literacy rate of {}".format(st))
            
            plt.show()



        elif k==2:
            x=[1,2,3,4,5,6,7,8,9,10,11]
            plt.bar(x,h,color="orange",edgecolor='black',width=1)
            plt.title("analysis of effective literacy rate of {}".format(st))
            plt.show()    


    if op==4:
        h=[]
        f1=xl.open_workbook("l1.xlsx")
        q1=f1.sheet_by_index(0)
        i=7
        for i in range(7,q1.nrows):
            if(st==q1.cell_value(i,0)):
                pos=i
                h.append(q1.cell_value(pos,6))
                

        f2=xl.open_workbook("l2.xlsx")
        q2=f2.sheet_by_index(0)
        i=7
        for i in range(7,q2.nrows):
            if(st==q2.cell_value(i,0)):
                pos=i
                h.append(q2.cell_value(pos,6))


        f3=xl.open_workbook("l3.xlsx")
        q3=f3.sheet_by_index(0)
        i=7
        for i in range(7,q3.nrows):
            if(st==q3.cell_value(i,0)):
                pos=i
                h.append(q3.cell_value(pos,6))

        f4=xl.open_workbook("l4.xlsx")
        q4=f4.sheet_by_index(0)
        i=7
        for i in range(7,q4.nrows):
            if(st==q4.cell_value(i,0)):
                pos=i
                h.append(q4.cell_value(pos,6))

        f5=xl.open_workbook("l5.xlsx")
        q5=f5.sheet_by_index(0)
        i=7
        for i in range(7,q5.nrows):
            if(st==q5.cell_value(i,0)):
                pos=i
                h.append(q5.cell_value(pos,6))

        f6=xl.open_workbook("l6.xlsx")
        q6=f6.sheet_by_index(0)
        i=7
        for i in range(7,q6.nrows):
            if(st==q6.cell_value(i,0)):
                pos=i
                h.append(q6.cell_value(pos,6))

        f7=xl.open_workbook("l7.xlsx")
        q7=f7.sheet_by_index(0)
        i=7
        for i in range(7,q7.nrows):
            if(st==q7.cell_value(i,0)):
                pos=i
                h.append(q7.cell_value(pos,6))

        f8=xl.open_workbook("l8.xlsx")
        q8=f8.sheet_by_index(0)
        i=7
        for i in range(7,q8.nrows):
            if(st==q8.cell_value(i,0)):
                pos=i
                h.append(q8.cell_value(pos,6))


        f9=xl.open_workbook("l9.xlsx")
        q9=f9.sheet_by_index(0)
        i=7
        for i in range(7,q9.nrows):
            if(st==q9.cell_value(i,0)):
                pos=i
                h.append(q9.cell_value(pos,6))


        f10=xl.open_workbook("l10.xlsx")
        q10=f10.sheet_by_index(0)
        i=7
        for i in range(7,q10.nrows):
            if(st==q10.cell_value(i,0)):
                pos=i
                h.append(q10.cell_value(pos,6))

        f11=xl.open_workbook("l11.xlsx")
        q11=f11.sheet_by_index(0)
        i=7
        for i in range(7,q11.nrows):
            if(st==q11.cell_value(i,0)):
                pos=i
                h.append(q11.cell_value(pos,6))

        k=int(input("1.line graph 2.bar plot"))
        if k==1:
            x=[1,2,3,4,5,6,7,8,9,10,11]
            plt.plot(x,h,color='green')
            plt.xlabel("Years 1-11")
            plt.title("analysis of effective literacy rate of {}".format(st))
            
            plt.show()



        elif k==2:
            x=[1,2,3,4,5,6,7,8,9,10,11]
            plt.bar(x,h,color="orange",edgecolor='black',width=1)
            plt.axis([0,11,0,max(h)])
            plt.title("analysis of effective literacy rate of {}".format(st))
            plt.show()
    q=input('y for choosing another state for analysis or n to next')




        





 