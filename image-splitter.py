# import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# import Image module
from PIL import Image, ImageTk

# setup tkinter instance called window
window = Tk()
window.geometry("800x500")
window.title("Image Splitter")

# Method to be excuted when browse button is clicked
def browseClick():
    # set img and img_path as global variables to be used outside this method
    global img, img_path
    
    # open dialog to choose image file. it returns a string of the absolute path of the selected file
    img_path = filedialog.askopenfilename(initialdir="./assets", title="Select an image to spit",filetypes=(("png files","*.png"),("All files","*")))
    # display the selected path in the window
    path_lbl = Label(window, text=img_path)
    path_lbl.grid(row=0, column=0)
    
    # prepare image object and show it in the window
    img = ImageTk.PhotoImage(Image.open(img_path))
    img_lbl = Label(window, image=img)
    img_lbl.grid(row=1, column=0)

# Method to be excuted when split and save button is clicked 
def splitImage():
    
    try:
        # gets the number of columns and rows from the entry fields
        rows = int(rows_entry.get()) # will raise ValueError if float or string are entered
        cols = int(cols_entry.get())

        # check if inputs are valide, if not raises ValueError
        if (rows<1) or (cols<1):
            raise ValueError

        # open image file
        with Image.open(img_path) as image:
            # get image height and width
            w, h = image.size
            # calculating crop box size in x and y directions
            crop_size_x=w/cols
            crop_size_y=h/rows
            # iterating to move cropping box over the image
            for i in range(0,rows): # first over rows
                for j in range(0,cols): # then over columns
                    # crop image based on box coordinates
                    cropped=image.crop(box=(j*crop_size_x,i*crop_size_y,j*crop_size_x+crop_size_x,i*crop_size_y+crop_size_y))
                    # save image to output directory
                    cropped.save("./output/cropped"+str(i)+str(j)+".png")
            # show a message that Splitting is completed
            messagebox.showinfo(title="Done", message="Splitting comleted sucessfully")

    except ValueError:
        # If the user enters 0 instead of a positive integer an error msg will appear
         messagebox.showerror(title="Error", message="rows and columns number should be integers greater than 0")

# create Browse button with link to method browseClick
browse_btn = Button(window, text="Browse images", command=browseClick)
browse_btn.grid(row=0,column=1)

# creating a label for rows
rows_label = Label(window, text = 'Rows', font=('calibre',10, 'bold'))
  
# creating an entry for rows
rows_entry = Entry(window, font=('calibre',10,'normal'))
  
# creating a label for cols
cols_label = Label(window, text = 'Columns', font = ('calibre',10,'bold'))
  
# creating an entry for cols
cols_entry=Entry(window, font = ('calibre',10,'normal'))
  
# creating a button using the widget
# Button that will call the splitImage method
split_btn=Button(window,text = 'Split and Save', command = splitImage)

# placing widgets on the grid
rows_label.grid(row=1,column=1)
rows_entry.grid(row=1,column=2)
cols_label.grid(row=2,column=1)
cols_entry.grid(row=2,column=2)
split_btn.grid(row=3,column=1)

# Tkinter mainloop 
window.mainloop()