import win32com.client as win32
import json
import util.constants as c


class Connection:

    # Load data
    def load_data():
        data = {}
        try:
            with open(c.DATA_PATH) as f:
                data = json.load(f)
                print('--> Data loaded successfully')
        except:
            print('\n Error loading data\n')
            return False
        return data
        
    # Connect to Outlook
    def connect_to_outlook():
        try:
            outlook = win32.Dispatch("Outlook.Application").GetNamespace('MAPI')
            return outlook
        except:
            print('\n Error connecting to Outlook\n')
            return False
