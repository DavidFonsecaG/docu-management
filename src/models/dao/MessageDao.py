import sys
from util.Connection import Connection


class MessageDao:
        
    def get_unread_emails_with_attachments(self):

        try:
            outlook = Connection.connect_to_outlook()
            result = {}

            # Get unread emails from Students Folder
            messages = outlook.GetDefaultFolder(6).folders['Students'].Items.Restrict("[Unread]=True")

            # Filter emails by attachements
            id = 1
            for message in messages:

                if message.Attachments.Count > 0:
                    result[id] = message
                    id += 1

            return result

        except:
            print('\n Error getting Unread Emails With Attachments \n')
            sys.exit(1)

        finally:
            if(outlook is not None):
                # self.outlook.Close
                pass
    