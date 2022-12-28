#!/usr/bin/env python3
#Import Tkinter for GUI
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from tkinter import *
#Import PIL for loading images
from PIL import Image, ImageTk
#import pandas for handing Excel files
import pandas as pd
from pandas.core.base import DataError
#import system for alerts and message boxes
import sys
if sys.version_info.major >= 3:
    from tkinter import messagebox
else:
    import tkMessageBox as messagebox
#create class for the gui
class frameIt(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        #configure the GUI
        global my_label
        global title
        self.master.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)
        #Create a text entry box for the user submission
        entry = Entry(self, width=100, bg='light blue', borderwidth=1, justify="center", font=('Arial 24'))
        entry.pack(padx=5, pady=5)
        entry.insert(0, '')
        #create control buttons
        closeButton = Button(self, text="Close", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK",command=lambda entry=entry: submit(entry))
        okButton.pack(side=RIGHT)
        self.bind('<Return>', lambda entry=entry: submit(entry))
        my_label = Label()
        my_label.pack()
        title = Label()
        title.pack()

def errorCallBack(tmp):
   messagebox.showerror( "Item is not found", "Item not found '"+tmp+"'")

#Using EAN barcode to lookup product sku, which is also the photo file name
def submit(entry):
    print("Searching...")
    tmpcode = entry.get()
    entry.delete(0, 'end')
    #find the user entry in the Dataframe
    try:
        new_df = df[df['Barcode'].astype(str).str.contains(tmpcode,case=False, na=False)][['SKU']].reset_index(drop = True)
        a = new_df.iloc[0]
        titlename = df[df['Barcode'].astype(str).str.contains(tmpcode,case=False, na=False)][['Ttitle']].reset_index(drop = True)
        t = titlename.iloc[0]
    except:
        print("Item not found '"+ tmpcode +"'")
        errorCallBack(tmpcode)
    #if the barcode is matched then grab the product data and format it
    if a['SKU'] != 0:
        value = a['SKU']
        valueb = t['Ttitle'].split('(')
        brand = valueb[0].split(" ")
        brand = brand[0].title()
        tmp = value.split("-")
        #Capture Adidas Exceptions - Adidas uses different SKU structure
        if brand == "Adidas":
            newvalue = tmp[0]
            print(newvalue)
        else:
            newvalue = tmp[0] +"-"+ tmp[1]
        sizescolour = valueb[1].split(",")
        sizes= sizescolour[0].split(" ")
        colour = sizescolour[1]
        valuec = valueb[0] +'\n' + colour.replace(")","")
        valuec = valuec + '\n' + sizes[0] + " "+ sizes[1] + " | "+ sizes[2] + " " + sizes[3] + " | " + sizes[4] + " " + sizes[5]
        #build the photo path
        link = r'D:\NewShared\Product_Images\{}\{}_2D_0001.jpg'.format(newvalue, newvalue)
        img = Image.open(link)
        img = img.resize((1000,500), resample=0)
        #load the image
        my_img = ImageTk.PhotoImage(img)
        #set the image label to the product title
        my_label.configure(image=my_img)
        my_label.image = my_img
        title.configure(text=valuec.title(), font=("Arial", 18))
        print("Done!")
    else:
        print("Not found!")


def main():
    global df
    print("Loading data...")
    #open the data file containing product barcodes
    file = 'C:/python/showlookup/data.xlsx'
    df = pd.read_excel(file, sheet_name = 'Sheet1')
    #set the GUI window
    root = Tk()
    root.geometry("300x200+300+300")
    app = frameIt()
    root.mainloop()

if __name__ == '__main__':
    main()
