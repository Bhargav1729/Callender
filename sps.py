from tkinter import *
import pickle as p
try:
   f=open("callenderdetails.dat","rb")
   xi=p.load(f)
   f.close()
except:
   open("callenderdetails.dat","wb").close()
   xi={}#mmddyyyyformat
def dayfrom_month(m: int,l=False):
    m-=1
    if m==0:
        x=0
    elif m==1:
        x=31
    elif m==2:
        x=59
    elif m==3:
        x=90
    elif m==4:
        x=120
    elif m==5:
        x=151
    elif m==6:
        x=181
    elif m==7:
        x=212
    elif m==8:
        x=243
    elif m==9:
        x=273
    elif m==10:
        x=304
    elif m==11:
        x=334
    else:
        return None
    if l and m>=2:
        return x+1
    else:
        return x
def dayfrom_year(y):
    y-=1
    return (y//4*366)+((y-y//4)*365)-((y%100)*366)+((y%100)*365)-((y%400)*365)+((y%400)*366)

window=Tk()
window.minsize(width=500,height=500)
window.title("Personal calender")
def matrix(y,m):
   l=False
   if (y%4!=0 and y%100) or (y%400!=0):
      l=True
   x=(dayfrom_month(m,l)+dayfrom_year(y)+1)%7
   mat=[]
   d=1
   m=[31,28,31,30,31,30,31,31,30,31,30,31][m-1]
   if l and m==2:
      m+=1
   while d<=m:
      temp=[]
      while x<7 and d<=m:
         x+=1
         temp.append(d)
         d+=1
      mat.append(temp)
      x=0
   while len(mat[0])!=7:
      mat[0].insert(0,0)
   while len(mat[-1])!=7:
      mat[-1].append(0)
   while len(mat)<7:
      mat.append([0,0,0,0,0,0,0])
   return mat


def mpage(yy=2025,mm=9):
   for i in window.winfo_children():
      i.destroy()
   window.minsize(width=500,height=500)
   window.maxsize(width=500,height=500)
   Label(text="sat  sun  mon  tue  wed   thu  fri",fg="red",font=("Times New Roman", 17)).place(x=120,y=100)
   yl=Label(text=str(yy),fg="green",font=(30))
   yl.place(x=240,y=10)
   ml=Label(text=["January","February","March","April","May","June","July","August","September","October","November","December"][mm-1],fg="green",font=(30))
   ml.place(x=210,y=50)
   def edit(d:int,o:Button):
      nonlocal mm,yy
      if d!=0:
         lk=xi.get(str(mm)+str(int(d))+str(yy))
         if lk==None or lk=="":
            l=""
         else:
            l=lk
      else :
         return None
      global lab,db
      try:
         lab.destroy()
         db.destroy()
      except:
         pass
      text = StringVar() 
      text.set(l)
      lm=Entry(width=35,textvariable=text,font=("Times New Roman", 17))
      lm.place(x=50,y=400)
      def save():
         xi[str(mm)+str(int(d))+str(yy)]=lm.get()
         o.config(fg="green")
         global db
         db=Button(text="DELETE")
         db.config(command=lambda x=db:delete(db))
         db.place(x=10,y=450)
      def delete(ox):
         xi.pop(str(mm)+str(int(d))+str(yy))
         o.config(fg="black")
         text.set("")
         lm.config(textvariable=text)
         ox.destroy()
      Button(text="SAVE",command=save).place(x=450,y=450)
      x=0
      if lk != None:
         db=Button(text="DELETE")
         db.config(command=lambda x=db:delete(db))
         db.place(x=10,y=450)
      
      lab=Label(text=str(d)+"/"+str(mm)+"/"+str(yy))
      lab.place(x=0,y=350)
      for i in xi.copy():
         if xi[i]=="" or xi[i]==None:
            xi.pop(i)
   def fy():
      nonlocal yy
      yy+=1
      x=matrix(yy,mm)
      yl.config(text=str(yy))
      for i,a in zip(objs,x):
         for j,b in zip(i,a):
            temp=str(b)
            if len(temp)==1:
               temp="0"+temp
            if b==0:
               temp="__"
            j.config(text=temp,fg="black",command=lambda b=b,j=j:edit(b,j))
      l=check(x)
      for i in l:
         for j in objs:
            for k in j:
               try:
                  if i==int(k.cget("text")):
                     k.config(fg="green",command=lambda b=i,k=k:edit(b,k))
               except:
                  pass
   def by():
      nonlocal yy
      yy-=1
      x=matrix(yy,mm)
      yl.config(text=str(yy))
      for i,a in zip(objs,x):
         for j,b in zip(i,a):
            temp=str(b)
            if len(temp)==1:
               temp="0"+temp
            if b==0:
               temp="__"
            j.config(text=temp,fg="black",command=lambda b=b,j=j:edit(b,j))
      l=check(x)
      for i in l:
         for j in objs:
            for k in j:
               try:
                  if i==int(k.cget("text")):
                     k.config(fg="green",command=lambda b=i,o=k:edit(b,o))
               except:
                  pass
   def fm():
      nonlocal mm
      nonlocal yy
      if mm==12:
         mm=1
         yy+=1
      else:
         mm+=1
      yl.config(text=str(yy))
      ml.config(text=["January","February","March","April","May","June","July","August","September","October","November","December"][mm-1])
      x=matrix(yy,mm)
      for i,a in zip(objs,x):
         for j,b in zip(i,a):
            temp=str(b)
            if len(temp)==1:
               temp="0"+temp
            if b==0:
               temp="__"
            j.config(text=temp,fg="black",command=lambda b=b,j=j:edit(b,j))
      l=check(x)
      for i in l:
         for j in objs:
            for k in j:
               try:
                  if i==int(k.cget("text")):
                     k.config(fg="green",command=lambda b=i,j=k:edit(b,j))
               except:
                  pass
   def bm():
      nonlocal mm
      nonlocal yy
      if mm==1:
         mm=12
         yy-=1
      else:
         mm-=1
      x=matrix(yy,mm)
      yl.config(text=str(yy))
      ml.config(text=["January","February","March","April","May","June","July","August","September","October","November","December"][mm-1])
      for i,a in zip(objs,x):
         for j,b in zip(i,a):
            temp=str(b)
            if len(temp)==1:
               temp="0"+temp
            if b==0:
               temp="__"
            j.config(text=temp,fg="black",command=lambda b=b,j=j:edit(b,j))
      l=check(x)
      for i in l:
         for j in objs:
            for k in j:
               try:
                  if i==int(k.cget("text")):
                     k.config(fg="green",command=lambda b=i,j=k:edit(b,j))
               except:
                  pass
   def check(m):
      nonlocal mm,yy
      for i in m:
         for j in i:
            if str(mm)+str(j)+str(yy) in xi:
               yield j
               
      
   y=140
   objs=[]
   for i in range(7):
      x=120
      tempo=[]
      for j in range(7):
         tempd="__"
         temp=Button(text=tempd,font=(20),fg="red")
         temp.place(x=x,y=y)
         tempo.append(temp)
         x+=45
      objs.append(tempo)
      y+=35
   by()
   
   Button(text=">",font=20,command=fy).place(x=300,y=10)
   Button(text="<",font=20,command=by).place(x=200,y=10)
   Button(text=">",font=20,command=fm).place(x=329,y=50)
   Button(text="<",font=20,command=bm).place(x=170,y=50)
mpage()
mainloop() 
for i in xi.copy():
   if xi[i]=="" or xi[i]==None:
      xi.pop(i)
x=open("callenderdetails.dat","wb")
p.dump(xi,x)
x.close()