import tkinter as tk, threading
from tkinter.constants import BOTH
from playsound import playsound
import statistics
import glob
from tkinter import font
from PIL import Image, ImageTk
import imageio


liste=[]
image_list=[]

for sound in glob.glob("SFX/*.mp3"):
    popo = "SFX/2.mp3"
    mmedmod ="SFX/3.mp3"
    twoptwo = "SFX/1.mp3"
    Yay = "SFX/4.mp3"
    trum = "SFX/5.mp3"
for images in glob.glob("IMG/*.*"):
    image_list.append(images)
print(image_list)
class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        img = tk.PhotoImage("photo", file="Calculator.gif")
        self.title("Grade Calculator")
        self.geometry('900x600')
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky='nsew')
        self.frames = {}
        self.resizable(width=False, height=False)
        self.configure(bg="gray")
        self.tk.call("wm", "iconphoto", self._w, img)

        for F in (Begin, Data, Mean, Median, Mode, Range):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.showframe(Begin)

    def showframe(self, pgname):
        frame = self.frames[pgname]
        frame.tkraise()

    
        
class Begin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="gray", width=1100, height=720)
        img = ImageTk.PhotoImage(Image.open(image_list[0]))

        share_tech_title = font.Font(
            family="Share Tech",
            size=20,
            weight="bold",
            underline=1
        )
        global share_tech_reg
        share_tech_reg = font.Font(
            family="Share Tech",
            size = 11,
        )

        global share_tech_sub
        share_tech_sub = font.Font(
            family="Share Tech",
            size=15,
            underline=1
        )

        global share_tech_response
        share_tech_response = font.Font(
            family="Share Tech",
            weight="bold",
            underline=2
        )

        

        lbl = tk.Label(self, text="Welcome to the Grade Calculator!",font=share_tech_title, fg="red", bg="gray")
        lbl.pack()

        btn = tk.Button(self,text="Data", font= share_tech_reg,fg="blue",bg="yellow",padx=30,pady=5,width=1,command=lambda:[controller.showframe(Data), self.pop(), self.frames()])
        btn.pack()

        btn1 = tk.Button(self,text="Mean",font= share_tech_reg,fg="blue",bg="yellow",padx=30, pady=5,width=1,command=lambda:[controller.showframe(Mean),self.pop()])
        btn1.pack()

        btn2 = tk.Button(self,text="Median",font= share_tech_reg,fg="blue",bg="yellow",padx=30, pady=5, width=1, command=lambda:[controller.showframe(Median), self.pop()])
        btn2.pack()

        btn3 = tk.Button(self,text="Mode",font= share_tech_reg,fg="blue",bg="yellow",padx=30, pady=5, width=1, command=lambda:[controller.showframe(Mode), self.pop()])
        btn3.pack()

        btn4 = tk.Button(self,text="Range",font= share_tech_reg,fg="blue",bg="yellow",padx=30, pady=5, width=1, command=lambda:[controller.showframe(Range), self.pop()])
        btn4.pack()

        lblimg = tk.Label(self, image=img)
        lblimg.image = img
        lblimg.pack(side="bottom")

        




    def pop(self):
        playsound(popo, False)

    
    
    

 

    
class Data(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="Gray")

        self.lbl = tk.Label(self, text="Please enter the numbers you would like to use for the mean, median, mode, and range", font=share_tech_sub, fg="red", bg="Gray")
        self.lbl.pack()

        self.ent = tk.Entry(self)
        self.ent.pack()

        self.btn = tk.Button(self, text='Submit',font=share_tech_reg, fg="blue",bg="yellow",padx=30, pady=10, width=1, command=lambda:[self.onbut(), self.yay()])
        self.btn.pack()

        self.btn1 = tk.Button(self, text='Back', font=share_tech_reg, fg="blue",bg="yellow",padx=30, pady=10, width=1,command=lambda:[controller.showframe(Begin), self.clear(), self.org(), self.sound()])
        self.btn1.pack()

    def onbut(self):
        store = self.ent.get()
        global liste
        liste = store.split()
        global lbl
        lbl = tk.Label(self, text="", font=share_tech_response, bg="yellow", fg="red", pady=10, padx=30)
        try:
            liste = [int(i) for i in liste]
            lbl["text"] = f"Submitted!"
            lbl.pack()
            self.ent.delete(0, 'end')
            print(liste)
        except ValueError or NameError:
            lbl["text"] = f"Enter a valid number!"
            lbl.pack()
            self.ent.delete(0, 'end') 
        return liste

    def clear(self):
        try:
           lbl.forget()
           self.ent.delete(0, "end")
        except NameError:
            pass
           

    def org(self):
        def partition(ar, fi, la):
            piv = ar[la]
            ind = fi - 1
            for i in range(fi, la):
                if ar[i] <= piv:
                    ind += 1
                    ar[ind], ar[i] = ar[i], ar[ind]
            ar[ind + 1], ar[la] = ar[la], ar[ind + 1]
            return ind + 1
        def quicksort(ar, fi, la):
            if fi < la:
                pi = partition(ar, fi, la)
                quicksort(ar, fi, pi - 1)
                quicksort(ar, pi + 1, la)
        quicksort(liste, 0, len(liste) - 1)
        print(liste)

    def sound(self):
        playsound(mmedmod, False)
    
    def yay(self):
        playsound(Yay, False)
    
class Mean(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.configure(bg="Gray")

        self.btn = tk.Button(self, text="Back", font=share_tech_reg, fg="blue",bg="yellow",padx=30, pady=10, width=1, command=lambda:[controller.showframe(Begin), self.clear(), self.back()])
        self.btn.pack()

        self.btn2 = tk.Button(self, text="Press me to show the mean!", bg="yellow", fg="blue", font=share_tech_reg, padx=30, pady=10, command=lambda:self.mean())
        self.btn2.pack()

    def mean(self):
        global lbl
        global lbl2
        try:
            c = sum(liste)/len(liste)
            lbl = tk.Label(self, text="", bg="yellow", fg="blue", font=share_tech_response, padx=30, pady=10)
            lbl["text"] = f'The mean is {c}'
            lbl.pack()
        except NameError and ZeroDivisionError:
            playsound(twoptwo, False)
            lbl2 = tk.Label(self, text="You must enter a list before proceeding!",font=share_tech_response, bg="yellow", fg="blue")
            lbl2.pack()



    def clear(self):
        try:
            lbl.forget()
            lbl2.forget()
        except NameError:
            pass

    def back(self):
        playsound(mmedmod, False)


class Median(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.btn = tk.Button(self, text="Back", command=lambda:[controller.showframe(Begin), self.forget(), self.back()])
        self.btn.pack()

        self.btn2 = tk.Button(self, text="Click me to show the median!",command=lambda:[self.median(), self.sound2()])
        self.btn2.pack()

    def median(self):
        global lbl1
        lbl1 = tk.Label(self, text="")
        try:
            if len(liste) % 2 != 0:
                c = liste[len(liste)//2]
                lbl1["text"] = f"Your median is {c}."
                lbl1.pack()
            else:
                mid1 = liste[len(liste)//2]
                mid2 = liste[(len(liste)//2) + 1]
                r_mid = (mid1 + mid2) / 2
                lbl1["text"] = f"Your median is {r_mid}."
                lbl1.pack()
        except IndexError:
            lbl1 = tk.Label(self, text="You must enter a list before proceeding!")
            lbl1.pack()

    def sound2(self):
        playsound(twoptwo, False)
    
    def forget(self):
        lbl1.forget()

    def back(self):
        playsound(mmedmod, False)



class Mode(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        btn = tk.Button(self, text="Back", command=lambda:[controller.showframe(Begin), self.forgett(), self.back()])
        btn.pack()

        btn2 = tk.Button(self, text="Press me to show your mode!", command=lambda:self.mode())
        btn2.pack()

    def mode(self):
        try:
            mod = str(statistics.mode(liste))
            global lbl
            lbl = tk.Label(self, text="")
            lbl["text"] = f"The mode is {mod}."
            lbl.pack()
            playsound(twoptwo, False)
        except statistics.StatisticsError:
            lbl = tk.Label(self, text="You must enter a list before proceeding!")
            lbl.pack()

    def forgett(self):
        lbl.forget()
    
    def back(self):
        playsound(mmedmod, False)
    


class Range(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        btn = tk.Button(self, text="Back", command=lambda:[controller.showframe(Begin), self.back_sound()])
        btn.pack()

        btn2 = tk.Button(self, text="Enter me to see the range!", command=lambda:[self.range(), self.sound()])
        btn2.pack()

    def range(self):
        ran = max(liste) - min(liste)
        lbl = tk.Label(self, text="")
        lbl["text"] = f"The range is {ran}."
        lbl.pack()
    
    def sound(self):
        playsound(twoptwo, False)
    
    def back_sound(self):
        playsound(mmedmod, False)

        
    

       
if __name__ == '__main__':
    app = window()
    app.mainloop()