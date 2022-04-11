import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
# from tkinter.simpledialog import Dialog
import util.constants as c
import datetime


class Main_View():

    # def __init__(self) -> None:
    #     tk.Tk.__init__(self)
    #     tk.Tk.title(self,'Select an Option')
    #     tk.Tk.protocol(self, 'WM_DELETE_WINDOW')
    #     tk.Tk.resizable(self, False, False)
    #     self.container = ttk.Frame(self, borderwidth=2, relief='flat', padding=(30,10))
    #     self.container.grid(column=0, row=0)

    def __int__(self):
        self.table_messages = None

    def get_table_messages(self):
        return self.table_messages

    # Function Generate Messages Table
    def generate_messages_table(self, container, messages):
        # Instanciating treeview -> Used as Table
        table_messages = ttk.Treeview(container)
        # Columns
        table_messages['columns'] = ('ID', 'Student', 'N. Attachments')
        table_messages.column('#0', width=0, stretch=tk.NO)
        table_messages.column('ID', anchor=tk.CENTER, width=30)
        table_messages.column('Student', anchor=tk.W, width=200)
        table_messages.column('N. Attachments', anchor=tk.CENTER, width=90)
        # Columns Headings
        table_messages.heading('#0', text='', anchor=tk.CENTER)
        table_messages.heading('ID', text='ID', anchor=tk.CENTER)
        table_messages.heading('Student', text='Student', anchor=tk.CENTER)
        table_messages.heading('N. Attachments', text='N. Attachments', anchor=tk.CENTER)
        # Insert info into table
        for id, message in messages.items():
            # Insert info into table
            table_messages.insert(parent='', index=id, iid=id, text='', values=(id, str(message.SenderName).title(), str(message.Attachments.Count)))
        return table_messages
    
    # Function Notify alert
    def show_alert(self, type, notification):
        showinfo(type, notification)

    # Function ask source path
    def ask_source_path(self):
        source_path = askdirectory(
            initialdir = c.SOURCE_PATH, 
            title='Select the Parent Directory')
        return source_path

    # Function ask student details
    def ask_student_details(self):
        date = datetime.datetime.now()
        term = askstring('Term', 'Enter Term') + ' ' + str(date.year)
        app_type = askstring('App Type', 'Enter App Type')
        program = askstring('Program', 'Enter Program')
        return term, app_type, program

    # Function Start GUI
    def start_GUI(self, controller, messages):
        # Initializing Tkinter
        m = tk.Tk()
        m.title('Manage Students Files')
        m.protocol('WM_DELETE_WINDOW')
        m.resizable(False, False)

        # Frames
        container = ttk.Frame(borderwidth=2, relief='flat', padding=(10,10))
        container_btns = ttk.Frame(borderwidth=2, relief='flat', padding=(10, 10))

        # ===================== Table =========================
        # Table to display messages
        self.table_messages = self.generate_messages_table(container, messages)

        # Placing Elements
        container.grid(column=0, row=0)
        self.table_messages.grid(column=0, row=0, columnspan=2)

        # ===================== Buttons =======================
        # Function listen action
        def listen_action(action):
            # Pass action to Controller
            controller.listen_action(action)
        # Btn to execute "Refresh"
        btn_refresh = ttk.Button(container_btns, text='Refresh', command=lambda:listen_action('Refresh'))
        # Btn to execute "Create New Folder"
        btn_create_folder = ttk.Button(container_btns, text='Create New Folder', command=lambda:listen_action('Create'))
        # Btn to execute "Save to Existing Folder"
        btn_save_existing = ttk.Button(container_btns, text='Save to Existing Folder', command=lambda:listen_action('Update'))

        # Loading Image
        from PIL import ImageTk, Image
        image = Image.open(c.IMAGE_PATH)
        image.thumbnail((c.W, c.H))
        image_loaded = ImageTk.PhotoImage(image)
        # Label that will wrap image
        lbl_image = tk.Label(container_btns)
        lbl_image.config(image=image_loaded, width=c.W, height=c.H)
        lbl_image.image = image_loaded

        # Placing Elements
        container_btns.grid(column=1, row=0, sticky=tk.N+tk.S)
        lbl_image.grid(column=1, row=0)
        btn_refresh.grid(column=1, row=1)
        btn_create_folder.grid(column=1, row=2)
        btn_save_existing.grid(column=1, row=3)

        return m


# class MyDialog(Dialog):
#     def body(self, master):
#         ttk.Label(master, text="First:").grid(row=0, sticky=tk.W)
#         ttk.Label(master, text="Second:").grid(row=1, sticky=tk.W)
    
#         self.e1 = ttk.Entry(master)
#         self.e2 = ttk.Entry(master)
    
#         self.e1.grid(row=0, column=1)
#         self.e2.grid(row=1, column=1)
    
#         self.cb = ttk.Checkbutton(master, text="Hardcopy")
#         self.cb.grid(row=2, columnspan=2, sticky=tk.W)
    
#     def apply(self):
#         first = self.e1.get()
#         second = self.e2.get()
#         print(first, second)
    

