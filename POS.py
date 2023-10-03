from tkinter import*
import math,random,os
from tkinter import messagebox
class POS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Point Of Sale")
        bg_color="grey"
        title=Label(self.root,text="Point Of Sale",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #=====Variables====
        #=====Basics===
        self.Veggie_Delite=IntVar()
        self.Roast_Beef=IntVar()
        self.Subway_Club=IntVar()
        self.Roasted_Chicken=IntVar()
        self.Zinger_Burger=IntVar()
        #======Drinks===
        self.Black_Coffee=IntVar()
        self.Soft_Drink=IntVar()
        self.Nestle_Juice=IntVar()
        self.Cappuccino=IntVar()
        self.Mineral_Water=IntVar()
        #=======Cookies=====
        self.Choclate_Chip=IntVar()
        self.Double_Choclate=IntVar()
        self.Macadamia_Nuts=IntVar()
        #=====Favourites=====
        self.Chicken_Fajita=IntVar()
        self.BBQ_Chicken=IntVar()
        #======Customer====
        self.Customer_Name=StringVar()
        self.Order_No=IntVar()
        x=random.randint(1,9999)
        self.Order_No.set(str(x))
        #=====Billing=====
        self.basic_items=IntVar()
        self.drinks_items=IntVar()
        self.Fav_items=IntVar()
        self.cookies_items=IntVar()

    
        #FrameTitle

        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Name",font=("times new roman",15,"bold"),fg="Gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        customerlable=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        customertext=Entry(F1,width=22,textvariable=self.Customer_Name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        billlabel=Label(F1,text="Order No",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        billtext=Entry(F1,width=22,textvariable=self.Order_No,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        #======BASICS ITEMS=====
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Basics",font=("times new roman",15,"bold"),fg="Gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=340)

        
        B1_lbl=Label(F2,text="Veggie Delite",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        B1_txt=Entry(F2,width=10,textvariable=self.Veggie_Delite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        B2_lbl=Label(F2,text="Roast Beef",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        B2_txt=Entry(F2,width=10,textvariable=self.Roast_Beef,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        B3_lbl=Label(F2,text="Subway Club",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        B3_txt=Entry(F2,width=10,textvariable=self.Subway_Club,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        B4_lbl=Label(F2,text="Roasted Chicken",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        B4_txt=Entry(F2,width=10,textvariable=self.Roasted_Chicken,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        B5_lbl=Label(F2,text="Zinger Burger",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        b5_txt=Entry(F2,width=10,textvariable=self.Zinger_Burger,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        

        #======DRINKS=====
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Drinks",font=("times new roman",15,"bold"),fg="Gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=340)

        
        D1_lbl=Label(F3,text="Black Coffee",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        D1_txt=Entry(F3,width=10,textvariable=self.Black_Coffee,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        D2_lbl=Label(F3,text="Soft Drinks",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=1,column=0,padx=10,pady=10,)
        D2_txt=Entry(F3,width=10,textvariable=self.Soft_Drink,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        D3_lbl=Label(F3,text="Nestle Juice",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=2,column=0,padx=10,pady=10,)
        D3_txt=Entry(F3,width=10,textvariable=self.Nestle_Juice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)


        D4_lbl=Label(F3,text="Cappucino",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=3,column=0,padx=10,pady=10,)
        D4_txt=Entry(F3,width=10,textvariable=self.Cappuccino,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        D5_lbl=Label(F3,text="Mineral Water",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=4,column=0,padx=10,pady=10,)
        D5_txt=Entry(F3,width=10,textvariable=self.Mineral_Water,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

         #======Cookies=====
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cookies",font=("times new roman",15,"bold"),fg="Gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=320)

        
        Stk_chese_lbl=Label(F4,text="Choclate Chip",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Stk_chese_txt=Entry(F4,width=10,textvariable=self.Choclate_Chip,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Rst_beef_lbl=Label(F4,text="Double Choclate",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=1,column=0,padx=10,pady=10,)
        Rst_beef_txt=Entry(F4,width=10,textvariable=self.Double_Choclate,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        sbwy_club_lbl=Label(F4,text="Macadamia Nuts",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=2,column=0,padx=10,pady=10,)
        sbwy_club_txt=Entry(F4,width=10,textvariable=self.Macadamia_Nuts,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

         #======Favourites=====
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Favourites",font=("times new roman",15,"bold"),fg="Gold",bg=bg_color)
        F2.place(x=670,y=370,width=325,height=150)

        
        Fav1_lbl=Label(F2,text="Chicken Fajita",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Fav1_txt=Entry(F2,width=10,textvariable=self.Chicken_Fajita,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Fav2_lbl=Label(F2,text="BBQ Chicken",font=("times new roman",16,"bold"),bg=bg_color,fg="blue").grid(row=1,column=0,padx=10,pady=10,)
        Fav2_txt=Entry(F2,width=10,textvariable=self.BBQ_Chicken,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        #=======BILL AREA======
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=365,height=340)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=====ButtonFrame===

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="Gold",bg=bg_color)
        F6.place(x=0,y=520,relwidth=1,height=220)
        m1_lbl=Label(F6,text="TPrice of Basics Items",bg=bg_color,fg="blue",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.basic_items,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="TPrice of Drinks",bg=bg_color,fg="blue",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.drinks_items,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="TPrice of Cookies",bg=bg_color,fg="blue",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cookies_items,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        m4_lbl=Label(F6,text="TPrice of Fav Items",bg=bg_color,fg="blue",font=("times new roman",14,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky="w")
        m4_txt=Entry(F6,width=18,textvariable=self.Fav_items,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=1)
        
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=650,width=790,height=180)

        total_btn=Button(btn_F,command=self.Total,text="Sum",bg="Cadetblue",fg="white",pady=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5,)
        Gbill_btn=Button(btn_F,command=self.bill_area,text="Total Bill",bg="Cadetblue",fg="white",pady=15,width=11,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5,)
        Exit_btn=Button(btn_F,command=self.Exit_app,text="Exit",bg="Cadetblue",fg="white",pady=15,width=11,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5,)
        self.welcome_bill()
###Functions
    def Total(self):
        self.total_basic_items=float(
                                 (self.Veggie_Delite.get()*250)+
                                 (self.Roasted_Chicken.get()*500)+
                                 (self.Zinger_Burger.get()*350)+
                                 (self.Subway_Club.get()*200)+
                                 (self.Roast_Beef.get()*400)
                                 )
        self.basic_items.set("Rs. "+str(self.total_basic_items))

        self.total_drinks_items=float(
                                 (self.Black_Coffee.get()*150)+
                                 (self.Soft_Drink.get()*120)+
                                 (self.Nestle_Juice.get()*100)+
                                 (self.Cappuccino.get()*200)+
                                 (self.Mineral_Water.get()*40)
                                 )
        self.drinks_items.set("Rs. "+str(self.total_drinks_items))

        self.total_cookies_items=float(
                                 (self.Choclate_Chip.get()*150)+
                                 (self.Double_Choclate.get()*120)+
                                 (self.Macadamia_Nuts.get()*100)
                                    )
        self.cookies_items.set("Rs. "+str(self.total_cookies_items))

        self.total_Fav_items=float(
                                 (self.Chicken_Fajita.get()*150)+
                                 (self.BBQ_Chicken.get()*120)
        )
        self.Fav_items.set("Rs. "+str(self.total_Fav_items))

        self.Total_Bill=float(self.total_basic_items+
                                self.total_cookies_items+
                                self.total_Fav_items+
                                self.total_drinks_items)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome To Food Fussion\n")
        self.txtarea.insert(END,f"\n ORDER NO : {self.Order_No.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.Customer_Name.get()}")
        self.txtarea.insert(END,f"\n========================================")
        self.txtarea.insert(END,f"\n Food\t\t\tQTY")        
        self.txtarea.insert(END,f"\n========================================")

        

    def bill_area(self):
        self.welcome_bill()
        if self.Veggie_Delite.get()!=0:
            self.txtarea.insert(END,f"Veggie Delite\t\t\t{self.Veggie_Delite.get()}")
        if self.Chicken_Fajita.get()!=0:
            self.txtarea.insert(END,f"\nChicken Fajita\t\t\t{self.Chicken_Fajita.get()}") 
        if self.Cappuccino.get()!=0:
            self.txtarea.insert(END,f"\nCappuccino\t\t\t{self.Cappuccino.get()}") 
        if self.Choclate_Chip.get()!=0:
            self.txtarea.insert(END,f"\nChoclate Chip\t\t\t{self.Choclate_Chip.get()}")  
        if self.BBQ_Chicken.get()!=0:
            self.txtarea.insert(END,f"\nBBQ Chicken\t\t\t{self.BBQ_Chicken.get()}") 
        if self.Black_Coffee.get()!=0:
            self.txtarea.insert(END,f"\nBlack Coffee\t\t\t{self.Black_Coffee.get()}")  
        if self.Mineral_Water.get()!=0:
            self.txtarea.insert(END,f"\nMineral Water\t\t\t{self.Mineral_Water.get()}")  
        if self.Double_Choclate.get()!=0:
            self.txtarea.insert(END,f"\nDouble Choclate\t\t\t{self.Double_Choclate.get()}")  
        if self.Roast_Beef.get()!=0:
            self.txtarea.insert(END,f"\nRoast Beef\t\t\t{self.Roast_Beef.get()}") 
        if self.Roasted_Chicken.get()!=0:
            self.txtarea.insert(END,f"\nRoasted Chicken\t\t\t{self.Roasted_Chicken.get()}") 
        if self.Nestle_Juice.get()!=0:
            self.txtarea.insert(END,f"\nNestle Juice\t\t\t{self.Nestle_Juice.get()}") 
        if self.Subway_Club.get()!=0:
            self.txtarea.insert(END,f"\nSubway Club\t\t\t{self.Subway_Club.get()}") 
        if self.Soft_Drink.get()!=0:
            self.txtarea.insert(END,f"\nSoft Drink\t\t\t{self.Soft_Drink.get()}") 
        if self.Macadamia_Nuts.get()!=0:
            self.txtarea.insert(END,f"\nMacadamia Nuts\t\t\t{self.Macadamia_Nuts.get()}")   
        if self.Zinger_Burger.get()!=0:
            self.txtarea.insert(END,f"\nZinger Burger\t\t\t{self.Zinger_Burger.get()}") 

        self.txtarea.insert(END,f"\n========================================")

        self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {str(self.Total_Bill)}")

        self.txtarea.insert(END,f"\n========================================")

        self.txtarea.insert(END,f"\t\tThanks For Visiting! \n")
        self.txtarea.insert(END,f"\t  Enjoy The Meal :)")

    def Exit_app(self):
        op=messagebox.askyesno("Do you Really Want to EXIT?")
        if op>0:
            self.root.destroy()

root=Tk()
obj = POS(root)
root.mainloop()
