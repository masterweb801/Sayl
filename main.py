from tkinter import Tk, END, Label, Button, Text, WORD, PhotoImage
from tkinter.ttk import Combobox, Scale
from tkinter.filedialog import asksaveasfilename
from pyttsx3 import init
from ctypes import windll

my_appid = 'logic_realm.sayl.1.1'
windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_appid)


def splash_screen():
    image = PhotoImage(file="icon-png.png")
    image = image.zoom(10)
    image = image.subsample(45)
    window.config(bg="#00a9fd")
    window.spl = Label(window, image=image, border=0)
    window.spl.pack(pady=20)
    window.spl.image = image
    window.st = Label(window, text="SAYL", font="Helvetica 30 bold",
                    border=0, bg="#00a9fd", fg="white")
    window.st.pack(pady=0)
    window.st2 = Label(window, text="By Logic Realm", font="Helvetica 14 bold italic", border=0, bg="#00a9fd", fg="white")
    window.st2.pack(pady=0)
    window.after(2100, dsps)


def dsps():
    window.spl.destroy()
    window.st.destroy()
    window.st2.destroy()
    gui()


def gui():
    window.config(bg="#f0f0f0")
    def on_enter(*args):
        status_label.config(text="Press Left Ctrl To Speak And Right To Save")

    def on_leave(*args):
        status_label.config(text="")

    def slup(value):
        engine.setProperty('rate', int(spr.get()))

    def save():
        text = text_entry.get(1.0, END)
        text_entry.delete(1.0, END)
        filename = asksaveasfilename(title="Save File", filetypes=[("MP3", "*.mp3")], initialfile="audio.mp3", confirmoverwrite=True)
        if gender.get() == "  Male":
            engine.setProperty('voice', voices[0].id)
        elif gender.get() == "  Female":
            engine.setProperty('voice', voices[1].id)
        engine.save_to_file(text, filename)
        engine.runAndWait()

    def speak(*args):
        text = text_entry.get(1.0, END)
        if gender.get() == "  Male":
            engine.setProperty('voice', voices[0].id)
        elif gender.get() == "  Female":
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    text_label = Label(window, text="Enter Text :-", font=("Helvetica", 12))
    text_label.place(x=20, y=40)
    text_entry = Text(window, font=("Helvetica", 12), wrap=WORD)
    text_entry.place(x=155, y=40, height=70, width=225)
    text_entry.focus()

    gender_label = Label(window, text="Select Gender :-", font=("Helvetica", 12))
    gender_label.place(x=20, y=140)
    gender = Combobox(window, font=("Helvetica", 12))
    gender.place(x=155, y=140, width=225)
    gender['values'] = ("  Male", "  Female")
    gender.current(0)

    spr_label = Label(window, text="Speech Rate :-", font=("Helvetica", 12))
    spr_label.place(x=20, y=180)
    spr = Scale(window, from_=0, to=500, orient="horizontal", command=slup)
    spr.place(x=155, y=180, width=225)
    spr.set(rate)

    speak_button = Button(window, text="Speak", font=("Helvetica", 12), command=speak)
    speak_button.place(x=65, y=230, width=70)
    speak_button.bind("<Enter>", on_enter)
    speak_button.bind("<Leave>", on_leave)

    convert_button = Button(window, text="Save", font=("Helvetica", 12), command=save)
    convert_button.place(x=265, y=230, width=70)
    convert_button.bind("<Enter>", on_enter)
    convert_button.bind("<Leave>", on_leave)

    status_label = Label(window, font=("Helvetica",12))
    status_label.pack(side="bottom", pady=15)

    window.bind("<Control_L>", speak)
    window.bind("<Control_R>", save)


engine = init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')

window = Tk()
window.title("Sayl")
window.geometry("400x310")
window.resizable(False, False)
window.iconbitmap("icon.ico")

splash_screen()
# gui()

window.mainloop()
