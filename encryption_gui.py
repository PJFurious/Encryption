import tkinter
from tkinter import *
from encryption_script import *


def browse_folder():
    global file_content
    global file_type
    global file_name

    file_info = open_file()
    file_content, file_type, file_name = file_info.file_content, file_info.file_type, file_info.f_name
    f_entry.insert(0, file_name)


def run():
    password = p_entry.get()
    if f_entry.get() == '':
        tkinter.messagebox.showerror(title='No Folder', message='Please browse a folder')
    else:
        if password == '':
            tkinter.messagebox.showwarning(title='Warning', message='Please enter a password')
        else:
            if v.get() == 0:
                encrypt(password.encode('utf_8'), file_content, file_type, file_name)
                f_entry.delete(0, END)
                p_entry.delete(0, END)
                tkinter.messagebox.showinfo(title='Encrypted', message='File was encrypted')
            elif v.get() == 1:
                if decrypt(password.encode('utf_8'), file_content, file_type):
                    f_entry.delete(0, END)
                    p_entry.delete(0, END)
                    tkinter.messagebox.showinfo(title='Encrypted', message='File was decrypted')
                else:
                    tkinter.messagebox.showerror(title='Wrong password', message='Password does not match!')

# GUI has been coded on a linux system. Might visually differ on a windows system.
def encryption_screen():
    global f_entry
    global p_entry
    global v

    screen = Tk()
    screen.geometry('370x345')
    screen.title('Encryption')
    screen.configure(bg='#111111')

    label_background = "#333333"
    button_background = "#222222"

    # components to browse a folder
    Label(screen, text = 'File:', height=1, width=5, font=(None, 13), bg=label_background, fg='white', borderwidth=2, relief='ridge').place(x=15, y = 15)
    f_entry = Entry(screen, width=24, font=(None, 13), bg='white', borderwidth=2, relief='ridge')
    f_entry.place(x=83, y = 15)
    Button(screen, text='Browse', height=1, width=28, font=(None, 13), bg=button_background, fg='white', borderwidth=2, relief='flat', command=browse_folder).place(x=16, y=53)

    # radiobuttons to choose encrypt or decrypt
    v = tkinter.IntVar()

    Radiobutton(screen, variable=v, value=0, text='Encrypt', height=1, width=11, font=(None, 13), bg='white').place(x=15, y = 125)
    Radiobutton(screen, variable=v, value=1, text='Decrypt', height=1, width=11, font=(None, 13), bg='white').place(x=193, y = 125)

    # components for password/key
    Label(screen, text = 'Password/key:', height=1, width=20, font=(None, 13), bg=label_background, fg='white', borderwidth=2, relief='ridge').place(x=75, y = 187)
    p_entry = Entry(screen, width=30, font=(None, 13), bg='white')
    p_entry.place(x=16, y = 227)

    # run and close button
    Button(screen, text='Run', height=1, width=12, font=(None, 13), bg=button_background, fg='white', borderwidth=2, relief='flat', command=run).place(x=15, y=289)
    Button(screen, text='Close', height=1, width=12, font=(None, 13), bg=button_background, fg='white', borderwidth=2, relief='flat', command=screen.destroy).place(x=190, y=289)


    screen.mainloop()

encryption_screen()