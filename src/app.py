import sys
from util.Connection import Connection
from controller.Controller import Controller


def app():
    # Load Data
    data = Connection.load_data()
    if not(data):
        sys.exit(1)

    # Connect to Outlook
    try:
        outlook = Connection.connect_to_outlook()
        print('--> Connected to outlook')
    except:
        # redirect outlook Login
        sys.exit(1)

    # Initialize app
    controller = Controller(data)
    m = controller.start_app()
    m.mainloop()

if __name__ == '__main__':
    app()
