# import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# import Image module
from PIL import Image, ImageTk

window = Tk()
window.geometry("800x500")
window.title("Image Splitter")

def browseClick():
    global img, img_path
    img_path = filedialog.askopenfilename(initialdir="./assets", title="Select an image to spit",filetypes=(("png files","*.png"),("All files","*")))
    path_lbl = Label(window, text=img_path)
    path_lbl.grid(row=0,column=0)
    
    img = ImageTk.PhotoImage(Image.open(img_path))
    img_lbl=Label(window,image=img)
    img_lbl.grid(row=1,column=0)

def split_image():
    try:
        rows=rows_var.get()
        cols=cols_var.get()
    
        # open image file
        with Image.open(img_path) as image:
            # get image height and width
            w, h = image.size
            # calculating crop box size in x and y directions
            crop_size_x=w/cols
            crop_size_y=w/rows
            # iterating to move cropping box over the image
            for i in range(0,rows): # first over rows
                for j in range(0,cols): # then over columns
                    # crop image based on box coordinates
                    cropped=image.crop(box=(j*crop_size_x,i*crop_size_y,j*crop_size_x+crop_size_x,i*crop_size_y+crop_size_y))
                    # save image to output directory
                    cropped.save("./output/cropped"+str(i)+str(j)+".png")
            messagebox.showinfo(title="Done", message="Splitting comleted sucessfully")

    except TclError as e:
        messagebox.showerror(title="Error", message=e)
    except ZeroDivisionError as zeroDiv:
         messagebox.showerror(title="Error", message="rows and columns number cannot be zero 0")

browse_btn = Button(window, text="Browse images", command=browseClick)
browse_btn.grid(row=0,column=1)

# initializing IntVars
rows_var=IntVar()
cols_var=IntVar()

# creating a label for rows
rows_label = Label(window, text = 'Rows', font=('calibre',10, 'bold'))
  
# creating a entry for rows
rows_entry = Entry(window,textvariable = rows_var, font=('calibre',10,'normal'))
  
# creating a label for cols
cols_label = Label(window, text = 'Columns', font = ('calibre',10,'bold'))
  
# creating a entry for cols
cols_entry=Entry(window, textvariable = cols_var, font = ('calibre',10,'normal'))
  
# creating a button using the widget
# Button that will call the submit function
split_btn=Button(window,text = 'Split and Save', command = split_image)

rows_label.grid(row=1,column=1)
rows_entry.grid(row=1,column=2)
cols_label.grid(row=2,column=1)
cols_entry.grid(row=2,column=2)
split_btn.grid(row=3,column=1)

window.mainloop()