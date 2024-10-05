from tkinter import *
from tkinter import messagebox


root=Tk()
root.configure(bg="#e7e7fb")
root.title("pickaboo shop")
root.geometry("500x750")
root.resizable(width=False,height=False)
root.wm_iconbitmap("pickaboo logo.ico")

def gotobeginning():
    pass
def showabout():
    messagebox.showinfo(title="about pickaboo",message="hello dear\nthis app made by just two person so feel free to tell us if it has any problem:)\nand this is just a demo version of the final app\nhave fun and enjoy it")
                        
menubar=Menu(root)
root.config(menu=menubar)
mainmenu=Menu(menubar)
menubar.add_cascade(label="main",menu=mainmenu)
mainmenu.add_command(command=gotobeginning)
mainmenu.add_separator()
infosmenu=Menu(menubar)
menubar.add_cascade(label="infos",menu=infosmenu)
infosmenu.add_command(label="about",command=showabout)

pic1=PhotoImage(file="mpillow.png")
pic1_lbl=Label(root,image=pic1 , borderwidth=0)
pic1_lbl.place(height=140,width=135,x=22,y=25)
pic1_info=Label(root,text="pillow",bg="#e7e7fb")
pic1_info.place(height=20,width=35,x=23,y=170)
pic1_info=Label(root,text="15$",bg="#e7e7fb")
pic1_info.place(height=20,width=30,x=70,y=170)

pic2=PhotoImage(file="mperfume.png")
pic2_lbl=Label(root,image=pic2 , borderwidth=0)
pic2_lbl.place(height=140,width=135,x=177,y=25)
pic2_info=Label(root,text="perfume",bg="#e7e7fb")
pic2_info.place(height=20,width=45,x=180,y=170)
pic2_info=Label(root,text="150$",bg="#e7e7fb")
pic2_info.place(height=20,width=30,x=230,y=170)

pic3=PhotoImage(file="mrefrigerator.png")
pic3_lbl=Label(root,image=pic3 , borderwidth=0)
pic3_lbl.place(height=140,width=135,x=332,y=25)
pic3_info=Label(root,text="refrigerator",bg="#e7e7fb")
pic3_info.place(height=20,width=80,x=325,y=170)
pic3_info=Label(root,text="220$",bg="#e7e7fb")
pic3_info.place(height=20,width=35,x=399,y=170)

pic4=PhotoImage(file="mcamera.png")
pic4_lbl=Label(root,image=pic4 , borderwidth=0)
pic4_lbl.place(height=140,width=135,x=22,y=215)
pic4_info=Label(root,text="camera",bg="#e7e7fb")
pic4_info.place(height=20,width=40,x=25,y=360)
pic4_info=Label(root,text="50$",bg="#e7e7fb")
pic4_info.place(height=20,width=35,x=80,y=360)


pic5=PhotoImage(file="mcandle.png")
pic5_lbl=Label(root,image=pic5 , borderwidth=0)
pic5_lbl.place(height=140,width=135,x=177,y=215)
pic5_info=Label(root,text="candle",bg="#e7e7fb")
pic5_info.place(height=20,width=35,x=177,y=360)
pic5_info=Label(root,text="20$",bg="#e7e7fb")
pic5_info.place(height=20,width=35,x=230,y=360)


pic6=PhotoImage(file="mclock.png")
pic6_lbl=Label(root,image=pic6 , borderwidth=0)
pic6_lbl.place(height=140,width=135,x=332,y=215)
pic6_info=Label(root,text="clock",bg="#e7e7fb")
pic6_info.place(height=20,width=35,x=332,y=360)
pic6_info=Label(root,text="60$",bg="#e7e7fb")
pic6_info.place(height=20,width=35,x=390,y=360)


pic7=PhotoImage(file="mcooler.png")
pic7_lbl=Label(root,image=pic7 , borderwidth=0)
pic7_lbl.place(height=140,width=135,x=22,y=405)
pic7_info=Label(root,text="cooler",bg="#e7e7fb")
pic7_info.place(height=20,width=35,x=25,y=550)
pic7_info=Label(root,text="70$",bg="#e7e7fb")
pic7_info.place(height=20,width=35,x=80,y=550)


pic8=PhotoImage(file="mhead phone.png")
pic8_lbl=Label(root,image=pic8 , borderwidth=0)
pic8_lbl.place(height=140,width=135,x=177,y=405)
pic8_info=Label(root,text="head phone",bg="#e7e7fb")
pic8_info.place(height=20,width=65,x=180,y=550)
pic8_info=Label(root,text="550$",bg="#e7e7fb")
pic8_info.place(height=20,width=35,x=245,y=550)


pic9=PhotoImage(file="mmirror.png")
pic9_lbl=Label(root,image=pic9 , borderwidth=0)
pic9_lbl.place(height=140,width=135,x=332,y=405)
pic9_info=Label(root,text="mirror",bg="#e7e7fb")
pic9_info.place(height=20,width=35,x=335,y=550)
pic9_info=Label(root,text="40$",bg="#e7e7fb")
pic9_info.place(height=20,width=35,x=385,y=550)


intsef=IntVar
spnnum1=Spinbox(root,from_=0,to=999,textvariable=intsef)
spnnum1.place(width=30,height=22,x=125,y=170)
spnnum2=Spinbox(root,from_=0,to=999,textvariable=intsef)
spnnum2.place(width=30,height=22,x=280,y=170)
spnnum3=Spinbox(root,from_=0,to=999,textvariable=intsef)
spnnum3.place(width=30,height=22,x=435,y=170)
spnnum4=Spinbox(root,from_=0,to=999,textvariable=intsef)
spnnum4.place(width=30,height=22,x=125,y=360)
spnnum5=Spinbox(root,from_=0,to=999,textvariable=intsef)
spnnum5.place(width=30,height=22,x=280,y=360)
spnnum6=Spinbox(root,from_=0,to=999,textvariable=intsef)
spnnum6.place(width=30,height=22,x=435,y=360)
spnnum7=Spinbox(root,from_=0,to=999,textvariable=intsef)
spnnum7.place(width=30,height=22,x=125,y=550)
spnnum8=Spinbox(root,from_=0,to=999,textvariable=intsef)
spnnum8.place(width=30,height=22,x=280,y=550)
spnnum9=Spinbox(root,from_=0,to=999,textvariable=intsef)
spnnum9.place(width=30,height=22,x=435,y=550)

def button_clicked():
    pillow_total=int(spnnum1.get())*15
    perfume_total=int(spnnum2.get())*150
    refrigerator_total=int(spnnum3.get())*220
    camera_total=int(spnnum4.get())*50
    candle_total=int(spnnum5.get())*20
    clock_total=int(spnnum6.get())*60
    cooler_total=int(spnnum7.get())*70
    headphone_total=int(spnnum8.get())*550
    mirror_total=int(spnnum9.get())*40
    total_bills=pillow_total+perfume_total+refrigerator_total+camera_total+candle_total+clock_total+cooler_total+headphone_total+mirror_total
    show_bills=Label(text=f"all of your things cost {total_bills} dollars")
    show_bills.place(x=160,y=640)
    
end_sefaresh=Button(text="total order",command=button_clicked)
end_sefaresh.place(height=30,width=90,x=200,y=590)

root.mainloop()