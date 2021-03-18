import tkinter as tk

def getScreenWidthPadded(pad):
    return str(window.winfo_screenwidth() * pad).split('.')[0]

def getScreenHeightPadded(pad):
    return str(window.winfo_screenheight() * pad).split('.')[0]

if __name__ == '__main__':
    window = tk.Tk()
    window.title("GeoPyplot")
    w = getScreenWidthPadded(0.7)
    h = getScreenHeightPadded(0.6)
    resolution = w + 'x' + h
    # set resolution of window
    window.geometry(resolution)

    points_text_label = tk.Label(window,
                                 text = 'GPS Coordenates',
                                 fg = 'white',
                                 font=('Helvetica', 20)
                                 ).place(x = int(165),
                                         y = int(60)
                                         )

    points1_text_label = tk.Label(window,
                                 text='1',
                                 fg='white',
                                 font=('Helvetica', 20)
                                 ).place(x=int(20),
                                         y=int(102)
                                         )

    point1_text_box = tk.Text(window,
                              width = 30,
                              height = 1,
                              bg = 'white',
                              fg = 'black',
                              font = ('Helvetica' , 20)
                              ).place(x=int(40),
                                      y=int(100)
                                      )


    points2_text_label = tk.Label(window,
                                 text='2',
                                 fg='white',
                                 font=('Helvetica', 20)
                                 ).place(x=int(20),
                                         y=int(152)
                                         )


    point2_text_box = tk.Text(window,
                              width=30,
                              height=1,
                              bg='white',
                              fg='black',
                              font=('Helvetica', 20)
                              ).place(x=int(40),
                                      y=int(150)
                                      )


    points3_text_label = tk.Label(window,
                                 text='3',
                                 fg='white',
                                 font=('Helvetica', 20)
                                 ).place(x=int(20),
                                         y=int(202)
                                         )


    point3_text_box = tk.Text(window,
                              width=30,
                              height=1,
                              bg='white',
                              fg='black',
                              font=('Helvetica', 20)
                              ).place(x=int(40),
                                      y=int(200)
                                      )

    submit_button = tk.Button(window,
                              text = "  Submit  ",
                              bg='white',
                              fg='black',
                              font = ('Helvetica', 15)
                              ).place(x=200, y=250)

    window.mainloop()
