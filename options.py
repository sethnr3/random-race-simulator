import validation


def main_menu():
    print("""\n\tType ADD for adding driver details
    \tType DDD for deleting
    \tType UDD for updating driver details
    \tType VCT for viewing the rally cross standings table
    \tType SRR for simulating a random race
    \tType VRL for viewing race table sorted according to the date
    \tType STF to save the current data to a text file
    \tType RFF to load data from the saved text file
    \tType ESC to exit the program """)

def add():
    validation.name()
    validation.age()
    validation.team()
    validation.car()
    validation.points()
    f= open('Drivers_Details.txt','a')
    f.write(f"{validation.list_of_inputs}\n")
    f.close()
    q=open('newfile.txt','a')
    q.write(f"{validation.list_of_inputs}\n")
    q.close()
    del validation.list_of_inputs[:5]
    print("\n\tData entered successfully")



def ddd():
    validation.delete_by_name()


def udd():
        ddd()
        print("Enter details again")
        add()

def vct():
    validation.sorting()


def srr():
   validation.random_rase_genarator()



def vrl():
    with open("race_table.txt") as r:
        print(r.read())


def stf():
    print("Data Saved into text file called 'Drivers_Details.txt'")


def rff():
    print("\n")
    print("  'NAME',   'AGE',   'TEAM',   'CAR',   'POINTS'")
    with open("Drivers_Details.txt") as r:
        print (r.read())


def esc():
    print ("Programm Terminated")
