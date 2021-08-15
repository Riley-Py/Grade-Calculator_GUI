import tkinter as tk
from playsound import playsound
import statistics
import glob
from tkinter import font
from PIL import Image, ImageTk

liste=[]
image_list=[]

for sound in glob.glob("SFX/*.mp3"):
    popo = "SFX/2.mp3"
    mmedmod ="SFX/3.mp3"
    twoptwo = "SFX/1.mp3"
    Yay = "SFX/4.mp3"
    buzz = "SFX/5.mp3"

for images in glob.glob("IMG/*.*"):
    image_list.append(images)

print(image_list)

class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        img = tk.PhotoImage("photo", file="Calculator.gif")
        self.tk.call("wm", "iconphoto", self._w, img)
        self.title("Grade Calculator")
        self.geometry('950x720')
        self.frames = {}
        self.resizable(width=False, height=False)
        self.configure(bg="gray")
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky='nsew')
        
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
            underline=1
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

        btn = tk.Button(self,text="Data", font= share_tech_reg,fg="blue",bg="yellow",padx=30,pady=5,width=1,command=lambda:[controller.showframe(Data), self.pop()])
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
        global store
        global ent

        self.configure(bg="Gray", width=1100, height=720)
        
        lbl = tk.Label(self, text="Please enter the numbers you would like to use for the mean, median, mode, and range", font=share_tech_sub, fg="red", bg="Gray")
        lbl.pack()

        self.ent = tk.Entry(self)
        self.ent.pack()
        

        btn = tk.Button(self, text='Submit',font=share_tech_reg, fg="blue",bg="yellow",padx=30, pady=10, width=1, command=lambda:[self.onbut(), self.yay()])
        btn.pack()

        btn1 = tk.Button(self, text='Back', font=share_tech_reg, fg="blue",bg="yellow",padx=30, pady=10, width=1,command=lambda:[controller.showframe(Begin), self.clear(), self.org(), self.sound()])
        btn1.pack()

    def onbut(self):
        
        global liste
        global lbl
        global lbl_image
        store = self.ent.get()
        liste = store.split()
        lbl = tk.Label(self, text="Submitted!", font=share_tech_response, bg="yellow", fg="red", pady=10, padx=30)
        lbl_image = tk.Label(self)

        img = ImageTk.PhotoImage(Image.open(image_list[3]))
        lbl_image = tk.Label(self, image=img)
        lbl_image.image = img

        liste = [int(i) for i in liste]
        self.ent.delete(0, 'end')
        lbl_image.pack()
        lbl.pack()

        print(liste)

        return liste

    def clear(self):
        try:
           lbl.forget()
           lbl_image.forget()
           self.ent.delete(0, "end")
        except AttributeError:
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

        self.configure(width=950, height=720, bg="Gray")

        btn = tk.Button(self, text="Back", font=share_tech_reg, fg="blue",bg="yellow",padx=30, pady=10, width=1, command=lambda:[controller.showframe(Begin), self.clear(), self.back()])
        btn.pack()

        btn2 = tk.Button(self, text="Press me to show the mean!", bg="yellow", fg="blue", font=share_tech_reg, padx=30, pady=10, command=lambda:self.mean())
        btn2.pack()

    def mean(self):     
        try:
            c = sum(liste)/len(liste)

            global lbl_image2
            image = ImageTk.PhotoImage(Image.open(image_list[6]))
            lbl_image2 = tk.Label(self, image=image)
            lbl_image2.image = image
            lbl_image2.pack()

            global lbl
            lbl = tk.Label(self, text="", bg="yellow", fg="blue", font=share_tech_response, padx=30, pady=10)
            lbl["text"] = f'The mean is {c}'
            lbl.pack()
            playsound(twoptwo, False)

        except:

            image = ImageTk.PhotoImage(Image.open(image_list[1]))
            lbl_image2 = tk.Label(self, image=image)
            lbl_image2.image = image
            lbl_image2.pack()

            lbl = tk.Label(self, text="",bg="yellow", fg="blue", font=share_tech_response, padx=30, pady=10)
            lbl["text"] = f"You must enter a list before proceeding!"
            lbl.pack()

            playsound(buzz, False)


    def clear(self):
        try:
            lbl.forget()
            lbl_image2.forget()
        except:
            pass

    def back(self):
        playsound(mmedmod, False)

class Median(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.configure(width=950, height=720, bg="Gray")

        self.btn = tk.Button(self, text="Back",bg="yellow", fg="blue", font=share_tech_reg, padx=30, pady=10, command=lambda:[controller.showframe(Begin), self.forget(), self.back()])
        self.btn.pack()

        self.btn2 = tk.Button(self, text="Click me to show the median!", bg="yellow", fg="blue", font=share_tech_reg, padx=30, pady=10, command=lambda:self.median())
        self.btn2.pack()

    def median(self):
        global lbl1
        lbl1 = tk.Label(self, text="",bg="yellow", fg="blue", font=share_tech_response, padx=30, pady=10)
        image = ImageTk.PhotoImage(Image.open(image_list[5]))
        global lbl_image
        lbl_image = tk.Label(self, image=image)
        lbl_image.image = image
        try:
            if len(liste) % 2 != 0:
                c = liste[len(liste)//2]
                lbl1["text"] = f"Your median is {c}."

                lbl1.pack()
                lbl_image.pack()

                playsound(twoptwo, False)
            else:
                mid1 = liste[len(liste)//2]
                mid2 = liste[(len(liste)//2) - 1]
                r_mid = (mid1 + mid2) / 2
                lbl1["text"] = f"Your median is {r_mid}."

                lbl_image.pack()
                lbl1.pack()

                playsound(twoptwo, False)

        except IndexError or NameError:
            image = ImageTk.PhotoImage(Image.open(image_list[1]))
            lbl_image = tk.Label(self, image=image)
            lbl_image.image = image

            lbl1 = tk.Label(self, text="You must enter a list before proceeding!", bg="yellow", fg="blue", font=share_tech_response, padx=30, pady=10)

            lbl_image.pack()
            lbl1.pack()

            playsound(buzz, False)
    
    def forget(self):
        try:
            lbl1.forget()
            lbl_image.forget()
        except NameError:
            pass

    def back(self):
        playsound(mmedmod, False)


class Mode(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.configure(width=950, height=720, bg="Gray")

        btn = tk.Button(self, text="Back",bg="yellow", fg="blue", font=share_tech_reg, padx=30, pady=10,command=lambda:[controller.showframe(Begin), self.forgett(), self.back()])
        btn.pack()

        btn2 = tk.Button(self, text="Press me to show your mode!",bg="yellow", fg="blue", font=share_tech_reg, padx=30, pady=10, command=lambda:self.mode())
        btn2.pack()

    def mode(self):
        global lbl
        global lbl_image
        lbl = tk.Label(self, text="", bg="yellow", fg="blue", font=share_tech_response, padx=30, pady=10)
        lbl_image = tk.Label(self)
        try:
            

            mod = str(statistics.mode(liste))
            lbl["text"] = f"The mode is {mod}."
            
            playsound(twoptwo, False)

            img = ImageTk.PhotoImage(Image.open(image_list[2]))
            lbl_image = tk.Label(self, image=img)
            lbl_image.image = img

            lbl_image.pack()
            lbl.pack()
            
        except statistics.StatisticsError:

            img2 = ImageTk.PhotoImage(Image.open(image_list[1]))
            lbl_image = tk.Label(self, image=img2)
            lbl_image.image = img2
            lbl_image.pack()

            lbl["text"]= f"You must enter a list before proceeding!"
            lbl.pack()

            playsound(buzz, False)

    def forgett(self):
        lbl.forget()
        lbl_image.forget()
    
    def back(self):
        playsound(mmedmod, False)
    


class Range(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        self.configure(width=950, height=720, bg="gray")

        btn = tk.Button(self, text="Back",bg="yellow", fg="blue", font=share_tech_reg, padx=30, pady=10, command=lambda:[controller.showframe(Begin), self.forget_sound()])
        btn.pack()

        btn2 = tk.Button(self, text="Enter me to see the range!",bg="yellow", fg="blue", font=share_tech_reg, padx=30, pady=10,command=lambda:self.range())
        btn2.pack()

    def range(self):
        global lbl
        global lbl_image
        lbl = tk.Label(self, text="",bg="yellow", fg="blue", font=share_tech_response, padx=30, pady=10)
        lbl_image = tk.Label(self)
        try:

            ran = max(liste) - min(liste)
            img = ImageTk.PhotoImage(Image.open(image_list[4]))
            lbl_image = tk.Label(self, image=img)
            lbl_image.image = img

            lbl["text"] = f"The range is {ran}."

            lbl_image.pack()
            lbl.pack()

            playsound(twoptwo, False)
        except:

            img = ImageTk.PhotoImage(Image.open(image_list[1]))
            lbl_image = tk.Label(self, image=img)
            lbl_image.image = img
            lbl_image.pack()

            lbl["text"] = f"You must enter a list before proceeding!"
            lbl.pack()

            playsound(buzz, False)
    
    def forget_sound(self):
        try:
            lbl.forget()
            lbl_image.forget()
            playsound(mmedmod, False)
        except:
            pass

if __name__ == '__main__':
    app = window()
    app.mainloop()