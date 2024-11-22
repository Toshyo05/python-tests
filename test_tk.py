import tkinter as tk

#-------variables---------------------------------------------------------------------------

bg_color = "#FFFFFF"
btn_color = "#FE9063"
txt_color = "#FDF0E7"

#-------tk_setup----------------------------------------------------------------------------

#creation dune nouvelle instance de tkinter
root = tk.Tk()

#configuration de la fenetre
root.title("test_tkinter")
root.configure(background=bg_color)

#-------fonctions---------------------------------------------------------------------------

def on_btn_click():
    print("Button clicked")

#-------elements----------------------------------------------------------------------------

button = tk.Button(
                   root,
                   text="click-me",
                   command=on_btn_click,
                   bg=btn_color,
                   fg=txt_color,
                   borderwidth=0,
                   font=("Courier", 16)
                  )

#-------placement des elements--------------------------------------------------------------

button.pack(padx=20, pady=20)

#-------boucle principale-------------------------------------------------------------------

root.mainloop()