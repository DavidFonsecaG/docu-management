import os
from models.dao.MessageDao import MessageDao
import util.constants as c
from view.Main_View import *
# from docx2pdf import convert


class Controller:

    def __init__(self, data):
        self.data = data
        self.main_view = Main_View()
        self.messages = MessageDao().get_unread_emails_with_attachments()

    def start_app(self):
        m =  self.main_view.start_GUI(self, self.messages)
        return m

    def ask_path(self, student_name):
        # Ask Student Details
        term, app_type, program = self.main_view.ask_student_details()
        # Create Directory
        path = (c.SOURCE_PATH + '\\' + term + '\\' + app_type + '\\' + program + '_' + student_name)
        return path

    def create_dir(self, path):
        try:
            os.makedirs(path)
        except:
            print(f'\n Error creating directory:\n {path}')
    
    def save_attachments(self, attachments, path):
        for attachment in attachments:
            # the name of attachment file      
            attachment_name = str(attachment).lower()
            # save attachment
            attachment.SaveASFile(path + '\\' + attachment_name)
  
    # Under Construction
    def Convert_to_pdf(self, path):
        # convert(path+'/')
        pass
    # def term():
    #     date = datetime.datetime.now()
    #     term = None
    #     if 1 <= date.month <= 3 :
    #         term = 'Fall ' + str(date.year)
    #     elif 4 <= date.month <= 7:
    #         term = 'Winter ' + str(date.year + 1)
    #     else:
    #         term = 'Spring ' + str(date.year + 1)
    #     # Select Term
    #     for filename in os.listdir(c.SOURCE_PATH):
    #         print(filename)

    # Main-View's actions Listener
    def  listen_action(self, action, message=None):
        match action:

            case('Create'):
                try:
                    # Get message selected
                    table_messages = self.main_view.get_table_messages()
                    message_id = int(table_messages.item(table_messages.focus(), 'values')[0])
                    message = self.messages[message_id]
                    # Get path
                    path = self.ask_path(str(message.SenderName).title())
                    # Create Directory
                    self.create_dir(path)
                    # Save Attachments
                    self.save_attachments(message.Attachments, path)
                    # Notify Success
                    self.main_view.show_alert("Done", "File successfully saved")
                    # Display message
                    message.Display(True)
                    # Delete Items from GUI table
                    for i in table_messages.get_children():
                        if int(i) == message_id:
                            table_messages.delete(i)
                except:
                    print(f'\n Error loading requirement {action}\n')

            case('Update'):
                try:
                    # Get message selected
                    table_messages = self.main_view.get_table_messages()
                    message_id = int(table_messages.item(table_messages.focus(), 'values')[0])
                    message = self.messages[message_id]
                    # Get path
                    path = self.main_view.ask_source_path()
                    # Save Attachments
                    self.save_attachments(message.Attachments, path)
                    # Notify Success
                    self.main_view.show_alert("Done", "File successfully saved")
                    # Display message
                    message.Display(True)
                    # Delete Items from GUI table
                    for i in table_messages.get_children():
                        if int(i) == message_id:
                            table_messages.delete(i)        
                except:
                    print(f'\n Error loading requirement {action}\n')

            case ('Refresh'):
                try:
                    # Get messages
                    self.messages = MessageDao().get_unread_emails_with_attachments()
                    # Get table of messages
                    table_messages = self.main_view.get_table_messages()
                    # Delete Items from GUI table
                    for i in table_messages.get_children():
                            table_messages.delete(i)
                    # Insert info into table
                    for id, message in self.messages.items():
                        # Insert info into table
                        table_messages.insert(parent='', index=id, iid=id, text='', values=(id, str(message.SenderName).title(), str(message.Attachments.Count)))
                except:
                    print(f'Error loading requirement {action}')

            case _:
                print(f'\n Action "{action}" not valid\n')
