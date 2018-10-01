# import datetime to get the actual time of day and import json in order to change dictionary into json
import datetime
import json

class PoolTable(object):
    def __init__(self, name, occupied = False, hour = 0, minute = 0):
        self.name = name
        self.occupied = occupied
        self.hour = hour
        self.minute = minute
    # is_occupied will return weither or not someone has taken the table if ran 
    def is_occupied(self):
        return self.occupied
    # checkout allows someone to get a pooltable it changes the occupied to true and start a date and time
    def checkout(self):
        if self.occupied == False:
            self.hour = datetime.datetime.now().hour
            self.minute = datetime.datetime.now().minute
            self.occupied = True
        # if occupied is True already then checkout will print this statment
        else:
            print('This table is already checked out')
    # checkin allows the customer to leave the pooltable and now their Elapsed time will be shown based off that you can calculate the price
    def checkin(self):
        if self.occupied == True:
            self.occupied = False
            print('Elapsed time: ' ),
            hour = datetime.datetime.now().hour - self.hour
            minute = datetime.datetime.now().minute - self.minute
            if hour > 0:
                print(str(hour)),
            elif minute > 0:
                print(str(minute))
            else:
                print(str(0-minute))
            return float(hour + 0.01*minute)
        else:
            print('Table not yet occupied')
            return 0.0
    # to_dictionary prints out the object and retruns it as json
    def to_dictionary(self):
        tableDictionary = { 'name':self.name,'occupied' : self.occupied,'hour': self.hour, 'minute': self.minute}
        djson = json.dumps(tableDictionary) 
        return djson

# created and instance of pooltable called table_1
table_1 = PoolTable(name = 'table 1')
# using pooltable one I can now run these methods on them and print them out
print(table_1.to_dictionary())
table_1.checkout()
print(table_1.to_dictionary())
table_1.checkin()
print(table_1.to_dictionary())


