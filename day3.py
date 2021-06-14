#importing tkinter module
from tkinter import *
from tkinter import ttk

#Creating object - root of Tk()
root = Tk()

#this will make a screen size
root.geometry("500x500")
root.configure(background="lightgreen")
#Providing title to the form
root.title('Registration form')

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Registration form", width=15,font=("bold",20))
#this method used to apply in specific postion
label_0.place(x=145,y=60)



label_1 =Label(root,text="FullName", width=10,font=("bold",10))
label_1.place(x=70,y=130)

entry_1=Entry(root)
entry_1.place(x=240,y=130)

label_3 =Label(root,text="Email", width=10,font=("bold",10))
label_3.place(x=68,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

label_4 =Label(root,text="Gender", width=10,font=("bold",10))
label_4.place(x=70,y=230)


#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)


label_5=Label(root,text="Country",width=10,font=("bold",10))
label_5.place(x=70,y=280)

#this creates list of countries available in the dropdownlist.
list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

#the variable 'c' mentioned here holds String Value, by default ""
c=StringVar()
droplist=OptionMenu(root,c, *list_of_country)
droplist.config(width=15)
c.set('Select your Country')
droplist.place(x=240,y=280)



# Creating Check Box
#the variable 'var1' mentioned here holds Integer Value, by default 0
var1=IntVar()
#this creates Checkbutton widget and uses place() method.
Checkbutton(root,text="Accept Terms and Condition", variable=var1).place(x=230,y=330)


#this creates button for submitting the details provides by the user
Button(root, text='Submit' , width=20,bg="black",fg='white',font=("bold",10)).place(x=70,y=380)

#this will run the mainloop.
root.mainloop()