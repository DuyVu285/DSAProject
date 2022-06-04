from ctypes import util
from re import L
from tkinter import *
from cell import Cell
import settings
import utils

# Create game window
root = Tk()
root.configure(bg = 'black')
root.geometry(f'{settings.width}x{settings.height}')
root.title('Minesweeper Game')
root.resizable(True, True)


# Divide the game window into sections
top_frame = Frame(
    root,
    bg = 'black', 
    width = settings.width,
    height = utils.height_prct(25)
)
top_frame.place(x=0, y=0)

# Game title
game_title = Label(
    top_frame,
    bg ='black',
    fg ='white',
    text ='Minesweeper Game',
    font =('', 48)
)

game_title.place(
    x=utils.width_prct(25), y= 0
    )

left_frame = Frame(
    root,
    bg = 'black', 
    width = utils.width_prct(25),
    height = utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg = 'black', 
    width = utils.width_prct(75),
    height = utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25),y=utils.height_prct(25))

# Designing the button (click on the cells)
btn1 = Button(
    center_frame,
    bg = 'blue',
    text = 'First Button'
)
btn1.place(x=0,y=0)

# The cell
for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
        
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

# Randomize the mines
Cell.randomize_mines()

# Run the window
root.mainloop()

