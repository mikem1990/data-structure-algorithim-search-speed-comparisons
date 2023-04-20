# Name: Michael Mei
# Date: 3/20/2022

from time import strftime   # used for current date and time

class Call:
    def __init__(self, client_id=0, client_name="Unknown", client_phone="Unknown"):
        self.client_id = client_id
        self.client_name = client_name
        self.client_phone = client_phone
        self.call_date = strftime("%m/%d/%Y")
        self.call_time = strftime("%H:%M")
        
    # __str__ method is automatically called when you print the object
    def __str__(self):
        return str(self.client_id) + ", " + self.client_name + \
            "\n\tPhone: " + self.client_phone + \
                "\tDate/Time: " + self.call_date + " @ " + self.call_time