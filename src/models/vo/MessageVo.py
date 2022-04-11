

class MessageVo:

    def __init__(self, id, sender_name, attachements, message):
        self.id = id
        self.sender_name = sender_name
        self.attachements = attachements
        self.message = message

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
    
    def get_sender_name(self):
        return self.sender_name

    def set_sender_name(self, sender_name):
        self.sender_name = sender_name

    def get_attachments(self):
        return self.attachments

    def set_attachments(self, attachments):
        self.attachments = attachments
    
    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message
           