from cgitb import text
from distutils import command
from itertools import count
from pydoc import describe
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io

def reset():
  global root
  root.destroy()

root=Tk()
root.geometry("1360x730")
root.resizable(False, False)
root.title("F-Billing Revolution 2022(FREE version) | Company database:fbillingdb | User:Administrator")
p1 = PhotoImage(file = 'images/fbicon.png')
root.iconphoto(False, p1)


s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="#999999", width=20, padding=10)
invoices= PhotoImage(file="images/invoice.png")
orders = PhotoImage(file="images/order.png")
estimates = PhotoImage(file="images/estimate.png")
recurring = PhotoImage(file="images/recurring.png")
purchase = PhotoImage(file="images/purchase.png")
expenses = PhotoImage(file="images/expense.png")
customer = PhotoImage(file="images/customer.png")
product = PhotoImage(file="images/package.png")
reports = PhotoImage(file="images/report.png")
setting = PhotoImage(file="images/setting.png")
tick = PhotoImage(file="images/check.png")
warnin = PhotoImage(file="images/sign_warning.png")
cancel = PhotoImage(file="images/close.png")
saves = PhotoImage(file="images/save.png")
folder = PhotoImage(file="images/folder-black.png")
photo11 = PhotoImage(file = "images/invoice-pvt.png")
customer = PhotoImage(file="images/customer.png")
smslog = PhotoImage(file = "images/smslog.png")
video = PhotoImage(file = "images/video.png")
mark1 = PhotoImage(file="images/mark.png")
mark2 = PhotoImage(file="images/mark2.png")
photo10 = PhotoImage(file = "images/text-message.png")
addnew = PhotoImage(file="images/plus.png")
delete = PhotoImage(file="images/delete_E.png")
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3=  ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6=  ttk.Frame(tabControl)
tab7 = ttk.Frame(tabControl)
tab8 = ttk.Frame(tabControl)
tab9 =  ttk.Frame(tabControl)
tab10=  ttk.Frame(tabControl)
tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoices',)
tabControl.add(tab2,image=orders,compound = LEFT, text ='Orders')
tabControl.add(tab3,image=estimates,compound = LEFT, text ='Estimates')
tabControl.add(tab4,image=recurring,compound = LEFT, text ='Recurring')
tabControl.add(tab5,image=purchase,compound = LEFT, text ='Purchase Orders') 
tabControl.add(tab6,image=expenses,compound = LEFT, text ='Expenses')
tabControl.add(tab7,image=customer,compound = LEFT, text ='Customers')
tabControl.add(tab8,image=product,compound = LEFT, text ='Product/Services')
tabControl.add(tab9,image=reports,compound = LEFT, text ='Report')
tabControl.add(tab10,image=setting,compound = LEFT, text ='Settings')
tabControl.pack(expand = 1, fill ="both")


selectall = PhotoImage(file="images/table_select_all.png")
cut = PhotoImage(file="images/cut.png")
copy = PhotoImage(file="images/copy.png")
paste = PhotoImage(file="images/paste.png")

undo = PhotoImage(file="images/undo.png")
redo = PhotoImage(file="images/redo.png")
bold = PhotoImage(file="images/bold.png")

italics = PhotoImage(file="images/italics.png")
underline = PhotoImage(file="images/underline.png")
left = PhotoImage(file="images/left.png")

right = PhotoImage(file="images/right.png")
center = PhotoImage(file="images/center.png")
hyperlink = PhotoImage(file="images/hyperlink.png")
remove = PhotoImage(file="images/eraser.png")


photo = PhotoImage(file = "images/plus.png")
photo1 = PhotoImage(file = "images/edit.png")
photo2 = PhotoImage(file = "images/delete_E.png")
photo3 = PhotoImage(file = "images/export-file.png")
photo4 = PhotoImage(file = "images/seo.png")
photo5 = PhotoImage(file = "images/printer.png")
photo6 = PhotoImage(file = "images/gmail.png")
photo7 = PhotoImage(file = "images/priewok.png")
photo8 = PhotoImage(file = "images/refresh_E.png")
photo9 = PhotoImage(file = "images/sum.png")
photo10 = PhotoImage(file = "images/text-message.png")


def check_empty() :
     if entry.get():
         pass     #your function where you want to jump
     else:
        messagebox.showinfo("Information", "Required entry")
#FIRST MODULE
#Estimate MODULE

#create new order

def create():
  pop=Toplevel(midFrame)
  pop.title("Estimate")
  pop.geometry("950x690+150+0")

  #select customer
  def custom():
    cuselection=Toplevel()
    cuselection.title("Select Customer")
    cuselection.geometry("930x650+240+10")
    cuselection.resizable(False, False)


    #add new customer
    def create1():
      ven=Toplevel(midFrame)
      ven.title("Add new vendor")
      ven.geometry("930x650+240+10")
      checkvar1=IntVar()
      checkvar2=IntVar()
      radio=IntVar()
      createFrame=Frame(ven, bg="#f5f3f2", height=650)
      createFrame.pack(side="top", fill="both")
      labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
      labelframe1.place(x=10,y=5,width=910,height=600)
      text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
      e1=Entry(labelframe1,width=25).place(x=150,y=10)
      text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
      e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
      text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
      Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
      
      labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
      labelframe2.place(x=5,y=40,width=420,height=150)
      name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
      e1 = Entry(labelframe2,width=28).place(x=130,y=5)
      addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
      e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
      
      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

      labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
      labelframe3.place(x=480,y=40,width=420,height=150)
      name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe3,width=28).place(x=130,y=5)
      addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
      e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
      
      labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe4.place(x=5,y=195,width=420,height=150)
      name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe4,width=28).place(x=130,y=5)
      email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
      e2 = Entry(labelframe4,width=28).place(x=130,y=35)
      tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe4,width=11).place(x=130,y=65)
      fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe4,width=11).place(x=280,y=65)
      sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
      e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

      
      labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
      labelframe5.place(x=480,y=195,width=420,height=125)
      name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe5,width=28).place(x=130,y=5)
      email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe5,width=28).place(x=130,y=35)
      tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe5,width=11).place(x=130,y=65)
      fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe5,width=11).place(x=280,y=65)

      labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe6.place(x=5,y=350,width=420,height=100)
      Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
      tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
      e1 = Entry(labelframe6,width=10).place(x=290,y=5)
      discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe6,width=10).place(x=100,y=35)

      labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe7.place(x=480,y=330,width=420,height=100)
      country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe7,width=28).place(x=130,y=5)
      city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe7,width=28).place(x=130,y=35)

      labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
      labelframe8.place(x=5,y=460,width=420,height=100)
      R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
      R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
      R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
      

      labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
      labelframe9.place(x=480,y=430,width=420,height=150)
      e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

      btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
      btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
        
               

    enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(cuselection, width=20).place(x=110, y=10)
    text=Label(cuselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(cuselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(cuselection, height=27)
    cusventtree["columns"]=["1","2","3", "4"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=140)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="Customer/Ventor ID")
    cusventtree.heading("2",text="Customer/Ventor Name")
    cusventtree.heading("3",text="Tel.")
    cusventtree.heading("4",text="Contact Person")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(cuselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(cuselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )

    btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=create1).place(x=250, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=create1).place(x=435, y=610)
    btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   



    

  #add new line item
  def newline():
    newselection=Toplevel()
    newselection.title("Select Customer")
    newselection.geometry("930x650+240+10")
    newselection.resizable(False, False)


    #add new product
    def product():  
      top = Toplevel()  
      top.title("Add a new Product/Service")
      p2 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p2)
    
      top.geometry("700x550+390+15")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
     
      tabControl.add(tab1,compound = LEFT, text ='Product/Service')
      tabControl.add(tab2,compound = LEFT, text ='Product Image')
     
      tabControl.pack(expand = 1, fill ="both")
     
      innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

      code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      code1.place(x=20,y=0)
      codeentry = Entry(Customerlabelframe,width=35)
      codeentry.place(x=120,y=8)

      checkvarStatus=IntVar()
      status1=Label(Customerlabelframe,text="Status:")
      status1.place(x=500,y=8)
      Button1 = Checkbutton(Customerlabelframe,
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                       
                        width = 10)

      Button1.place(x=550,y=5)

      category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
      category1.place(x=20,y=40)
      n = StringVar()
      country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
       
      country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
      
      country.place(x=120,y=45)
      country.current(0)


      name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
      name1.place(x=20,y=70)
      nameentry = Entry(Customerlabelframe,width=60)
      nameentry.place(x=120,y=75)

      des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
      des1.place(x=20,y=100)
      desentry = Entry(Customerlabelframe,width=60)
      desentry.place(x=120,y=105)

      uval = IntVar(Customerlabelframe, value='$0.00')
      unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      unit1.place(x=20,y=130)
      unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
      unitentry.place(x=120,y=135)

      pcsval = IntVar(Customerlabelframe, value='$0.00')
      pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      pcs1.place(x=320,y=140)
      pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
      pcsentry.place(x=410,y=140)

      costval = IntVar(Customerlabelframe, value='$0.00')
      cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
      cost1.place(x=20,y=160)
      costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
      costentry.place(x=120,y=165)

      priceval = IntVar(Customerlabelframe, value='$0.00')
      price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
      price1.place(x=20,y=190)
      priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
      priceentry.place(x=120,y=195)

      checkvarStatus2=IntVar()
     
      Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                        text="Taxable Tax1rate",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        height=2,
                        width = 12)

      Button2.place(x=415,y=170)


      checkvarStatus3=IntVar()
     
      Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                        text="No stock Control",
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      Button3.place(x=40,y=220)


      stockval = IntVar(Customerlabelframe)
      stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
      stock1.place(x=90,y=260)
      stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
      stockentry.place(x=150,y=265)

      lowval = IntVar(Customerlabelframe)
      low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      low1.place(x=300,y=260)
      lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
      lowentry.place(x=495,y=265)

     
      ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
      ware1.place(x=60,y=290)
      wareentry = Entry(Customerlabelframe,width=50)
      wareentry.place(x=150,y=295)

      text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      text1.place(x=20,y=330)

      txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
      txt.place(x=32,y=358)




      okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
      okButton.pack(side=LEFT)

      cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
      cancelButton.pack(side=RIGHT)

      imageFrame = Frame(tab2, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse')
      browsebutton.place(x=580,y=30,height=30,width=50)
      
      removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
      removeButton.place(x=400,y=450)



    
                    
    enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(newselection, width=20).place(x=110, y=10)
    text=Label(newselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(newselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(newselection, height=27)
    cusventtree["columns"]=["1","2","3", "4","5"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=70)
    cusventtree.column("5", width=70)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="ID/SKU")
    cusventtree.heading("2",text="Product/Service Name")
    cusventtree.heading("3",text="Unit price")
    cusventtree.heading("4",text="Service")
    cusventtree.heading("5",text="Stock")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(newselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(newselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )
   

    btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
    btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



  #preview new line
  def previewline():
    messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


  
  #sms notification
  def sms1():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 



  
  #delete line item  
  def delete1():
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")
    
    

  firFrame=Frame(pop, bg="#f5f3f2", height=60)
  firFrame.pack(side="top", fill=X)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=custom)
  create.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=newline)
  add.pack(side="left", pady=3, ipadx=4)

  dele= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=delete1)
  dele.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  prev= Button(firFrame,compound="top", text="Preview\nEstimate",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline)
  prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(firFrame,compound="top", text="Print \nEstimate",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(firFrame,compound="top", text="Email\nEstimate",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=emailord)
  mail.pack(side="left", pady=3, ipadx=4)

  sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms1)
  sms1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  calc.pack(side="left", pady=3, ipadx=4)

  fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
  fir1Frame.pack(side="top", fill=X)

  labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)
  order = Label(labelframe1, text="Estimate to").place(x=10,y=5)
  e1 = ttk.Combobox(labelframe1, value="Hello",width=28).place(x=80,y=5)
  address=Label(labelframe1,text="Address").place(x=10,y=30)
  e2=Text(labelframe1,width=23).place(x=80,y=30,height=70)
  ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
  e3=Entry(labelframe1,width=30).place(x=402,y=3)
  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  e4=Text(labelframe1,width=23).place(x=402,y=30,height=70)

  btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
  
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  email=Label(labelframe2,text="Email").place(x=10,y=5)
  e5=Entry(labelframe2,width=30).place(x=80,y=5)
  sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
  e6=Entry(labelframe2,width=30).place(x=402,y=5)
    
  labelframe = LabelFrame(fir1Frame,text="Estimate",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)
  order=Label(labelframe,text="Estimate#").place(x=5,y=5)
  e1=Entry(labelframe,width=25).place(x=100,y=5,)
  orderdate=Label(labelframe,text="Estimate date").place(x=5,y=33)
  e2=Entry(labelframe,width=20).place(x=150,y=33)
  checkvarStatus5=IntVar()
  duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
  e3=Entry(labelframe,width=20).place(x=150,y=62)
  terms=Label(labelframe,text="Terms").place(x=5,y=92)
  e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  e1=Entry(labelframe,width=27).place(x=100,y=118)

  fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
  
  tree=ttk.Treeview(listFrame)
  tree["columns"]=["1","2","3","4","5","6","7","8"]

  tree.column("#0", width=40)
  tree.column("1", width=80)
  tree.column("2", width=190)
  tree.column("3", width=190)
  tree.column("4", width=80)
  tree.column("5", width=60)
  tree.column("6", width=60)
  tree.column("7", width=60)
  tree.column("8", width=80)
  
  tree.heading("#0")
  tree.heading("1",text="ID/SKU")
  tree.heading("2",text="Product/Service")
  tree.heading("3",text="Description")
  tree.heading("4",text="Unit Price")
  tree.heading("5",text="Quality")
  tree.heading("6",text="Pcs/Weight")
  tree.heading("7",text="Tax1")
  tree.heading("8",text="Price")
  
  tree.pack(fill="both", expand=1)
  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

  fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  orderFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
  
  myNotebook.add(orderFrame,compound="left", text="Estimate")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both")  

  labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=800,height=170)
  cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  e1=ttk.Combobox(labelframe1, value="",width=20).place(x=115,y=5)
  rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  e2=Entry(labelframe1,width=6).place(x=460,y=5)
  cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  e3=Entry(labelframe1,width=10).place(x=115,y=35)
  tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
  e4=Entry(labelframe1,width=7).place(x=460,y=35)
  template=Label(labelframe1,text="Template").place(x=37,y=70)
  e5=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
  sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  e6=Entry(labelframe1,width=18).place(x=115,y=100)
  category=Label(labelframe1,text="Category").place(x=300,y=100)
  e7=Entry(labelframe1,width=22).place(x=370,y=100)
  
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
  on1=Label(statusfrme, text="Emailed on:").place( y=50)
  nev1=Label(statusfrme, text="Never").place(x=100,y=50)
  on2=Label(statusfrme, text="Printed on:").place( y=90)
  nev2=Label(statusfrme, text="Never").place(x=100,y=90)

  text1=Label(headerFrame,text="Title text").place(x=50,y=5)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
  text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
  text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

  text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
  e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

  e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

  e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

  btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
  text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  cusventtree=ttk.Treeview(documentFrame, height=5)
  cusventtree["columns"]=["1","2","3"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=250)
  cusventtree.column("2", width=250)
  cusventtree.column("2", width=200)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Attach to Email")
  cusventtree.heading("2",text="Filename")
  cusventtree.heading("3",text="Filesize")  
  cusventtree.place(x=50, y=45)
  

  fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme.place(x=0,y=0,width=200,height=170)
  discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
  discount1=Label(summaryfrme, text="$0.00").place(x=130 ,y=0)
  sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
  sub1=Label(summaryfrme, text="$0.00").place(x=130 ,y=21)
  tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
  tax1=Label(summaryfrme, text="$0.00").place(x=130 ,y=42)
  cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
  cost=Label(summaryfrme, text="$0.00").place(x=130 ,y=63)
  order=Label(summaryfrme, text="Order total").place(x=0 ,y=84)
  order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)
  total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
  total1=Label(summaryfrme, text="$0.00").place(x=130 ,y=105)
  balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
  balance1=Label(summaryfrme, text="$0.00").place(x=130 ,y=126)

  fir5Frame=Frame(pop,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
  btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)




#printselected order
  
def printsele():

  def property1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 15, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy count:").place(x=55, y=95)

      okbtn=Button(propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
      canbtn=Button(propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
      
      


    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=property2).place(x=550, y=380)
    btn=Button(property_Frame,compound = LEFT,image=tick  ,text="OK", width=60,).place(x=430, y=420)
    btn=Button(property_Frame,compound = LEFT,image=cancel , text="Cancel", width=60,).place(x=550, y=420)     


    
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=370)
      canbtn=Button(print1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=370)
      


#email
      
def emailord():
  mailDetail=Toplevel()
  mailDetail.title("Orders E-Mail")
  p2 = PhotoImage(file = "images/fbicon.png")
  mailDetail.iconphoto(False, p2)
  mailDetail.geometry("1030x550+150+120")
 
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)
  messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)
  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)
  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)



#sms notification order
  
def sms():
  send_SMS=Toplevel()
  send_SMS.geometry("700x480+240+150")
  send_SMS.title("Send SMS notification")

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  sms_Notebook = ttk.Notebook(send_SMS)
  SMS_Notification = Frame(sms_Notebook, height=470, width=700)
  SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
  sms_Notebook.add(SMS_Notification, text="SMS Notification")
  sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
  sms_Notebook.place(x=0, y=0)

  numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
  numlbel.place(x=10, y=10)
  numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
  stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
  stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
  
  dclbel=Label(SMS_Notification, text="Double click to insert into text")
  dclbel.place(x=410, y=60)
  dcl=Entry(SMS_Notification, width=30)
  dcl.place(x=400, y=85,height=200)
  
  smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
  smstype.place(x=10, y=223)
  snuvar=IntVar()
  normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
  unicode_rbtn.place(x=190, y=5)
  tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
  tiplbf.place(x=10, y=290)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
  tiplabl.place(x=5, y=5)

  btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
  btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
  btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
  

  smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
  smstype.place(x=10, y=5)
  snumvar=IntVar()
  normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
  unicode_rbtn.place(x=290, y=5)

  sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
  sms1type.place(x=10, y=80)
  name=Label(sms1type, text="Username").place(x=10, y=5)
  na=Entry(sms1type, width=20).place(x=100, y=5)
  password=Label(sms1type, text="Password").place(x=10, y=45)
  pas=Entry(sms1type, width=20).place(x=100, y=45)
  combo=Label(sms1type, text="Route").place(x=400, y=5)
  n = StringVar()
  combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
  btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

  
  tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
  tiplbf.place(x=10, y=190)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
  tiplabl.place(x=0, y=5)
  tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
  tiplabl1.place(x=0, y=60)
  tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
  tiplabl2.place(x=0, y=100)
  tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
  tiplabl3.place(x=0, y=140)
  checkvar1=IntVar()
  chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200)  



#print preview order
def printpreview():
  messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")



#convert to invoice
def convert():
  if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
        messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
  else:
      messagebox.destroy()
  

#delete orders  
def dele():  
  messagebox.askyesno("Delete order", "Are you sure to delete this order? All products will be placed back into stock")




#search in orders  
def search():  
    top = Toplevel()     
    top.title("Find Text")   
    top.geometry("600x250+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
    n = StringVar()
    findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
    findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
    n = StringVar()
    findIN = ttk.Combobox(top, width = 30, textvariable = n )
    findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
    findIN.place(x=90,y=54)
    findIN.current(0)

    findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
    closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
    match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
    n = StringVar()
    match = ttk.Combobox(top, width = 23, textvariable = n )   
    match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
    match.place(x=90,y=83)
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
    n = StringVar()
    search = ttk.Combobox(top, width = 23, textvariable = n )
    search['values'] = ('All', 'up',' Down')
    search.place(x=90,y=112)
    search.current(0)
    checkvarStatus4=IntVar()  
    Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button4.place(x=90,y=141)
    checkvarStatus5=IntVar()   
    Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button5.place(x=300,y=141)





mainFrame=Frame(tab3, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

invoiceLabel = Button(midFrame,compound="top", text="Create new\nEstimate",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=create)
invoiceLabel.pack(side="left", pady=3, ipadx=4)

orderLabel = Button(midFrame,compound="top", text="View/Edit\nEstimate",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=create)
orderLabel.pack(side="left")

estimateLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=dele)
estimateLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

recurLabel = Button(midFrame,compound="top", text="Convert to\nInvoice",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=convert)
recurLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

previewLabel = Button(midFrame,compound="top", text="Print\nPreview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red",command=printpreview)
previewLabel.pack(side="left")

purchaseLabel = Button(midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=printsele)
purchaseLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

expenseLabel = Button(midFrame,compound="top", text=" E-mail \nEstimate",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=emailord)
expenseLabel.pack(side="left")

smsLabel = Button(midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=sms)
smsLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Search\nEstimate",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=search)
productLabel.pack(side="left")

lbframe = LabelFrame(midFrame, height=60, width=200, bg="#f8f8f2")
lbframe.pack(side="left", padx=10, pady=0)
lbl_invdt = Label(lbframe, text="Estimate date from : ", bg="#f8f8f2")
lbl_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
lbl_invdtt = Label(lbframe, text="Estimate date to  :  ", bg="#f8f8f2")
lbl_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))
invdt = Entry(lbframe, width=15)
invdt.grid(row=0, column=1)
invdtt = Entry(lbframe, width=15)
invdtt.grid(row=1, column=1)
checkvar1 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

productLabel = Button(midFrame,compound="top", text="Refresh\nOrders list",relief=RAISED, image=photo8,fg="black", height=55, bd=1, width=55)
productLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
productLabel.pack(side="left")

invoilabel = Label(mainFrame, text="Estimate(All)", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))
drop = ttk.Combobox(mainFrame, value="Hello")
drop.pack(side="right", padx=(0,10))
invoilabel = Label(mainFrame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
invoilabel.pack(side="right", padx=(0,10))

class MyApp:
  def __init__(self, parent):
    
    self.myParent = parent 

    self.myContainer1 = Frame(parent) 
    self.myContainer1.pack()
    
    self.top_frame = Frame(self.myContainer1) 
    self.top_frame.pack(side=TOP,
      fill=BOTH, 
      expand=YES,
      )  

    self.left_frame = Frame(self.top_frame, background="white",
      borderwidth=5,  relief=RIDGE,
      height=250, 
      width=2000, 
      )
    self.left_frame.pack(side=LEFT,
      fill=BOTH, 
      expand=YES,
      )

    
    tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Estimate#")
    tree.heading(3, text="Estimate date")
    tree.heading(4, text="Due date")
    tree.heading(5, text="Customer Name")
    tree.heading(6, text="Status")
    tree.heading(7, text="Emailed on")
    tree.heading(8, text="Printed on")
    tree.heading(9, text="SMS on")
    tree.heading(10, text="Order Total")   
    tree.column(1, width = 30)
    tree.column(2, width = 150)
    tree.column(3, width = 140)
    tree.column(4, width = 130)
    tree.column(5, width = 200)
    tree.column(6, width = 130)
    tree.column(7, width = 150)
    tree.column(8, width = 130)
    tree.column(9, width = 130)
    tree.column(10, width = 160)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=990+330+15, y=0, height=300+20)
    scrollbar.config( command=tree.yview )

    tabControl = ttk.Notebook(self.left_frame,width=1)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tabControl.add(tab1,image=invoices,compound = LEFT, text ='Estimate Items',)
    tabControl.add(tab2,image=photo11,compound = LEFT, text ='Private Notes')
    tabControl.add(tab3,image=smslog,compound = LEFT, text ='SMS Log')
    tabControl.add(tab4,image=photo11,compound = LEFT, text ='Documents')
    tabControl.pack(expand = 1, fill ="both")
    
    tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Product/Service ID",)
    tree.heading(3, text="Name")
    tree.heading(4, text="Description")
    tree.heading(5, text="Price")
    tree.heading(6, text="QTY")
    tree.heading(7, text="Tax1")
    tree.heading(8, text="Line Total")   
    tree.column(1, width = 50)
    tree.column(2, width = 270)
    tree.column(3, width = 250)
    tree.column(4, width = 300)
    tree.column(5, width = 130)
    tree.column(6, width = 100)
    tree.column(7, width = 100)
    tree.column(8, width = 150)

    note1=Text(tab2, width=170,height=10).place(x=10, y=10)

    note1=Text(tab3, width=170,height=10).place(x=10, y=10)

    tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Attach to Email",)
    tree.heading(3, text="Filename")
    tree.column(1, width = 70)
    tree.column(2, width = 270)
    tree.column(3, width = 1000)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=990+330+15, y=360, height=190)
    scrollbar.config( command=tree.yview )
       
myapp = MyApp(tab3)










######################## TAB=7-CUSTOMER SECTION-JAFREENA #######################################################################



#add new customer

def add_customer():
    add_customer = Toplevel()  
    add_customer.title("Add new Customer ")
    p2 = PhotoImage(file = "images/fbicon.png")
    add_customer.iconphoto(False, p2)
    add_customer.geometry("775x580+300+100")
    Labelframe1=LabelFrame(add_customer,text="Customer")
    Labelframe1.place(x=10,y=10,width=755,height=525)
    a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
    a2=Label(Labelframe1,text="Category:")
    a3=Label(Labelframe1,text="Status :")
    a3.place(x=620,y=7)
    b1=Entry(Labelframe1)
    ca=StringVar() 
    b2=ttk.Combobox(Labelframe1,textvariable = ca )    
    b2['values'] = ('Default')  
    b2.place(x=390,y=220) 
    b2.current(0)
    a1.place(x=10,y=7)
    a2.place(x=330,y=7)   
    b1.place(x=120,y=7,width=200)
    b2.place(x=390,y=7,width=220)
    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = checkvar1, onvalue = 0, offvalue = 1)
    chkbtn1.place(x=670,y=6)
    Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
    Labelframe2.place(x=10,y=35,width=340,height=125)
    a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
    a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)
    b1=Entry(Labelframe2).place(x=110,y=10,width=210)
    b2=Entry(Labelframe2).place(x=110,y=35,width=210,height=63)  
    btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=85,height=20)
    Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
    Labelframe3.place(x=400,y=35,width=340,height=125)
    a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
    a21=Label(Labelframe3,text="Address:").place(x=10,y=35)
    b11=Entry(Labelframe3).place(x=110,y=10,width=210)
    b21=Entry(Labelframe3).place(x=110,y=35,width=210,height=63)
    Labelframe4=LabelFrame(Labelframe1,text="Contact")
    Labelframe4.place(x=10,y=170,width=340,height=137)
    a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
    a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
    a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)
    b11=Entry(Labelframe4).place(x=110,y=10,width=210)
    b21=Entry(Labelframe4).place(x=110,y=35,width=210)
    b31=Entry(Labelframe4).place(x=110,y=60,width=90)
    b41=Entry(Labelframe4).place(x=230,y=60,width=90)
    b51=Entry(Labelframe4).place(x=215,y=85,width=105)
    btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=220,height=20)
    Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
    Labelframe5.place(x=400,y=170,width=340,height=108)
    a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
    a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)
    b11=Entry(Labelframe5).place(x=110,y=10,width=210)
    b21=Entry(Labelframe5).place(x=110,y=35,width=210)
    b31=Entry(Labelframe5).place(x=110,y=60,width=90)
    b41=Entry(Labelframe5).place(x=230,y=60,width=90)
    Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
    Labelframe6.place(x=10,y=317,width=340,height=80)
    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = checkvar1, onvalue = 1, offvalue = 0, font=("arial", 8))
    chkbtn1.place(x=10,y=6)
    a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
    a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)
    b11val = IntVar(Labelframe6)
    b11=Entry(Labelframe6).place(x=250,y=7,width=70)
    b12=Entry(Labelframe6,textvariable=b11val).place(x=80,y=30,width=70)
    Labelframe7=LabelFrame(Labelframe1,text="Customer type")
    Labelframe7.place(x=10,y=405,width=340,height=90)
    i=IntVar()
    r1=Radiobutton(Labelframe7, text = "Client", variable = i, value = 1).place(x=5,y=15)
    r2=Radiobutton(Labelframe7, text = "Vender", variable = i, value = 2).place(x=90,y=15)
    r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = i, value = 3).place(x=180,y=15)
    Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
    Labelframe8.place(x=400,y=288,width=340,height=80)
    a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
    a12=Label(Labelframe8,text="City:").place(x=10,y=30)
    c=StringVar() 
    b11=ttk.Combobox(Labelframe8,textvariable=c)
    b11.place(x=110,y=5,width=210)
    b11['values'] = ('India','America')    
    b11.place(x=110,y=5) 
    b12=Entry(Labelframe8).place(x=110,y=30,width=210)
    Labelframe9=LabelFrame(Labelframe1,text="Notes")
    Labelframe9.place(x=400,y=380,width=340,height=115)
    '''scrollbar = Scrollbar(Labelframe9)
        scrollbar.place(x=300,y=10)
        b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
        yscrollcommand.config(command=b12.yview)'''
    b12=Entry(Labelframe9).place(x=20,y=10,width=295,height=70)
    scrollbar = Scrollbar(Labelframe9)
    scrollbar.place(x=295,y=10)
    btn1=Button(add_customer,width=50,compound = LEFT,image=tick ,text="  OK").place(x=20, y=545)
    btn2=Button(add_customer,width=80,compound = LEFT,image=cancel,text="  Cancel").place(x=665, y=545)
    add_customer.mainloop()





# Edit/View customer

def edit_customer():
    edit_customer = Toplevel()  
    edit_customer.title("Edit Customer Details ")
    p2 = PhotoImage(file = "images/fbicon.png")
    edit_customer.iconphoto(False, p2)
    edit_customer.geometry("775x580+300+100")
    Labelframe1=LabelFrame(edit_customer,text="Customer")
    Labelframe1.place(x=10,y=10,width=755,height=525)
    a1=Label(Labelframe1,text="Customer ID:",fg="Blue")
    a2=Label(Labelframe1,text="Category:")
    a3=Label(Labelframe1,text="Status :")
    a3.place(x=620,y=7)
    b1=Entry(Labelframe1)
    ca=StringVar() 
    b2=ttk.Combobox(Labelframe1,textvariable = ca )    
    b2['values'] = ('Default')  
    b2.place(x=390,y=220) 
    b2.current(0)
    a1.place(x=10,y=7)
    a2.place(x=330,y=7)   
    b1.place(x=120,y=7,width=200)
    b2.place(x=390,y=7,width=220)
    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe1, text = "Active", variable = checkvar1, onvalue = 0, offvalue = 1)
    chkbtn1.place(x=670,y=6)
    Labelframe2=LabelFrame(Labelframe1,text="Invoice to (appears on invoice)")
    Labelframe2.place(x=10,y=35,width=340,height=125)
    a1=Label(Labelframe2,text="Business Name:",fg="Blue").place(x=10,y=10)
    a2=Label(Labelframe2,text="Address:",fg="Blue").place(x=10,y=35)
    b1=Entry(Labelframe2).place(x=110,y=10,width=210)
    b2=Entry(Labelframe2).place(x=110,y=35,width=210,height=63)  
    btn110=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=85,height=20)
    Labelframe3=LabelFrame(Labelframe1,text="Ship to (appears on invoice)")
    Labelframe3.place(x=400,y=35,width=340,height=125)
    a11=Label(Labelframe3,text="Ship to Name:").place(x=10,y=10)
    a21=Label(Labelframe3,text="Address:").place(x=10,y=35)
    b11=Entry(Labelframe3).place(x=110,y=10,width=210)
    b21=Entry(Labelframe3).place(x=110,y=35,width=210,height=63)
    Labelframe4=LabelFrame(Labelframe1,text="Contact")
    Labelframe4.place(x=10,y=170,width=340,height=137)
    a11=Label(Labelframe4,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe4,text="Email Address:",fg="Blue").place(x=10,y=35)
    a31=Label(Labelframe4,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe4,text="Fax:").place(x=200,y=60)
    a51=Label(Labelframe4,text="Mobile number for SMS notification:").place(x=10,y=85)
    b11=Entry(Labelframe4).place(x=110,y=10,width=210)
    b21=Entry(Labelframe4).place(x=110,y=35,width=210)
    b31=Entry(Labelframe4).place(x=110,y=60,width=90)
    b41=Entry(Labelframe4).place(x=230,y=60,width=90)
    b51=Entry(Labelframe4).place(x=215,y=85,width=105)
    btn111=Button(Labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=359,y=220,height=20)
    Labelframe5=LabelFrame(Labelframe1,text="Ship To Contact")
    Labelframe5.place(x=400,y=170,width=340,height=108)
    a11=Label(Labelframe5,text="Contact Person:").place(x=10,y=10)
    a21=Label(Labelframe5,text="Email Address:").place(x=10,y=35)
    a31=Label(Labelframe5,text="Tel. No:").place(x=10,y=60)
    a41=Label(Labelframe5,text="Fax:").place(x=200,y=60)
    b11=Entry(Labelframe5).place(x=110,y=10,width=210)
    b21=Entry(Labelframe5).place(x=110,y=35,width=210)
    b31=Entry(Labelframe5).place(x=110,y=60,width=90)
    b41=Entry(Labelframe5).place(x=230,y=60,width=90)
    Labelframe6=LabelFrame(Labelframe1,text="Payment Option")
    Labelframe6.place(x=10,y=317,width=340,height=80)
    checkvar1 = IntVar()
    chkbtn1 = Checkbutton(Labelframe6, text = "Tax Exempt", variable = checkvar1, onvalue = 1, offvalue = 0, font=("arial", 8))
    chkbtn1.place(x=10,y=6)
    a11=Label(Labelframe6,text="Specific Tax1%:").place(x=150,y=7)
    a12=Label(Labelframe6,text="Discount%:").place(x=10,y=30)
    b11val = IntVar(Labelframe6)
    b11=Entry(Labelframe6).place(x=250,y=7,width=70)
    b12=Entry(Labelframe6,textvariable=b11val).place(x=80,y=30,width=70)
    Labelframe7=LabelFrame(Labelframe1,text="Customer type")
    Labelframe7.place(x=10,y=405,width=340,height=90)
    i=IntVar()
    r1=Radiobutton(Labelframe7, text = "Client", variable = i, value = 1).place(x=5,y=15)
    r2=Radiobutton(Labelframe7, text = "Vender", variable = i, value = 2).place(x=90,y=15)
    r3=Radiobutton(Labelframe7, text = "Both(Client/Vender)", variable = i, value = 3).place(x=180,y=15)
    Labelframe8=LabelFrame(Labelframe1,text="Additional Info")
    Labelframe8.place(x=400,y=288,width=340,height=80)
    a11=Label(Labelframe8,text="Country:").place(x=10,y=5)
    a12=Label(Labelframe8,text="City:").place(x=10,y=30)
    c=StringVar() 
    b11=ttk.Combobox(Labelframe8,textvariable=c)
    b11.place(x=110,y=5,width=210)
    b11['values'] = ('India','America')    
    b11.place(x=110,y=5) 
    b12=Entry(Labelframe8).place(x=110,y=30,width=210)
    Labelframe9=LabelFrame(Labelframe1,text="Notes")
    Labelframe9.place(x=400,y=380,width=340,height=115)
    '''scrollbar = Scrollbar(Labelframe9)
        scrollbar.place(x=300,y=10)
        b12=Entry(Labelframe9,yscrollcommand=scrollbar.set).place(x=10,y=10,width=290,height=70)
        yscrollcommand.config(command=b12.yview)'''
    b12=Entry(Labelframe9).place(x=20,y=10,width=295,height=70)
    scrollbar = Scrollbar(Labelframe9)
    scrollbar.place(x=295,y=10)
    btn1=Button(edit_customer,width=50,compound = LEFT,image=tick ,text="  OK").place(x=20, y=545)
    btn2=Button(edit_customer,width=80,compound = LEFT,image=cancel,text="  Cancel").place(x=665, y=545)
    edit_customer.mainloop()





#delete Customer

def delete_customer():
   
    messagebox.askyesno("Delete Customers", "Are you sure want to delete 1 Customer(s) ?")





#Preview Invoice List

def previewinvoice_customer():
  preview = Toplevel()
  preview.title("F-Billing Revolution Invoice Report ")
  p2= PhotoImage(file = "images/fbicon.png")
  preview.iconphoto(False, p2)
  preview.geometry("1800x1800+0+0")
  canvas = Canvas(preview)
  canvas.place(relwidth=1, relheight=1,x=250,y=10) 
  paperheigth = preview.winfo_fpixels('1m') * 297
  paperwidth = preview.winfo_fpixels('1m') * 210
  canvas.create_rectangle(20, 20, 20+paperwidth, 20+paperheigth, outline='', fill='white')
  




#print Invoice


def printinvoice_customer():

  def property1():
    propert=Toplevel()
    propert.title("OneNote for Windows 10 Document Properties")
    p2 = PhotoImage(file = "images/fbicon.png")
    propert.iconphoto(False, p2)
    propert.geometry("580x470+380+210")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Options")
      p2 = PhotoImage(file = "images/fbicon.png")
      propert1.iconphoto(False, p2)
      propert1.geometry("580x470+410+220")
      property1_Frame1=LabelFrame(propert1,height=405, width=560)
      property1_Frame1.place(x=10, y=10)  
      name=Label(property1_Frame1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(property1_Frame1, text="Paper/Output").place(x=30, y=35)
      size=Label(property1_Frame1, text="Paper size:").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(property1_Frame1, width = 28, textvariable = n )
      search['values'] = ('A4','Letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(property1_Frame1, text="Copy Count:").place(x=55, y=95)
      nocopy = Spinbox(property1_Frame1,from_=0,to=100000000, width=28).place(x=150, y=95)    
      btn=Button(propert1,text="OK", width=10,).place(x=390, y=425)
      btn=Button(propert1,text="Cancel", width=10,).place(x=490, y=425)     
      
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=450, width=581)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)
    property_Frame1=LabelFrame(property_Frame,height=380, width=560)
    property_Frame1.place(x=10, y=10)   
    name=Label(property_Frame1, text="Orientation:").place(x=10, y=15)
    n = StringVar()
    search = ttk.Combobox(property_Frame1, width = 28, textvariable = n )
    search['values'] = ('Landscape','Portrait')
    search.place(x=10,y=40)
    search.current(0)
    text=Text(property_Frame1,width=40).place(x=217, y=20,height=300)
    btn=Button(property_Frame1, text="Advanced...", width=10,command=property2).place(x=430, y=335)
    btn=Button(property_Frame,text="OK", width=10,).place(x=390, y=400)
    btn=Button(property_Frame, text="Cancel", width=10,).place(x=490, y=400)     
 
  print1=Toplevel()
  print1.title("Print")
  p2 = PhotoImage(file = "images/fbicon.png")
  print1.iconphoto(False, p2)   
  print1.geometry("580x390+350+200")
  printerframe=LabelFrame(print1, text="Printer", height=85, width=563)
  printerframe.place(x=10, y=5)   
  name=Label(printerframe, text="Name:").place(x=10, y=5)
  v=StringVar() 
  e1= ttk.Combobox(printerframe,textvariable=v)
  e1['values'] = ('OneNote for Windows10','Microsoft XPS Document Writer','Microsoft Print PDF','Fax')   
  e1.place(x=70,y=5,width=310) 
  e1.current(0)
  where=Label(printerframe, text="Where:").place(x=10, y=35)
  printocheckvar=IntVar()
  printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
  printochkbtn.place(x=390, y=35)
  btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=470, y=5)
  pageslblframe=LabelFrame(print1, text="Pages", height=140, width=277)
  pageslblframe.place(x=10, y=95)
  radvar=IntVar()
  radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
  radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
  radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
  pagecountentry = Entry(pageslblframe, width=30).place(x=80, y=47)
  pageinfolabl=Label(pageslblframe,text="Enter page numbers and/or page ranges\n      seperated by commas. For example:1,3,5-12")
  pageinfolabl.place(x=0, y=75)
  copylblframe=LabelFrame(print1, text="Copies", height=140, width=277)
  copylblframe.place(x=295, y=95)
  nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
  noentry = Spinbox(copylblframe,from_=0,to=100000000, width=18).place(x=140, y=5)      
  one=Frame(copylblframe, width=30, height=50, bg="black").place(x=20, y=40)     
  two=Frame(copylblframe, width=30, height=50, bg="grey").place(x=15, y=45)     
  three=Frame(copylblframe, width=30, height=50, bg="white").place(x=10, y=50)      
  four=Frame(copylblframe, width=30, height=50, bg="black").place(x=80, y=40)      
  fiv=Frame(copylblframe, width=30, height=50, bg="grey").place(x=75, y=45)      
  six=Frame(copylblframe, width=30, height=50, bg="white").place(x=70, y=50)      
  collatecheckvar=IntVar()
  collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
  collatechkbtn.place(x=120, y=40)
  othrlblframe=LabelFrame(print1, text="Other", height=100, width=277)
  othrlblframe.place(x=10, y=240)
  printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
  va=StringVar()  
  dropprint= ttk.Combobox(othrlblframe,textvariable=va)
  dropprint['values'] = ('AllPages','Odd Pages','Even Pages')     
  dropprint.place(x=80,y=0,width=185) 
  dropprint.current(0)
  orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
  dropord = ttk.Combobox(othrlblframe, width=28).place(x=80, y=25)
  val=StringVar() 
  dropord= ttk.Combobox(othrlblframe,textvariable=val)
  dropord['values'] = ('Direct(1-9)','Reverse(1-9)')   
  dropord.place(x=80,y=25,width=185) 
  dropord.current(0)
  duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
  val1=StringVar() 
  droplex= ttk.Combobox(othrlblframe,textvariable=val1)
  droplex['values'] = ('Default','Vertical','Horizontal','Simplex') 
  droplex.place(x=80,y=50,width=185) 
  droplex.current(0)
  prmodelblframe=LabelFrame(print1, text="Print mode",height=100, width=277)
  prmodelblframe.place(x=295, y=240)
  val11=StringVar() 
  dropscal= ttk.Combobox(prmodelblframe,textvariable=val11)
  dropscal['values'] = ('Default','Split big Pages','Join Small Pages','Scale') 
  dropscal.place(x=5,y=5,width=260,height=40) 
  dropscal.current(0)
  poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=50)
  val12=StringVar() 
  droppos= ttk.Combobox(prmodelblframe,textvariable=val12)
  droppos['values'] = ('Default')   
  droppos.place(x=136,y=50,width=129) 
  droppos.current(0)
  okbtn=Button(print1, text="Ok", width=10).place(x=390, y=350)
  canbtn=Button(print1, text="Cancel", width=10).place(x=490, y=350)





#EMAIL INVOICE LIST
   
def emailinvoice_customer():
  mailDetail=Toplevel()
  mailDetail.title("E-Mail Invoice List")
  p2 = PhotoImage(file = "images/fbicon.png")
  mailDetail.iconphoto(False, p2)
  mailDetail.geometry("1030x550+150+120")
 
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)
  messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)
  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)
  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)







#sms notification order
  
def customersms():
  send_SMS=Toplevel()
  send_SMS.title("Send SMS notification")
  p2 = PhotoImage(file = "images/fbicon.png")
  send_SMS.iconphoto(False, p2)
  send_SMS.geometry("580x500+380+150")
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  sms_Notebook = ttk.Notebook(send_SMS)
  SMS_Notification = Frame(sms_Notebook, height=485, width=585)
  SMS_Service_Account = Frame(sms_Notebook, height=485, width=585)
  sms_Notebook.add(SMS_Notification, text="SMS Notification")
  sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
  sms_Notebook.place(x=0, y=0)
  numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
  numlbel.place(x=10, y=10)
  numentry=Entry(SMS_Notification,width=92).place(x=10, y=35,height=25)
  stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=65)
  stex=Entry(SMS_Notification, width=60).place(x=10, y=90,height=120)
  no=Label(SMS_Notification, text="0/160 characters")
  no.place(x=285, y=210)
  dclbel=Label(SMS_Notification, text="Double click to insert into text")
  dclbel.place(x=395, y=65)
  dcl=Entry(SMS_Notification, width=27)
  dcl.place(x=395, y=90,height=200)
  smstype=LabelFrame(SMS_Notification, text="SMS message type", width=365, height=60)
  smstype.place(x=10, y=230)
  snuvar=IntVar()
  normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
  normal_rbtn.place(x=15, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
  unicode_rbtn.place(x=195, y=5)
  tiplbf=LabelFrame(SMS_Notification, text="Tips", width=552, height=120)
  tiplbf.place(x=10, y=292)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS number with the country code. Do not use the + sign at the beginning(example\nUS number: 8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
  tiplabl.place(x=5, y=5)
  btn1=Button(SMS_Notification,width=150,compound = LEFT,image=tick ,text="  Send SMS notification").place(x=10, y=425,height=31)
  btn2=Button(SMS_Notification,width=215,compound = LEFT,image=warnin,text="  Confirm SMS cost before sending").place(x=190, y=425,height=31)
  btn3=Button(SMS_Notification,width=80,compound = LEFT,image=cancel,text="  Cancel").place(x=472, y=425,height=31)
  smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=555, height=65)
  smstype.place(x=10, y=5)
  snumvar=IntVar()
  normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="EXPERTTEXTING(www.experttexting.com-Recommended", variable=snumvar, value=2)
  unicode_rbtn.place(x=210, y=5)
  sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=555, height=100)
  sms1type.place(x=10, y=80)
  name=Label(sms1type, text="Username").place(x=10, y=5)
  na=Entry(sms1type,width=29).place(x=100, y=5,height=23)
  password=Label(sms1type, text="Password").place(x=10, y=45)
  pas=Entry(sms1type, width=29).place(x=100, y=45,height=23)
  combo=Label(sms1type,text="Route").place(x=320, y=5)
  n = StringVar()
  combo1 = ttk.Combobox(sms1type,textvariable = n )
  combo1['values'] = ('1-Economy (test first)','2-Standard (default)','3-Premium') 
  combo1.place(x=375,y=5,height=23,width=165)  
  combo1.current(0)
  btn1=Button(sms1type,width=110,compound = LEFT,image=saves,text="  Save settings").place(x=420, y=35,height=31)  
  tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=555, height=250)
  tiplbf.place(x=10, y=190)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
  tiplabl.place(x=2, y=5)
  tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
  tiplabl1.place(x=2, y=60)
  tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
  tiplabl2.place(x=2, y=100)
  tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
  tiplabl3.place(x=2, y=140)
  checkvar1=IntVar()
  chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=130, y=200)  





#IMPORT CUSTOMERS

def import_customer():
    top=Toplevel()
    top.title("Import Customers list from Excel(XLS)File")
    p2 = PhotoImage(file = "images/fbicon.png")
    top.iconphoto(False, p2)
    top.geometry("785x540+280+100")
    importframe=Frame(top)
    importframe.place(x=0,y=0,height=700,width=785)
    impolbl=Label(importframe,text="Import source Excel(XLS) File:").place(x=10,y=10)
    impoentry=Entry(importframe,bg="white")
    impoentry.place(x=10,y=40,width=400,height=25)
    previewlbl=Label(importframe,text="Source XLS File preview").place(x=10,y=75)
    langs = ()
    langs_var = StringVar(value=langs)
    listbox = Listbox(
        importframe,
        listvariable=langs_var,
        width=71,
        height=8,
        selectmode='extended')
    listbox.place(x=10,y=102,height=390) 
    scrollbar = Scrollbar(
        importframe,
        orient='vertical',
        command=listbox.yview
    )
    
    listbox['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=422,y=104,height=370)

    scrollbar = Scrollbar(
        importframe,
        orient='horizontal',
        
        command=listbox.xview
    ) 
    listbox['xscrollcommand'] = scrollbar.set
    scrollbar.place(x=12,y=474,width=427)
    lb1=Label(importframe,text="Select import source XLs file first after build column associations").place(x=10,y=500)
    
    def callback(url):
        webbrowser.open_new(url) 

    link1 = Label(importframe, text="More info", fg="blue", cursor="hand2")
    link1.place(x=360,y=500)
    link1.bind("<Button-1>", lambda e: callback("https://f-billing.com/faq.php"))
    importbutton=Button(top,command=export_customer,image=folder,compound=LEFT)
    importbutton.place(x=410,y=40,height=25,width=30)
    lb1=Label(importframe,text="     Please associate datafields with data columns").place(x=500,y=10)
    id1=Label(importframe,text="CUSTOMER ID = ",fg="blue")
    id1.place(x=460,y=40)
    no = StringVar() 
    idd = ttk.Combobox(importframe, width = 27, textvariable = no ) 
    idd['values'] = ('    -NotAssociated-')
    idd.place(x=580,y=40,height=23) 
    idd.current(0)
    name1=Label(importframe,text="CUSTOMER NAME = ",fg="blue")
    name1.place(x=460,y=65)
    namevar = StringVar() 
    name = ttk.Combobox(importframe, width = 27, textvariable = namevar ) 
    name['values'] = ('    -NotAssociated-' 
                              )  
    name.place(x=580,y=65,height=23) 
    name.current(0)
    category1=Label(importframe,text="CATEGORY = ",fg="blue")
    category1.place(x=460,y=90)
    categoryvar = StringVar() 
    category = ttk.Combobox(importframe, width = 27, textvariable = categoryvar ) 
    category['values'] = ('    -NotAssociated-' 
                              ) 
    category.place(x=580,y=90,height=23) 
    category.current(0)
    add=Label(importframe,text="ADDRESS = ",fg="blue")
    add.place(x=460,y=115)
    addvar = StringVar() 
    addc = ttk.Combobox(importframe, width = 27, textvariable = addvar ) 
    addc['values'] = ('    -NotAssociated-' 
                              )
    addc.place(x=580,y=115,height=23) 
    addc.current(0)
    tel1=Label(importframe,text="TEL.= ")
    tel1.place(x=460,y=140)
    telvar = StringVar() 
    telc = ttk.Combobox(importframe, width = 27, textvariable = telvar ) 
    telc['values'] = ('    -NotAssociated-' 
                              )  
    telc.place(x=580,y=140,height=23) 
    telc.current(0)
    fax1=Label(importframe,text="FAX = ")
    fax1.place(x=460,y=165)
    faxvar = StringVar() 
    faxc = ttk.Combobox(importframe, width = 27, textvariable = faxvar )
    faxc['values'] = ('    -NotAssociated-' 
                              )
    faxc.place(x=580,y=165,height=23) 
    faxc.current(0)
    email1=Label(importframe,text="EMAIL = ")
    email1.place(x=460,y=190)
    emailvar = StringVar() 
    emailc = ttk.Combobox(importframe, width = 27, textvariable = emailvar ) 
    emailc['values'] = ('    -NotAssociated-'
                              )    
    emailc.place(x=580,y=190,height=23) 
    emailc.current(0)
    cp1=Label(importframe,text="CONTACT PERSION = ")
    cp1.place(x=460,y=215)
    cpvar = StringVar() 
    cp = ttk.Combobox(importframe, width = 27, textvariable = cpvar )  
    cp['values'] = ('    -NotAssociated-' 
                              )     
    cp.place(x=580,y=215,height=23) 
    cp.current(0)
    sn2=Label(importframe,text="SHIP TO NAME = ")
    sn2.place(x=460,y=240)
    snvar = StringVar() 
    sn = ttk.Combobox(importframe, width = 27, textvariable = snvar )
    sn['values'] = ('    -NotAssociated-' 
                              )
    sn.place(x=580,y=240,height=23) 
    sn.current(0)
    saa2=Label(importframe,text="SHIP TO ADDESS = ")
    saa2.place(x=460,y=265)
    saa2var = StringVar() 
    saa = ttk.Combobox(importframe, width = 27, textvariable = saa2var ) 
    saa['values'] = ('    -NotAssociated-')
    saa.place(x=580,y=265,height=23) 
    saa.current(0)
    stt2=Label(importframe,text="SHIP TO TEL. = ")
    stt2.place(x=460,y=290)
    stt2var = StringVar() 
    stt = ttk.Combobox(importframe, width = 27, textvariable = stt2var )
    stt['values'] = ('    -NotAssociated-' 
                              ) 
    stt.place(x=580,y=290,height=23) 
    stt.current(0)
    stf2=Label(importframe,text="SHIP TO FAX = ")
    stf2.place(x=460,y=315)
    stf2var = StringVar() 
    stf = ttk.Combobox(importframe, width = 27, textvariable = stf2var )
    stf['values'] = ('    -NotAssociated-' 
                              )   
    stf.place(x=580,y=315,height=23) 
    stf.current(0)
    dd2=Label(importframe,text="DISCOUNT = ")
    dd2.place(x=460,y=340)
    dd2var = StringVar() 
    dd = ttk.Combobox(importframe, width = 27, textvariable = dd2var) 
    dd['values'] = ('    -NotAssociated-'
                              )
    dd.place(x=580,y=340,height=23) 
    dd.current(0)
    st112=Label(importframe,text="SPECIAL TAX 1 = ")
    st112.place(x=460,y=365)
    st112var = StringVar() 
    st11 = ttk.Combobox(importframe, width = 27, textvariable = st112var )  
    st11['values'] = ('    -NotAssociated-' 
                              )   
    st11.place(x=580,y=365,height=23) 
    st11.current(0)
    st222=Label(importframe,text="SPECIAL TAX 2 = ")
    st222.place(x=460,y=390)
    st222var = StringVar() 
    st22 = ttk.Combobox(importframe, width = 27, textvariable = st222var )
    st22['values'] = ('    -NotAssociated-'
                              )     
    st22.place(x=580,y=390,height=23) 
    st22.current(0)
    vrn2=Label(importframe,text="VAT REG.NUMBER = ")
    vrn2.place(x=460,y=415)
    vrn2var = StringVar() 
    vrn = ttk.Combobox(importframe, width = 27, textvariable = vrn2var ) 
    vrn['values'] = ('    -NotAssociated-' 
                              )     
    vrn.place(x=580,y=415,height=23) 
    vrn.current(0)
    avt2=Label(importframe,text="ACTIVE = ")
    avt2.place(x=460,y=440)
    avt2var = StringVar() 
    avt = ttk.Combobox(importframe, width = 27, textvariable = avt2var )
    avt['values'] = ('    -NotAssociated-'
                              )
    avt.place(x=580,y=440,height=23) 
    avt.current(0)
    tee2=Label(importframe,text="TAX EXEMPTED= ")
    tee2.place(x=460,y=465)
    teevar = StringVar() 
    tee= ttk.Combobox(importframe, width = 27, textvariable = teevar )
    tee['values'] = ('    -NotAssociated-' 
                              ) 
    tee.place(x=580,y=465,height=23) 
    tee.current(0)
    btn=Button(importframe,text="Clear associations", width=15,).place(x=560, y=500)
    btn=Button(importframe, text="Next", width=10,).place(x=685, y=500)     
    top.mainloop()






#export_customer

def export_customer():
    name = askopenfilename(filetypes=[('Excel', ('*.xls', '*.xslm', '*.xlsx')),('CSV', '*.csv',)])
    if name:
        if name.endswith('.csv'):
            df = pd.read_csv(name)
        else:
            df = pd.read_excel(name)

            filename = name

           
            


#Search in Customers

def search_customers():
    top = Toplevel()  
    top.title("Find Text")
    p2 = PhotoImage(file = "images/fbicon.png")
    top.iconphoto(False, p2)
    top.geometry("520x180+390+250")
    findwhat1=Label(top,text="Find What:")
    findwhat1.place(x=5,y=15)
    n = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = n )
    findwhat.place(x=85,y=15,height=23) 
    findButton = Button(top, text ="Find next",width=10)
    findButton.place(x=420,y=15)
    findin1=Label(top,text="Find in:")
    findin1.place(x=5,y=40)
    n = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable = n )
    findIN['values'] = ('Customer name',  
                              'Customer ID', 
                              'Category', 
                              'Customer name', 
                              'Contact Person', 
                              'Customer Tel.', 
                              'SMS number',
                              'Type',
                              '<<All>>')    
    findIN.place(x=85,y=40,height=23) 
    findIN.current(0)
    closeButton = Button(top, text ="Close",width=10)
    closeButton.place(x=420,y=45)
    match1=Label(top,text="Match:")
    match1.place(x=5,y=65)
    n = StringVar() 
    match = ttk.Combobox(top, width = 27, textvariable = n ) 
    match['values'] = ('From any part of the field','Whole field',  
                              'From beging of field')
    match.place(x=85,y=65,height=23) 
    match.current(0)
    search1=Label(top,text="Search:")
    search1.place(x=5,y=90)
    n = StringVar() 
    search = ttk.Combobox(top, width = 27, textvariable = n )
    search['values'] = ('Up','Down','All') 
    search.place(x=85,y=90,height=23) 
    checkvarStatus4=IntVar()
    Button4 = Checkbutton(top,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)
    Button4.place(x=60,y=120)
    checkvarStatus5=IntVar()  
    Button5 = Checkbutton(top,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)
    Button5.place(x=270,y=120)
    top.mainloop()



#refresh

def refresh_customers(self):
    self.destroy()
    self.__init__()
 



######################## FRONT PAGE OF CUSTOMER SECTION #######################################################################

    
mainFrame=Frame(tab7, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(5, 2))
pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

addcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_add.png"))
addcustomerLabel = Button(midFrame,compound="top", text="Add new\nCustomer",relief=RAISED,  command=add_customer,          image=addcustomerIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
addcustomerLabel.pack(side="left", pady=3, ipadx=4)

editcustomerIcon = ImageTk.PhotoImage(Image.open("images/user_edit.png"))
editcustomerLabel = Button(midFrame,compound="top", text="Edit/View\nCustomer",relief=RAISED,command=edit_customer, image=editcustomerIcon,  font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
editcustomerLabel.pack(side="left")

deletecustomerIcon = ImageTk.PhotoImage(Image.open("images/user_delete.png"))
deletecustomerLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, command=delete_customer,image=deletecustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
deletecustomerLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

previewinvoiceIcon = ImageTk.PhotoImage(Image.open("images/priewok.png"))
previewinvoiceLabel = Button(midFrame,compound="top",command=previewinvoice_customer, text="Preview\nInvoice List",relief=RAISED,               image=previewinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
previewinvoiceLabel.pack(side="left")

printinvoiceIcon = ImageTk.PhotoImage(Image.open("images/printer.png"))
printinvoiceLabel = Button(midFrame,compound="top", text="Print\n Invoice List",relief=RAISED,  command=printinvoice_customer, image=printinvoiceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
printinvoiceLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

emailinviceIcon = ImageTk.PhotoImage(Image.open("images/gmail.png"))
emailinviceLabel = Button(midFrame,compound="top",command=emailinvoice_customer, text="E-mail\nInvoice List",relief=RAISED,               image=emailinviceIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
emailinviceLabel.pack(side="left")

smsIcon = ImageTk.PhotoImage(Image.open("images/text-message.png"))
smsLabel = Button(midFrame,compound="top", text="Send SMS\nNotification",command=customersms, relief=RAISED, image=smsIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
smsLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

importcustomerIcon = ImageTk.PhotoImage(Image.open("images/import.png"))
importcustomerLabel = Button(midFrame,compound="top", text="Import\nCustomers",command=import_customer,relief=RAISED, image=importcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
importcustomerLabel.pack(side="left")

exportcustomerIcon = ImageTk.PhotoImage(Image.open("images/export.png"))
exportcustomerLabel = Button(midFrame,compound="top", text="Export\nCustomers",command=export_customer,relief=RAISED, image=exportcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
exportcustomerLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

customersearchIcon = ImageTk.PhotoImage(Image.open("images/search-icon.png"))
customersearchLabel = Button(midFrame,compound="top",command=search_customers, text="Search in\nCustomers",relief=RAISED,               image=customersearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
customersearchLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

refreshcustomerIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
refreshcustomerLabel = Button(midFrame,compound="top", command=refresh_customers,text="Refresh\ncustomer list",relief=RAISED,               image=refreshcustomerIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
refreshcustomerLabel.pack(side="left")

invoi1label = Label(mainFrame, text="Customers", font=("arial", 18), bg="#f8f8f2")
invoi1label.pack(side="left", padx=(20,0))
invoi1label = Label(mainFrame, text="Right click on datagrid row for more options.", font=("arial", 10), bg="#f8f8f2")
invoi1label.pack(side="left", padx=(600,0))

invoi1label = Label(mainFrame, text="Category ", font=("arial", 15), bg="#f8f8f2")
invoi1label.pack(side="right", padx=(0,120))

s=ttk.Style()
s.configure('Treeview.Heading',background='white')
tree=ttk.Treeview(tab7,selectmode='browse')
tree.place(x=0,y=100,height=570)
vertical_bar=ttk.Scrollbar(tab7,orient="vertical")
vertical_bar.place(x=1083,y=101,height=570)
tree["columns"]=("1","2","3","4","5","6","7","8")
tree["show"]='headings'
tree.column("1",width=2,anchor='c')
tree.column("2",width=170,anchor='c')
tree.column("3",width=190,anchor='c')
tree.column("4",width=176,anchor='c')
tree.column("5",width=176,anchor='c')
tree.column("6",width=120,anchor='c')
tree.column("7",width=130,anchor='c')
tree.column("8",width=120,anchor='c')
tree.heading("1",text="")
tree.heading("2",text="Customer ID")
tree.heading("3",text="Category")
tree.heading("4",text="Customer Name")
tree.heading("5",text="Contact Persion")
tree.heading("6",text="Customer Tel.")
tree.heading("7",text="SMS Number")
tree.heading("8",text="Type")

tree1=ttk.Treeview(tab7,selectmode='browse')
tree1.place(height=580,width=254,
                      x=1099,y=101
                      )
tree1["columns"]=("1")
tree1["show"]='headings'
tree1.column("1",width=254,anchor='c')
tree1.heading("1",text="View filter by category")
listbox = Listbox(tab7,height =8,  
                      width = 29,  
                      bg = "white",
                      activestyle = 'dotbox',  
                      fg = "black",
                      highlightbackground="white")  
listbox.insert(0, "  View all records")
listbox.insert(1, "  View only Client/Vendor Type")
listbox.insert(2, "  View only Client Type")
listbox.insert(3, "  View only Vendor Type")
listbox.insert(4, "  Default")
listbox.place(x=1099,y=120,height=545,width=254)


#--------------------TAB-4  RECURRING-ASHBY---------------------



 #generate recurring invoice popups
def generate_recurring_noinvoice(): 
  #  if result=='ok': 
   messagebox.showinfo("F-Billing Revolution 2022", "No recurring invoices are ready today")

def generate_recurring_invoice_success():  
   messagebox.showinfo("F-Billing Revolution 2022", "1 new invoice successfully created.")
  
     



#print invoice
  
def print_invoice_recurring():

  def property1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 28, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy Count:").place(x=55, y=95)
      nocopy = Spinbox(propert1,from_=0,to=100000000, width=28).place(x=150, y=95)    

      btn=Button(propert1,text="OK", width=10,).place(x=390, y=425)
      btn=Button(propert1,text="Cancel", width=10,).place(x=490, y=425) 




      okbtn=Button(propert1,text="OK", width=10,).place(x=390, y=425)
      canbtn=Button(propert1,text="Cancel", width=10,).place(x=490, y=425)  
      
      
   
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=property2).place(x=450, y=370)
    btn=Button(property_Frame,text="OK", width=10,).place(x=390, y=410)
    btn=Button(property_Frame, text="Cancel", width=10,).place(x=490, y=410)  


    
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1, text="Ok", width=10).place(x=460, y=370)
      canbtn=Button(print1, text="Cancel", width=10).place(x=560, y=370)
      


#email
      
def email_invoice_recurring():
  mailDetail=Toplevel()
  mailDetail.title("Invoice E-Mail")
  mailDetail.geometry("1080x550")
  mailDetail.resizable(False, False)
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)

  messagelbframe=LabelFrame(email_Frame,text="Message", height=500, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1,command=addacnt).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)



  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)

  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings",command=savesettings).place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)


def addacnt():  
   messagebox.showinfo("F-Billing Revolution 2022", "No sender email address.\nPlease fill Your company email address textfield under the Account tab.")

def savesettings():  
   messagebox.showinfo("F-Billing Revolution 2022", "Your E-mail configuration settings has been saved.")



#print preview invoice-recurring
# def printpreview():
  #messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")
  # win= Tk()
#Set the Geometry
  # win.geometry("750x450")
  # win.title("F-Billing Revolution 2022 - Invoice")
  # text= Text(win,width= 80,height=30)
  # text.pack(pady=20)


def printpreviewinvoice_recurring():
  preview = Toplevel()
  preview.title("F-Billing Revolution Invoice Report ")
  p2= PhotoImage(file = "images/fbicon.png")
  preview.iconphoto(False, p1)
  preview.geometry("1800x1800+0+0")
  canvas = Canvas(preview)
  canvas.place(relwidth=1, relheight=1,x=250,y=10) 
  paperheigth = preview.winfo_fpixels('1m') * 297
  paperwidth = preview.winfo_fpixels('1m') * 210
  canvas.create_rectangle(20, 20, 20+paperwidth, 20+paperheigth, outline='', fill='white')  



#convert to invoice
def convert():
  if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
        messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
  else:
      messagebox.destroy()
  

#search in invoice 
def search_invoice_recurring():  
    top = Toplevel()     
    top.title("Find Text")   
    top.geometry("600x250+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
    n = StringVar()
    findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
    findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
    n = StringVar()
    findIN = ttk.Combobox(top, width = 30, textvariable = n )
    findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
    findIN.place(x=90,y=54)
    findIN.current(0)

    findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
    closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
    match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
    n = StringVar()
    match = ttk.Combobox(top, width = 23, textvariable = n )   
    match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                    
    match.place(x=90,y=83)
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
    n = StringVar()
    search = ttk.Combobox(top, width = 23, textvariable = n )
    search['values'] = ('All', 'up',' Down')
    search.place(x=90,y=112)
    search.current(0)
    checkvarStatus4=IntVar()  
    Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button4.place(x=90,y=141)
    checkvarStatus5=IntVar()   
    Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button5.place(x=300,y=141)

#-------------------------view/edit invoice---------------------------

#--------------------------calculator-recurring----------------------

def calculator_recurring():
  subprocess.Popen('C:\\Windows\\System32\\calc.exe')

#edit/view invoice in recurring 

def view_invoice_recurring():
  pop=Toplevel(midFrame)
  pop.title("Invoice")
  pop.geometry("950x690+150+0")


  #select customer
  def customer_invoice_recurring():
    cuselection=Toplevel()
    cuselection.title("Select Customer")
    cuselection.geometry("930x650+240+10")
    cuselection.resizable(False, False)


    #add new customer
    def create_newcustomer_recurring():
      ven=Toplevel(midFrame)
      ven.title("Add new vendor")
      ven.geometry("930x650+240+10")
      checkvar1=IntVar()
      checkvar2=IntVar()
      radio=IntVar()
      createFrame=Frame(ven, bg="#f5f3f2", height=650)
      createFrame.pack(side="top", fill="both")
      labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
      labelframe1.place(x=10,y=5,width=910,height=600)
      text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
      e1=Entry(labelframe1,width=25).place(x=150,y=10)
      text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
      e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
      text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
      Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
      
      labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
      labelframe2.place(x=5,y=40,width=420,height=150)
      name = Label(labelframe2, text="Business name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
      e1 = Entry(labelframe2,width=28).place(x=130,y=5)
      addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
      e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
      
      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

      labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
      labelframe3.place(x=480,y=40,width=420,height=150)
      name = Label(labelframe3, text="Ship to name:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe3,width=28).place(x=130,y=5)
      addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
      e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
      
      labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe4.place(x=5,y=195,width=420,height=150)
      name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe4,width=28).place(x=130,y=5)
      email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
      e2 = Entry(labelframe4,width=28).place(x=130,y=35)
      tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe4,width=11).place(x=130,y=65)
      fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe4,width=11).place(x=280,y=65)
      sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
      e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

      
      labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
      labelframe5.place(x=480,y=195,width=420,height=125)
      name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe5,width=28).place(x=130,y=5)
      email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe5,width=28).place(x=130,y=35)
      tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe5,width=11).place(x=130,y=65)
      fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe5,width=11).place(x=280,y=65)

      labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe6.place(x=5,y=350,width=420,height=100)
      Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
      tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
      e1 = Entry(labelframe6,width=10).place(x=290,y=5)
      discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe6,width=10).place(x=100,y=35)

      labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe7.place(x=480,y=330,width=420,height=100)
      country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe7,width=28).place(x=130,y=5)
      city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe7,width=28).place(x=130,y=35)

      labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
      labelframe8.place(x=5,y=460,width=420,height=100)
      R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
      R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
      R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
      

      labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
      labelframe9.place(x=480,y=430,width=420,height=150)
      e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

      btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
      btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
        
               

    enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(cuselection, width=20).place(x=110, y=10)
    text=Label(cuselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(cuselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(cuselection, height=27)
    cusventtree["columns"]=["1","2","3", "4"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=140)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="Customer/Ventor ID")
    cusventtree.heading("2",text="Customer/Ventor Name")
    cusventtree.heading("3",text="Tel.")
    cusventtree.heading("4",text="Contact Person")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(cuselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(cuselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )

    btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=create_newcustomer_recurring).place(x=250, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=create_newcustomer_recurring).place(x=435, y=610)
    btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   



    

  #add new line item
  def newline_recurring():
    newselection=Toplevel()
    newselection.title("Product/Services")
    newselection.geometry("930x650+240+10")
    newselection.resizable(False, False)


    #add new product
    def product():  
      top = Toplevel()  
      top.title("Add a new Product/Service")
      p2 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p2)
    
      top.geometry("700x550+390+15")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
     
      tabControl.add(tab1,compound = LEFT, text ='Product/Service')
      tabControl.add(tab2,compound = LEFT, text ='Product Image')
     
      tabControl.pack(expand = 1, fill ="both")
     
      innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

      code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      code1.place(x=20,y=0)
      codeentry = Entry(Customerlabelframe,width=35)
      codeentry.place(x=120,y=8)

      checkvarStatus=IntVar()
      status1=Label(Customerlabelframe,text="Status:")
      status1.place(x=500,y=8)
      Button1 = Checkbutton(Customerlabelframe,
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                       
                        width = 10)

      Button1.place(x=550,y=5)

      category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
      category1.place(x=20,y=40)
      n = StringVar()
      country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
       
      country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
      
      country.place(x=120,y=45)
      country.current(0)


      name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
      name1.place(x=20,y=70)
      nameentry = Entry(Customerlabelframe,width=60)
      nameentry.place(x=120,y=75)

      des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
      des1.place(x=20,y=100)
      desentry = Entry(Customerlabelframe,width=60)
      desentry.place(x=120,y=105)

      uval = IntVar(Customerlabelframe, value='$0.00')
      unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      unit1.place(x=20,y=130)
      unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
      unitentry.place(x=120,y=135)

      pcsval = IntVar(Customerlabelframe, value='$0.00')
      pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      pcs1.place(x=320,y=140)
      pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
      pcsentry.place(x=410,y=140)

      costval = IntVar(Customerlabelframe, value='$0.00')
      cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
      cost1.place(x=20,y=160)
      costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
      costentry.place(x=120,y=165)

      priceval = IntVar(Customerlabelframe, value='$0.00')
      price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
      price1.place(x=20,y=190)
      priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
      priceentry.place(x=120,y=195)

      checkvarStatus2=IntVar()
     
      Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                        text="Taxable Tax1rate",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        height=2,
                        width = 12)

      Button2.place(x=415,y=170)


      checkvarStatus3=IntVar()
     
      Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                        text="No stock Control",
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      Button3.place(x=40,y=220)


      stockval = IntVar(Customerlabelframe)
      stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
      stock1.place(x=90,y=260)
      stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
      stockentry.place(x=150,y=265)

      lowval = IntVar(Customerlabelframe)
      low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      low1.place(x=300,y=260)
      lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
      lowentry.place(x=495,y=265)

     
      ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
      ware1.place(x=60,y=290)
      wareentry = Entry(Customerlabelframe,width=50)
      wareentry.place(x=150,y=295)

      text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      text1.place(x=20,y=330)

      txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
      txt.place(x=32,y=358)




      okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
      okButton.pack(side=LEFT)

      cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
      cancelButton.pack(side=RIGHT)

      imageFrame = Frame(tab2, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse')
      browsebutton.place(x=580,y=30,height=30,width=50)
      
      removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
      removeButton.place(x=400,y=450)



    
                    
    enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(newselection, width=20).place(x=110, y=10)
    text=Label(newselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(newselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(newselection, height=27)
    cusventtree["columns"]=["1","2","3", "4","5"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=70)
    cusventtree.column("5", width=70)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="ID/SKU")
    cusventtree.heading("2",text="Product/Service Name")
    cusventtree.heading("3",text="Unit price")
    cusventtree.heading("4",text="Service")
    cusventtree.heading("5",text="Stock")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(newselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(newselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )
   

    btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
    btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



  # #preview message if customer  is not
  # def previewline():
  #   messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


  
  #sms notification
  def sms_recurring():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 

  #mark invoice
  def markinvoice_recurring():
    mark_inv=Toplevel()
    mark_inv.geometry("700x480+240+150")
    mark_inv.title("Record Payement for Invoice")
    checkvar=IntVar()
    checkvar1=IntVar()
    checkvar2=IntVar()

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    mark_Notebook = ttk.Notebook(mark_inv)
    Mark_Invoice = Frame(mark_Notebook, height=470, width=750)
    mark_Notebook.add(Mark_Invoice, text="Mark Invoice")
    mark_Notebook.place(x=0, y=0)

    involbel=Label(Mark_Invoice, text="Invoice Balance")
    involbel.place(x=10, y=10)
    numentry=Entry(Mark_Invoice, width=45).place(x=130, y=10)

    labelframe5 = LabelFrame(Mark_Invoice,text="Payement Record Details",bg="#f5f3f2")
    labelframe5.place(x=10,y=60,width=670,height=250)
    e1 = Entry(labelframe5,width=28).place(x=30,y=45)
    pdate = Label(labelframe5, text="Payement Date:",bg="#f5f3f2").place(x=250,y=20)
    e2 = Entry(labelframe5,width=28).place(x=220,y=45)
    payd = Label(labelframe5, text="Paid By:",bg="#f5f3f2").place(x=450,y=20)
    drop = ttk.Combobox(labelframe5, value="Hello")
    drop.place(x=450,y=45)
    involbel=Label(labelframe5, text="Description")
    involbel.place(x=30, y=80)
    numentry=Entry(labelframe5, width=100).place(x=30, y=120)
    Checkbutton(labelframe5,text="Paid in full and close invoice",variable=checkvar,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=30 ,y=150)
    pl = Label(labelframe5,text="Payement Reciepts",bg="#f5f3f2")
    pl.place(x=300,y=145)
    Checkbutton(labelframe5,text="Send Payement Reciept",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=170)
    Checkbutton(labelframe5,text="Attach updated invoice",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=200)

    okbtn=Button(Mark_Invoice,compound = LEFT,image=tick , text="Save payement", width=100).place(x=10, y=350)
    canbtn=Button(Mark_Invoice,compound = LEFT,image=cancel, text="Cancel", width=100).place(x=500, y=350)

    
  #voidinvoice
  def voidinvoice_recurring():
    messagebox.askyesno("F-Billing Revolution","Are you sure to avoid this invoice?\nAll products will be placed back into stock and all payemnts will be voided.")
  
  #delete line item  
  def delete_recurring():
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")
    
    

  firFrame=Frame(pop, bg="#f5f3f2", height=60)
  firFrame.pack(side="top", fill=X)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=customer_invoice_recurring)
  create.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=addnew,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=newline_recurring)
  add.pack(side="left", pady=3, ipadx=4)

  dele= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=delete,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=delete_recurring)
  dele.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  prev= Button(firFrame,compound="top", text="Preview\nInvoice",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printpreviewinvoice_recurring)
  prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(firFrame,compound="top", text="Print \nInvoice",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=print_invoice_recurring)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(firFrame,compound="top", text="Email\nInvoice",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
  mail.pack(side="left", pady=3, ipadx=4)

  sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms_recurring)
  sms1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mark= Button(firFrame,compound="top", text="Mark invoice\nas 'Paid'",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=57,command=markinvoice_recurring)
  mark.pack(side="left", pady=3, ipadx=4)

  void= Button(firFrame,compound="top", text="Void\ninvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=56,command=voidinvoice_recurring)
  void.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=calculator_recurring)
  calc.pack(side="left", pady=3, ipadx=4)

  fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
  fir1Frame.pack(side="top", fill=X)

  labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)
  order = Label(labelframe1, text="Order to").place(x=10,y=5)
  e1 = ttk.Combobox(labelframe1, value="Hello",width=28).place(x=80,y=5)
  address=Label(labelframe1,text="Address").place(x=10,y=30)
  e2=Text(labelframe1,width=23).place(x=80,y=30,height=70)
  ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
  e3=Entry(labelframe1,width=30).place(x=402,y=3)
  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  e4=Text(labelframe1,width=23).place(x=402,y=30,height=70)

  btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
  
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  email=Label(labelframe2,text="Email").place(x=10,y=5)
  e5=Entry(labelframe2,width=30).place(x=80,y=5)
  sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
  e6=Entry(labelframe2,width=30).place(x=402,y=5)
    
  labelframe = LabelFrame(fir1Frame,text="Invoice",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)
  order=Label(labelframe,text="Invoice#").place(x=5,y=5)
  e1=Entry(labelframe,width=25).place(x=100,y=5,)
  orderdate=Label(labelframe,text="Invoice date").place(x=5,y=33)
  e2=Entry(labelframe,width=20).place(x=150,y=33)
  checkvarStatus5=IntVar()
  duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
  e3=Entry(labelframe,width=20).place(x=150,y=62)
  terms=Label(labelframe,text="Terms").place(x=5,y=92)
  e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  e1=Entry(labelframe,width=27).place(x=100,y=118)

  fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
  
  tree=ttk.Treeview(listFrame)
  tree["columns"]=["1","2","3","4","5","6","7","8"]

  tree.column("#0", width=40)
  tree.column("1", width=80)
  tree.column("2", width=190)
  tree.column("3", width=190)
  tree.column("4", width=80)
  tree.column("5", width=60)
  tree.column("6", width=60)
  tree.column("7", width=60)
  tree.column("8", width=80)
  
  tree.heading("#0")
  tree.heading("1",text="ID/SKU")
  tree.heading("2",text="Product/Service")
  tree.heading("3",text="Description")
  tree.heading("4",text="Unit Price")
  tree.heading("5",text="Quality")
  tree.heading("6",text="Pcs/Weight")
  tree.heading("7",text="Tax1")
  tree.heading("8",text="Price")
  
  tree.pack(fill="both", expand=1)
  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

  fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  invoiceFrame = Frame(myNotebook, height=200, width=800)
  recurFrame = Frame(myNotebook, height=200, width=800)
  payementFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
  
  myNotebook.add(invoiceFrame,compound="left", text="Invoice")
  myNotebook.add(recurFrame,compound="left", text="Recurring")
  myNotebook.add(payementFrame,compound="left", text="Payements")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both")  

  labelframe1 = LabelFrame(invoiceFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=800,height=170)
  cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  e1=ttk.Combobox(labelframe1, value="",width=20).place(x=115,y=5)
  rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  e2=Entry(labelframe1,width=6).place(x=460,y=5)
  cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  e3=Entry(labelframe1,width=10).place(x=115,y=35)
  tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
  e4=Entry(labelframe1,width=7).place(x=460,y=35)
  template=Label(labelframe1,text="Template").place(x=37,y=70)
  e5=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
  sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  e6=Entry(labelframe1,width=18).place(x=115,y=100)
  category=Label(labelframe1,text="Category").place(x=300,y=100)
  e7=Entry(labelframe1,width=22).place(x=370,y=100)
  
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
  on1=Label(statusfrme, text="Emailed on:").place( y=50)
  nev1=Label(statusfrme, text="Never").place(x=100,y=50)
  on2=Label(statusfrme, text="Printed on:").place( y=90)
  nev2=Label(statusfrme, text="Never").place(x=100,y=90)

  text1=Label(headerFrame,text="Title text").place(x=50,y=5)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
  text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
  text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

  text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
  e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

  e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

  e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

  btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
  text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  cusventtree=ttk.Treeview(documentFrame, height=5)
  cusventtree["columns"]=["1","2","3"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=250)
  cusventtree.column("2", width=250)
  cusventtree.column("2", width=200)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Attach to Email")
  cusventtree.heading("2",text="Filename")
  cusventtree.heading("3",text="Filesize")  
  cusventtree.place(x=50, y=45)
  

  fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme.place(x=0,y=0,width=200,height=170)
  discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
  discount1=Label(summaryfrme, text="$0.00").place(x=130 ,y=0)
  sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
  sub1=Label(summaryfrme, text="$0.00").place(x=130 ,y=21)
  tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
  tax1=Label(summaryfrme, text="$0.00").place(x=130 ,y=42)
  cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
  cost=Label(summaryfrme, text="$0.00").place(x=130 ,y=63)
  order=Label(summaryfrme, text="Order total").place(x=0 ,y=84)
  order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)
  total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
  total1=Label(summaryfrme, text="$0.00").place(x=130 ,y=105)
  balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
  balance1=Label(summaryfrme, text="$0.00").place(x=130 ,y=126)

  fir5Frame=Frame(pop,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
  btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)





#---------------------------- Buttons--------------------------------------

mainFrame=Frame(tab4, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

invoiceLabel = Button(midFrame,compound="top", text="Generate recurring\n invoices",relief=RAISED, image=video,bg="#f8f8f2", fg="black", height=55, bd=1, width=95,command=generate_recurring_invoice_success)
invoiceLabel.pack(side="left", pady=3, ipadx=4)


w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

orderLabel = Button(midFrame,compound="top", text="View/Edit\nInvoice",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=view_invoice_recurring) 
orderLabel.pack(side="left")


w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

previewLabel = Button(midFrame,compound="top", text="Print Preview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=printpreviewinvoice_recurring)
previewLabel.pack(side="left")

purchaseLabel = Button(midFrame,compound="top", text="Print Invoice",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=print_invoice_recurring)
purchaseLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

expenseLabel = Button(midFrame,compound="top", text=" E-mail \nInvoice",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=email_invoice_recurring)
expenseLabel.pack(side="left")


w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Search in\nInvoices",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=search_invoice_recurring)
productLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Refresh\nInvoices list",relief=RAISED, image=photo8,bg="#f8f8f2",fg="black", height=55, bd=1, width=75)
productLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Show totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=lambda: label.place())
productLabel.pack(side="left")

productLabel = Button(midFrame,compound="top", text="Hide totals\nSUM",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=75,command=lambda: label.place_forget())
productLabel.pack(side="left")

label = Label(mainFrame, text = "$500")
label.place(x= 100 , y=120)


invoilabel = Label(mainFrame, text="Recurring invoices", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))



#------------------------------End Buttons-----------------------------------------------







# Recurring invoice table and scrollbars


class MyApp1:
  def __init__(self, parent):
    
    self.myParent = parent 

    self.myContainer1 = Frame(parent) 
    self.myContainer1.pack()
    
    self.top_frame = Frame(self.myContainer1) 
    self.top_frame.pack(side=TOP,
      fill=BOTH, 
      expand=YES,
      )  

    self.left_frame = Frame(self.top_frame, background="white",
      borderwidth=5,  relief=RIDGE,
      height=250, 
      width=2000, 
      )
    self.left_frame.pack(side=LEFT,
      fill=BOTH, 
      expand=YES,
      )

    
    tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Invoice#")
    tree.heading(3, text="Next Invoice")
    tree.heading(4, text="Recurring Period")
    tree.heading(5, text="Stop After")
    tree.heading(6, text="Customer Name")
    tree.heading(7, text="Invoice Total")  
    tree.column(1, width = 40)
    tree.column(2, width = 200)
    tree.column(3, width = 200)
    tree.column(4, width = 200)
    tree.column(5, width = 200)
    tree.column(6, width = 340)
    tree.column(7, width = 190)
  

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=1008+300+25, y=0, height=300+20)
    scrollbar.config( command=tree.yview )



    tabControl = ttk.Notebook(self.left_frame,width=1)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoice Items')
    tabControl.add(tab2,image=photo11,compound = LEFT, text ='Invoice Private Notes')
    tabControl.add(tab3,image=smslog,compound = LEFT, text ='SMS log')
    tabControl.add(tab4,image=photo11,compound = LEFT, text ='Documents')
    tabControl.pack(expand = 1, fill ="both")
    
    tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Product/Service ID",)
    tree.heading(3, text="Name")
    tree.heading(4, text="Description")
    tree.heading(5, text="Price")
    tree.heading(6, text="QTY")
    tree.heading(7, text="Tax1")
    tree.heading(8, text="Line Total")   
    tree.column(1, width = 40)
    tree.column(2, width = 250)
    tree.column(3, width = 270)
    tree.column(4, width = 300)
    tree.column(5, width = 130)
    tree.column(6, width = 100)
    tree.column(7, width = 100)
    tree.column(8, width = 190)

    note1=Text(tab2, width=170,height=10).place(x=10, y=10)

    note1=Text(tab3, width=170,height=10).place(x=10, y=10)

    tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Attach to Email",)
    tree.heading(3, text="Filename")
    tree.column(1, width = 30)
    tree.column(2, width = 310)
    tree.column(3, width = 1000)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=1004+300+25, y=360, height=195)
    scrollbar.config( command=tree.yview )
       
myapp = MyApp1(tab4)


####### TAB 5Expense Module-###################################################

def add_expense():
    window = Toplevel()  
    
    window.title("Add new Expense")
    p2 = PhotoImage(file = 'images/fbicon.png')
    window.iconphoto(False, p1)
 
    window.geometry("618x449+380+167")

    innerexpFrame = Frame(window, relief=GROOVE)
    innerexpFrame.pack(side="top",fill=BOTH)

    expenselabelframe = LabelFrame(innerexpFrame,text="Expense Cost",width=580,height=400)
    expenselabelframe.pack(side="top",fill=BOTH,padx=10)


    expamountval = IntVar(expenselabelframe, value='$.00')
    expamount=Label(expenselabelframe,text="Expense amount:",pady=10,padx=10)
    expamount.place(x=12,y=0)
    expamountentry = Entry(expenselabelframe,width=15,textvariable=expamountval)
    expamountentry.place(x=130,y=10)

    lbl_date=Label(expenselabelframe,text=" Date :",fg='black')
    lbl_date.place(x=380,y=10)
    
    expdate=DateEntry(expenselabelframe)
    expdate.place(x=450,y=12)

    vendor1=Label(expenselabelframe,text="Vendor:",pady=5,padx=10)
    vendor1.place(x=20,y=40)
    vn = StringVar() 
    vendor = ttk.Combobox(expenselabelframe, width = 27, textvariable = vn ) 
      
    # Adding combobox drop down list 
    vendor['values'] = ('Default') 
      
    vendor.place(x=130,y=45) 
    vendor.current(0)

    categoryexp1=Label(expenselabelframe,text="Category:",pady=5,padx=10)
    categoryexp1.place(x=330,y=40)
    cn = StringVar() 
    categorydrop = ttk.Combobox(expenselabelframe, width = 22, textvariable = cn ) 
      
    # Adding combobox drop down list 
    categorydrop['values'] = ('Default' ) 
      
    categorydrop.place(x=400,y=45) 
    categorydrop.current(0)

    

    expdescription=Label(expenselabelframe,text="Description:",pady=10,padx=10)
    expdescription.place(x=12,y=70)
    expdescriptionentry = Entry(expenselabelframe,width=70)
    expdescriptionentry.place(x=130,y=81)

    expstafftval = StringVar(expenselabelframe, value='Administrator')
    expstaff=Label(expenselabelframe,text="Staff member:",pady=10,padx=10)
    expstaff.place(x=12,y=108)
    expstaffentry = Entry(expenselabelframe,width=30,textvariable=expstafftval)
    expstaffentry.place(x=130,y=118)

    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(expenselabelframe,variable = checkvarStatus4, 
                      text="Taxable Tax1 rate", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=400,y=120)

    Button5 = Checkbutton(expenselabelframe, text = "Assign to customer (optional)")
    Button5.place(x=40, y=160)
    
    Button6 = Checkbutton(expenselabelframe, text = "Attach receipt image(optional,image will be stored to the database)")
    Button6.place(x=40, y=200)


    exptext1=Label(expenselabelframe,text="Notes",pady=5,padx=10)
    exptext1.place(x=12,y=246)
    exptxt = scrolledtext.ScrolledText(expenselabelframe, undo=True,width=67,height=5)
    exptxt.place(x=22,y=280)

    expokButton = Button(window, text ="Ok",image=tick,width=70,compound = LEFT)
    expokButton.place(x=280,y=415)

    window.mainloop()

########################VIEW/EDIT EXPENSE#######################################################################



def edit_expense():
    window1 = Toplevel()  
    
    window1.title("Edit Expense")
    p2 = PhotoImage(file = 'images/fbicon.png')
    window1.iconphoto(False, p1)
 
    window1.geometry("618x449+380+167")

    innerexpFrame = Frame(window1, relief=GROOVE)
    innerexpFrame.pack(side="top",fill=BOTH)

    expenselabelframe = LabelFrame(innerexpFrame,text="Expense Cost",width=580,height=400)
    expenselabelframe.pack(side="top",fill=BOTH,padx=10)


    expamountval = IntVar(expenselabelframe, value='$.00')
    expamount=Label(expenselabelframe,text="Expense amount:",pady=10,padx=10)
    expamount.place(x=12,y=0)
    expamountentry = Entry(expenselabelframe,width=15,textvariable=expamountval)
    expamountentry.place(x=130,y=10)

    lbl_date=Label(expenselabelframe,text=" Date :",fg='black')
    lbl_date.place(x=380,y=10)
    
    expdate=DateEntry(expenselabelframe)
    expdate.place(x=450,y=12)

    vendor1=Label(expenselabelframe,text="Vendor:",pady=5,padx=10)
    vendor1.place(x=20,y=40)
    vn = StringVar() 
    vendor = ttk.Combobox(expenselabelframe, width = 27, textvariable = vn ) 
      
    # Adding combobox drop down list 
    vendor['values'] = ('Default') 
      
    vendor.place(x=130,y=45) 
    vendor.current(0)

    categoryexp1=Label(expenselabelframe,text="Category:",pady=5,padx=10)
    categoryexp1.place(x=330,y=40)
    cn = StringVar() 
    categorydrop = ttk.Combobox(expenselabelframe, width = 22, textvariable = cn ) 
      
    # Adding combobox drop down list 
    categorydrop['values'] = ('Default') 
      
    categorydrop.place(x=400,y=45) 
    categorydrop.current(0)

    

    expdescription=Label(expenselabelframe,text="Description:",pady=10,padx=10)
    expdescription.place(x=12,y=70)
    expdescriptionentry = Entry(expenselabelframe,width=70)
    expdescriptionentry.place(x=130,y=81)

    expstafftval = StringVar(expenselabelframe, value='Administrator')
    expstaff=Label(expenselabelframe,text="Staff member:",pady=10,padx=10)
    expstaff.place(x=12,y=108)
    expstaffentry = Entry(expenselabelframe,width=30,textvariable=expstafftval)
    expstaffentry.place(x=130,y=118)

    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(expenselabelframe,variable = checkvarStatus4, 
                      text="Taxable Tax1 rate", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=400,y=120)

    Button5 = Checkbutton(expenselabelframe, text = "Assign to customer (optional)")
    Button5.place(x=40, y=160)
    
    Button6 = Checkbutton(expenselabelframe, text = "Attach receipt image(optional,image will be stored to the database)")
    Button6.place(x=40, y=200)


    exptext1=Label(expenselabelframe,text="Notes",pady=5,padx=10)
    exptext1.place(x=12,y=246)
    exptxt = scrolledtext.ScrolledText(expenselabelframe, undo=True,width=67,height=50)
    exptxt.place(x=22,y=280)

    expokButton = Button(window1, text ="Ok",image=tick,width=70,compound = LEFT)
    expokButton.place(x=280,y=415)

    window1.mainloop()


######################## DELETE EXPENSE #######################################################################


def delete_expense():
    
    messagebox.askyesno("Delete Expense", "Are you sure to delete this Expense?")


######################## SEARCH EXPENSE ######################################################################
    

def search_expense():
    top = Toplevel()  
    
    top.title("Find Text")
    
    
    top.geometry("520x200+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10)
    findwhat1.place(x=5,y=20)
    n = StringVar() 
    findwhat = ttk.Combobox(top, width = 50, textvariable = n ) 
      
    # Adding combobox drop down list 
    
    findwhat.place(x=80,y=25) 
    

    findButton = Button(top, text ="Find next",width=10)
    findButton.place(x=420,y=20)

    findin1=Label(top,text="Find in:",pady=5,padx=10)
    findin1.place(x=5,y=47)
    n = StringVar() 
    findIN = ttk.Combobox(top, width = 37, textvariable = n ) 
      
    # Adding combobox drop down list 
    findIN['values'] = ('Client',  
                              ' Date', 
                              ' Category', 
                              ' Vendor', 
                              ' Staff Member', 
                              ' Description', 
                              ' Rebillable',
                              'Invoiced',
                              'Image',
                              'Rebill Amount',
                              'Amount',
                        
                              ' <<All>>') 
      
    findIN.place(x=80,y=54) 
    findIN.current(0)

    closeButton = Button(top, text ="Close",width=10)
    closeButton.place(x=420,y=50)

    match1=Label(top,text="Match:",pady=5,padx=10)
    match1.place(x=5,y=74)
    n = StringVar() 
    match = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    match['values'] = ('From Any part of the field',' Whole Field',  
                              ' From the beginning of the field')
      
    match.place(x=80,y=83) 
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10)
    search1.place(x=5,y=102)
    n = StringVar() 
    search = ttk.Combobox(top, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    search['values'] = ('All', 'up', 
                              ' Down')
      
    search.place(x=80,y=112) 
    search.current(0)


    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(top,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=60,y=141)

    checkvarStatus5=IntVar()
   
    Button5 = Checkbutton(top,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button5.place(x=270,y=141)





  

######################## FRONT PAGE OF EXPENSE MODULE #######################################################################


    
expframe = Frame(tab6,relief=GROOVE,bg="#f8f8f2")
expframe.pack(side="top", fill=BOTH)

expmidFrame=Frame(expframe, height=60,bg="#f5f3f2")
expmidFrame.pack(side="top", fill=X)

e = Canvas(expmidFrame, width=1, height=65, bg="#f8f8f2", bd=0)
e.pack(side="left", padx=(5, 2))
e = Canvas(expmidFrame, width=1, height=65, bg="#f8f8f2", bd=0)
e.pack(side="left", padx=(0, 5))

expenseIcon = ImageTk.PhotoImage(Image.open("images/plus.png"))
expenseLabel = Button(expmidFrame,compound="top", text="Create new\nExpense",relief=RAISED,command=add_expense, image=expenseIcon,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,)
expenseLabel.pack(side="left", pady=3, ipadx=4)

expeditIcon = ImageTk.PhotoImage(Image.open("images/edit.png"))
expeditLabel = Button(expmidFrame,compound="top", text="Edit/View\nExpense",relief=RAISED, image=expeditIcon,command=edit_expense,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
expeditLabel.pack(side="left")

expdeleteIcon = ImageTk.PhotoImage(Image.open("images/delete.png"))
expdeleteLabel = Button(expmidFrame,compound="top", text="Delete\nSelected", relief=RAISED, command=delete_expense,image=expdeleteIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
expdeleteLabel.pack(side="left")

e = Canvas(expmidFrame, width=1, height=65, bg="#b3b3b3", bd=0)
e.pack(side="left", padx=5)

expsearchIcon = ImageTk.PhotoImage(Image.open("images/search-icon.png"))
expsearchLabel = Button(expmidFrame,compound="top", text="Search in\nExpenses",relief=RAISED,command=search_expense, image=expsearchIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, )
expsearchLabel.pack(side="left")


lbframe = LabelFrame(expmidFrame, height=60, width=200)
lbframe.pack(side="left", padx=10, pady=0)

lbl_expdt=Label(lbframe,text="Expense date from:",fg='black')
lbl_expdt.grid(row=0, column=0, pady=5, padx=(5, 0))

lbl_expdtt=Label(lbframe,text="Expense date to:" , fg='black')
lbl_expdtt.grid(row=1, column=0, pady=5, padx=(5, 0))

   
expdt=DateEntry(lbframe)
expdt.grid(row=0, column=1)
   
expdtt=DateEntry(lbframe)
expdtt.grid(row=1, column=1)
   
checkvar1 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8)
chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))


e = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
e.pack(side="left", padx=5)

exprefreshIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
exprefreshLabel = Button(expmidFrame,compound="top", text="Refresh\nExpense List",relief=RAISED, image=exprefreshIcon,bg="#f8f8f2", fg="black", height=55, bd=1, width=63)
exprefreshLabel.pack(side="left")



invoi1label = Label(expframe, text="Expenses (All)", font=("arial", 18), bg="#f8f8f2")
invoi1label.pack(side="left", padx=(20,0))
drop1 = ttk.Combobox(expframe, value="Hello")
drop1.pack(side="right", padx=(0,10))
invoi1label = Label(expframe, text="Category filter", font=("arial", 15), bg="#f8f8f2")
invoi1label.pack(side="right", padx=(0,10))



#table 
s = ttk.Style()
s.configure('Treeview.Heading', background='white', State='DISABLE')


tree=ttk.Treeview(tab6,selectmode='browse')
tree.place(x=0,y=105,height=580)

expverticalbar=ttk.Scrollbar(tab6,orient="vertical",command=tree.yview,)
expverticalbar.place(x=1345,y=102,height=570,)
expverticalbar.place(x=1345,y=102,height=570)
tree["columns"]=("1","2","3","4","5","6","7","8","9","10","11","12")
tree["show"]='headings'
tree.column("1",width=5,anchor='c')
tree.column("2",width=130,anchor='c')
tree.column("3",width=110,anchor='c')
tree.column("4",width=120,anchor='c')
tree.column("5",width=120,anchor='c')
tree.column("6",width=120,anchor='c')
tree.column("7",width=220,anchor='c')
tree.column("8",width=120,anchor='c')
tree.column("9",width=100,anchor='c')
tree.column("10",width=100,anchor='c')
tree.column("11",width=100,anchor='c')
tree.column("12",width=100,anchor='c')
tree.heading("2",text="Client")
tree.heading("3",text="Date")
tree.heading("4",text="Category")
tree.heading("5",text="Vendor")
tree.heading("6",text="Staff member")
tree.heading("7",text="Description")
tree.heading("8",text="Rebillable")
tree.heading("9",text="Invoiced")
tree.heading("10",text="Image")
tree.heading("11",text="Rebill Amount")
tree.heading("12",text="Amount")

#######sandep###INVOICE
def create():
  pop=Toplevel(midFrame)
  pop.title("Invoice")
  pop.geometry("950x690+150+0")


  #select customer
  def custom():
    cuselection=Toplevel()
    cuselection.title("Select Customer")
    cuselection.geometry("930x650+240+10")
    cuselection.resizable(False, False)


    #add new customer
    def create1():
      ven=Toplevel(midFrame)
      ven.title("Add new vendor")
      ven.geometry("930x650+240+10")
      checkvar1=IntVar()
      checkvar2=IntVar()
      radio=IntVar()
      createFrame=Frame(ven, bg="#f5f3f2", height=650)
      createFrame.pack(side="top", fill="both")
      labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
      labelframe1.place(x=10,y=5,width=910,height=600)
      text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
      e1=Entry(labelframe1,width=25).place(x=150,y=10)
      text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
      e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
      text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
      Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
      
      labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
      labelframe2.place(x=5,y=40,width=420,height=150)
      name = Label(labelframe2, text="Business name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
      e1 = Entry(labelframe2,width=28).place(x=130,y=5)
      addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
      e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
      
      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

      labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
      labelframe3.place(x=480,y=40,width=420,height=150)
      name = Label(labelframe3, text="Ship to name:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe3,width=28).place(x=130,y=5)
      addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
      e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
      
      labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe4.place(x=5,y=195,width=420,height=150)
      name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe4,width=28).place(x=130,y=5)
      email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
      e2 = Entry(labelframe4,width=28).place(x=130,y=35)
      tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe4,width=11).place(x=130,y=65)
      fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe4,width=11).place(x=280,y=65)
      sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
      e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

      
      labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
      labelframe5.place(x=480,y=195,width=420,height=125)
      name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe5,width=28).place(x=130,y=5)
      email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe5,width=28).place(x=130,y=35)
      tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe5,width=11).place(x=130,y=65)
      fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe5,width=11).place(x=280,y=65)

      labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe6.place(x=5,y=350,width=420,height=100)
      Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
      tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
      e1 = Entry(labelframe6,width=10).place(x=290,y=5)
      discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe6,width=10).place(x=100,y=35)

      labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe7.place(x=480,y=330,width=420,height=100)
      country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe7,width=28).place(x=130,y=5)
      city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe7,width=28).place(x=130,y=35)

      labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
      labelframe8.place(x=5,y=460,width=420,height=100)
      R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
      R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
      R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
      

      labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
      labelframe9.place(x=480,y=430,width=420,height=150)
      e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

      btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
      btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
        
               

    enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(cuselection, width=20).place(x=110, y=10)
    text=Label(cuselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(cuselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(cuselection, height=27)
    cusventtree["columns"]=["1","2","3", "4"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=140)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="Customer/Ventor ID")
    cusventtree.heading("2",text="Customer/Ventor Name")
    cusventtree.heading("3",text="Tel.")
    cusventtree.heading("4",text="Contact Person")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(cuselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(cuselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )

    btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=create1).place(x=250, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=create1).place(x=435, y=610)
    btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   



    

  #add new line item
  def newline():
    newselection=Toplevel()
    newselection.title("Product/Services")
    newselection.geometry("930x650+240+10")
    newselection.resizable(False, False)


    #add new product
    def product():  
      top = Toplevel()  
      top.title("Add a new Product/Service")
      p2 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p2)
    
      top.geometry("700x550+390+15")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
     
      tabControl.add(tab1,compound = LEFT, text ='Product/Service')
      tabControl.add(tab2,compound = LEFT, text ='Product Image')
     
      tabControl.pack(expand = 1, fill ="both")
     
      innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

      code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      code1.place(x=20,y=0)
      codeentry = Entry(Customerlabelframe,width=35)
      codeentry.place(x=120,y=8)

      checkvarStatus=IntVar()
      status1=Label(Customerlabelframe,text="Status:")
      status1.place(x=500,y=8)
      Button1 = Checkbutton(Customerlabelframe,
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                       
                        width = 10)

      Button1.place(x=550,y=5)

      category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
      category1.place(x=20,y=40)
      n = StringVar()
      country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
       
      country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
      
      country.place(x=120,y=45)
      country.current(0)


      name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
      name1.place(x=20,y=70)
      nameentry = Entry(Customerlabelframe,width=60)
      nameentry.place(x=120,y=75)

      des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
      des1.place(x=20,y=100)
      desentry = Entry(Customerlabelframe,width=60)
      desentry.place(x=120,y=105)

      uval = IntVar(Customerlabelframe, value='$0.00')
      unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      unit1.place(x=20,y=130)
      unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
      unitentry.place(x=120,y=135)

      pcsval = IntVar(Customerlabelframe, value='$0.00')
      pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      pcs1.place(x=320,y=140)
      pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
      pcsentry.place(x=410,y=140)

      costval = IntVar(Customerlabelframe, value='$0.00')
      cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
      cost1.place(x=20,y=160)
      costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
      costentry.place(x=120,y=165)

      priceval = IntVar(Customerlabelframe, value='$0.00')
      price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
      price1.place(x=20,y=190)
      priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
      priceentry.place(x=120,y=195)

      checkvarStatus2=IntVar()
     
      Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                        text="Taxable Tax1rate",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        height=2,
                        width = 12)

      Button2.place(x=415,y=170)


      checkvarStatus3=IntVar()
     
      Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                        text="No stock Control",
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      Button3.place(x=40,y=220)


      stockval = IntVar(Customerlabelframe)
      stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
      stock1.place(x=90,y=260)
      stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
      stockentry.place(x=150,y=265)

      lowval = IntVar(Customerlabelframe)
      low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      low1.place(x=300,y=260)
      lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
      lowentry.place(x=495,y=265)

     
      ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
      ware1.place(x=60,y=290)
      wareentry = Entry(Customerlabelframe,width=50)
      wareentry.place(x=150,y=295)

      text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      text1.place(x=20,y=330)

      txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
      txt.place(x=32,y=358)




      okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
      okButton.pack(side=LEFT)

      cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
      cancelButton.pack(side=RIGHT)

      imageFrame = Frame(tab2, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse')
      browsebutton.place(x=580,y=30,height=30,width=50)
      
      removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
      removeButton.place(x=400,y=450)



    
                    
    enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(newselection, width=20).place(x=110, y=10)
    text=Label(newselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(newselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(newselection, height=27)
    cusventtree["columns"]=["1","2","3", "4","5"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=70)
    cusventtree.column("5", width=70)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="ID/SKU")
    cusventtree.heading("2",text="Product/Service Name")
    cusventtree.heading("3",text="Unit price")
    cusventtree.heading("4",text="Service")
    cusventtree.heading("5",text="Stock")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(newselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(newselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )
   

    btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
    btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



  #preview new line
  def previewline():
    messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


  
  #sms notification
  def sms1():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 

  #mark invoice
  def markinvo():
    mark_inv=Toplevel()
    mark_inv.geometry("700x480+240+150")
    mark_inv.title("Record Payement for Invoice")
    checkvar=IntVar()
    checkvar1=IntVar()
    checkvar2=IntVar()

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    mark_Notebook = ttk.Notebook(mark_inv)
    Mark_Invoice = Frame(mark_Notebook, height=470, width=750)
    mark_Notebook.add(Mark_Invoice, text="Mark Invoice")
    mark_Notebook.place(x=0, y=0)

    involbel=Label(Mark_Invoice, text="Invoice Balance")
    involbel.place(x=10, y=10)
    numentry=Entry(Mark_Invoice, width=45).place(x=130, y=10)

    labelframe5 = LabelFrame(Mark_Invoice,text="Payement Record Details",bg="#f5f3f2")
    labelframe5.place(x=10,y=60,width=670,height=250)
    e1 = Entry(labelframe5,width=28).place(x=30,y=45)
    pdate = Label(labelframe5, text="Payement Date:",bg="#f5f3f2").place(x=250,y=20)
    e2 = Entry(labelframe5,width=28).place(x=220,y=45)
    payd = Label(labelframe5, text="Paid By:",bg="#f5f3f2").place(x=450,y=20)
    drop = ttk.Combobox(labelframe5, value="Hello")
    drop.place(x=450,y=45)
    involbel=Label(labelframe5, text="Description")
    involbel.place(x=30, y=80)
    numentry=Entry(labelframe5, width=100).place(x=30, y=120)
    Checkbutton(labelframe5,text="Paid in full and close invoice",variable=checkvar,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=30 ,y=150)
    pl = Label(labelframe5,text="Payement Reciepts",bg="#f5f3f2")
    pl.place(x=300,y=145)
    Checkbutton(labelframe5,text="Send Payement Reciept",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=170)
    Checkbutton(labelframe5,text="Attach updated invoice",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=320 ,y=200)

    okbtn=Button(Mark_Invoice,compound = LEFT,image=tick , text="Save payement", width=100).place(x=10, y=350)
    canbtn=Button(Mark_Invoice,compound = LEFT,image=cancel, text="Cancel", width=100).place(x=500, y=350)

    
  #voidinvoice
  def voidinvoice():
    messagebox.askyesno("F-Billing Revolution","Are you sure to avoid this invoice?\nAll products will be placed back into stock and all payemnts will be voided.")
  
  #delete line item  
  def delete1():
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")
    
    

  firFrame=Frame(pop, bg="#f5f3f2", height=60)
  firFrame.pack(side="top", fill=X)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=custom)
  create.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=newline)
  add.pack(side="left", pady=3, ipadx=4)

  dele= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=delete1)
  dele.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  prev= Button(firFrame,compound="top", text="Preview\nInvoice",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline)
  prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(firFrame,compound="top", text="Print \nInvoice",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(firFrame,compound="top", text="Email\nInvoice",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=emailord)
  mail.pack(side="left", pady=3, ipadx=4)

  sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms1)
  sms1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mark= Button(firFrame,compound="top", text="Mark invoice\nas 'Paid'",relief=RAISED, image=mark1,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=markinvo)
  mark.pack(side="left", pady=3, ipadx=4)

  void= Button(firFrame,compound="top", text="Void\ninvoice",relief=RAISED, image=mark2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=voidinvoice)
  void.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  calc.pack(side="left", pady=3, ipadx=4)

  fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
  fir1Frame.pack(side="top", fill=X)

  labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)
  order = Label(labelframe1, text="Order to").place(x=10,y=5)
  e1 = ttk.Combobox(labelframe1, value="Hello",width=28).place(x=80,y=5)
  address=Label(labelframe1,text="Address").place(x=10,y=30)
  e2=Text(labelframe1,width=23).place(x=80,y=30,height=70)
  ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
  e3=Entry(labelframe1,width=30).place(x=402,y=3)
  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  e4=Text(labelframe1,width=23).place(x=402,y=30,height=70)

  btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
  
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  email=Label(labelframe2,text="Email").place(x=10,y=5)
  e5=Entry(labelframe2,width=30).place(x=80,y=5)
  sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
  e6=Entry(labelframe2,width=30).place(x=402,y=5)
    
  labelframe = LabelFrame(fir1Frame,text="Invoice",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)
  order=Label(labelframe,text="Invoice#").place(x=5,y=5)
  e1=Entry(labelframe,width=25).place(x=100,y=5,)
  orderdate=Label(labelframe,text="Invoice date").place(x=5,y=33)
  e2=Entry(labelframe,width=20).place(x=150,y=33)
  checkvarStatus5=IntVar()
  duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
  e3=Entry(labelframe,width=20).place(x=150,y=62)
  terms=Label(labelframe,text="Terms").place(x=5,y=92)
  e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  e1=Entry(labelframe,width=27).place(x=100,y=118)

  fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
  
  tree=ttk.Treeview(listFrame)
  tree["columns"]=["1","2","3","4","5","6","7","8"]

  tree.column("#0", width=40)
  tree.column("1", width=80)
  tree.column("2", width=190)
  tree.column("3", width=190)
  tree.column("4", width=80)
  tree.column("5", width=60)
  tree.column("6", width=60)
  tree.column("7", width=60)
  tree.column("8", width=80)
  
  tree.heading("#0")
  tree.heading("1",text="ID/SKU")
  tree.heading("2",text="Product/Service")
  tree.heading("3",text="Description")
  tree.heading("4",text="Unit Price")
  tree.heading("5",text="Quality")
  tree.heading("6",text="Pcs/Weight")
  tree.heading("7",text="Tax1")
  tree.heading("8",text="Price")
  
  tree.pack(fill="both", expand=1)
  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

  fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  invoiceFrame = Frame(myNotebook, height=200, width=800)
  recurFrame = Frame(myNotebook, height=200, width=800)
  payementFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
  
  myNotebook.add(invoiceFrame,compound="left", text="Invoice")
  myNotebook.add(recurFrame,compound="left", text="Recurring")
  myNotebook.add(payementFrame,compound="left", text="Payements")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both")  

  labelframe1 = LabelFrame(invoiceFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=800,height=170)
  cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  e1=ttk.Combobox(labelframe1, value="",width=20).place(x=115,y=5)
  rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  e2=Entry(labelframe1,width=6).place(x=460,y=5)
  cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  e3=Entry(labelframe1,width=10).place(x=115,y=35)
  tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
  e4=Entry(labelframe1,width=7).place(x=460,y=35)
  template=Label(labelframe1,text="Template").place(x=37,y=70)
  e5=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
  sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  e6=Entry(labelframe1,width=18).place(x=115,y=100)
  category=Label(labelframe1,text="Category").place(x=300,y=100)
  e7=Entry(labelframe1,width=22).place(x=370,y=100)
  
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
  on1=Label(statusfrme, text="Emailed on:").place( y=50)
  nev1=Label(statusfrme, text="Never").place(x=100,y=50)
  on2=Label(statusfrme, text="Printed on:").place( y=90)
  nev2=Label(statusfrme, text="Never").place(x=100,y=90)

  text1=Label(headerFrame,text="Title text").place(x=50,y=5)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
  text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
  text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

  text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
  e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

  e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

  e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

  btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
  text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  cusventtree=ttk.Treeview(documentFrame, height=5)
  cusventtree["columns"]=["1","2","3"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=250)
  cusventtree.column("2", width=250)
  cusventtree.column("2", width=200)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Attach to Email")
  cusventtree.heading("2",text="Filename")
  cusventtree.heading("3",text="Filesize")  
  cusventtree.place(x=50, y=45)
  

  fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme.place(x=0,y=0,width=200,height=170)
  discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
  discount1=Label(summaryfrme, text="$0.00").place(x=130 ,y=0)
  sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
  sub1=Label(summaryfrme, text="$0.00").place(x=130 ,y=21)
  tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
  tax1=Label(summaryfrme, text="$0.00").place(x=130 ,y=42)
  cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
  cost=Label(summaryfrme, text="$0.00").place(x=130 ,y=63)
  order=Label(summaryfrme, text="Order total").place(x=0 ,y=84)
  order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)
  total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
  total1=Label(summaryfrme, text="$0.00").place(x=130 ,y=105)
  balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
  balance1=Label(summaryfrme, text="$0.00").place(x=130 ,y=126)

  fir5Frame=Frame(pop,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
  btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)




#printselected order
  
def printsele():

  def property1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 15, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy count:").place(x=55, y=95)

      okbtn=Button(propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
      canbtn=Button(propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
      
      


    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=property2).place(x=550, y=380)
    btn=Button(property_Frame,compound = LEFT,image=tick  ,text="OK", width=60,).place(x=430, y=420)
    btn=Button(property_Frame,compound = LEFT,image=cancel , text="Cancel", width=60,).place(x=550, y=420)     


    
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=370)
      canbtn=Button(print1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=370)
      


#email
      
def emailorder():
  mailDetail=Toplevel()
  mailDetail.title("E-Mail Invoice List")
  p2 = PhotoImage(file = "images/fbicon.png")
  mailDetail.iconphoto(False, p2)
  mailDetail.geometry("1030x550+150+120")
 
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)
  messagelbframe=LabelFrame(email_Frame,text="Message", height=495, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)

  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)
  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)
  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings").place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)





#sms notification order
  
def sms():
  send_SMS=Toplevel()
  send_SMS.geometry("700x480+240+150")
  send_SMS.title("Send SMS notification")

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  sms_Notebook = ttk.Notebook(send_SMS)
  SMS_Notification = Frame(sms_Notebook, height=470, width=700)
  SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
  sms_Notebook.add(SMS_Notification, text="SMS Notification")
  sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
  sms_Notebook.place(x=0, y=0)

  numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
  numlbel.place(x=10, y=10)
  numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
  stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
  stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
  
  dclbel=Label(SMS_Notification, text="Double click to insert into text")
  dclbel.place(x=410, y=60)
  dcl=Entry(SMS_Notification, width=30)
  dcl.place(x=400, y=85,height=200)
  
  smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
  smstype.place(x=10, y=223)
  snuvar=IntVar()
  normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
  unicode_rbtn.place(x=190, y=5)
  tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
  tiplbf.place(x=10, y=290)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
  tiplabl.place(x=5, y=5)

  btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
  btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
  btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
  

  smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
  smstype.place(x=10, y=5)
  snumvar=IntVar()
  normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
  unicode_rbtn.place(x=290, y=5)

  sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
  sms1type.place(x=10, y=80)
  name=Label(sms1type, text="Username").place(x=10, y=5)
  na=Entry(sms1type, width=20).place(x=100, y=5)
  password=Label(sms1type, text="Password").place(x=10, y=45)
  pas=Entry(sms1type, width=20).place(x=100, y=45)
  combo=Label(sms1type, text="Route").place(x=400, y=5)
  n = StringVar()
  combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
  btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

  
  tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
  tiplbf.place(x=10, y=190)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
  tiplabl.place(x=0, y=5)
  tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
  tiplabl1.place(x=0, y=60)
  tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
  tiplabl2.place(x=0, y=100)
  tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
  tiplabl3.place(x=0, y=140)
  checkvar1=IntVar()
  chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200)  



#print preview order
def printpreview():
  messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")



#convert to invoice
def convert():
  if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
        messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
  else:
      messagebox.destroy()
  

#delete orders  
def dele():  
  messagebox.askyesno("Delete order", "Are you sure to delete this order? All products will be placed back into stock")




#search in orders  
def search():  
    top = Toplevel()     
    top.title("Find Text")   
    top.geometry("600x250+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
    n = StringVar()
    findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
    findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
    n = StringVar()
    findIN = ttk.Combobox(top, width = 30, textvariable = n )
    findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
    findIN.place(x=90,y=54)
    findIN.current(0)

    findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
    closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
    match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
    n = StringVar()
    match = ttk.Combobox(top, width = 23, textvariable = n )   
    match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
    match.place(x=90,y=83)
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
    n = StringVar()
    search = ttk.Combobox(top, width = 23, textvariable = n )
    search['values'] = ('All', 'up',' Down')
    search.place(x=90,y=112)
    search.current(0)
    checkvarStatus4=IntVar()  
    Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button4.place(x=90,y=141)
    checkvarStatus5=IntVar()   
    Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button5.place(x=300,y=141)





mainFrame=Frame(tab1, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

invoiceLabel = Button(midFrame,compound="top", text="Create new\nInvoice",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=create)
invoiceLabel.pack(side="left", pady=3, ipadx=4)

orderLabel = Button(midFrame,compound="top", text="View/Edit\nInvoice",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=create)
orderLabel.pack(side="left")

estimateLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=dele)
estimateLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)


w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

previewLabel = Button(midFrame,compound="top", text="Print\nPreview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red",command=printpreview)
previewLabel.pack(side="left")

purchaseLabel = Button(midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=printsele)
purchaseLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

expenseLabel = Button(midFrame,compound="top", text=" E-mail \nInvoice",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=emailord)
expenseLabel.pack(side="left")

smsLabel = Button(midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=sms)
smsLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Search in\nInvoices",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=search)
productLabel.pack(side="left")

lbframe = LabelFrame(midFrame, height=60, width=200, bg="#f8f8f2")
lbframe.pack(side="left", padx=10, pady=0)
lbl_invdt = Label(lbframe, text="Invoice date from : ", bg="#f8f8f2")
lbl_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
lbl_invdtt = Label(lbframe, text="Invoice date to  :  ", bg="#f8f8f2")
lbl_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))
invdt = Entry(lbframe, width=15)
invdt.grid(row=0, column=1)
invdtt = Entry(lbframe, width=15)
invdtt.grid(row=1, column=1)
checkvar1 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

productLabel = Button(midFrame,compound="top", text="Refresh\nInvoice list",relief=RAISED, image=photo8,fg="black", height=55, bd=1, width=55)
productLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
productLabel.pack(side="left")

invoilabel = Label(mainFrame, text="Invoices(All)", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))
drop = ttk.Combobox(mainFrame, value="Hello")
drop.pack(side="right", padx=(0,10))
invoilabel = Label(mainFrame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
invoilabel.pack(side="right", padx=(0,10))

class MyApp:
  def __init__(self, parent):
    
    self.myParent = parent 

    self.myContainer1 = Frame(parent) 
    self.myContainer1.pack()
    
    self.top_frame = Frame(self.myContainer1) 
    self.top_frame.pack(side=TOP,
      fill=BOTH, 
      expand=YES,
      )  

    self.left_frame = Frame(self.top_frame, background="white",
      borderwidth=5,  relief=RIDGE,
      height=250, 
      width=2000, 
      )
    self.left_frame.pack(side=LEFT,
      fill=BOTH, 
      expand=YES,
      )

    
    tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10,11,12), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Invoice#")
    tree.heading(3, text="Invoice date")
    tree.heading(4, text="Due date")
    tree.heading(5, text="Customer Name")
    tree.heading(6, text="Status")
    tree.heading(7, text="Emailed on")
    tree.heading(8, text="Printed on")
    tree.heading(9, text="SMS on")
    tree.heading(10, text="Invoice Total")
    tree.heading(11, text="Total Paid")
    tree.heading(12, text="Balance")
    tree.column(1, width = 35)
    tree.column(2, width = 130)
    tree.column(3, width = 110)
    tree.column(4, width = 110)
    tree.column(5, width = 180)
    tree.column(6, width = 110)
    tree.column(7, width = 130)
    tree.column(8, width = 110)
    tree.column(9, width = 110)
    tree.column(10, width = 110)
    tree.column(11, width = 110)
    tree.column(12, width = 100)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=995+340, y=0, height=300+20)
    scrollbar.config( command=tree.yview )

    tabControl = ttk.Notebook(self.left_frame,width=1)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tabControl.add(tab1,image=invoices,compound = LEFT, text ='Invoice Items',)
    tabControl.add(tab2,image=photo11,compound = LEFT, text ='Payements')
    tabControl.add(tab3,image=smslog,compound = LEFT, text ='Invoice private notes')
    tabControl.add(tab4,image=photo11,compound = LEFT, text ='SMS Log')
    tabControl.add(tab5,image=photo11,compound = LEFT, text ='Documents')
    tabControl.pack(expand = 1, fill ="both")
    
    tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Product/Service ID",)
    tree.heading(3, text="Name")
    tree.heading(4, text="Description")
    tree.heading(5, text="Price")
    tree.heading(6, text="QTY")
    tree.heading(7, text="Tax1")
    tree.heading(8, text="Line Total")   
    tree.column(1, width = 75)
    tree.column(2, width = 230)
    tree.column(3, width = 230)
    tree.column(4, width = 275)
    tree.column(5, width = 130)
    tree.column(6, width = 130)
    tree.column(7, width = 137)
    tree.column(8, width = 130)

    tree = ttk.Treeview(tab2, columns = (1,2,3,4,5,6), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Payement ID",)
    tree.heading(3, text="Payement Date")
    tree.heading(4, text="PaidBy")
    tree.heading(5, text="Description")
    tree.heading(6, text="Amount")
    tree.column(1, width = 50)
    tree.column(2, width = 270)
    tree.column(3, width = 270)
    tree.column(4, width = 300)
    tree.column(5, width = 450)
    tree.column(6, width = 150)
    

    note1=Text(tab3, width=170,height=10).place(x=10, y=10)

    tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Attach to Email",)
    tree.heading(3, text="Filename")
    tree.column(1, width = 70)
    tree.column(2, width = 430)
    tree.column(3, width = 1000)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=980+350, y=360, height=195)
    scrollbar.config( command=tree.yview )
       
myapp = MyApp(tab1)

###Order Module ###### MINHAJ

#ORDER MODULE



#create new order

def create():
  pop=Toplevel(midFrame)
  pop.title("Orders")
  pop.geometry("950x690+150+0")


  #select customer
  def custom():
    cuselection=Toplevel()
    cuselection.title("Select Customer")
    cuselection.geometry("930x650+240+10")
    cuselection.resizable(False, False)


    #add new customer
    def create1():
      ven=Toplevel(midFrame)
      ven.title("Add new vendor")
      ven.geometry("930x650+240+10")
      checkvar1=IntVar()
      checkvar2=IntVar()
      radio=IntVar()
      createFrame=Frame(ven, bg="#f5f3f2", height=650)
      createFrame.pack(side="top", fill="both")
      labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
      labelframe1.place(x=10,y=5,width=910,height=600)
      text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
      e1=Entry(labelframe1,width=25).place(x=150,y=10)
      text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
      e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
      text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
      Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
      
      labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
      labelframe2.place(x=5,y=40,width=420,height=150)
      name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
      e1 = Entry(labelframe2,width=28).place(x=130,y=5)
      addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
      e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)
      
      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

      labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
      labelframe3.place(x=480,y=40,width=420,height=150)
      name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe3,width=28).place(x=130,y=5)
      addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
      e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
      
      labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe4.place(x=5,y=195,width=420,height=150)
      name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe4,width=28).place(x=130,y=5)
      email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
      e2 = Entry(labelframe4,width=28).place(x=130,y=35)
      tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe4,width=11).place(x=130,y=65)
      fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe4,width=11).place(x=280,y=65)
      sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
      e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

      
      labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
      labelframe5.place(x=480,y=195,width=420,height=125)
      name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe5,width=28).place(x=130,y=5)
      email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe5,width=28).place(x=130,y=35)
      tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe5,width=11).place(x=130,y=65)
      fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe5,width=11).place(x=280,y=65)

      labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe6.place(x=5,y=350,width=420,height=100)
      Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
      tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
      e1 = Entry(labelframe6,width=10).place(x=290,y=5)
      discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe6,width=10).place(x=100,y=35)

      labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe7.place(x=480,y=330,width=420,height=100)
      country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe7,width=28).place(x=130,y=5)
      city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe7,width=28).place(x=130,y=35)

      labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
      labelframe8.place(x=5,y=460,width=420,height=100)
      R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
      R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
      R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
      

      labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
      labelframe9.place(x=480,y=430,width=420,height=150)
      e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

      btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick ,text="OK").place(x=20, y=615)
      btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
        
               

    enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(cuselection, width=20).place(x=110, y=10)
    text=Label(cuselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(cuselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(cuselection, height=27)
    cusventtree["columns"]=["1","2","3", "4"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=140)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="Customer/Ventor ID")
    cusventtree.heading("2",text="Customer/Ventor Name")
    cusventtree.heading("3",text="Tel.")
    cusventtree.heading("4",text="Contact Person")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(cuselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(cuselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )

    btn1=Button(cuselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick,text="Edit selected customer", width=150,command=create1).place(x=250, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick, text="Add new customer", width=150,command=create1).place(x=435, y=610)
    btn1=Button(cuselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)   



    

  #add new line item
  def newline():
    newselection=Toplevel()
    newselection.title("Select Customer")
    newselection.geometry("930x650+240+10")
    newselection.resizable(False, False)


    #add new product
    def product():  
      top = Toplevel()  
      top.title("Add a new Product/Service")
      p2 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p2)
    
      top.geometry("700x550+390+15")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
     
      tabControl.add(tab1,compound = LEFT, text ='Product/Service')
      tabControl.add(tab2,compound = LEFT, text ='Product Image')
     
      tabControl.pack(expand = 1, fill ="both")
     
      innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

      code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      code1.place(x=20,y=0)
      codeentry = Entry(Customerlabelframe,width=35)
      codeentry.place(x=120,y=8)

      checkvarStatus=IntVar()
      status1=Label(Customerlabelframe,text="Status:")
      status1.place(x=500,y=8)
      Button1 = Checkbutton(Customerlabelframe,
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                       
                        width = 10)

      Button1.place(x=550,y=5)

      category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
      category1.place(x=20,y=40)
      n = StringVar()
      country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
       
      country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
      
      country.place(x=120,y=45)
      country.current(0)


      name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
      name1.place(x=20,y=70)
      nameentry = Entry(Customerlabelframe,width=60)
      nameentry.place(x=120,y=75)

      des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
      des1.place(x=20,y=100)
      desentry = Entry(Customerlabelframe,width=60)
      desentry.place(x=120,y=105)

      uval = IntVar(Customerlabelframe, value='$0.00')
      unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      unit1.place(x=20,y=130)
      unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
      unitentry.place(x=120,y=135)

      pcsval = IntVar(Customerlabelframe, value='$0.00')
      pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      pcs1.place(x=320,y=140)
      pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
      pcsentry.place(x=410,y=140)

      costval = IntVar(Customerlabelframe, value='$0.00')
      cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
      cost1.place(x=20,y=160)
      costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
      costentry.place(x=120,y=165)

      priceval = IntVar(Customerlabelframe, value='$0.00')
      price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
      price1.place(x=20,y=190)
      priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
      priceentry.place(x=120,y=195)

      checkvarStatus2=IntVar()
     
      Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                        text="Taxable Tax1rate",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        height=2,
                        width = 12)

      Button2.place(x=415,y=170)


      checkvarStatus3=IntVar()
     
      Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                        text="No stock Control",
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      Button3.place(x=40,y=220)


      stockval = IntVar(Customerlabelframe)
      stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
      stock1.place(x=90,y=260)
      stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
      stockentry.place(x=150,y=265)

      lowval = IntVar(Customerlabelframe)
      low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      low1.place(x=300,y=260)
      lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
      lowentry.place(x=495,y=265)

     
      ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
      ware1.place(x=60,y=290)
      wareentry = Entry(Customerlabelframe,width=50)
      wareentry.place(x=150,y=295)

      text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      text1.place(x=20,y=330)

      txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
      txt.place(x=32,y=358)




      okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
      okButton.pack(side=LEFT)

      cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=60)
      cancelButton.pack(side=RIGHT)

      imageFrame = Frame(tab2, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse')
      browsebutton.place(x=580,y=30,height=30,width=50)
      
      removeButton = Button(imageFrame,compound = LEFT,image=cancel, text ="Remove Product Image",width=150)
      removeButton.place(x=400,y=450)



    
                    
    enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(newselection, width=20).place(x=110, y=10)
    text=Label(newselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(newselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(newselection, height=27)
    cusventtree["columns"]=["1","2","3", "4","5"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=70)
    cusventtree.column("5", width=70)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="ID/SKU")
    cusventtree.heading("2",text="Product/Service Name")
    cusventtree.heading("3",text="Unit price")
    cusventtree.heading("4",text="Service")
    cusventtree.heading("5",text="Stock")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(newselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(newselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )
   

    btn1=Button(newselection,compound = LEFT,image=tick ,text="ok", width=60).place(x=15, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
    btn1=Button(newselection,compound = LEFT,image=cancel ,text="Cancel", width=60).place(x=740, y=610)



  #preview new line
  def previewline():
    messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")


  
  #sms notification
  def sms1():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)
    
    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 



  
  #delete line item  
  def delete1():
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item .")
    
    

  firFrame=Frame(pop, bg="#f5f3f2", height=60)
  firFrame.pack(side="top", fill=X)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  create = Button(firFrame,compound="top", text="Select\nCustomer",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=custom)
  create.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  add= Button(firFrame,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=newline)
  add.pack(side="left", pady=3, ipadx=4)

  dele= Button(firFrame,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=delete1)
  dele.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  prev= Button(firFrame,compound="top", text="Preview\nOrder",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline)
  prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(firFrame,compound="top", text="Print \nOrder",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(firFrame,compound="top", text="Email\nOrder",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
  mail.pack(side="left", pady=3, ipadx=4)

  sms1= Button(firFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=sms1)
  sms1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  calc= Button(firFrame,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  calc.pack(side="left", pady=3, ipadx=4)

  fir1Frame=Frame(pop, height=180,bg="#f5f3f2")
  fir1Frame.pack(side="top", fill=X)

  labelframe1 = LabelFrame(fir1Frame,text="Customers",font=("arial",15))
  labelframe1.place(x=10,y=5,width=640,height=160)
  order = Label(labelframe1, text="Order to").place(x=10,y=5)
  e1 = ttk.Combobox(labelframe1, value="Hello",width=28).place(x=80,y=5)
  address=Label(labelframe1,text="Address").place(x=10,y=30)
  e2=Text(labelframe1,width=23).place(x=80,y=30,height=70)
  ship=Label(labelframe1,text="Ship to").place(x=342,y=5)
  e3=Entry(labelframe1,width=30).place(x=402,y=3)
  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  e4=Text(labelframe1,width=23).place(x=402,y=30,height=70)

  btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
  
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  email=Label(labelframe2,text="Email").place(x=10,y=5)
  e5=Entry(labelframe2,width=30).place(x=80,y=5)
  sms=Label(labelframe2,text="SMS Number").place(x=328,y=5)
  e6=Entry(labelframe2,width=30).place(x=402,y=5)
    
  labelframe = LabelFrame(fir1Frame,text="Order",font=("arial",15))
  labelframe.place(x=652,y=5,width=290,height=170)
  order=Label(labelframe,text="Order#").place(x=5,y=5)
  e1=Entry(labelframe,width=25).place(x=100,y=5,)
  orderdate=Label(labelframe,text="Order date").place(x=5,y=33)
  e2=Entry(labelframe,width=20).place(x=150,y=33)
  checkvarStatus5=IntVar()
  duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
  e3=Entry(labelframe,width=20).place(x=150,y=62)
  terms=Label(labelframe,text="Terms").place(x=5,y=92)
  e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  e1=Entry(labelframe,width=27).place(x=100,y=118)

  fir2Frame=Frame(pop, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
  
  tree=ttk.Treeview(listFrame)
  tree["columns"]=["1","2","3","4","5","6","7","8"]

  tree.column("#0", width=40)
  tree.column("1", width=80)
  tree.column("2", width=190)
  tree.column("3", width=190)
  tree.column("4", width=80)
  tree.column("5", width=60)
  tree.column("6", width=60)
  tree.column("7", width=60)
  tree.column("8", width=80)
  
  tree.heading("#0")
  tree.heading("1",text="ID/SKU")
  tree.heading("2",text="Product/Service")
  tree.heading("3",text="Description")
  tree.heading("4",text="Unit Price")
  tree.heading("5",text="Quality")
  tree.heading("6",text="Pcs/Weight")
  tree.heading("7",text="Tax1")
  tree.heading("8",text="Price")
  
  tree.pack(fill="both", expand=1)
  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

  fir3Frame=Frame(pop,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  orderFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
  
  myNotebook.add(orderFrame,compound="left", text="Order")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both")  

  labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=800,height=170)
  cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  e1=ttk.Combobox(labelframe1, value="",width=20).place(x=115,y=5)
  rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  e2=Entry(labelframe1,width=6).place(x=460,y=5)
  cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  e3=Entry(labelframe1,width=10).place(x=115,y=35)
  tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
  e4=Entry(labelframe1,width=7).place(x=460,y=35)
  template=Label(labelframe1,text="Template").place(x=37,y=70)
  e5=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
  sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  e6=Entry(labelframe1,width=18).place(x=115,y=100)
  category=Label(labelframe1,text="Category").place(x=300,y=100)
  e7=Entry(labelframe1,width=22).place(x=370,y=100)
  
  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
  on1=Label(statusfrme, text="Emailed on:").place( y=50)
  nev1=Label(statusfrme, text="Never").place(x=100,y=50)
  on2=Label(statusfrme, text="Printed on:").place( y=90)
  nev2=Label(statusfrme, text="Never").place(x=100,y=90)

  text1=Label(headerFrame,text="Title text").place(x=50,y=5)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
  text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
  text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

  text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
  e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

  e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

  e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

  btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
  text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  cusventtree=ttk.Treeview(documentFrame, height=5)
  cusventtree["columns"]=["1","2","3"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=250)
  cusventtree.column("2", width=250)
  cusventtree.column("2", width=200)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Attach to Email")
  cusventtree.heading("2",text="Filename")
  cusventtree.heading("3",text="Filesize")  
  cusventtree.place(x=50, y=45)
  

  fir4Frame=Frame(pop,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme.place(x=0,y=0,width=200,height=170)
  discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
  discount1=Label(summaryfrme, text="$0.00").place(x=130 ,y=0)
  sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
  sub1=Label(summaryfrme, text="$0.00").place(x=130 ,y=21)
  tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
  tax1=Label(summaryfrme, text="$0.00").place(x=130 ,y=42)
  cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
  cost=Label(summaryfrme, text="$0.00").place(x=130 ,y=63)
  order=Label(summaryfrme, text="Order total").place(x=0 ,y=84)
  order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)
  total=Label(summaryfrme, text="Total paid").place(x=0 ,y=105)
  total1=Label(summaryfrme, text="$0.00").place(x=130 ,y=105)
  balance=Label(summaryfrme, text="Balance").place(x=0 ,y=126)
  balance1=Label(summaryfrme, text="$0.00").place(x=130 ,y=126)

  fir5Frame=Frame(pop,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
  btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)




#printselected order
  
def printsele():

  def property1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def property2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 15, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy count:").place(x=55, y=95)

      okbtn=Button(propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
      canbtn=Button(propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
      
      


    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=property2).place(x=550, y=380)
    btn=Button(property_Frame,compound = LEFT,image=tick  ,text="OK", width=60,).place(x=430, y=420)
    btn=Button(property_Frame,compound = LEFT,image=cancel , text="Cancel", width=60,).place(x=550, y=420)     


    
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=property1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=370)
      canbtn=Button(print1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=370)
      


#email
      
def email_invoice_recurring():
  mailDetail=Toplevel()
  mailDetail.title("Invoice E-Mail")
  mailDetail.geometry("1080x550")
  mailDetail.resizable(False, False)
  def my_SMTP():
      if True:
          em_ser_conbtn.destroy()
          mysmtpservercon=LabelFrame(account_Frame,text="SMTP server connection(ask your ISP for your SMTP settings)", height=165, width=380)
          mysmtpservercon.place(x=610, y=110)
          lbl_hostn=Label(mysmtpservercon, text="Hostname").place(x=5, y=10)
          hostnent=Entry(mysmtpservercon, width=30).place(x=80, y=10)
          lbl_portn=Label(mysmtpservercon, text="Port").place(x=5, y=35)
          portent=Entry(mysmtpservercon, width=30).place(x=80, y=35)
          lbl_usn=Label(mysmtpservercon, text="Username").place(x=5, y=60)
          unament=Entry(mysmtpservercon, width=30).place(x=80, y=60)
          lbl_pasn=Label(mysmtpservercon, text="Password").place(x=5, y=85)
          pwdent=Entry(mysmtpservercon, width=30).place(x=80, y=85)
          ssl_chkvar=IntVar()
          ssl_chkbtn=Checkbutton(mysmtpservercon, variable=ssl_chkvar, text="This server requires a secure connection(SSL)", onvalue=1, offvalue=0)
          ssl_chkbtn.place(x=50, y=110)
          em_ser_conbtn1=Button(account_Frame, text="Test E-mail Server Connection").place(x=610, y=285)
      else:
          pass
    
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  email_Notebook = ttk.Notebook(mailDetail)
  email_Frame = Frame(email_Notebook, height=500, width=1080)
  account_Frame = Frame(email_Notebook, height=550, width=1080)
  email_Notebook.add(email_Frame, text="E-mail")
  email_Notebook.add(account_Frame, text="Account")
  email_Notebook.place(x=0, y=0)

  messagelbframe=LabelFrame(email_Frame,text="Message", height=500, width=730)
  messagelbframe.place(x=5, y=5)
  lbl_emailtoaddr=Label(messagelbframe, text="Email to address").place(x=5, y=5)
  emailtoent=Entry(messagelbframe, width=50).place(x=120, y=5)
  sendemail_btn=Button(messagelbframe, text="Send Email", width=10, height=1,command=addacnt).place(x=600, y=10)
  lbl_carcopyto=Label(messagelbframe, text="Carbon copy to").place(x=5, y=32)
  carcopyent=Entry(messagelbframe, width=50).place(x=120, y=32)
  stopemail_btn=Button(messagelbframe, text="Stop sending", width=10, height=1).place(x=600, y=40)
  lbl_subject=Label(messagelbframe, text="Subject").place(x=5, y=59)
  subent=Entry(messagelbframe, width=50).place(x=120, y=59)

  
  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
  mess_Notebook = ttk.Notebook(messagelbframe)
  emailmessage_Frame = Frame(mess_Notebook, height=350, width=710)
  htmlsourse_Frame = Frame(mess_Notebook, height=350, width=710)
  mess_Notebook.add(emailmessage_Frame, text="E-mail message")
  mess_Notebook.add(htmlsourse_Frame, text="Html sourse code")
  mess_Notebook.place(x=5, y=90)

  btn1=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  btn5=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=undo).place(x=140, y=1)
  btn6=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=redo).place(x=175, y=1)
  btn7=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=bold).place(x=210, y=1)
  btn8=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=italics).place(x=245, y=1)
  btn9=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=underline).place(x=280, y=1)
  btn10=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=left).place(x=315, y=1)
  btn11=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=right).place(x=350, y=1)
  btn12=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=center).place(x=385, y=1)
  btn13=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=hyperlink).place(x=420, y=1)
  
  btn14=Button(emailmessage_Frame,width=31,height=23,compound = LEFT,image=remove).place(x=455, y=1)


  dropcomp = ttk.Combobox(emailmessage_Frame, width=12, height=3).place(x=500, y=5)
  dropcompo = ttk.Combobox(emailmessage_Frame, width=6, height=3).place(x=600, y=5)
  mframe=Frame(emailmessage_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)



  btn1=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=selectall).place(x=0, y=1)

  
  btn2=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=cut).place(x=36, y=1)
  btn3=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=copy).place(x=73, y=1)
  btn4=Button(htmlsourse_Frame,width=31,height=23,compound = LEFT,image=paste).place(x=105, y=1)
  mframe=Frame(htmlsourse_Frame, height=350, width=710, bg="white")
  mframe.place(x=0, y=28)

  attachlbframe=LabelFrame(email_Frame,text="Attachment(s)", height=350, width=280)
  attachlbframe.place(x=740, y=5)
  htcodeframe=Frame(attachlbframe, height=220, width=265, bg="white").place(x=5, y=5)
  lbl_btn_info=Label(attachlbframe, text="Double click on attachment to view").place(x=30, y=230)
  btn17=Button(attachlbframe, width=20, text="Add attacment file...").place(x=60, y=260)
  btn18=Button(attachlbframe, width=20, text="Remove attacment").place(x=60, y=295)
  lbl_tt_info=Label(email_Frame, text="You can create predefined invoice, order, estimate\nand payment receipt email templates under Main\nmenu/Settings/E-Mail templates tab")
  lbl_tt_info.place(x=740, y=370)

  ready_frame=Frame(mailDetail, height=20, width=1080, bg="#b3b3b3").place(x=0,y=530)
  
  sendatalbframe=LabelFrame(account_Frame,text="E-Mail(Sender data)",height=270, width=600)
  sendatalbframe.place(x=5, y=5)
  lbl_sendermail=Label(sendatalbframe, text="Your company email address").place(x=5, y=30)
  sentent=Entry(sendatalbframe, width=40).place(x=195, y=30)
  lbl_orcompanyname=Label(sendatalbframe, text="Your name or company name").place(x=5, y=60)
  nament=Entry(sendatalbframe, width=40).place(x=195, y=60)
  lbl_reply=Label(sendatalbframe, text="Reply to email address").place(x=5, y=90)
  replyent=Entry(sendatalbframe, width=40).place(x=195, y=90)
  lbl_sign=Label(sendatalbframe, text="Signature").place(x=5, y=120)
  signent=Entry(sendatalbframe,width=50).place(x=100, y=120,height=75)
  confirm_chkvar=IntVar()
  confirm_chkbtn=Checkbutton(sendatalbframe, variable=confirm_chkvar, text="Confirmation reading", onvalue=1, offvalue=0)
  confirm_chkbtn.place(x=200, y=215)
  btn18=Button(account_Frame, width=15, text="Save settings",command=savesettings).place(x=25, y=285)

  sendatalbframe=LabelFrame(account_Frame,text="SMTP Server",height=100, width=380)
  sendatalbframe.place(x=610, y=5)
  servar=IntVar()
  SMTP_rbtn=Radiobutton(sendatalbframe, text="Use the Built-In SMTP Server Settings", variable=servar, value=1)
  SMTP_rbtn.place(x=10, y=10)
  MySMTP_rbtn=Radiobutton(sendatalbframe, text="Use My Own SMTP Server Settings(Recommended)", variable=servar, value=2, command=my_SMTP)
  MySMTP_rbtn.place(x=10, y=40)
  em_ser_conbtn=Button(account_Frame, text="Test E-mail Server Connection")
  em_ser_conbtn.place(x=710, y=110)




#sms notification order
  
def sms():
  send_SMS=Toplevel()
  send_SMS.geometry("700x480+240+150")
  send_SMS.title("Send SMS notification")

  style = ttk.Style()
  style.theme_use('default')
  style.configure('TNotebook.Tab', background="#999999", padding=5)
  sms_Notebook = ttk.Notebook(send_SMS)
  SMS_Notification = Frame(sms_Notebook, height=470, width=700)
  SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
  sms_Notebook.add(SMS_Notification, text="SMS Notification")
  sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
  sms_Notebook.place(x=0, y=0)

  numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
  numlbel.place(x=10, y=10)
  numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
  stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
  stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
  
  dclbel=Label(SMS_Notification, text="Double click to insert into text")
  dclbel.place(x=410, y=60)
  dcl=Entry(SMS_Notification, width=30)
  dcl.place(x=400, y=85,height=200)
  
  smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
  smstype.place(x=10, y=223)
  snuvar=IntVar()
  normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
  unicode_rbtn.place(x=190, y=5)
  tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
  tiplbf.place(x=10, y=290)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
  tiplabl.place(x=5, y=5)

  btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
  btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
  btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
  

  smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
  smstype.place(x=10, y=5)
  snumvar=IntVar()
  normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
  normal_rbtn.place(x=5, y=5)
  unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
  unicode_rbtn.place(x=290, y=5)

  sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
  sms1type.place(x=10, y=80)
  name=Label(sms1type, text="Username").place(x=10, y=5)
  na=Entry(sms1type, width=20).place(x=100, y=5)
  password=Label(sms1type, text="Password").place(x=10, y=45)
  pas=Entry(sms1type, width=20).place(x=100, y=45)
  combo=Label(sms1type, text="Route").place(x=400, y=5)
  n = StringVar()
  combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
  btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

  
  tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
  tiplbf.place(x=10, y=190)
  tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
  tiplabl.place(x=0, y=5)
  tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
  tiplabl1.place(x=0, y=60)
  tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
  tiplabl2.place(x=0, y=100)
  tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
  tiplabl3.place(x=0, y=140)
  checkvar1=IntVar()
  chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200)  



#print preview order
def printpreview():
  messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")



#convert to invoice
def convert():
  if messagebox.askyesno("Make invoice from Orders", "Are you sure to make invoice from this Orders ") == True:
        messagebox.askyesno("Make invoice from Estimate", "Invoice Creation was Successfull.\n New Invoice is \n Would you like to open this invoice ")
  else:
      messagebox.destroy()
  

#delete orders  
def dele():  
  messagebox.askyesno("Delete order", "Are you sure to delete this order? All products will be placed back into stock")




#search in orders  
def search():  
    top = Toplevel()     
    top.title("Find Text")   
    top.geometry("600x250+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
    n = StringVar()
    findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
    findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
    n = StringVar()
    findIN = ttk.Combobox(top, width = 30, textvariable = n )
    findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
    findIN.place(x=90,y=54)
    findIN.current(0)

    findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
    closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
    match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
    n = StringVar()
    match = ttk.Combobox(top, width = 23, textvariable = n )   
    match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
    match.place(x=90,y=83)
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
    n = StringVar()
    search = ttk.Combobox(top, width = 23, textvariable = n )
    search['values'] = ('All', 'up',' Down')
    search.place(x=90,y=112)
    search.current(0)
    checkvarStatus4=IntVar()  
    Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button4.place(x=90,y=141)
    checkvarStatus5=IntVar()   
    Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button5.place(x=300,y=141)





mainFrame=Frame(tab2, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

invoiceLabel = Button(midFrame,compound="top", text="Create new\nOrder",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=create)
invoiceLabel.pack(side="left", pady=3, ipadx=4)

orderLabel = Button(midFrame,compound="top", text="View/Edit\nOrders",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=create)
orderLabel.pack(side="left")

estimateLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=dele)
estimateLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

recurLabel = Button(midFrame,compound="top", text="Convert to\nInvoice",relief=RAISED, image=photo3,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=convert)
recurLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

previewLabel = Button(midFrame,compound="top", text="Print\nPreview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red",command=printpreview)
previewLabel.pack(side="left")

purchaseLabel = Button(midFrame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=printsele)
purchaseLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

expenseLabel = Button(midFrame,compound="top", text=" E-mail \nOrder",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
expenseLabel.pack(side="left")

smsLabel = Button(midFrame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=sms)
smsLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Search\nOrders",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=search)
productLabel.pack(side="left")

lbframe = LabelFrame(midFrame, height=60, width=200, bg="#f8f8f2")
lbframe.pack(side="left", padx=10, pady=0)
lbl_invdt = Label(lbframe, text="Order date from : ", bg="#f8f8f2")
lbl_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
lbl_invdtt = Label(lbframe, text="Order date to  :  ", bg="#f8f8f2")
lbl_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))
invdt = Entry(lbframe, width=15)
invdt.grid(row=0, column=1)
invdtt = Entry(lbframe, width=15)
invdtt.grid(row=1, column=1)
checkvar1 = IntVar()
chkbtn1 = Checkbutton(lbframe, text = "Apply filter", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
chkbtn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

productLabel = Button(midFrame,compound="top", text="Refresh\nOrders list",relief=RAISED, image=photo8,fg="black", height=55, bd=1, width=55)
productLabel.pack(side="left")

w = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

productLabel = Button(midFrame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
productLabel.pack(side="left")

invoilabel = Label(mainFrame, text="Orders(All)", font=("arial", 18), bg="#f8f8f2")
invoilabel.pack(side="left", padx=(20,0))
drop = ttk.Combobox(mainFrame, value="Hello")
drop.pack(side="right", padx=(0,10))
invoilabel = Label(mainFrame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
invoilabel.pack(side="right", padx=(0,10))

class MyApp:
  def __init__(self, parent):
    
    self.myParent = parent 

    self.myContainer1 = Frame(parent) 
    self.myContainer1.pack()
    
    self.top_frame = Frame(self.myContainer1) 
    self.top_frame.pack(side=TOP,
      fill=BOTH, 
      expand=YES,
      )  

    self.left_frame = Frame(self.top_frame, background="white",
      borderwidth=5,  relief=RIDGE,
      height=250, 
      width=2000, 
      )
    self.left_frame.pack(side=LEFT,
      fill=BOTH, 
      expand=YES,
      )

    
    tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Order#")
    tree.heading(3, text="Order date")
    tree.heading(4, text="Due date")
    tree.heading(5, text="Customer Name")
    tree.heading(6, text="Status")
    tree.heading(7, text="Emailed on")
    tree.heading(8, text="Printed on")
    tree.heading(9, text="SMS on")
    tree.heading(10, text="Order Total")   
    tree.column(1, width = 50)
    tree.column(2, width = 140)
    tree.column(3, width = 140)
    tree.column(4, width = 140)
    tree.column(5, width = 210)
    tree.column(6, width = 130)
    tree.column(7, width = 150)
    tree.column(8, width = 130)
    tree.column(9, width = 130)
    tree.column(10, width = 130)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=990+300+50, y=0, height=300+20)
    scrollbar.config( command=tree.yview )

    tabControl = ttk.Notebook(self.left_frame,width=1)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 =  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tabControl.add(tab1,image=invoices,compound = LEFT, text ='Order Items',)
    tabControl.add(tab2,image=orders,compound = LEFT, text ='Private Notes')
    tabControl.add(tab3,image=estimates,compound = LEFT, text ='SMS Log')
    tabControl.add(tab4,image=estimates,compound = LEFT, text ='Documents')
    tabControl.pack(expand = 1, fill ="both")
    
    tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Product/Service ID",)
    tree.heading(3, text="Name")
    tree.heading(4, text="Description")
    tree.heading(5, text="Price")
    tree.heading(6, text="QTY")
    tree.heading(7, text="Tax1")
    tree.heading(8, text="Line Total")   
    tree.column(1, width = 50)
    tree.column(2, width = 270) 
    tree.column(3, width = 270)
    tree.column(4, width = 300)
    tree.column(5, width = 130)
    tree.column(6, width = 100)
    tree.column(7, width = 100)
    tree.column(8, width = 150)

    note1=Text(tab2, width=220,height=10).place(x=10, y=10)

    note1=Text(tab3, width=2200,height=10).place(x=10, y=10)

    tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Attach to Email",)
    tree.heading(3, text="Filename")
    tree.column(1, width = 50)
    tree.column(2, width = 290)
    tree.column(3, width = 1000)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=990+300+50, y=360, height=190)
    scrollbar.config( command=tree.yview )
       
myapp = MyApp(tab2)


#######TAB-5#### KRISHNA


#PURCHASE ORDERS MODULE



#create new purchase order
def createpur():
  pop1=Toplevel(midFrame)
  pop1.title("Orders")
  pop1.geometry("950x690+150+0")


  #select vendor
  def purchase():
    cuselection=Toplevel()
    cuselection.title("Select Customer")
    cuselection.geometry("930x650+240+10")
    cuselection.resizable(False, False)


    #add new customer
    def addedit():
      ven=Toplevel(midFrame)
      ven.title("Add new vendor")
      ven.geometry("930x650+240+10")
      checkvar1=IntVar()
      checkvar2=IntVar()
      radio=IntVar()
      createFrame=Frame(ven, bg="#f5f3f2", height=650)
      createFrame.pack(side="top", fill="both")
      labelframe1 = LabelFrame(createFrame,text="Customer",bg="#f5f3f2",font=("arial",15))
      labelframe1.place(x=10,y=5,width=910,height=600)
      text1=Label(labelframe1, text="Customer ID:",bg="#f5f3f2",fg="blue").place(x=5 ,y=10)
      e1=Entry(labelframe1,width=25).place(x=150,y=10)
      text2=Label(labelframe1, text="Category:",bg="#f5f3f2").place(x=390 ,y=10)
      e2=ttk.Combobox(labelframe1,width=25,value="Default").place(x=460 ,y=10)
      text3=Label(labelframe1, text="Status:",bg="#f5f3f2").place(x=710 ,y=10)
      Checkbutton(labelframe1,text="Active",variable=checkvar1,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=760 ,y=10)
      labelframe2 = LabelFrame(labelframe1,text="Invoice to (appears on invoices)",bg="#f5f3f2")
      labelframe2.place(x=5,y=40,width=420,height=150)
      name = Label(labelframe2, text="Ship to name:",bg="#f5f3f2",fg="blue").place(x=5,y=5)
      e1 = Entry(labelframe2,width=28).place(x=130,y=5)
      addr = Label(labelframe2, text="Address:",bg="#f5f3f2",fg="blue").place(x=5,y=40)
      e2 = Entry(labelframe2,width=28).place(x=130,y=40,height=80)

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=90)

      labelframe3 = LabelFrame(labelframe1,text="Ship to (appears on invoices)",bg="#f5f3f2")
      labelframe3.place(x=480,y=40,width=420,height=150)
      name = Label(labelframe3, text="Business name:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe3,width=28).place(x=130,y=5)
      addr = Label(labelframe3, text="Address:",bg="#f5f3f2").place(x=5,y=40)
      e2 = Entry(labelframe3,width=28).place(x=130,y=40,height=80)
      
      labelframe4 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe4.place(x=5,y=195,width=420,height=150)
      name = Label(labelframe4, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe4,width=28).place(x=130,y=5)
      email = Label(labelframe4, text="E-mail address:",bg="#f5f3f2",fg="blue").place(x=5,y=35)
      e2 = Entry(labelframe4,width=28).place(x=130,y=35)
      tel = Label(labelframe4, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe4,width=11).place(x=130,y=65)
      fax = Label(labelframe4, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe4,width=11).place(x=280,y=65)
      sms = Label(labelframe4, text="Mobile number for SMS notifications:",bg="#f5f3f2").place(x=5,y=95)
      e5 = Entry(labelframe4,width=15).place(x=248,y=95)      

      btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=440, y=250)

      labelframe5 = LabelFrame(labelframe1,text="Ship to contact",bg="#f5f3f2")
      labelframe5.place(x=480,y=195,width=420,height=125)
      name = Label(labelframe5, text="Contact person:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe5,width=28).place(x=130,y=5)
      email = Label(labelframe5, text="E-mail address:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe5,width=28).place(x=130,y=35)
      tel = Label(labelframe5, text="Tel.number:",bg="#f5f3f2").place(x=5,y=65)
      e3 = Entry(labelframe5,width=11).place(x=130,y=65)
      fax = Label(labelframe5, text="Fax:",bg="#f5f3f2").place(x=240,y=65)
      e4 = Entry(labelframe5,width=11).place(x=280,y=65)

      labelframe6 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2")
      labelframe6.place(x=5,y=350,width=420,height=100)
      Checkbutton(labelframe6,text="Tax Exempt",variable=checkvar2,onvalue=1,offvalue=0,bg="#f5f3f2").place(x=5 ,y=5)
      tax = Label(labelframe6, text="Specific Tax1 %:",bg="#f5f3f2").place(x=180,y=5)
      e1 = Entry(labelframe6,width=10).place(x=290,y=5)
      discount = Label(labelframe6, text="Discount%:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe6,width=10).place(x=100,y=35)

      labelframe7 = LabelFrame(labelframe1,text="Contact",bg="#f5f3f2",)
      labelframe7.place(x=480,y=330,width=420,height=100)
      country = Label(labelframe7, text="country:",bg="#f5f3f2").place(x=5,y=5)
      e1 = Entry(labelframe7,width=28).place(x=130,y=5)
      city = Label(labelframe7, text="City:",bg="#f5f3f2").place(x=5,y=35)
      e2 = Entry(labelframe7,width=28).place(x=130,y=35)

      labelframe8 = LabelFrame(labelframe1,text="Customer Type",bg="#f5f3f2")
      labelframe8.place(x=5,y=460,width=420,height=100)
      R1=Radiobutton(labelframe8,text=" Client ",variable=radio,value=1,bg="#f5f3f2").place(x=5,y=15)
      R2=Radiobutton(labelframe8,text=" Vendor ",variable=radio,value=2,bg="#f5f3f2").place(x=150,y=15)
      R3=Radiobutton(labelframe8,text=" Both(client/vendor)",variable=radio,value=3,bg="#f5f3f2").place(x=250,y=15)
      

      labelframe9 = LabelFrame(labelframe1,text="Notes",bg="#f5f3f2")
      labelframe9.place(x=480,y=430,width=420,height=150)
      e1 = Entry(labelframe9).place(x=10,y=10,height=100,width=390)

      btn1=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=tick,text="OK").place(x=20, y=615)
      btn2=Button(ven,width=60,height=10,bg="#f5f3f2",compound = LEFT,image=cancel,text="Cancel").place(x=800, y=615)
        
               

    enter=Label(cuselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(cuselection, width=20).place(x=110, y=10)
    text=Label(cuselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(cuselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(cuselection, height=27)
    cusventtree["columns"]=["1","2","3", "4"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=140)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="Customer/Ventor ID")
    cusventtree.heading("2",text="Customer/Ventor Name")
    cusventtree.heading("3",text="Tel.")
    cusventtree.heading("4",text="Contact Person")
    cusventtree.place(x=5, y=45)

    ctegorytree=ttk.Treeview(cuselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(cuselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )

    btn1=Button(cuselection,compound = LEFT,image=tick, text="ok", width=60).place(x=15, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick, text="Edit selected customer", width=150,command=addedit).place(x=250, y=610)
    btn1=Button(cuselection,compound = LEFT,image=tick,text="Add new customer", width=150,command=addedit).place(x=435, y=610)
    btn1=Button(cuselection,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=740, y=610)   



  #add new line item
  def newlineproduct():
    newselection=Toplevel()
    newselection.title("Select Customer")
    newselection.geometry("930x650+240+10")
    newselection.resizable(False, False)

    def product():  
      top = Toplevel()  
      top.title("Add a new Product/Service")
      p2 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p2)
    
      top.geometry("700x550+390+15")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999",padding=10,bd=0)


      tab1 = ttk.Frame(tabControl)
      tab2 = ttk.Frame(tabControl)
     
      tabControl.add(tab1,compound = LEFT, text ='Product/Service')
      tabControl.add(tab2,compound = LEFT, text ='Product Image')
     
      tabControl.pack(expand = 1, fill ="both")

      innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      Customerlabelframe.pack(side="top",fill=BOTH,padx=10)

      code1=Label(Customerlabelframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      code1.place(x=20,y=0)
      codeentry = Entry(Customerlabelframe,width=35)
      codeentry.place(x=120,y=8)

      checkvarStatus=IntVar()
      status1=Label(Customerlabelframe,text="Status:")
      status1.place(x=500,y=8)
      Button1 = Checkbutton(Customerlabelframe,
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                       
                        width = 10)

      Button1.place(x=550,y=5)

      category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
      category1.place(x=20,y=40)
      n = StringVar()
      country = ttk.Combobox(Customerlabelframe, width = 40, textvariable = n )
       
      country['values'] = ('Default',' India',' China',' Australia',' Nigeria',' Malaysia',' Italy',' Turkey',)
      
      country.place(x=120,y=45)
      country.current(0)


      name1=Label(Customerlabelframe,text="Name :",fg="blue",pady=5,padx=10)
      name1.place(x=20,y=70)
      nameentry = Entry(Customerlabelframe,width=60)
      nameentry.place(x=120,y=75)

      des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
      des1.place(x=20,y=100)
      desentry = Entry(Customerlabelframe,width=60)
      desentry.place(x=120,y=105)

      uval = IntVar(Customerlabelframe, value='$0.00')
      unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      unit1.place(x=20,y=130)
      unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
      unitentry.place(x=120,y=135)

      pcsval = IntVar(Customerlabelframe, value='$0.00')
      pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      pcs1.place(x=320,y=140)
      pcsentry = Entry(Customerlabelframe,width=20,textvariable=pcsval)
      pcsentry.place(x=410,y=140)

      costval = IntVar(Customerlabelframe, value='$0.00')
      cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
      cost1.place(x=20,y=160)
      costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
      costentry.place(x=120,y=165)

      priceval = IntVar(Customerlabelframe, value='$0.00')
      price1=Label(Customerlabelframe,text="(Price Cost):",pady=5,padx=10)
      price1.place(x=20,y=190)
      priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
      priceentry.place(x=120,y=195)

      checkvarStatus2=IntVar()
     
      Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2,
                        text="Taxable Tax1rate",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        height=2,
                        width = 12)

      Button2.place(x=415,y=170)

      checkvarStatus3=IntVar()
     
      Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3,
                        text="No stock Control",
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      Button3.place(x=40,y=220)


      stockval = IntVar(Customerlabelframe)
      stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
      stock1.place(x=90,y=260)
      stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
      stockentry.place(x=150,y=265)

      lowval = IntVar(Customerlabelframe)
      low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      low1.place(x=300,y=260)
      lowentry = Entry(Customerlabelframe,width=10,textvariable=lowval)
      lowentry.place(x=495,y=265)

     
      ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
      ware1.place(x=60,y=290)
      wareentry = Entry(Customerlabelframe,width=50)
      wareentry.place(x=150,y=295)

      text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      text1.place(x=20,y=330)

      note1=Text(Customerlabelframe, width=90,height=6).place(x=20, y=360)


      okButton = Button(innerFrame,compound = LEFT,image=tick , text ="Ok",width=60)
      okButton.pack(side=LEFT)

      cancelButton = Button(innerFrame,compound = LEFT,image=cancel ,text="Cancel",width=50)
      cancelButton.pack(side=RIGHT)

      imageFrame = Frame(tab2, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse')
      browsebutton.place(x=580,y=30,height=30,width=50)
      
      removeButton = Button(imageFrame,compound = LEFT,image=cancel , text ="Remove Product Image",width=150)
      removeButton.place(x=400,y=450)

                   
    enter=Label(newselection, text="Enter filter text").place(x=5, y=10)
    e1=Entry(newselection, width=20).place(x=110, y=10)
    text=Label(newselection, text="Filtered column").place(x=340, y=10)
    e2=Entry(newselection, width=20).place(x=450, y=10)

    cusventtree=ttk.Treeview(newselection, height=27)
    cusventtree["columns"]=["1","2","3", "4","5"]
    cusventtree.column("#0", width=35)
    cusventtree.column("1", width=160)
    cusventtree.column("2", width=160)
    cusventtree.column("3", width=140)
    cusventtree.column("4", width=70)
    cusventtree.column("5", width=70)
    cusventtree.heading("#0",text="")
    cusventtree.heading("1",text="ID/SKU")
    cusventtree.heading("2",text="Product/Service Name")
    cusventtree.heading("3",text="Unit price")
    cusventtree.heading("4",text="Service")
    cusventtree.heading("5",text="Stock")
    cusventtree.place(x=5, y=45)


    ctegorytree=ttk.Treeview(newselection, height=27)
    ctegorytree["columns"]=["1"]
    ctegorytree.column("#0", width=35, minwidth=20)
    ctegorytree.column("1", width=205, minwidth=25, anchor=CENTER)    
    ctegorytree.heading("#0",text="", anchor=W)
    ctegorytree.heading("1",text="View filter by category", anchor=CENTER)
    ctegorytree.place(x=660, y=45)

    scrollbar = Scrollbar(newselection)
    scrollbar.place(x=640, y=45, height=560)
    scrollbar.config( command=tree.yview )

    btn1=Button(newselection,compound = LEFT,image=tick , text="ok", width=60).place(x=15, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Edit product/Service", width=150,command=product).place(x=250, y=610)
    btn1=Button(newselection,compound = LEFT,image=tick , text="Add product/Service", width=150,command=product).place(x=435, y=610)
    btn1=Button(newselection,compound = LEFT,image=cancel , text="Cancel", width=60).place(x=740, y=610)




  #preview new line
  def previewline1():
    messagebox.showerror("F-Billing Revolution","line is required,please select customer for this order before printing.")



  #sms notification
  def smspurch():
    send_SMS=Toplevel()
    send_SMS.geometry("700x480+240+150")
    send_SMS.title("Send SMS notification")

    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", padding=5)
    sms_Notebook = ttk.Notebook(send_SMS)
    SMS_Notification = Frame(sms_Notebook, height=470, width=700)
    SMS_Service_Account = Frame(sms_Notebook, height=470, width=700)
    sms_Notebook.add(SMS_Notification, text="SMS Notification")
    sms_Notebook.add(SMS_Service_Account, text="SMS Service Account")
    sms_Notebook.place(x=0, y=0)

    numlbel=Label(SMS_Notification, text="SMS number or comma seperated SMS number list(Please start each SMS number with the country code)")
    numlbel.place(x=10, y=10)
    numentry=Entry(SMS_Notification, width=92).place(x=10, y=30)
    stexbel=Label(SMS_Notification, text="SMS Text").place(x=10, y=60)
    stex=Entry(SMS_Notification, width=40).place(x=10, y=85,height=120)
    
    dclbel=Label(SMS_Notification, text="Double click to insert into text")
    dclbel.place(x=410, y=60)
    dcl=Entry(SMS_Notification, width=30)
    dcl.place(x=400, y=85,height=200)

    smstype=LabelFrame(SMS_Notification, text="SMS message type", width=377, height=60)
    smstype.place(x=10, y=223)
    snuvar=IntVar()
    normal_rbtn=Radiobutton(smstype, text="Normal SMS(160 chars)", variable=snuvar, value=1)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)", variable=snuvar, value=2)
    unicode_rbtn.place(x=190, y=5)
    tiplbf=LabelFrame(SMS_Notification, text="Tips", width=680, height=120)
    tiplbf.place(x=10, y=290)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="Always start the SMS nymber with the country code. Do not use the + sign at the beginning(example\nUS number:8455807546). Do not use any special characters in your normal SMS text. Please use the\nstndard SMS characters or the English alphabet and numbers only. Otherwise the SMS will be\nunreadable or undeliverable. If you need to enter international characters, accents,email address, or\nspecial characters to the SMS text field then choose the Unicode SMS format.")
    tiplabl.place(x=5, y=5)

    btn1=Button(SMS_Notification, width=20, text="Send SMS notification").place(x=10, y=420)
    btn2=Button(SMS_Notification, width=25, text="Confirm SMS cost before sending").place(x=280, y=420)
    btn3=Button(SMS_Notification, width=15, text="Cancel").place(x=550, y=420)
    

    smstype=LabelFrame(SMS_Service_Account, text="Select the notification service provider", width=670, height=65)
    smstype.place(x=10, y=5)
    snumvar=IntVar()
    normal_rbtn=Radiobutton(smstype,text="BULKSMS(www.bulksms.com)",variable=snumvar,value=1,)
    normal_rbtn.place(x=5, y=5)
    unicode_rbtn=Radiobutton(smstype, text="Unicode SMS(70 chars)-Recommended", variable=snumvar, value=2)
    unicode_rbtn.place(x=290, y=5)

    sms1type=LabelFrame(SMS_Service_Account, text="Your BULKSMS.COM Account", width=670, height=100)
    sms1type.place(x=10, y=80)
    name=Label(sms1type, text="Username").place(x=10, y=5)
    na=Entry(sms1type, width=20).place(x=100, y=5)
    password=Label(sms1type, text="Password").place(x=10, y=45)
    pas=Entry(sms1type, width=20).place(x=100, y=45)
    combo=Label(sms1type, text="Route").place(x=400, y=5)
    n = StringVar()
    combo1 = ttk.Combobox(sms1type, width = 20, textvariable = n ).place(x=450,y=5)
    btn1=Button(sms1type, width=10, text="Save settings").place(x=550, y=45)

    
    tiplbf=LabelFrame(SMS_Service_Account, text="Terms of service", width=680, height=250)
    tiplbf.place(x=10, y=190)
    tiplabl=Label(tiplbf,justify=LEFT,fg="red",  text="The SMS notification service is not free.This service costs you creadit.You must have your own account\nat BULKSMS.COM and you need to have sufficient creadit and an active internet connection to use\nthis feature.Please review all fields in this form for accuracy")
    tiplabl.place(x=0, y=5)
    tiplabl1=Label(tiplbf,justify=LEFT,fg="black",  text="visit www.bulksms.com website to create your own account.please make sure the BULKSMS .COM\n service works well in your country before you busy creadit")
    tiplabl1.place(x=0, y=60)
    tiplabl2=Label(tiplbf,justify=LEFT,fg="black",  text="Our SMS notification tool comes without any warranty.our software only forwards your SMS message\nthe BULKSMS API server .The BULKSMS API server will try to sent SMS message your recipient")
    tiplabl2.place(x=0, y=100)
    tiplabl3=Label(tiplbf,justify=LEFT,fg="red",  text="Please note that you access and use the SMS notification tool your own risk.F-Billing software is not\nresponsible for any type of loss or damage or undelivered SMS massage which you may as a result\nof accessing and using the SMS notification service.")
    tiplabl3.place(x=0, y=140)
    checkvar1=IntVar()
    chkbtn1=Checkbutton(tiplbf,text="I have read and agree to the terms of service above",variable=checkvar1,onvalue=1,offvalue=0).place(x=70, y=200) 
 

  #delete line item 
  def deletepurch():
    messagebox.showerror("F-Billing Revolution","Customer is required,please select customer before deleting line item.")



  #finalize
  def finalize():  
    messagebox.askyesno("Finalize purchase order", "Would you like to mark this purchase order as completed ?All product will be added in to stock and purchase order will be closed")


  firFrame1=Frame(pop1, bg="#f5f3f2", height=60)
  firFrame1.pack(side="top", fill=X)

  w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  create = Button(firFrame1,compound="top", text="Select\nVendor",relief=RAISED, image=customer,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=purchase)
  create.pack(side="left", pady=3, ipadx=4)


  w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  add= Button(firFrame1,compound="top", text="Add new\nline item",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=newlineproduct)
  add.pack(side="left", pady=3, ipadx=4)

  dele= Button(firFrame1,compound="top", text="Delete line\nitem",relief=RAISED, image=photo2,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=deletepurch)
  dele.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  prev= Button(firFrame1,compound="top", text="Preview\nP.Order",relief=RAISED, image=photo4,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=previewline1)
  prev.pack(side="left", pady=3, ipadx=4)

  prin= Button(firFrame1,compound="top", text="Print \nP.Order",relief=RAISED, image=photo5,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=printsele1)
  prin.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  mail= Button(firFrame1,compound="top", text="Email\nP.Order",relief=RAISED, image=photo6,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
  mail.pack(side="left", pady=3, ipadx=4)

  sms1= Button(firFrame1,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=smspurch)
  sms1.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)

  finalize= Button(firFrame1,compound="top", text="Finalize\nP.Order",relief=RAISED, image=photo10,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=finalize)
  finalize.pack(side="left", pady=3, ipadx=4)

  w = Canvas(firFrame1, width=1, height=65, bg="#b3b3b3", bd=0)
  w.pack(side="left", padx=5)


  calc= Button(firFrame1,compound="top", text="Open\nCalculator",relief=RAISED, image=photo9,bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
  calc.pack(side="left", pady=3, ipadx=4)

  fir1Frame=Frame(pop1, height=180,bg="#f5f3f2")
  fir1Frame.pack(side="top", fill=X)

  labelframe1 = LabelFrame(fir1Frame,text=" Vendor")
  labelframe1.place(x=10,y=5,width=640,height=160)
  order = Label(labelframe1, text="Vendor to").place(x=10,y=5)
  e1 = ttk.Combobox(labelframe1, value="Hello",width=28).place(x=80,y=5)
  address=Label(labelframe1,text="Address").place(x=10,y=30)
  e2=Text(labelframe1,width=23).place(x=80,y=30,height=70)
  ship=Label(labelframe1,text="Delivery to").place(x=342,y=5)
  e3=Entry(labelframe1,width=30).place(x=402,y=3)
  address1=Label(labelframe1,text="Address").place(x=340,y=30)
  e4=Text(labelframe1,width=23).place(x=402,y=30,height=70)

  btn1=Button(labelframe1,width=3,height=2,compound = LEFT,text=">>").place(x=280, y=50)
  
  labelframe2 = LabelFrame(fir1Frame,text="")
  labelframe2.place(x=10,y=130,width=640,height=42)
  email=Label(labelframe2,text="Email").place(x=10,y=5)
  e5=Entry(labelframe2,width=30).place(x=80,y=5)
  sms=Label(labelframe2,text="SMS Number").place(x=327,y=5)
  e6=Entry(labelframe2,width=28).place(x=402,y=3)

  labelframe = LabelFrame(fir1Frame,text="Purchase Order")
  labelframe.place(x=652,y=5,width=290,height=170)
  order=Label(labelframe,text="P.Order#").place(x=5,y=5)
  e1=Entry(labelframe,width=27).place(x=100,y=5,)
  orderdate=Label(labelframe,text="P.Order date").place(x=5,y=33)
  e2=Entry(labelframe,width=20).place(x=150,y=33)
  checkvarStatus5=IntVar()
  duedate=Checkbutton(labelframe,variable = checkvarStatus5,text="P.Due date",onvalue =0 ,offvalue = 1).place(x=5,y=62)
  e3=Entry(labelframe,width=20).place(x=150,y=62)
  terms=Label(labelframe,text="Terms").place(x=5,y=92)
  e4=ttk.Combobox(labelframe, value="",width=25).place(x=100,y=92)
  ref=Label(labelframe,text="Order ref#").place(x=5,y=118)
  e1=Entry(labelframe,width=27).place(x=100,y=118)

  fir2Frame=Frame(pop1, height=150,width=100,bg="#f5f3f2")
  fir2Frame.pack(side="top", fill=X)
  listFrame = Frame(fir2Frame, bg="white", height=140,borderwidth=5,  relief=RIDGE)
  
  tree=ttk.Treeview(listFrame)
  tree["columns"]=["1","2","3","4","5","6","7","8"]

  tree.column("#0", width=40)
  tree.column("1", width=80)
  tree.column("2", width=190)
  tree.column("3", width=190)
  tree.column("4", width=80)
  tree.column("5", width=60)
  tree.column("6", width=60)
  tree.column("7", width=60)
  tree.column("8", width=80)
  
  tree.heading("#0")
  tree.heading("1",text="ID/SKU")
  tree.heading("2",text="Product/Service")
  tree.heading("3",text="Description")
  tree.heading("4",text="Unit Price")
  tree.heading("5",text="Quality")
  tree.heading("6",text="Pcs/Weight")
  tree.heading("7",text="Tax1")
  tree.heading("8",text="Price")
  
  tree.pack(fill="both", expand=1)
  listFrame.pack(side="top", fill="both", padx=5, pady=3, expand=1)

  fir3Frame=Frame(pop1,height=200,width=700,bg="#f5f3f2")
  fir3Frame.place(x=0,y=490)

  tabStyle = ttk.Style()
  tabStyle.theme_use('default')
  tabStyle.configure('TNotebook.Tab', background="#999999", width=12, padding=5)
  myNotebook=ttk.Notebook(fir3Frame)
  orderFrame = Frame(myNotebook, height=200, width=800)
  headerFrame = Frame(myNotebook, height=200, width=800)
  commentFrame = Frame(myNotebook, height=200, width=800)
  termsFrame = Frame(myNotebook, height=200, width=800)
  noteFrame = Frame(myNotebook, height=200, width=800)
  documentFrame = Frame(myNotebook, height=200, width=800)
  
  myNotebook.add(orderFrame,compound="left", text="Purchase Order")
  myNotebook.add(headerFrame,compound="left",  text="Header/Footer")
  myNotebook.add(commentFrame,compound="left",  text="Comments")
  myNotebook.add(termsFrame,compound="left", text="Terms")
  myNotebook.add(noteFrame,compound="left",  text="Private notes")
  myNotebook.add(documentFrame,compound="left",  text="Documents")
  myNotebook.pack(expand = 1, fill ="both")

  labelframe1 = LabelFrame(orderFrame,text="",font=("arial",15))
  labelframe1.place(x=1,y=1,width=800,height=170)
  cost1=Label(labelframe1,text="Extra cost name").place(x=2,y=5)
  e1=ttk.Combobox(labelframe1, value="",width=20).place(x=115,y=5)
  rate=Label(labelframe1,text="Discount rate").place(x=370,y=5)
  e2=Entry(labelframe1,width=6).place(x=460,y=5)
  cost2=Label(labelframe1,text="Extra cost").place(x=35,y=35)
  e3=Entry(labelframe1,width=10).place(x=115,y=35)
  tax=Label(labelframe1,text="Tax1").place(x=420,y=35)
  e4=Entry(labelframe1,width=7).place(x=460,y=35)
  template=Label(labelframe1,text="Template").place(x=37,y=70)
  e5=ttk.Combobox(labelframe1, value="",width=25).place(x=115,y=70)
  sales=Label(labelframe1,text="Sales Person").place(x=25,y=100)
  e6=Entry(labelframe1,width=18).place(x=115,y=100)
  category=Label(labelframe1,text="Category").place(x=300,y=100)
  e7=Entry(labelframe1,width=22).place(x=370,y=100)

  statusfrme = LabelFrame(labelframe1,text="Status",font=("arial",15))
  statusfrme.place(x=540,y=0,width=160,height=160)
  draft=Label(statusfrme, text="Draft",font=("arial", 15, "bold"), fg="grey").place(x=50, y=3)
  on1=Label(statusfrme, text="Emailed on:").place( y=50)
  nev1=Label(statusfrme, text="Never").place(x=100,y=50)
  on2=Label(statusfrme, text="Printed on:").place( y=90)
  nev2=Label(statusfrme, text="Never").place(x=100,y=90)

  text1=Label(headerFrame,text="Title text").place(x=50,y=5)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=5)
  text2=Label(headerFrame,text="Page header text").place(x=2,y=45)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=45)
  text3=Label(headerFrame,text="Footer text").place(x=35,y=85)
  e1=ttk.Combobox(headerFrame, value="",width=60).place(x=125,y=85)

  text=Label(noteFrame,text="Private notes(not shown on invoice/order/estemates)").place(x=10,y=10)
  e1=Text(noteFrame,width=100,height=7).place(x=10,y=32)

  e1=Text(termsFrame,width=100,height=9).place(x=10,y=10)

  e1=Text(commentFrame,width=100,height=9).place(x=10,y=10)

  btn1=Button(documentFrame,height=2,width=3,text="+").place(x=5,y=10)
  btn2=Button(documentFrame,height=2,width=3,text="-").place(x=5,y=50)
  text=Label(documentFrame,text="Attached documents or image files.If you attach large email then email taken long time to send").place(x=50,y=10)
  cusventtree=ttk.Treeview(documentFrame, height=5)
  cusventtree["columns"]=["1","2","3"]
  cusventtree.column("#0", width=20)
  cusventtree.column("1", width=250)
  cusventtree.column("2", width=250)
  cusventtree.column("2", width=200)
  cusventtree.heading("#0",text="", anchor=W)
  cusventtree.heading("1",text="Attach to Email")
  cusventtree.heading("2",text="Filename")
  cusventtree.heading("3",text="Filesize")  
  cusventtree.place(x=50, y=45)

  fir4Frame=Frame(pop1,height=190,width=210,bg="#f5f3f2")
  fir4Frame.place(x=740,y=520)
  summaryfrme = LabelFrame(fir4Frame,text="Summary",font=("arial",15))
  summaryfrme.place(x=0,y=0,width=200,height=170)
  discount=Label(summaryfrme, text="Discount").place(x=0 ,y=0)
  discount1=Label(summaryfrme, text="$0.00").place(x=130 ,y=0)
  sub=Label(summaryfrme, text="Subtotal").place(x=0 ,y=21)
  sub1=Label(summaryfrme, text="$0.00").place(x=130 ,y=21)
  tax=Label(summaryfrme, text="Tax1").place(x=0 ,y=42)
  tax1=Label(summaryfrme, text="$0.00").place(x=130 ,y=42)
  cost=Label(summaryfrme, text="Extra cost").place(x=0 ,y=63)
  cost=Label(summaryfrme, text="$0.00").place(x=130 ,y=63)
  order=Label(summaryfrme, text="P.Order total").place(x=0 ,y=84)
  order1=Label(summaryfrme, text="$0.00").place(x=130 ,y=84)

  fir5Frame=Frame(pop1,height=38,width=210)
  fir5Frame.place(x=735,y=485)
  btndown=Button(fir5Frame, compound="left", text="Line Down").place(x=75, y=0)
  btnup=Button(fir5Frame, compound="left", text="Line Up").place(x=150, y=0)



# print preview purchase order
def printpreview1():
  messagebox.showerror("F-Billing Revolution","Customer is required,please select customer for this order before printing.")




#delete purchase order
def dele1():  
  messagebox.askyesno("Delete order", "Are you sure to delete this order? All products will be placed back into stock")
    


#search in purchase order
def search1():  
    top = Toplevel()     
    top.title("Find Text")   
    top.geometry("600x250+390+250")
    findwhat1=Label(top,text="Find What:",pady=5,padx=10).place(x=5,y=20)
    n = StringVar()
    findwhat = ttk.Combobox(top, width = 40, textvariable = n ).place(x=90,y=25)
   
    findin1=Label(top,text="Find in:",pady=5,padx=10).place(x=5,y=47)
    n = StringVar()
    findIN = ttk.Combobox(top, width = 30, textvariable = n )
    findIN['values'] = ('Product/Service id', ' Category', ' Active',' name',' stock',' location', ' image',' <<All>>')                       
    findIN.place(x=90,y=54)
    findIN.current(0)

    findButton = Button(top, text ="Find next",width=10).place(x=480,y=22)
    closeButton = Button(top,text ="Close",width=10).place(x=480,y=52)
    
    match1=Label(top,text="Match:",pady=5,padx=10).place(x=5,y=74)
    n = StringVar()
    match = ttk.Combobox(top, width = 23, textvariable = n )   
    match['values'] = ('From Any part',' Whole Field',' From the beginning of the field')                                   
    match.place(x=90,y=83)
    match.current(0)

    search1=Label(top,text="Search:",pady=5,padx=10).place(x=5,y=102)
    n = StringVar()
    search = ttk.Combobox(top, width = 23, textvariable = n )
    search['values'] = ('All', 'up',' Down')
    search.place(x=90,y=112)
    search.current(0)
    checkvarStatus4=IntVar()  
    Button4 = Checkbutton(top,variable = checkvarStatus4,text="Match Case",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button4.place(x=90,y=141)
    checkvarStatus5=IntVar()   
    Button5 = Checkbutton(top,variable = checkvarStatus5,text="Match Format",onvalue =0 ,offvalue = 1,height=3,width = 15)
    Button5.place(x=300,y=141)




#print selectede purchase order
def printsele1():

  def proper1():
    propert=Toplevel()
    propert.title("Microsoft Print To PDF Advanced Document Settings")
    propert.geometry("670x500+240+150")

    def proper2():
      propert1=Toplevel()
      propert1.title("Microsoft Print To PDF Advanced Document Settings")
      propert1.geometry("670x500+240+150")

      name=Label(propert1, text="Microsoft Print To PDF Advanced Document Settings").place(x=10, y=5)
      paper=Label(propert1, text="Paper/Output").place(x=30, y=35)
      size=Label(propert1, text="Paper size").place(x=55, y=65)
      n = StringVar()
      search = ttk.Combobox(propert1, width = 15, textvariable = n )
      search['values'] = ('letter')
      search.place(x=150,y=65)
      search.current(0)
      copy=Label(propert1, text="Copy count:").place(x=55, y=95)

      okbtn=Button(propert1,compound = LEFT,image=tick , text="Ok", width=60).place(x=460, y=450)
      canbtn=Button(propert1,compound = LEFT,image=cancel, text="Cancel", width=60).place(x=570, y=450)
      


    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook.Tab', background="#999999", width=20, padding=5)
    property_Notebook = ttk.Notebook(propert)
    property_Frame = Frame(property_Notebook, height=500, width=670)
    property_Notebook.add(property_Frame, text="Layout")
    property_Notebook.place(x=0, y=0)

    name=Label(property_Frame, text="Orientation:").place(x=10, y=5)
    n = StringVar()
    search = ttk.Combobox(property_Frame, width = 23, textvariable = n )
    search['values'] = ('Portrait')
    search.place(x=10,y=25)
    search.current(0)

    text=Text(property_Frame,width=50).place(x=250, y=5,height=350)

    btn=Button(property_Frame, text="Advanced",command=proper2).place(x=550, y=380)
    btn=Button(property_Frame,compound = LEFT,image=tick, text="OK", width=60,).place(x=430, y=420)
    btn=Button(property_Frame,compound = LEFT,image=tick, text="Cancel", width=60,).place(x=550, y=420)     

      
  
  if(False):
      messagebox.showwarning("FBilling Revelution 2020", "Customer is required, Please select customer for this invoice\nbefore printing")
  elif(False):
      messagebox.showinfo("FBilling Revelution 2020", "Print job has been completed.")
  else:
      print1=Toplevel()
      print1.title("Print")
      print1.geometry("670x400+240+150")
      
      printerframe=LabelFrame(print1, text="Printer", height=80, width=650)
      printerframe.place(x=7, y=5)      
      name=Label(printerframe, text="Name:").place(x=10, y=5)
      e1= ttk.Combobox(printerframe, width=40).place(x=70, y=5)
      where=Label(printerframe, text="Where:").place(x=10, y=30)
      printocheckvar=IntVar()
      printochkbtn=Checkbutton(printerframe,text="Print to file",variable=printocheckvar,onvalue=1,offvalue=0,height=1,width=10)
      printochkbtn.place(x=450, y=30)
      btn=Button(printerframe, text="Properties", width=10,command=proper1).place(x=540, y=5)

      pageslblframe=LabelFrame(print1, text="Pages", height=140, width=320)
      pageslblframe.place(x=10, y=90)
      radvar=IntVar()
      radioall=Radiobutton(pageslblframe, text="All", variable=radvar, value="1").place(x=10, y=5)
      radiocpage=Radiobutton(pageslblframe, text="Current Page", variable=radvar, value="2").place(x=10, y=25)
      radiopages=Radiobutton(pageslblframe, text="Pages: ", variable=radvar, value="3").place(x=10, y=45)
      pagecountentry = Entry(pageslblframe, width=23).place(x=80, y=47)
      pageinfolabl=Label(pageslblframe, text="Enter page numbers and/or page ranges\nseperated by commas. For example:1,3,5-12")
      pageinfolabl.place(x=5, y=75)

      copylblframe=LabelFrame(print1, text="Copies", height=140, width=320)
      copylblframe.place(x=335, y=90)
      nolabl=Label(copylblframe, text="Number of copies").place(x=5, y=5)      
      noentry = Entry(copylblframe, width=18).place(x=130, y=5)      
      one=Frame(copylblframe, width=30, height=40, bg="black").place(x=20, y=40)     
      two=Frame(copylblframe, width=30, height=40, bg="grey").place(x=15, y=45)     
      three=Frame(copylblframe, width=30, height=40, bg="white").place(x=10, y=50)      
      four=Frame(copylblframe, width=30, height=40, bg="black").place(x=80, y=40)      
      fiv=Frame(copylblframe, width=30, height=40, bg="grey").place(x=75, y=45)      
      six=Frame(copylblframe, width=30, height=40, bg="white").place(x=70, y=50)      
      collatecheckvar=IntVar()
      collatechkbtn=Checkbutton(copylblframe,text="Collate",variable=collatecheckvar,onvalue=1,offvalue=0,height=1,width=10)
      collatechkbtn.place(x=130, y=70)

      othrlblframe=LabelFrame(print1, text="Other", height=120, width=320)
      othrlblframe.place(x=10, y=235)
      printlb=Label(othrlblframe, text="Print").place(x=5, y=0)
      dropprint = ttk.Combobox(othrlblframe, width=23).place(x=80, y=0)
      orderlb=Label(othrlblframe, text="Order").place(x=5, y=25)
      dropord = ttk.Combobox(othrlblframe, width=23).place(x=80, y=25)
      duplexlb=Label(othrlblframe, text="Duplex").place(x=5, y=50)
      droplex = ttk.Combobox(othrlblframe, width=23).place(x=80, y=50)

      prmodelblframe=LabelFrame(print1, text="Print mode", height=120, width=320)
      prmodelblframe.place(x=335, y=235)
      dropscal = ttk.Combobox(prmodelblframe, width=30).place(x=5, y=5)
      poslb=Label(prmodelblframe, text="Print on sheet").place(x=5, y=35)
      droppos = ttk.Combobox(prmodelblframe, width=10).place(x=155, y=35)

      okbtn=Button(print1,compound = LEFT,image=tick,text="Ok", width=60).place(x=460, y=370)
      canbtn=Button(print1,compound = LEFT,image=tick, text="Cancel", width=60).place(x=570, y=370)
      




main1Frame=Frame(tab5, relief=GROOVE, bg="#f8f8f2")
main1Frame.pack(side="top", fill=BOTH)

mid1Frame=Frame(main1Frame, bg="#f5f3f2", height=60)
mid1Frame.pack(side="top", fill=X)

w = Canvas(mid1Frame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(5, 2))
w = Canvas(mid1Frame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=(0, 5))

invoice1Label = Button(mid1Frame,compound="top", text="Create new\nP.Order",relief=RAISED, image=photo,bg="#f5f3f2", fg="black", height=55, bd=1, width=55,command=createpur)
invoice1Label.pack(side="left", pady=3, ipadx=4)

order1Label = Button(mid1Frame,compound="top", text="View/Edit\nP.Orders",relief=RAISED, image=photo1,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=createpur)
order1Label.pack(side="left")

estimate1Label = Button(mid1Frame,compound="top", text="Delete\nSelected",relief=RAISED, image=photo2,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=dele1)
estimate1Label.pack(side="left")

w = Canvas(mid1Frame, width=1, height=65, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

preview1Label = Button(mid1Frame,compound="top", text="Print\nPreview",relief=RAISED, image=photo4,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=printpreview1)
preview1Label.pack(side="left")

purchase1Label = Button(mid1Frame,compound="top", text="Print\nSelected",relief=RAISED, image=photo5,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=printsele1)
purchase1Label.pack(side="left")

w = Canvas(mid1Frame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

expense1Label = Button(mid1Frame,compound="top", text=" E-mail \nP.Order",relief=RAISED, image=photo6,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=email_invoice_recurring)
expense1Label.pack(side="left")

sms1Label = Button(mid1Frame,compound="top", text="Send SMS\nnotification",relief=RAISED, image=photo10,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=sms)
sms1Label.pack(side="left")

w = Canvas(mid1Frame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

product1Label = Button(mid1Frame,compound="top", text="Search\nP.Orders",relief=RAISED, image=photo7,bg="#f8f8f2", fg="black", height=55, bd=1, width=55,command=search1)
product1Label.pack(side="left")

lb1frame = LabelFrame(mid1Frame, height=60, width=200, bg="#f8f8f2")
lb1frame.pack(side="left", padx=10, pady=0)
lbl1_invdt = Label(lb1frame, text="Order date from : ", bg="#f8f8f2")
lbl1_invdt.grid(row=0, column=0, pady=5, padx=(5, 0))
lbl1_invdtt = Label(lb1frame, text="Order date to  :  ", bg="#f8f8f2")
lbl1_invdtt.grid(row=1, column=0, pady=5, padx=(5, 0))
invdt1 = Entry(lb1frame, width=15)
invdt1.grid(row=0, column=1)
invdtt1 = Entry(lb1frame, width=15)
invdtt1.grid(row=1, column=1)
check1var1 = IntVar()
chk1btn1 = Checkbutton(lb1frame, text = "Apply filter", variable = check1var1, onvalue = 1, offvalue = 0, height = 2, width = 8, bg="#f8f8f2")
chk1btn1.grid(row=0, column=2, rowspan=2, padx=(5,5))

product1Label = Button(mid1Frame,compound="top", text="Refresh\nP.Orders list",relief=RAISED, image=photo8,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
product1Label.pack(side="left")

w = Canvas(mid1Frame, width=1, height=55, bg="#b3b3b3", bd=0)
w.pack(side="left", padx=5)

product1Label = Button(mid1Frame,compound="top", text="Hide totals\nSum",relief=RAISED, image=photo9,bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
product1Label.pack(side="left")


invoi1label = Label(main1Frame, text="Purchase Orders(All)", font=("arial", 18), bg="#f8f8f2")
invoi1label.pack(side="left", padx=(20,0))
drop1 = ttk.Combobox(main1Frame, value="Hello")
drop1.pack(side="right", padx=(0,10))
invoi1label = Label(main1Frame, text="Category filter", font=("arial", 15), bg="#f8f8f2")
invoi1label.pack(side="right", padx=(0,10))

class MyApp1:
  def __init__(self, parent):
    
    self.myParent = parent 

    self.myContainer1 = Frame(parent) 
    self.myContainer1.pack()
    
    self.top_frame = Frame(self.myContainer1) 
    self.top_frame.pack(side=TOP,
      fill=BOTH, 
      expand=YES,
      )  

    self.left_frame = Frame(self.top_frame, background="white",
      borderwidth=5,  relief=RIDGE,
      height=250, 
      width=2000, 
      )
    self.left_frame.pack(side=LEFT,
      fill=BOTH, 
      expand=YES,
      )

    
    tree = ttk.Treeview(self.left_frame, columns = (1,2,3,4,5,6,7,8,9,10), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="P.Order#")
    tree.heading(3, text="Order date")
    tree.heading(4, text="Due date")
    tree.heading(5, text="Customer Name")
    tree.heading(6, text="Status")
    tree.heading(7, text="Emailed on")
    tree.heading(8, text="Printed on")
    tree.heading(9, text="SMS on")
    tree.heading(10, text="Order Total")   
    tree.column(1, width = 40)
    tree.column(2, width = 145)
    tree.column(3, width = 140)
    tree.column(4, width = 140)
    tree.column(5, width = 200)
    tree.column(6, width = 140)
    tree.column(7, width = 150)
    tree.column(8, width = 130)
    tree.column(9, width = 130)
    tree.column(10, width = 130)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=990+345, y=0, height=300+20)
    scrollbar.config( command=tree.yview )

    tabControl = ttk.Notebook(self.left_frame,width=1)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tabControl.add(tab1,image=invoices,compound = LEFT, text ='P.Order Items')
    tabControl.add(tab2,image=photo11,compound = LEFT, text ='Invoice Private Notes')
    tabControl.add(tab3,image=smslog,compound = LEFT, text ='SMS log')
    tabControl.add(tab4,image=photo11,compound = LEFT, text ='Documents')
    tabControl.pack(expand = 1, fill ="both")
    
    tree = ttk.Treeview(tab1, columns = (1,2,3,4,5,6,7,8,), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Product/Service ID",)
    tree.heading(3, text="Name")
    tree.heading(4, text="Description")
    tree.heading(5, text="Price")
    tree.heading(6, text="QTY")
    tree.heading(7, text="Tax1")
    tree.heading(8, text="Line Total")   
    tree.column(1, width = 40)
    tree.column(2, width = 260)
    tree.column(3, width = 260)
    tree.column(4, width = 300)
    tree.column(5, width = 130)
    tree.column(6, width = 100)
    tree.column(7, width = 100)
    tree.column(8, width = 150)

    note1=Text(tab2, width=170,height=10).place(x=10, y=10)

    note1=Text(tab3, width=170,height=10).place(x=10, y=10)

    tree = ttk.Treeview(tab4, columns = (1,2,3), height = 15, show = "headings")
    tree.pack(side = 'top')
    tree.heading(1)
    tree.heading(2, text="Attach to Email",)
    tree.heading(3, text="Filename")
    tree.column(1, width = 50)
    tree.column(2, width = 250)
    tree.column(3, width = 1000)

    scrollbar = Scrollbar(self.left_frame)
    scrollbar.place(x=990+340, y=360, height=190)
    scrollbar.config( command=tree.yview )

# productandservice

def file():
    filename = filedialog.askopenfilename(title='open')
    return filename

def file_upload():
    f = file()
    img = Image.open(f)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(tab2, image=img)
    panel.image = img
    panel.pack()


######### ADD New Product ##############

def adda_product():
    top = Toplevel()  
    
    top.title("Add a new Product/Service")
    p2 = PhotoImage(file = 'images/fbicon.png')
    top.iconphoto(False, p1)
    top.geometry("600x550+390+125")
    
    
    tabControl = ttk.Notebook(top)
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#999999", width=50, padding=10,bd=0)


    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    
    tabControl.add(tab1,compound = LEFT, text ='Product/Service')
    tabControl.add(tab2,compound = LEFT, text ='Product Image')
    
    tabControl.pack(expand = 1, fill ="both")
    
    innerFrame = Frame(tab1,bg="#f5f3f2", relief=GROOVE, height=490)
    innerFrame.pack(side="top",fill=BOTH)

    Customerlabelframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=475)
    Customerlabelframe.pack(side="top",fill=BOTH,padx=10)
    
    global filename
    filename = ""
    
    def upload_file():
      global filename,img, b2
      f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
      filename = filedialog.askopenfilename(filetypes=f_types)
      image = Image.open(filename)
      resize_image = image.resize((350, 350))
      img = ImageTk.PhotoImage(resize_image)
      b2 = Button(imageFrame,image=img)
      b2.place(x=130, y=80)
    
    def addproducts():
      global img , filename 
      sku = codeentry.get()
      status = checkvarStatus.get()
      catgory = n.get()
      name = nameentry.get()
      description = desentry.get()
      unitprice = uval.get()
      peices = pcsentry.get()
      cost = costval.get()
      price_cost = priceval.get()
      taxable = checkvarStatus2.get()
      nostockcontrol = checkvarStatus3.get()
      stock = stockval.get()
      lowstock = lowval.get()
      warehouse = wareentry.get()
      # pnotes = pnoteval.get()
      entries = [sku, name, unitprice, cost]
      entri = []
      for i in entries:
        if i == '':
          entri.append(i)
      if len(entri) == 0:
        mydb = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='fbilldb')
        mycursor = mydb.cursor()
        sql = 'select * from Productservice where sku = %s or name = %s'
        val  = (sku, name)
        mycursor.execute(sql, val)
        mycursor.fetchall()
        row_count = mycursor.rowcount
        if row_count == 0:
          if filename == "":
            sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse)
            mycursor.execute(sql, val)
            mydb.commit()
          else:
            fob=open(filename,'rb') # filename from upload_file()
            fob=fob.read()
            sql = 'insert into Productservice(sku, category, name, description, status, unitprice, peices, cost, taxable, priceminuscost, serviceornot, stock, stocklimit, warehouse, image) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, fob)
            mycursor.execute(sql, val)
            mydb.commit()
        else:
          messagebox.showinfo("Alert", "Entry with same name or SKU already exists.\nTry again.")
        mydb.close()
        top.destroy()
        messagebox.showinfo("F-Billing Revolution", "Product added successfully.")
      else:
        messagebox.showinfo("Alert", "Fields name and SKU should not be empty.\nFill out required fields and try again")
        top.destroy()
    
    code1=Label(Customerlabelframe,text="Code or SKU* :",fg="blue",pady=10,padx=10)
    code1.place(x=20,y=0)
    codeentry = Entry(Customerlabelframe,width=35)
    codeentry.place(x=110,y=8)

    checkvarStatus=IntVar()
    status1=Label(Customerlabelframe,text="Status:")
    status1.place(x=380,y=8)
    Button1 = Checkbutton(Customerlabelframe, 
                      variable = checkvarStatus,text="Active",compound="right",
                      onvalue =1,
                      offvalue = 0,
                      width = 10)

    Button1.place(x=420,y=5)

    category1=Label(Customerlabelframe,text="Category:",pady=5,padx=10)
    category1.place(x=20,y=40)
    n = StringVar() 
    catgory = Entry(Customerlabelframe, width = 40, textvariable = n ) 
    catgory.place(x=110,y=45)
    catgory.insert(0, 'Default')


    name1=Label(Customerlabelframe,text="Name* :",fg="blue",pady=5,padx=10)
    name1.place(x=20,y=70)
    nameentry = Entry(Customerlabelframe,width=70)
    nameentry.place(x=110,y=75)

    des1=Label(Customerlabelframe,text="Description :",pady=5,padx=10)
    des1.place(x=20,y=100)
    desentry = Entry(Customerlabelframe,width=70)
    desentry.place(x=110,y=105)

    uval = IntVar()
    unit1=Label(Customerlabelframe,text="Unit Price:",fg="blue",pady=5,padx=10)
    unit1.place(x=20,y=130)
    unitentry = Entry(Customerlabelframe,width=20,textvariable=uval)
    unitentry.place(x=110,y=135)

    # pcsval = IntVar()
    pcs1=Label(Customerlabelframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
    pcs1.place(x=320,y=130)
    pcsentry = Entry(Customerlabelframe,width=20)
    pcsentry.place(x=410,y=135)

    costval = IntVar()
    cost1=Label(Customerlabelframe,text="Cost:",pady=5,padx=10)
    cost1.place(x=20,y=160)
    
    costentry = Entry(Customerlabelframe,width=20,textvariable=costval)
    costentry.place(x=110,y=165)
    
    priceval = IntVar()
    price1=Label(Customerlabelframe,text="(Price-Cost):",pady=5,padx=10)
    price1.place(x=20,y=190)
    priceentry = Entry(Customerlabelframe,width=20,textvariable=priceval)
    priceentry.place(x=110,y=195)

    checkvarStatus2=IntVar()
   
    Button2 = Checkbutton(Customerlabelframe,variable = checkvarStatus2, 
                      text="Taxable Tax1rate",compound="right",
                      onvalue =0 ,
                      offvalue = 1,
                      height=2,
                      width = 12)

    Button2.place(x=415,y=153)


    checkvarStatus3=IntVar()
   
    Button3 = Checkbutton(Customerlabelframe,variable = checkvarStatus3, 
                      text="No stock Control", 
                      onvalue =1 ,
                      offvalue = 0,
                      height=3,
                      width = 15)

    Button3.place(x=40,y=220)


    stockval = IntVar()
    stock1=Label(Customerlabelframe,text="Stock:",pady=5,padx=10)
    stock1.place(x=90,y=260)
    stockentry = Entry(Customerlabelframe,width=15,textvariable=stockval)
    stockentry.place(x=140,y=265)

    lowval = IntVar()
    low1=Label(Customerlabelframe,text="Low Stock Warning Limit:",pady=5,padx=10)
    low1.place(x=280,y=260)
    lowentry = Entry(Customerlabelframe,width=15,textvariable=lowval)
    lowentry.place(x=435,y=265)

   
    ware1=Label(Customerlabelframe,text="Warehouse:",pady=5,padx=10)
    ware1.place(x=60,y=290)
    wareentry = Entry(Customerlabelframe,width=64)
    wareentry.place(x=140,y=295)

    # pnoteval = StringVar()
    text1=Label(Customerlabelframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
    text1.place(x=20,y=320)
    txt = scrolledtext.ScrolledText(Customerlabelframe, undo=True,width=62,height=4)
    txt.place(x=32,y=358)
    
    okButton = Button(innerFrame, text ="Ok",image=tick,width=70,compound = LEFT, command=addproducts)
    okButton.pack(side=LEFT, padx=(10, 0), pady=(5, 10))
    
    def closetab():
      top.destroy()

    cancelButton = Button(innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT, command=closetab)
    cancelButton.pack(side=RIGHT, padx=(0, 10), pady=(5, 10))

    imageFrame = Frame(tab2, relief=GROOVE,height=580)
    imageFrame.pack(side="top",fill=BOTH)

    
      
    browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
    browseimg.place(x=30,y=35)
      
    browsebutton=Button(imageFrame,text = 'Browse',command=upload_file)
    browsebutton.place(x=485,y=30,height=30,width=50)

    removeButton = Button(imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT, command=lambda: b2.destroy())
    removeButton.place(x=410,y=460)

    top.mainloop()

def fileimport_product():

    top=Toplevel()
    top.title("Import items list from Excel(XLS)File")
    top.geometry("785x520+280+100")
    importframe=Frame(top)
    importframe.place(x=0,y=0,height=700,width=785)
    impolbl=Label(importframe,text="Import source Excel(xlsx) File:").place(x=8,y=30)
    impoentry=Entry(importframe,bg="white")
    impoentry.place(x=8,y=50,width=280, height=25)
    previewlbl=Label(importframe,text="Source File preview").place(x=8,y=77)
   
    ###### LISTBOX #####################
    langs = ()

    langs_var = StringVar(value=langs)

    listbox = Listbox(
        importframe,
        listvariable=langs_var,
        width=60,
        height=6,
        selectmode='extended')

    listbox.place(x=8,y=100,height=320)
    
    # link a scrollbar to a list
    scrollbar = Scrollbar(
        importframe,
        orient='vertical',
        command=listbox.yview
    )
    
    listbox['yscrollcommand'] = scrollbar.set
    scrollbar.place(x=354,y=100,height=319)
       


    lb1=Label(importframe,text="Select import source XLs file first after build column associations").place(x=8,y=480)

    def callback(url):
        webbrowser.open_new(url)
    # link1 = Label(importframe, text="More info", fg="blue", cursor="hand2")
    # link1.place(x=360,y=480)
    # link1.bind("<Button-1>", lambda e: callback("https://f-billing.com/faq.php"))
    
    importbutton=Button(top,command=export_product,text = 'Browse',compound=LEFT)
    importbutton.place(x=290,y=48,height=25,width=80)

    lb1=Label(importframe,text="Please associate datafields with data columns").place(x=460,y=30)

    id1=Label(importframe,text="ID = ",pady=5,padx=10,fg="blue")
    id1.place(x=450,y=70)
    no = StringVar() 
    idd = ttk.Combobox(importframe, width = 27, textvariable = no ) 
      
    # Adding combobox drop down list 
    idd['values'] = ('notassociated' 
                              )
      
    idd.place(x=570,y=78) 
    idd.current(0)

    name1=Label(importframe,text="NAME = ",pady=5,padx=10,fg="blue")
    name1.place(x=450,y=92)
    namevar = StringVar() 
    name = ttk.Combobox(importframe, width = 27, textvariable = namevar ) 
      
    # Adding combobox drop down list 
    name['values'] = ('notassociated' 
                              )
      
    name.place(x=570,y=98) 
    name.current(0)


    category1=Label(importframe,text="CATEGORY = ",pady=5,padx=10,fg="blue")
    category1.place(x=450,y=117)
    categoryvar = StringVar() 
    category = ttk.Combobox(importframe, width = 27, textvariable = categoryvar ) 
      
    # Adding combobox drop down list 
    category['values'] = ('notassociated' 
                              )
      
    category.place(x=570,y=118) 
    category.current(0)

    desc1=Label(importframe,text="DESCRIPTION = ",pady=5,padx=10)
    desc1.place(x=450,y=139)
    descvar = StringVar() 
    desc = ttk.Combobox(importframe, width = 27, textvariable = descvar ) 
      
    # Adding combobox drop down list 
    desc['values'] = ('notassociated' 
                              )
      
    desc.place(x=570,y=140) 
    desc.current(0)

    quan1=Label(importframe,text="QUANTITY= ",pady=5,padx=10)
    quan1.place(x=450,y=161)
    quanvar = StringVar() 
    quantity = ttk.Combobox(importframe, width = 27, textvariable = categoryvar ) 
      
    # Adding combobox drop down list 
    quantity['values'] = ('notassociated' 
                              )
      
    quantity.place(x=570,y=166) 
    quantity.current(0)

    cost1=Label(importframe,text="COST = ",pady=5,padx=10)
    cost1.place(x=450,y=183)
    costvar = StringVar() 
    cost = ttk.Combobox(importframe, width = 27, textvariable = costvar ) 
      
    # Adding combobox drop down list 
    cost['values'] = ('notassociated' 
                              )
      
    cost.place(x=570,y=192) 
    cost.current(0)

    price1=Label(importframe,text="PRICE = ",pady=5,padx=10,fg="blue")
    price1.place(x=450,y=205)
    pricevar = StringVar() 
    price = ttk.Combobox(importframe, width = 27, textvariable = costvar ) 
      
    # Adding combobox drop down list 
    price['values'] = ('notassociated' 
                              )
      
    price.place(x=570,y=218) 
    price.current(0)


    taxx1=Label(importframe,text="TAX1 = ",pady=5,padx=10,fg="blue")
    taxx1.place(x=450,y=230)
    taxvar = StringVar() 
    tax = ttk.Combobox(importframe, width = 27, textvariable = taxvar ) 
      
    # Adding combobox drop down list 
    tax['values'] = ('notassociated' 
                              )
      
    tax.place(x=570,y=243) 
    tax.current(0)

    taxx2=Label(importframe,text="TAX2 = ",pady=5,padx=10)
    taxx2.place(x=450,y=262)
    tax2var = StringVar() 
    tax2 = ttk.Combobox(importframe, width = 27, textvariable = tax2var ) 
      
    # Adding combobox drop down list 
    tax2['values'] = ('notassociated' 
                              )
      
    tax2.place(x=570,y=270) 
    tax2.current(0)

    stock2=Label(importframe,text="STOCK = ",pady=5,padx=10)
    stock2.place(x=450,y=291)
    stock2var = StringVar() 
    stock2 = ttk.Combobox(importframe, width = 27, textvariable = stock2var ) 
      
    # Adding combobox drop down list 
    stock2['values'] = ('notassociated')
      
    stock2.place(x=570,y=295) 
    stock2.current(0)


    lowstock2=Label(importframe,text="LOW STOCK = ",pady=5,padx=10)
    lowstock2.place(x=450,y=315)
    lowstock2var = StringVar() 
    lowstock = ttk.Combobox(importframe, width = 27, textvariable = lowstock2var ) 
      
    # Adding combobox drop down list 
    lowstock['values'] = ('notassociated' 
                              )
      
    lowstock.place(x=570,y=320) 
    lowstock.current(0)


    location2=Label(importframe,text="LOCATION = ",pady=5,padx=10)
    location2.place(x=450,y=339)
    Location2var = StringVar() 
    location = ttk.Combobox(importframe, width = 27, textvariable = Location2var ) 
      
    # Adding combobox drop down list 
    location['values'] = ('notassociated' 
                              )
      
    location.place(x=570,y=345) 
    location.current(0)


    active2=Label(importframe,text="ACTIVE = ",pady=5,padx=10)
    active2.place(x=450,y=363)
    active2var = StringVar() 
    active = ttk.Combobox(importframe, width = 27, textvariable = active2var ) 
      
    # Adding combobox drop down list 
    active['values'] = ('notassociated' 
                              )
      
    active.place(x=570,y=370) 
    active.current(0)

    service2=Label(importframe,text="SERVICE = ",pady=5,padx=10)
    service2.place(x=450,y=387)
    service2var = StringVar() 
    service = ttk.Combobox(importframe, width = 27, textvariable = service2var ) 
      
    # Adding combobox drop down list 
    service['values'] = ('notassociated' 
                              )
      
    service.place(x=570,y=395) 
    service.current(0)


    b = Button(importframe,text = "Clear associations").place(x=600,y=470)  
    n = Button(importframe, text ="Next").place(x=710,y=470)
  
    
    top.mainloop()
    
#########EXPORT PRODUCT#######################################################################################
    
def export_product():
    name = askopenfilename(filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xslm', '*.xlsx'))])

    if name:
        if name.endswith('.csv'):
            df = pd.read_csv(name)
        else:
            df = pd.read_excel(name)

            filename = name
            text.insert('end', str(df.head()) + '\n')

########################VIEW/EDIT PRODUCT#######################################################################


def edit_product():  
    try:
      itemid = tree.item(tree.focus())["values"][1]
      
      global filename
      filename = ""
      
      def upload_file():
        global filename,img, b2
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        image = Image.open(filename)
        resize_image = image.resize((350, 350))
        img = ImageTk.PhotoImage(resize_image)
        b2 = Button(imageFrame,image=img)
        b2.place(x=130, y=80)
      
      def updateproducts():
        global img , filename 
        sku = codeentry.get()
        status = checkvarStatus.get()
        catgory = n.get()
        name = nameentry.get()
        description = desentry.get()
        unitprice = uval.get()
        peices = pcsentry.get()
        cost = costval.get()
        price_cost = priceval.get()
        taxable = checkvarStatus2.get()
        nostockcontrol = checkvarStatus3.get()
        stock = stockval.get()
        lowstock = lowval.get()
        warehouse = wareentry.get()
        # pnotes = pnoteval.get()
        entries = [sku, name, unitprice, cost]
        entri = []
        for i in entries:
          if i == '':
            entri.append(i)
        if len(entri) == 0:
          mydb = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='fbilldb')
          mycursor = mydb.cursor()
          if filename == "":
            sql = "update Productservice set sku=%s, category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s where Productserviceid = %s"
            val = (sku, catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, itemid)
            mycursor.execute(sql, val)
            mydb.commit()
          else:
            fob=open(filename,'rb') # filename from upload_file()
            fob=fob.read()
            sql = "update Productservice set category=%s, name=%s, description=%s, status=%s, unitprice=%s, peices=%s, cost=%s, taxable=%s, priceminuscost=%s, serviceornot=%s, stock=%s, stocklimit=%s, warehouse=%s, image=%s where Productserviceid = %s"
            val = (catgory, name, description, status, unitprice, peices, cost, taxable, price_cost, nostockcontrol, stock, lowstock, warehouse, fob, itemid)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("F-Billing Revolution", "Product updated successfully.")
          mydb.close()
          top.destroy()
        else:
          messagebox.showinfo("F-Billing Revolution", "Fields name or SKU entered is already in database.")
          top.destroy()
      fbilldb = mysql.connector.connect(
          host="localhost", user="root", password="", database="fbilldb", port="3306"
      )
      feditcursor = fbilldb.cursor()
      sql = "select * from Productservice where Productserviceid = %s"
      val = (itemid, )
      feditcursor.execute(sql, val)
      psdata = feditcursor.fetchone()
      fbilldb.close()
      
      top = Toplevel()  
      top.title("Edit Product/Service details")
      p3 = PhotoImage(file = 'images/fbicon.png')
      top.iconphoto(False, p1)
      top.geometry("600x550+390+125")
      tabControl = ttk.Notebook(top)
      s = ttk.Style()
      s.theme_use('default')
      s.configure('TNotebook.Tab', background="#999999", width=50, padding=10,bd=0)

      taba = ttk.Frame(tabControl)
      tabb = ttk.Frame(tabControl)
      
      tabControl.add(taba,compound = LEFT, text ='Product/Service')
      tabControl.add(tabb,compound = LEFT, text ='Product Image')
      
      tabControl.pack(expand = 1, fill ="both")
      
      innerFrame = Frame(taba,bg="#f5f3f2", relief=GROOVE)
      innerFrame.pack(side="top",fill=BOTH)

      updateframe = LabelFrame(innerFrame,text="Product/Service",width=580,height=485)
      updateframe.pack(side="top",fill=BOTH,padx=10)

      code1=Label(updateframe,text="Code or SKU:",fg="blue",pady=10,padx=10)
      code1.place(x=20,y=0)
      codeentry = Entry(updateframe,width=35)
      codeentry.place(x=110,y=8)
      codeentry.insert(0, psdata[2])

      checkvarStatus=IntVar()
      status1=Label(updateframe,text="Status:")
      status1.place(x=380,y=8)
      Button1 = Checkbutton(updateframe, 
                        variable = checkvarStatus,text="Active",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        width = 10)
      Button1.place(x=420,y=5)

      category1=Label(updateframe,text="Category:",pady=5,padx=10)
      category1.place(x=20,y=40)
      n = StringVar() 
      category = Entry(updateframe,width=70) 
      category.place(x=110,y=45)
      category.insert(0, psdata[3])


      name1=Label(updateframe,text="Name :",fg="blue",pady=5,padx=10)
      name1.place(x=20,y=70)
      nameentry = Entry(updateframe,width=70)
      nameentry.place(x=110,y=75)
      nameentry.insert(0, psdata[4])

      des1=Label(updateframe,text="Description :",pady=5,padx=10)
      des1.place(x=20,y=100)
      desentry = Entry(updateframe,width=70)
      desentry.place(x=110,y=105)
      desentry.insert(0, psdata[5])
      
      uval = IntVar()
      unit1=Label(updateframe,text="Unit Price:",fg="blue",pady=5,padx=10)
      unit1.place(x=20,y=130)
      unitentry = Entry(updateframe,width=20,textvariable=uval)
      unitentry.place(x=110,y=135)
      unitentry.insert(0, psdata[7])
      

      pcsval = IntVar()
      pcs1=Label(updateframe,text="Pcs/Weight:",fg="blue",pady=5,padx=10)
      pcs1.place(x=320,y=130)
      pcsentry = Entry(updateframe,width=20,textvariable=pcsval)
      pcsentry.place(x=410,y=135)
      pcsentry.insert(0, psdata[8])
      

      costval = IntVar()
      cost1=Label(updateframe,text="Cost:",pady=5,padx=10)
      cost1.place(x=20,y=160)
      costentry = Entry(updateframe,width=20,textvariable=costval)
      costentry.place(x=110,y=165)
      costentry.insert(0, psdata[9])
      

      priceval = IntVar()
      price1=Label(updateframe,text="(Price-Cost):",pady=5,padx=10)
      price1.place(x=20,y=190)
      priceentry = Entry(updateframe,width=20,textvariable=priceval)
      priceentry.place(x=110,y=195)
      priceentry.insert(0, psdata[11])
      

      checkvarStatus2=IntVar()
    
      Button2 = Checkbutton(updateframe,variable = checkvarStatus2, 
                        text="Taxable Tax1rate",compound="right",
                        onvalue =0 ,
                        offvalue = 1,
                        height=2,
                        width = 12)

      Button2.place(x=415,y=153)


      checkvarStatus3=IntVar()
    
      Button3 = Checkbutton(updateframe,variable = checkvarStatus3, 
                        text="No stock Control", 
                        onvalue =1 ,
                        offvalue = 0,
                        height=3,
                        width = 15)

      Button3.place(x=40,y=220)


      stockval = IntVar(updateframe)
      stock1=Label(updateframe,text="Stock:",pady=5,padx=10)
      stock1.place(x=90,y=260)
      stockentry = Entry(updateframe,width=15,textvariable=stockval)
      stockentry.place(x=140,y=265)
      stockentry.insert(0, psdata[13])
      

      lowval = IntVar(updateframe)
      low1=Label(updateframe,text="Low Stock Warning Limit:",pady=5,padx=10)
      low1.place(x=280,y=260)
      lowentry = Entry(updateframe,width=15,textvariable=lowval)
      lowentry.place(x=435,y=265)
      lowentry.insert(0, psdata[14])
      

    
      ware1=Label(updateframe,text="Warehouse:",pady=5,padx=10)
      ware1.place(x=60,y=290)
      wareentry = Entry(updateframe,width=64)
      wareentry.place(x=140,y=295)
      wareentry.insert(0, psdata[15])
      

      text1=Label(updateframe,text="Private notes(not appears on invoice):",pady=5,padx=10)
      text1.place(x=20,y=320)
      txt = scrolledtext.ScrolledText(updateframe, undo=True,width=62,height=4)
      txt.place(x=32,y=358)

      okButton = Button(innerFrame, text ="Ok",image=tick,width=70,compound = LEFT, command=updateproducts)
      okButton.pack(side=LEFT, padx=(10, 0))

      cancelButton = Button(innerFrame,image=cancel,text="Cancel",width=70,compound = LEFT)
      cancelButton.pack(side=RIGHT, padx=(0, 10))
      
      
      imageFrame = Frame(tabb, relief=GROOVE,height=580)
      imageFrame.pack(side="top",fill=BOTH)

      browseimg=Label(imageFrame,text=" Browse for product image file(recommended image type:JPG,size 480x320 pixels) ",bg='#f5f3f2')
      browseimg.place(x=15,y=35)

      browsebutton=Button(imageFrame,text = 'Browse', command=upload_file)
      browsebutton.place(x=470,y=30,height=30,width=50)
      
      # image = Image.open(psdata[17])
      # resize_image = image.resize((350, 350))
      # img = ImageTk.PhotoImage(resize_image)
      # b2 = Button(imageFrame,image=img)
      # b2.place(x=130, y=80)
      img = Image.open(io.BytesIO(psdata[17]))
      resize_image = img.resize((350, 350))
      img = ImageTk.PhotoImage(resize_image)
      b2 = Button(imageFrame,image=img)
      b2.place(x=130, y=80)

      removeButton = Button(imageFrame,image=cancel,text="Remove Product Image",width=150,compound = LEFT)
      removeButton.place(x=410,y=460)
    except:
      try:
        top.destroy()
      except:
        pass
      messagebox.showerror('F-Billing Revolution', 'Select a record to edit.')
  


######################## DELETE PRODUCT #######################################################################


def delete_product():
    delmess = messagebox.askyesno("Delete product/service", "Are you sure to delete this product/service?")
    if delmess == True:
      itemid = tree.item(tree.focus())["values"][1]
      fbilldb = mysql.connector.connect(
          host="localhost", user="root", password="", database="fbilldb", port="3306"
      )
      fcursor = fbilldb.cursor()
      sql = "delete from Productservice where Productserviceid = %s"
      val = (itemid, )
      fcursor.execute(sql, val)
      fbilldb.commit()
      fbilldb.close()
      tree.delete(tree.selection()[0])
      messagebox.showinfo("F-Billing Revolution", "Record deleted successfully.")
    else:
      pass


######################## SEARCH PRODUCT  #######################################################################
def search_records():
  sear = searchvar.get()
  for record in treeproducts.get_children():
    treeproducts.delete(record)
  searchtop.destroy()
  
  fbilldb = mysql.connector.connect(
      host="localhost", user="root", password="", database="fbilldb", port="3306"
  )
  fcursor = fbilldb.cursor()
  
  sql = "select * from Productservice where name = %s"
  val = (sear, )
  fcursor.execute(sql, val)
  records = fcursor.fetchall()
  
  count=0
  for i in records:
    if True:
      treeproducts.insert(parent='', index='end', iid=countp, text='trtree', values=('', i[0], i[2], '', i[4], i[7], i[13], i[15]))
    else:
      pass
  count += 1
  
  fbilldb.commit()
  fbilldb.close()

def search_product():
    global searchvar, searchtop
    searchtop = Toplevel()  
    searchtop.title("Find Text")
    searchtop.geometry("520x200+390+250")
    
    findwhat1=Label(searchtop,text="Find What:",pady=5,padx=10)
    findwhat1.place(x=5,y=20)
    searchvar = StringVar() 
    findwhat = ttk.Combobox(searchtop, width = 50, textvariable = searchvar)
    findwhat.place(x=80,y=25) 
    

    findButton = Button(searchtop, text ="Find next",width=10, command=search_records)
    findButton.place(x=420,y=20)
    
    findin1=Label(searchtop,text="Find in:",pady=5,padx=10)
    findin1.place(x=5,y=47)
    n = StringVar() 
    findIN = ttk.Combobox(searchtop, width = 37, textvariable = n ) 
    # Adding combobox drop down list 
    findIN['values'] = ('Product/Service id',  
                              ' Category', 
                              ' Active', 
                              ' name', 
                              ' stock', 
                              ' location', 
                              ' image', 
                              ' <<All>>') 
      
    findIN.place(x=80,y=54) 
    findIN.current(0)

    closeButton = Button(searchtop, text ="Close",width=10, command=lambda : searchtop.destroy())
    closeButton.place(x=420,y=50)

    match1=Label(searchtop,text="Match:",pady=5,padx=10)
    match1.place(x=5,y=74)
    n = StringVar() 
    match = ttk.Combobox(searchtop, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    match['values'] = ('From Any part',' Whole Field',  
                              ' From the beginning of the field')
      
    match.place(x=80,y=83) 
    match.current(0)

    search1=Label(searchtop,text="Search:",pady=5,padx=10)
    search1.place(x=5,y=102)
    n = StringVar() 
    search = ttk.Combobox(searchtop, width = 27, textvariable = n ) 
      
    # Adding combobox drop down list 
    search['values'] = ('All', 'up', 
                              'Down')
      
    search.place(x=80,y=112) 
    search.current(0)


    checkvarStatus4=IntVar()
   
    Button4 = Checkbutton(searchtop,variable = checkvarStatus4, 
                      text="Match Case", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button4.place(x=60,y=141)

    checkvarStatus5=IntVar()
   
    Button5 = Checkbutton(searchtop,variable = checkvarStatus5, 
                      text="Match Format", 
                      onvalue =0 ,
                      offvalue = 1,
                      height=3,
                      width = 15)

    Button5.place(x=270,y=141)

    searchtop.mainloop()


######################## FRONT PAGE OF PRODUCT SERVICE SECTION #######################################################################

    
mainFrame=Frame(tab8, relief=GROOVE, bg="#f8f8f2")
mainFrame.pack(side="top", fill=BOTH)

midFrame=Frame(mainFrame, bg="#f5f3f2", height=60)
midFrame.pack(side="top", fill=X)

lFrame=Frame(tab8, bg="#f8f8f2", height=600)
lFrame.pack(side="top", fill=X)



pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(5, 2))
pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=(0, 5))

productIcon = ImageTk.PhotoImage(Image.open("images/plus.png"))
productLabel = Button(midFrame,compound="top", text="Add new\nProduct",relief=RAISED,command=adda_product, image=productIcon, font=("arial", 8),bg="#f5f3f2", fg="black", height=55, bd=1, width=55)
productLabel.pack(side="left", pady=3, ipadx=4)

proeditIcon = ImageTk.PhotoImage(Image.open("images/edit.png"))
proeditLabel = Button(midFrame,compound="top", text="Edit/View\nProduct",relief=RAISED, image=proeditIcon,command=edit_product, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
proeditLabel.pack(side="left")

prodeleteIcon = ImageTk.PhotoImage(Image.open("images/delete.png"))
prodeleteLabel = Button(midFrame,compound="top", text="Delete\nSelected",relief=RAISED, command=delete_product,image=prodeleteIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
prodeleteLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=65, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

prosearchIcon = ImageTk.PhotoImage(Image.open("images/research.png"))
prosearchLabel = Button(midFrame,compound="top", text="Search in\nproducts",relief=RAISED,command=search_product, image=prosearchIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55, activebackground="red")
prosearchLabel.pack(side="left")

proimportIcon = ImageTk.PhotoImage(Image.open("images/import.png"))
proimportLabel = Button(midFrame,compound="top", text="Import\nProducts",relief=RAISED,command=fileimport_product, image=proimportIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
proimportLabel.pack(side="left")

pn = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
pn.pack(side="left", padx=5)

proexportIcon = ImageTk.PhotoImage(Image.open("images/export-file.png"))
proexportLabel = Button(midFrame,compound="top",command=export_product, text="Export\nProducts",relief=RAISED, image=proexportIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55)
proexportLabel.pack(side="left")


pn = Canvas(midFrame, width=1, height=55, bg="#b3b3b3", bd=0)
pn.pack(side="left")

prorefreshIcon = ImageTk.PhotoImage(Image.open("images/refresh.png"))
productrefreshLabel = Button(midFrame,compound="top", text="Refresh\nProduct List",relief=RAISED, image=prorefreshIcon, font=("arial", 8),bg="#f8f8f2", fg="black", height=55, bd=1, width=55, command=reset)
productrefreshLabel.pack(side="left")

prolabel = Label(mainFrame, text="Products/Services", font=("arial", 18), bg="#f8f8f2")
prolabel.pack(side="left", padx=(20,0))

pr_label = Label(mainFrame, text="Category", font=("arial", 16), bg="#f8f8f2")
pr_label.place(x=1099,y=70)

pro_search = Label(mainFrame, text="Product name quick search:", bg="#f8f8f2")
pro_search.pack(side="left", padx=(250,0))

pro_searchentry = Entry(mainFrame)
pro_searchentry.pack(side="left", padx=(10,0))

 

pro_label = Label(mainFrame, text="Right click on datagrid row for more options.",  bg="#f8f8f2")
pro_label.pack(side="right", padx=(0,260))

mydb = mysql.connector.connect(host='localhost', user='root', password='', port='3306', database='fbilldb')
mycursor = mydb.cursor()
sql = 'select * from Productservice'
mycursor.execute(sql)
pandsdata = mycursor.fetchall()

treeproducts=ttk.Treeview(tab8,selectmode='browse')
treeproducts.place(x=8,y=100,height=580)
vertical_bar=ttk.Scrollbar(tab8,orient="vertical")
vertical_bar.place(x=1083,y=101,height=580)

treeproducts["columns"]=("1","2","3","4","5","6","7","8","9")
treeproducts["show"]='headings'
treeproducts.column("1",width=0,anchor='c', stretch=False)
treeproducts.column("2",width=160,anchor='c')
treeproducts.column("3",width=190,anchor='c')
treeproducts.column("4",width=120,anchor='c')
treeproducts.column("5",width=120,anchor='c')
treeproducts.column("6",width=120,anchor='c')
treeproducts.column("7",width=130,anchor='c')
treeproducts.column("8",width=120,anchor='c')
treeproducts.column("9",width=112,anchor='c')
treeproducts.heading("1",text="")
treeproducts.heading("2",text="Product/Service ID")
treeproducts.heading("3",text="Category")
treeproducts.heading("4",text="Active")
treeproducts.heading("5",text="Name")
treeproducts.heading("6",text="Price")
treeproducts.heading("7",text="Stock")
treeproducts.heading("8",text="Location/warehouse")
treeproducts.heading("9",text="Image")
countp = 0
for i in pandsdata:
  treeproducts.insert(parent='', index='end', iid=countp, text='hello', values=('', i[0], i[2], '', i[4], i[7], i[13], i[15]))
  countp += 1
treeproducts.place(height=580, width=1070, x=10, y=101)
######side_Listbox##############
treeps=ttk.Treeview(tab8,selectmode='browse')
treeps.place(height=580,width=254,
                      x=1099,y=101
                      )
treeps["columns"]=("1")
treeps["show"]='headings'
treeps.column("1",width=254,anchor='c')
treeps.heading("1",text="View filter by category")
listbox = Listbox(tab8,height =8,  
                      width = 29,  
                      bg = "white",
                      activestyle = 'dotbox',  
                      fg = "black",
                      highlightbackground="white")  
listbox.insert(0, "View all records")
listbox.insert(1, "View all products")
listbox.insert(2, "View all services")
listbox.place(x=1099,y=118,height=564,width=255)
       
myapp = MyApp1(tab5)

root.mainloop()
