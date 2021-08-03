import keyboard
import threading
import os
import ctypes
import sys

class NoAdmin(Exception):
    """Raised when the the script does not have permissions to run the script

    Attributes:
        permission_level -- permission level
        message -- explanation of the error
    """
    def __init__(self, message="Invalid permissions. Try executing with admin/root."):
        self.message = message
        super().__init__(self.message)

class Bind():
    def __init__(self, key='q', callback=print, rappid_fire=False, print_data=True, close_on_error=True, end_on_press=False):
        self.key = key
        self.callback = callback
        self.rappidFire = rappid_fire
        self.printData = print_data
        self.closeOnError = close_on_error
        self.endThreadOnPress = end_on_press

        if self.checkAdmin():
            self.createKeyLoop()
        else:
            raise NoAdminPermissions()
    def print(self, data):
        if self.printData:
            print(data)

    def createKeyLoop(self):
        def __keyLoop(key, callback):
            checkPressed = False # check so the script does not spam the key
            while True:
                try:
                    if keyboard.is_pressed(key): # check if the key is pressed
                        if self.rappidFire:
                            callback(key) # spam the key if rappid fire is on
                        elif not(checkPressed):
                            callback(key) # call the key and then enable checkPressed
                            checkPressed = True

                        self.print(f'Recieved with key: {key}!')


                        if self.endThreadOnPress:
                            return 0
                    if not(keyboard.is_pressed(key)) and checkPressed:
                        checkPressed = False # disable checkPressed if the key is not pressed
                except:
                    self.print(f'\n\nError with key: {key}!')

                    if self.closeOnError:
                        exit(1)


        thread = threading.Thread(target = __keyLoop, args=(self.key, self.callback))
        thread.start()

    def checkAdmin(self):
        try:
            return os.getuid() == 0 # root uid is 0 so this first checks for that
        except AttributeError:
            try:
                return ctypes.windll.shell32.IsUserAnAdmin() == 1 # incase the user is running windows, check for admin
            except AttributeError:
                try:
                    return os.system("whoami") == "root" # last cause - check if the username is 'root' as it is default for linux and other OSes
                except AttributeError:
                    raise AttributeError # raise error if all of the attempts fail
