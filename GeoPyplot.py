import tkinter as tk
import GPAPI as API

# GUI
root = tk.Tk()
root.title('GeoPyplot')
w = API.getScreenWidthPadded(root, 0.7)
h = API.getScreenHeightPadded(root, 0.6)
resolution = w + 'x' + h

# set resolution of window
root.geometry(resolution)

# coordinates
point1 = tk.StringVar()
point2 = tk.StringVar()
point3 = tk.StringVar()


# submit button press reaction
def submit():
    p1 = point1.get()
    p2 = point2.get()
    p3 = point3.get()
    API.run(p1, p2, p3)


# labels
point1_label = tk.Label(root, text=' GPS Point 1: ', font=('Helvetica', 16, 'bold'))
point2_label = tk.Label(root, text=' GPS Point 2: ', font=('Helvetica', 16, 'bold'))
point3_label = tk.Label(root, text=' GPS Point 3: ', font=('Helvetica', 16, 'bold'))

# textboxes
point1_entry = tk.Entry(root, width=40, justify='center', textvariable=point1, font=('Helvetica', 16, 'normal'))
point2_entry = tk.Entry(root, width=40, justify='center', textvariable=point2, font=('Helvetica', 16, 'normal'))
point3_entry = tk.Entry(root, width=40, justify='center', textvariable=point3, font=('Helvetica', 16, 'normal'))

# submit button
sub_btn = tk.Button(root, width=15, text='Submit', font=('Helvetica', 16, 'bold'), command=submit)

# component placements
point1_label.grid(row=0, column=0, padx=10, pady=5)
point2_label.grid(row=1, column=0, padx=10, pady=5)
point3_label.grid(row=2, column=0, padx=10, pady=5)
point1_entry.grid(row=0, column=2, padx=10, pady=5)
point2_entry.grid(row=1, column=2, padx=10, pady=5)
point3_entry.grid(row=2, column=2, padx=10, pady=5)
sub_btn.grid(row=3, column=2)

# window loop
root.mainloop()
# END GUI
