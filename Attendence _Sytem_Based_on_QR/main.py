import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\shwetank\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
import tkinter as tk
from tkinter import filedialog
import cv2
from pyzbar.pyzbar import decode
from tkinter.ttk import *
from time import strftime
import csv
import datetime as dt
import tkinter.ttk as ttk
import pandas as pd

# Main Window ----------------------------------------

my_w = tk.Tk()
my_w.geometry("750x400")  # Size of the window
my_w.title('Student Attendence System')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Student Attendence System',bg='#E6E6FA',width=35,font=('Calibri',30,'bold'))
l1.place(x=10,y=60)
my_w.configure(background='#E6E6FA')

# -----------------------------------------------
# Buttons ---------------------------------------

options_list = ["Maths", "Python", "Operating System", "Microprocessor"]
value_inside = tk.StringVar(my_w)
value_inside.set("Select an Option")
question_menu = tk.OptionMenu(my_w,value_inside, *options_list)
question_menu.place(x=320,y=170)

b0 = tk.Button(my_w, text='Capture Photo',font=('Calibri',12),relief='flat', fg="white", bg="#9D33E2",width=20,command = lambda:Capture())
b0.place(x=210,y=130)
b1 = tk.Button(my_w, text='Upload File',font=('Calibri',12),width=20,relief='flat', fg="white", bg="#9D33E2",command = lambda:upload_file())
b1.place(x=390,y=130)
linetext = tk.Label(my_w,text='____________________________________________',font=('Calibri',10,'bold'),background='#E6E6FA',)
linetext.place(x=240,y=250)
b3 = tk.Button(my_w, text='Show Attendence',font=('Calibri',12),relief='flat', fg="white", bg="#9D33E2",
   width=20,command = lambda:ShowAttendence())
b3.place(x=300,y=300)

# -----------------------------------------------------
# Menu Bar --------------------------------------------

def Exit():
    my_w.destroy()

menubar = tk.Menu(my_w, relief='ridge')
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Help' )
filemenu.add_command(label='Exit' ,font=('roboto', 10, ' bold '),command=lambda : Exit())
menubar.add_cascade(label='Help', font=('roboto', 29, ' bold '), menu=filemenu)

# -----------------------------------------------------
# DateTime --------------------------------------------

def clock():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, clock)

lbl = Label(my_w, font=('calibri', 12, 'bold'),foreground='black',background='#E6E6FA')
lbl.place(x=345,y=10)
clock()

date1 = dt.datetime.now()
label = Label(my_w, text=f"{date1:%A, %B %d, %Y}", font=('Calibri', 12,'bold'), foreground='black',background='#E6E6FA',)
label.place(x=300,y=30)

# -------------------------------------------------------
# Functions ---------------------------------------------

def upload_file():
    global img
    f_types = [('JPEG Files', '*.jpeg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    # img = ImageTk.PhotoImage(file=filename)
    # img = Image.open(filename)
    # text = tess.image_to_string(filename)
    # print(text)
    # imageObject = Image.open(filename)
    # hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
    img = cv2.imread(filename)
    # code = decode(img)
    for barcode in decode(img):
        # print(barcode.data)
        global Data
        Data = barcode.data.decode('utf-8')
        print(Data)


def Capture():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)

    while True:
        success, img = cap.read()
        for barcode in decode(img):
            # print(barcode.data)
            # global Data
            Data = barcode.data.decode('utf-8')
            print(Data)

            if value_inside.get() == 'Python':
                fields = ['Data', 'Date', 'Subject']
                rows = [[Data, date1.date(), value_inside.get()]]
                # rows = [str(Data), str(date1)]
                filename = "Attendence/records_python_" + str(date1.date()) + ".csv"
                with open(filename, 'a+', newline="") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    # csvwriter.writerow(fields)
                    csvwriter.writerows(rows)
                csvfile.close()
            elif value_inside.get() == 'Microprocessor':
                fields = ['Data', 'Date', 'Subject']
                rows = [[Data, date1.date(), value_inside.get()]]
                # rows = [str(Data), str(date1)]
                filename = "Attendence/records_micro_" + str(date1.date()) + ".csv"
                with open(filename, 'a+', newline="") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    # csvwriter.writerow(fields)
                    csvwriter.writerows(rows)
            elif value_inside.get() == 'Maths':
                fields = ['Data', 'Date', 'Subject']
                rows = [[Data, date1.date(), value_inside.get()]]
                # rows = [str(Data), str(date1)]
                filename = "Attendence/records_maths_" + str(date1.date()) + ".csv"
                with open(filename, 'a+', newline="") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    # csvwriter.writerow(fields)
                    csvwriter.writerows(rows)
            elif value_inside.get() == 'Operating System':
                fields = ['Data', 'Date', 'Subject']
                rows = [[Data, date1.date(), value_inside.get()]]
                # rows = [str(Data), str(date1)]
                filename = "Attendence/records_os_" + str(date1.date()) + ".csv"
                with open(filename, 'a+', newline="") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    # csvwriter.writerow(fields)
                    csvwriter.writerows(rows)
        cv2.imshow("window", img)
        if cv2.waitKey(2000) & 0xFF == ord("q"):
            break
    cv2.destroyAllWindows()


def ShowAttendence():
    root = tk.Tk()
    root.geometry("400x500")
    root.title('Student Attendence')
    root.configure(background='#E6E6FA')

    lbz = tk.Label(root, text='Read File & create DataFrame',
                   width=30, font=my_font1,background='#E6E6FA')
    lbz.grid(row=1, column=1)
    b6 = tk.Button(root, text='Browse File',font=('Calibri',12),width=20,relief='flat', fg="white", bg="#9D33E2", command=lambda: upload_file())
    b6.grid(row=4, column=1, pady=5)
    lb2 = tk.Label(root, width=40, text='', bg='#E6E6FA')
    lb2.grid(row=3, column=1, padx=5)
    l3 = []  # List to hold headers of the Treeview

    def upload_file():
        global df, l3
        f_types = [('CSV files', "*.csv"), ('All', "*.*")]
        file = filedialog.askopenfilename(filetypes=f_types)
        lbz.config(text="")  # display the path
        df = pd.read_csv(file)  # create DataFrame
        l3 = list(df)  # List of column names as header
        str1 = "Number of Student Present :" + str(df.shape[0]+1)
        # print(str1)
        lb2.config(text=str1,font=('Calibri',12))  # add to Text widget
        trv_refresh()

    def trv_refresh():  # Refresh the Treeview to reflect changes
        global df, trv, l3
        r_set = df.to_numpy().tolist()  # create list of list using rows
        trv = ttk.Treeview(root, selectmode='browse', height=10,
                           show='headings', columns=l3)
        trv.grid(row=4, column=1, columnspan=3, padx=10, pady=20)

        for i in l3:
            trv.column(i, width=90, anchor='c')
            trv.heading(i, text=str(i))
        for dt in r_set:
            v = [r for r in dt]
            trv.insert("", 'end', iid=v[0], values=v)

# -------------------------------------------------

my_w.configure(menu=menubar)
my_w.mainloop()

