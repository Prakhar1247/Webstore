from Tkinter import *
root=Tk()
from tkMessageBox import *
root.geometry('725x620+15+15')
def enter(root1):
    root1.destroy()
    root=Tk()
    import sqlite3
    con=sqlite3.Connection('Laptop_Store')
    cur=con.cursor()
    #cur.execute('create table laptops(brand varchar(20),model_no varchar(20),processor varchar(40),operating_system varchar(40),hard_disk varchar(20),ram varchar(20),display varchar(45),integrated_graphics varchar(40),dedicated_graphics varchar(40),warranty_period varchar(20),price varchar(15))')
    #cur.execute("insert into laptops values('Dell','3458','5th Gen Dual Core','DOS','500GB','4GB','14.1 WLED HD','Intel HD','No Dedicated Graphics','1 Year','20,990')")
    #con.commit()
    #cur.execute("insert into laptops values('Dell','3542','4th Gen Core i3','DOS','500GB','4GB','15.6 WLED HD','Intel HD 4400','2GB NVIDIA','1 Year','30,990')")
    #con.commit()
    #cur.execute("insert into laptops values('Dell','3558','5th Gen Core i3','DOS','1TB','4GB','15.6 WLED HD','Intel HD 4400','No Dedicated Graphics','1 Year','28,990')")
    #con.commit()
    #cur.execute("insert into laptops values('Dell','5558','5th Gen Core i5','Windows 8.1','1TB','4GB','15.6 WLED HD','Intel HD 5500','2GB NVIDIA','1 Year','45,490')")
    #con.commit()
    #cur.execute("insert into laptops values('Dell','Touch 7548','5th Gen Core i5','Windows 8.1','1TB','8GB','15.6 LED HD','Intel HD 5500','4GB AMD Radeon','1 Year','68,990')")
    #con.commit()
    #cur.execute("insert into laptops values('Lenovo','G50-80','5th Gen Core i3','DOS','1TB','4GB','15.6 WLED HD','Intel HD 5500','2GB ATI Radeon','1 Year','32,490')")
    #con.commit()
    #cur.execute("insert into laptops values('Lenovo','G50-70','5th Gen Core i3','Windows 8.1','500GB','4GB','15.6 WLED HD','Intel HD 5500','2GB ATI Radeon','1 Year','34,990')")
    #con.commit()
    #cur.execute("insert into laptops values('Lenovo','Yoga 500','5th Gen Core i7','Windows 10','500GB+8GB SSHD','4GB','14 Full HD Touch','Intel HD 5500','2GB NVIDIA Geforce','1 Year','55,990')")
    #con.commit()
    #cur.execute("insert into laptops values('Lenovo','IP500','5th Gen Core i5','Windows 10','1TB','8GB','15.6 Full HD','Intel HD 5500','4GB NVIDIA Geforce','1 Year','61,990')")
    #con.commit()
    #cur.execute("insert into laptops values('Lenovo','G50','AMD Dual Core','Windows 8.1','500GB','4GB','15.6 WLED HD','Intel HD 4400','No Dedicated Graphics','1 Year','21,490')")
    #con.commit()
    #cur.execute("insert into laptops values('HP','15 AC030TX','5th Gen Core i3','Windows 8.1','1TB','4GB','15.6 HP LED','Intel HD 5500','2GB AMD Radeon','1 Year','38,190')")
    #con.commit()
    #cur.execute("insert into laptops values('HP','15 AC155TX','5th Gen Core i3','Windows 10','1TB','8GB','15.6 HP LED','Intel HD 5500','2GB AMD Radeon','1 Year','40,190')")
    #con.commit()
    #cur.execute("insert into laptops values('HP','15 AC649TU','5th Gen Pentium Quad Core','DOS','500GB','4GB','15.6 HP LED','Intel HD 5500','No Dedicated Graphics','1 Year','22,990')")
    #con.commit()
    #cur.execute("insert into laptops values('HP','PAV15 AU003TX','6th Gen Core i5','Windows 10','1TB','8GB','15.6 HP HD LED','Intel HD 5500','2GB NVIDIA','1 Year','56,190')")
    #con.commit()
    #cur.execute("insert into laptops values('HP','Pavillion11 S102TU','6th Gen Core i3','Windows 10','1TB','4GB','13.3 Full HD Touch','Intel HD Card 520','No Dedicated Graphics','1 Year','47,390')")
    #con.commit()
    #cur.execute("insert into laptops values('ASUS','A553SA','5th Gen Pentium Quad Core ','DOS','500GB','4GB','15.6 WLED HD','Intel HD 5500','No Dedicated Graphics','1 Year','20,990')")
    #con.commit()
    #cur.execute("insert into laptops values('ASUS','A555LA','5th Gen Core i3','Windows 10','1TB','4GB','15.6 WLED HD','Intel HD 5500','No Dedicated Graphics','1 Year','20,990')")
    #con.commit()
    #cur.execute("insert into laptops values('ASUS','A555LF','5th Gen Core i3','Windows 10','1TB','4GB','15.6 WLED HD','Intel HD 5500','2GB NVIDIA','1 Year','20,990')")
    #con.commit()
    #cur.execute("insert into laptops values('ASUS','GL552JX','5th Gen Core i7','Windows 10','1TB','8GB','15.6 WLED HD','Intel HD 5500','8GB NVIDIA','1 Year','20,990')")
    #con.commit()
    #cur.execute("insert into laptops values('ASUS','R558UF','6th Gen Core i5','Windows 10','1TB','4GB','15.6 WLED HD','Intel HD 5500','2GB NVIDIA','1 Year','20,990')")
    #con.commit()
    root.geometry("940x500+40+40")

    #cur.execute('create table details1(First_Name varchar(20),Last_Name varchar(20),address varchar(40),city varchar(20),mobile_no number,email varchar(20),model_no varchar(20),serial_no varchar(15))')

    def view_model1(root1):
        root1.destroy()
        root=Tk()
        root.geometry("1025x675+20+20")
        Label(root,text='Models:',font='Ariel 20 bold',bg='orange').grid(row=0,column=2)
        Label(root,text=' ').grid(row=2,column=1)
        Label(root,text='G50-80',font='Ariel 10 bold').grid(row=3,column=1)
        Button(root,text='View Specifications',command=lambda:view1()).grid(row=2,column=2,sticky=W)
        d11=PhotoImage(file="rsz_g50-80.gif")
        Label(root,image=d11).grid(row=2,column=1)
        def view1():
            cur.execute("select * from laptops where model_no='G50-80'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("laptops","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text='G50-70',font='Ariel 10 bold').grid(row=3,column=5)
        Button(root,text='View Specifications',command=lambda:view2()).grid(row=2,column=6)
        d12=PhotoImage(file="rsz_3g50-70.gif")
        Label(root,image=d12).grid(row=2,column=5)
        def view2():
            cur.execute("select * from laptops where model_no='G50-70'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("laptops","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text='Yoga 500',font='Ariel 10 bold').grid(row=7,column=1)
        Button(root,text='View Specifications',command=lambda:view3()).grid(row=6,column=2,sticky=W)
        d13=PhotoImage(file="rsz_yoga_500.gif")
        Label(root,image=d13).grid(row=6,column=1)
        def view3():
            cur.execute("select * from laptops where model_no='Yoga 500'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=6,column=1)
        Label(root,text='IP500',font='Ariel 10 bold').grid(row=7,column=5)
        Button(root,text='View Specifications',command=lambda:view4()).grid(row=6,column=6)
        d14=PhotoImage(file="rsz_ip500.gif")
        Label(root,image=d14).grid(row=6,column=5)
        def view4():
            cur.execute("select * from laptops where model_no='IP500'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11) 
        Label(root,text='G50',font='Ariel 10 bold').grid(row=5,column=2)
        Button(root,text='View Specifications',command=lambda:view5()).grid(row=4,column=2,sticky=E)
        d15=PhotoImage(file="rsz_1g50.gif")
        Label(root,image=d15).grid(row=4,column=2)
        def view5():
            cur.execute("select * from laptops where model_no='G50'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11) 
        Label(root,text=' ').grid(row=8,column=0)
        Label(root,text='If you want to Purchase click on Purchase->',compound='center',font='Ariel 15 bold').grid(row=10,column=2)
        Label(root,text=' ').grid(row=11,column=0)
        Label(root,text=' ').grid(row=9,column=0)
        Button(root,text='Purchase',command=lambda:fill()).grid(row=12,column=2)
        Button(root,text='<-',font='Ariel 15 bold',command=lambda:brands(root)).grid(row=0,column=0,sticky=W)
        root.mainloop()
        
    def view_model2(root1):
        root1.destroy()
        root=Tk()
        root.geometry("1025x675+10+10")
        Label(root,text='Models:',font='Ariel 20 bold',bg='orange').grid(row=0,column=2)
        Label(root,text=' ').grid(row=2,column=1)
        Label(root,text='3458',font='Ariel 10 bold').grid(row=3,column=1)
        Button(root,text='View Specifications',command=lambda:view6()).grid(row=2,column=2,sticky=W)
        d16=PhotoImage(file="rsz_1rsz_dell-inspiron-7447-141.gif")
        Label(root,image=d16).grid(row=2,column=1)
        def view6():
            cur.execute("select * from laptops where model_no='3458'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text='3542',font='Ariel 10 bold').grid(row=3,column=5)
        Button(root,text='View Specifications',command=lambda:view7()).grid(row=2,column=6)
        d17=PhotoImage(file="rsz_1dell_3542.gif")
        Label(root,image=d17).grid(row=2,column=5)
        def view7():
            cur.execute("select * from laptops where model_no='3542'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=5,column=1)
        Label(root,text='3558',font='Ariel 10 bold').grid(row=7,column=1)
        Button(root,text='View Specifications',command=lambda:view8()).grid(row=6,column=2,sticky=W)
        d18=PhotoImage(file="rsz_dell_3558.gif")
        Label(root,image=d18).grid(row=6,column=1)
        def view8():
            cur.execute("select * from laptops where model_no='3558'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand:  "+info1+"\nModel: "+info2+"\nProcessor:  "+info3+"\nOperating System:  "+info4+"\nHard Disk:  "+info5+"\nRam:  "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=6,column=1)
        Label(root,text='5558',font='Ariel 10 bold').grid(row=7,column=5)
        Button(root,text='View Specifications',command=lambda:view9()).grid(row=6,column=6)
        d19=PhotoImage(file="rsz_dell_5558.gif")
        Label(root,image=d19).grid(row=6,column=5)
        def view9():
            cur.execute("select * from laptops where model_no='5558'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text='Touch 7548',font='Ariel 10 bold').grid(row=5,column=2)
        Button(root,text='View Specifications',command=lambda:view10()).grid(row=4,column=2,sticky=E)
        d20=PhotoImage(file="rsz_touch_7548.gif")
        Label(root,image=d20).grid(row=4,column=2)
        def view10():
            cur.execute("select * from laptops where model_no='Touch 7548'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=9,column=0)
        Label(root,text='If you want to Purchase click on Purchase->',compound='center',font='Ariel 15 bold').grid(row=8,column=2)
        Button(root,text='Purchase',command=lambda:fill()).grid(row=10,column=2)
        Button(root,text='<-',font='Ariel 15 bold',command=lambda:brands(root)).grid(row=0,column=0,sticky=W)
        root.mainloop()
    
    def view_model3(root1):
        root1.destroy()
        root=Tk()
        root.geometry("940x675+10+10")
        Label(root,text='Models:',font='Ariel 20 bold',bg='orange').grid(row=0,column=2)
        Label(root,text=' ').grid(row=2,column=1)
        Label(root,text='15 AC030TX',font='Ariel 10 bold').grid(row=3,column=2)
        Button(root,text='View Specifications',command=lambda:view11()).grid(row=2,column=2,sticky=W)
        d21=PhotoImage(file="rsz_rsz_aco30tx.gif")
        Label(root,image=d21).grid(row=2,column=1)
        def view11():
            cur.execute("select * from laptops where model_no='15 AC030TX'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text='15 AC155TX',font='Ariel 10 bold').grid(row=3,column=5)
        Button(root,text='View Specifications',command=lambda:view12()).grid(row=2,column=6)
        d22=PhotoImage(file="rsz_rsz_ac155tx.gif")
        Label(root,image=d22).grid(row=2,column=5)
        def view12():
            cur.execute("select * from laptops where model_no='15 AC155TX'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("laptops","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=5,column=1)
        Label(root,text='15 AC649TU',font='Ariel 10 bold').grid(row=7,column=1)
        Button(root,text='View Specifications',command=lambda:view13()).grid(row=6,column=2,sticky=W)
        d23=PhotoImage(file="rsz_rsz_ac649tu.gif")
        Label(root,image=d23).grid(row=6,column=1)
        def view13():
            cur.execute("select * from laptops where model_no='15 AC649TU'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=6,column=1)
        Label(root,text='PAV15 AU003TX',font='Ariel 10 bold').grid(row=7,column=5)
        Button(root,text='View Specifications',command=lambda:view14()).grid(row=6,column=6)
        d24=PhotoImage(file="rsz_rsz_au003tx.gif")
        Label(root,image=d24).grid(row=6,column=5)
        def view14():
            cur.execute("select * from laptops where model_no='PAV15 AU003TX'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=9,column=1)
        Label(root,text='Pavillion11 S102TU',font='Ariel 10 bold').grid(row=5,column=2)
        Button(root,text='View Specifications',command=lambda:view15()).grid(row=4,column=2,sticky=E)
        d25=PhotoImage(file="rsz_rsz_u005tu.gif")
        Label(root,image=d25).grid(row=4,column=2)
        def view15():
            cur.execute("select * from laptops where model_no='Pavillion11 S102TU'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text='If you want to Purchase click on Purchase->',compound='center',font='Ariel 15 bold').grid(row=8,column=2)
        Label(root,text=' ').grid(row=9,column=0)
        Button(root,text='Purchase',command=lambda:fill()).grid(row=10,column=2)
        Button(root,text='<-',font='Ariel 15 bold',command=lambda:brands(root)).grid(row=0,column=0,sticky=W)
        root.mainloop()
    
    def view_model4(root1):
        root1.destroy()
        root=Tk()
        root.geometry("940x675+10+10")
        Label(root,text='Models:',font='Ariel 20 bold',compound='center',bg='orange').grid(row=0,column=2)
        Label(root,text=' ').grid(row=2,column=1)
        Label(root,text='A553SA',font='Ariel 10 bold').grid(row=3,column=1)
        Button(root,text='View Specifications',command=lambda:view16()).grid(row=2,column=2,sticky=W)
        d26=PhotoImage(file="rsz_a553sa.gif")
        Label(root,image=d26).grid(row=2,column=1)
        def view16():
            cur.execute("select * from laptops where model_no='A553SA'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text='A555LA',font='Ariel 10 bold').grid(row=3,column=5)
        Button(root,text='View Specifications',command=lambda:view17()).grid(row=2,column=6)
        d27=PhotoImage(file="rsz_rsz_a555la.gif")
        Label(root,image=d27).grid(row=2,column=5)
        def view17():
            cur.execute("select * from laptops where model_no='A555LA'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text='A555LF',font='Ariel 10 bold').grid(row=7,column=1)
        Label(root,text=' ').grid(row=5,column=1)
        Button(root,text='View Specifications',command=lambda:view18()).grid(row=6,column=2,sticky=W)
        d28=PhotoImage(file="rsz_rsz_a555lf.gif")
        Label(root,image=d28).grid(row=6,column=1)
        def view18():
            cur.execute("select * from laptops where model_no='A555LF'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=6,column=1)
        Label(root,text='GL552JX',font='Ariel 10 bold').grid(row=7,column=5)
        Button(root,text='View Specifications',command=lambda:view19()).grid(row=6,column=6)
        d29=PhotoImage(file="rsz_gl552jx.gif")
        Label(root,image=d29).grid(row=6,column=5)
        def view19():
            cur.execute("select * from laptops where model_no='GL552JX'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=9,column=1)
        Label(root,text='R558UF',font='Ariel 10 bold').grid(row=5,column=2)
        Button(root,text='View Specifications',command=lambda:view20()).grid(row=4,column=2,sticky=E)
        d30=PhotoImage(file="rsz_r558uf.gif")
        Label(root,image=d30).grid(row=4,column=2)
        def view20():
            cur.execute("select * from laptops where model_no='R558UF'")
            a=cur.fetchall()
            info1=a[0][0]
            info2=a[0][1]
            info3=a[0][2]
            info4=a[0][3]
            info5=a[0][4]
            info6=a[0][5]
            info7=a[0][6]
            info8=a[0][7]
            info9=a[0][8]
            info10=a[0][9]
            info11=a[0][10]
            showinfo("Laptop Specifications","Brand: "+info1+"\nModel: "+info2+"\nProcessor: "+info3+"\nOperating System: "+info4+"\nHard Disk: "+info5+"\nRam: "+info6+"\nDisplay: "+info7+"\nIntegrated Graphics:  "+info8+"\nDedicated Graphics:  "+info9+"\nWarranty Period:  "+info10+"\nPrice: "+info11)
        Label(root,text=' ').grid(row=11,column=1)
        Label(root,text='If you want to Purchase click on Purchase->',compound='center',font='Ariel 15 bold').grid(row=8,column=2)
        Label(root,text=' ').grid(row=9,column=0)
        Button(root,text='Purchase',command=lambda:fill()).grid(row=10,column=2)
        Button(root,text='<-',font='Ariel 15 bold',command=lambda:brands(root)).grid(row=0,column=0,sticky=W)
        root.mainloop()
    
    def deals1():
        root=Tk()
        root.geometry("400x185+250+250")
        Label(root,text='Various Deals:',font='Ariel 20 bold',bg='red',fg='white').grid(row=0,column=0)
        Label(root,text='1.You would be provided a laptop bag along with laptop.',font='Ariel 10 bold').grid(row=2,column=0,sticky=W)
        Label(root,text='2.Get laptops at best prices.',font='Ariel 10 bold').grid(row=4,column=0,sticky=W)
        Label(root,text='3.2 Years additional warranty.',font='Ariel 10 bold').grid(row=6,column=0,sticky=W)
        Label(root,text='4.Accidental Damage Protection.',font='Ariel 10 bold').grid(row=8,column=0,sticky=W)
        Label(root,text=' ').grid(row=9,column=1)
        Button(root,text='Ok',command=root.destroy).grid(row=10,column=0)
    
    def fill():
        root=Tk()
        root.geometry("470x380+250+250")
        Label(root,text='Enter your Details:',font='Ariel 20 bold',fg='yellow',bg='blue').grid(row=0,column=0)
        Label(root,text=' ').grid(row=1,column=0)
        Label(root,text='Enter your First Name:').grid(row=2,column=0)
        r1=Entry(root)
        r1.grid(row=2,column=1,sticky=W)
        Label(root,text='Enter your Last Name:').grid(row=3,column=0)
        r2=Entry(root)
        r2.grid(row=3,column=1,sticky=W)
        Label(root,text='Enter your Address:').grid(row=4,column=0)
        r3=Entry(root)
        r3.grid(row=4,column=1,sticky=W)
        Label(root,text='Enter your City:').grid(row=5,column=0)
        r4=Entry(root)
        r4.grid(row=5,column=1,sticky=W)
        Label(root,text='Enter your Mobile Number:').grid(row=6,column=0)
        r5=Entry(root)
        r5.grid(row=6,column=1,sticky=W)
        Label(root,text='Enter your Email ID:').grid(row=7,column=0)
        r6=Entry(root)
        r6.grid(row=7,column=1,sticky=W)
        Label(root,text='Enter the Model you want to Buy:').grid(row=8,column=0)
        r7=Entry(root)
        r7.grid(row=8,column=1,sticky=W)
        Label(root,text='Enter a Serial Number as a Password:').grid(row=9,column=0)
        r8=Entry(root,show=".")
        r8.grid(row=9,column=1,sticky=W)        
        Label(root,text=' ').grid(row=12,column=0)
        Button(root,text='Confirm',command=lambda:proceed()).grid(row=17,column=0,sticky=E)

        def proceed():
           x2=(r1.get(),r2.get(),r3.get(),r4.get(),r5.get(),r6.get(),r7.get(),r8.get())
           cur.execute("insert into details1 values(?,?,?,?,?,?,?,?)",x2)
           con.commit()
           Button(root,text='  Proceed for Payment  ',command=lambda:buy(root)).grid(row=17,column=0,sticky=E) 
            
        def buy(root1):
           root1.destroy()
           root=Tk()
           root.geometry("550x200+250+250")
           v5=IntVar(root)
           Label(root,text=' ',font='Arile 20 bold').grid(row=0,column=0,sticky=E)
           Label(root,text='Complete Your Payment Through',font='Ariel 20 bold').grid(row=0,column=1)
           Radiobutton(root,text='Credit Card',variable=v5,value=1).grid(row=2,column=1,sticky=W)
           Radiobutton(root,text='Online Banking',variable=v5,value=2).grid(row=2,column=1)
           Button(root,text='Buy',command=lambda:confirm1()).grid(row=7,column=1)

           def confirm1():
               if v5.get()==1:
                   Label(root,text='    Enter your Pin Number:  ',font='Ariel 15 bold',fg='blue').grid(row=4,column=1,sticky=W)
                   p1=Entry(root,show=".",font="Ariel 10 bold")
                   p1.grid(row=4,column=1,sticky=E)
                   Label(root,text=' ').grid(row=3,column=0)
                   Label(root,text=' ').grid(row=5,column=0)
                   Label(root,text=' ').grid(row=6,column=0)
                   Button(root,text='Buy',command=lambda:confirm(root)).grid(row=7,column=1)
               elif v5.get()==2:
                   Label(root,text='    Enter your Password:   ',font='Ariel 15 bold',fg='blue').grid(row=4,column=1,sticky=W)
                   p2=Entry(root,show=".",font="Ariel 10 bold")
                   p2.grid(row=4,column=1,sticky=E)
                   Label(root,text=' ').grid(row=3,column=0)
                   Label(root,text=' ').grid(row=5,column=0)
                   Label(root,text=' ').grid(row=6,column=0)
                   Button(root,text='Buy',command=lambda:confirm(root)).grid(row=7,column=1)
               else:
                   Label(root,text=' ').grid(row=15,column=0)
                   Label(root,text='Please Select medium of transaction',font='Ariel 10 bold',fg='red').grid(row=4,column=1,sticky=W)  
                   Button(root,text='Buy',command=lambda:confirm1()).grid(row=7,column=1)
               root.mainloop()

    def confirm(root1):
        root1.destroy()
        root=Tk()
        Label(root,text='*Transaction successfull.',font='Ariel 15 bold',fg='blue').grid(row=0,column=0)
        Label(root,text='*Your Laptop will be delivered soon.',font='Ariel 15 bold',fg='blue').grid(row=2,column=0)
        Label(root,text='*Thank You for purchasing from our store.',font='Ariel 15 bold',fg='blue').grid(row=4,column=0)
        Label(root,text='*Hope you will visit again.',font='Ariel 15 bold',fg='blue').grid(row=6,column=0)
        

    def contact_us():
        root=Tk()
        root.geometry("255x200+150+150")
        Label(root,text='Contact Details',font='Ariel 20 bold',bg='red',fg='white').grid(row=0,column=0)
        Label(root,text='1.Email Support',font='Ariel 10 bold',fg='blue',bg='white').grid(row=2,column=0,sticky=W)
        Label(root,text='* Email us at weblapy54@gmail.com ',font='Ariel 10 bold').grid(row=3,column=0)
        Label(root,text='2.Call Support ',font='Ariel 10 bold',fg='blue',bg='white').grid(row=5,column=0,sticky=W)
        Label(root,text='* Call us At 7712412455 ',font='Ariel 10 bold').grid(row=6,column=0,sticky=W)
        Label(root,text=' ').grid(row=7,column=1)
        Button(root,text='Ok',command=root.destroy).grid(row=8,column=0)

    def purchase_details():
        root=Tk()
        root.geometry("800x200+150+150")
        Label(root,text='Enter the details below to see purchase details:',font='Ariel 20 bold',bg='orange',fg='white').grid(row=0,column=0,sticky=W)
        Label(root,text=' ').grid(row=2,column=1)
        Label(root,text='Enter your Model Number:',font='Ariel 15 bold').grid(row=3,column=0,sticky=E)
        d1=Entry(root)
        d1.grid(row=3,column=1,sticky=W)
        Label(root,text='Enter your your Serial Number:',font='Ariel 15 bold').grid(row=4,column=0,sticky=E)
        d2=Entry(root,show='.')
        d2.grid(row=4,column=1,sticky=W)
        Label(root,text=' ').grid(row=7,column=1)
        Button(root,text='Show Details',command=lambda:details()).grid(row=8,column=0)
        Label(root,text=' ').grid(row=10,column=1)

        def details():
            x17=(d2.get(),d1.get())
            s1=d1.get()
            s2=d2.get()
            cur.execute("select First_Name,Last_Name from details1 where serial_no=(?) and model_no=(?)",x17)
            if s1=="" or s2=="":
                showerror("OOPs","Please fill all details")
            elif cur.fetchall()==[]: 
                showerror('OOPs','Please enter the correct details.')
            else:
                root=Tk()
                root.config(bg='yellow')
                x=(d2.get(),d1.get())
                x1=(d1.get())
                cur.execute("select First_Name,Last_Name from details1 where serial_no=(?) and model_no=(?)",x)
                dd=cur.fetchall()
                info=dd[0][0]
                info10=dd[0][1]
                Label(root,text='Name: '+str(info)+" "+str(info10),font='Ariel 15 bold',bg='yellow',fg='red').grid(row=0,column=0,sticky=W)
                cur.execute("select address from details1 where serial_no=(?) and model_no=(?)",x)
                dd1=cur.fetchall()
                info1=dd1[0][0]
                Label(root,text='Address: '+str(info1),font='Ariel 15 bold',bg='yellow',fg='red').grid(row=2,column=0,sticky=W)
                cur.execute("select city from details1 where serial_no=(?) and model_no=(?)",x)
                dd2=cur.fetchall()
                info2=dd2[0][0]
                Label(root,text='City: '+str(info2),font='Ariel 15 bold',bg='yellow',fg='red').grid(row=4,column=0,sticky=W)
                cur.execute("select mobile_no from details1 where serial_no=(?) and model_no=(?)",x)
                dd3=cur.fetchall()
                info3=dd3[0][0]
                Label(root,text='Mobile Number: '+str(info3),font='Ariel 15 bold',bg='yellow',fg='red').grid(row=6,column=0,sticky=W)
                cur.execute("select email from details1 where serial_no=(?) and model_no=(?)",x)
                dd4=cur.fetchall()
                info4=dd4[0][0]
                Label(root,text='Email Id: '+str(info4),font='Ariel 15 bold',bg='yellow',fg='red').grid(row=8,column=0,sticky=W)
                cur.execute("select model_no from details1 where serial_no=(?) and model_no=(?)",x)
                dd5=cur.fetchall()
                info5=dd5[0][0]
                Label(root,text='Model Number: '+str(info5),font='Ariel 15 bold',bg='yellow',fg='red').grid(row=10,column=0,sticky=W)
                cur.execute("select serial_no from details1 where serial_no=(?) and model_no=(?)",x)
                dd6=cur.fetchall()
                info6=dd6[0][0]
                Label(root,text='Serial Number: '+str(info6),font='Ariel 15 bold',bg='yellow',fg='red').grid(row=12,column=0,sticky=W)
                cur.execute("select warranty_period from laptops where model_no=(?)",(x1,))
                dd7=cur.fetchall()
                info7=dd7[0][0]
                Label(root,text='Warranty: '+str(info7)+' + 2 years additional',font='Ariel 15 bold',bg='yellow',fg='red').grid(row=14,column=0,sticky=W)
                cur.execute("select price from laptops where model_no=(?)",(x1,))
                dd8=cur.fetchall()
                info8=dd8[0][0]
                Label(root,text='Price: '+str(info8),font='Ariel 15 bold',bg='yellow',fg='red').grid(row=17,column=0,sticky=W)    

    def show():
        showerror("OOPs","Please fill all details")

    Label(root,text='LAPTOP STORE',font='Ariel 50 bold',fg='blue',compound='center').grid(row=0,column=0)

    def brands(root1):
        root1.destroy()
        root=Tk()
        root.geometry("1450x657+2+2")
        Label(root,text='Brands Available In Store:',font='Ariel 20 bold',bg='yellow',fg='black').grid(row=0,column=2)
        Label(root,text='Lenovo',font='Ariel 10 bold').grid(row=3,column=1)
        a1=PhotoImage(file="rsz_lenovo-z500-59-380463-core-i5-3rd-gen-6-gb-1-tb-windows-8-2-gb-59331-large-1 (1).gif")
        Label(root,image=a1).grid(row=2,column=1)
        Label(root,text='DELL',font='Ariel 10 bold').grid(row=3,column=5)
        a2=PhotoImage(file="rsz_dell-inspiron-13z-15z-laptop (1).gif")
        Label(root,image=a2).grid(row=2,column=5)
        Label(root,text='HP',font='Ariel 10 bold').grid(row=8,column=1)
        a4=PhotoImage(file="rsz_1xl-2016-hp-spectre-1.gif")
        Label(root,image=a4).grid(row=7,column=1)
        Label(root,text='ASUS',font='Ariel 10 bold').grid(row=8,column=5)
        a5=PhotoImage(file="rsz_asus_trasnformer_flip_book_tp550.gif")
        Label(root,image=a5).grid(row=7,column=5)
        Button(root,text='View Models',command=lambda:view_model1(root)).grid(row=2,column=2,sticky=W)
        Label(root,text=' ').grid(row=4,column=0)
        Label(root,text=' ').grid(row=5,column=2)
        Label(root,text=' ').grid(row=3,column=8)
        Label(root,text=' ').grid(row=7,column=8)
        Button(root,text='View Models',command=lambda:view_model2(root)).grid(row=2,column=7,sticky=W)
        Label(root,text=' ').grid(row=5,column=1)
        Button(root,text='View Models',command=lambda:view_model3(root)).grid(row=7,column=2,sticky=W)
        Label(root,text=' ').grid(row=7,column=1)
        Button(root,text='View Models',command=lambda:view_model4(root)).grid(row=7,column=7,sticky=W)
        Label(root,text=' ').grid(row=11,column=1)
        Button(root,text='<-',font='Ariel 15 bold',command=lambda:enter(root)).grid(row=0,column=0,sticky=W)
        root.mainloop()
    
    Button(root,text='Brands Available',command=lambda:brands(root)).grid(row=2,column=0,sticky=W)
    Button(root,text='Purchase Details',command=lambda:purchase_details()).grid(row=2,column=0)
    Label(root,text=' ').grid(row=4,column=0)
    Button(root,text='Contact Us',command=lambda:contact_us()).grid(row=5,column=0)
    Button(root,text='Deals',command=lambda:deals1()).grid(row=2,column=0,sticky=E)
    a=PhotoImage(file="dellskylakelaptopdesktop930x359.gif")
    Label(root,image=a).grid(row=6,column=0)
    root.mainloop()

dd12=PhotoImage(file="rsz_4laptops.gif")
Label(root,image=dd12).grid(row=1,column=0)
Label(root,text='Name-Prakhar Jaiswal',font='Ariel 25 bold').grid(row=2,column=0)
Label(root,text='Batch-B4',font='Ariel 25 bold').grid(row=4,column=0)
Label(root,text='Erollment No-151347',font='Ariel 25 bold').grid(row=6,column=0)
Label(root,text='Project on Webtore Management',font='Ariel 25 bold').grid(row=8,column=0)
Label(root,text=' ').grid(row=9,column=1)
Button(root,text='Enter Project',font='Ariel 15 bold',command=lambda:enter(root)).grid(row=10,column=0)
root.mainloop()
