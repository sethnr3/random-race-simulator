import random

list_of_inputs=list()
x=0

def name():
    file = open("Drivers_Details.txt","r")
    name = []
    for x in file:
        x = x.replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").replace(" ","").replace("\n", "").strip().split(",")
        name.append(x[0])
    file.close()
    while True:
        try:
            d_name = input("\n\t\tEnter the driver's name\t\t\t: ")
            if d_name not in name:
                d_name.lower()
                list_of_inputs.append(d_name)
                break
            else:
                print("\t\tname exist")
                continue
        except:
            break

def age():
    try:
        d_age =int(input("\t\tEnter driver's age\t\t\t: "))
        list_of_inputs.append(d_age)
    except ValueError:
        print(("\t\tEnter an intiger for age"))
        age()
    return

def team():
    try:
        d_team = input("\t\tEnter the driver's team\t\t\t: ")
        list_of_inputs.append(d_team)
    except  ValueError:
        print(("\t\tEnter string for team"))
        team()
    return

def car():
    try:
        d_car = input("\t\tEnter driver's car \t\t\t: ")
        list_of_inputs.append(d_car)
    except  :
        car()
    return

def points():
    try:
        d_point = int(input("\t\tEnter the driver's current points\t: "))
        list_of_inputs.append(d_point)

        global x
        x+=1
    except  ValueError:
        print(("\t\tEnter intiger for current points"))
        points()
    return

def delete_by_name():
    try:
        rd=0
        rdt=0
        name = str(input("\n\t\tEnter the driver's name to delete \t\t: "))
        name=name.lower()
        with open("Drivers_Details.txt", "r") as file_input:
            with open("newfile.txt", "w") as output:
                for line in file_input:
                    rd+=1
                    data = line.replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").replace(" ", "").replace("\n", "").strip().split(",")
                    if data[0] == name:
                        print("Data deleted successfully")

                        # output.write(line)
                    elif data[0]!=name:
                        rdt+=1
                        output.write(line)
                if rd==rdt:
                    print("Name Not found\nEnter the name again")
                    delete_by_name()
        f = open('newfile.txt')
        f1 = open('Drivers_Details.txt', 'r+')
        f1.truncate()
        for x in f.readlines():
            f1.write(x)
        f.close()
        f1.close()
    except ValueError:
        print(("\t\tEnter a valid name"))
        delete_by_name()
    return



def sorting():
    driver_list = []
    file = open("Drivers_Details.txt","r")
    contents = file.readlines()
    file.close()

    for x in contents:
        x = x.replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").replace(" ","").replace("\n", "").strip().split(",")
        driver_list.append(x)

    points = []
    for y in driver_list:
        points.append(int(y[4]))


    max_list = []

    while points:
        max_points = points[0]
        for xy in points:
            if xy > max_points:
                max_points = xy

        max_list.append(max_points)
        points.remove(max_points)

    new_driver = []
    for xxx in max_list:
        # count = 0
        for z in driver_list:

            if int(z[-1]) == xxx:
                new_driver.append(z)
                driver_list.remove(z)
                break

    file = open("Drivers_Details.txt", "w")
    for xvc in new_driver:
        file.write(str(xvc) + "\n")

    file.close()



def random_rase_genarator():
    driver_list_rox = []
    location = ["Nyirad", "Holjes", "Montalegre", "Barcelona", "Riga", "Norway"]
    date = "2022-11-"

    file = open("Drivers_Details.txt", "r")
    driver_no = 0
    no_race = 0
    for x in file:
        driver_no += 1
        no_race += 1
        y = x.replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").replace(" ", "").replace("\n", ""). \
            strip().split(",")
        driver_list_rox.append(y)
    file.close()

    generate_day = []
    count1 = 0
    while driver_no >= count1:
        i = random.randrange(1, 30)
        if i not in generate_day:
            generate_day.append(i)
            count1 += 1

    sort_day = []
    while generate_day:
        small_day = generate_day[0]
        for xy in generate_day:
            if xy < small_day:
                small_day = xy

        sort_day.append(small_day)
        generate_day.remove(small_day)

    count = 0
    f = open("race_table.txt", 'w')
    while no_race >= count:
        driver_position = []
        # location
        rand_race = random.choice(location)

        # day
        day = date + str(sort_day[count])

        f.write(str(day) + "\t" + rand_race + "\n")

        random.shuffle(driver_list_rox)
        position = 1

        for y in driver_list_rox:
            driver = []
            driver.append(position)

            count_no = 0
            for x in y:
                count_no += 1
                if count_no < 5:
                    driver.append(x)
                if count_no == 5:
                    if position == 1:
                        point = int(x) + 10
                        driver.append(point)

                    elif position == 2:
                        point = int(x) + 7
                        driver.append(point)

                    elif position == 3:
                        point = int(x) + 5
                        driver.append(point)

                    else:
                        driver.append(x)

            f.write(str(driver) + "\n")
            driver_position.append(driver)
            position += 1
        f.write("\n")
        count += 1

        list_update = []
        for y in driver_list_rox:
            list_driver_update = []
            for z in driver_position:
                count22 = 0

                if y[:-1] == z[1:-1]:
                    for k in y:
                        if count22 < 4:
                            list_driver_update.append(k)
                        count22 += 1
                    list_driver_update.append(z[-1])
            list_update.append(list_driver_update)
        driver_list_rox = list_update

    f.close()

    f1 = open("Drivers_Details.txt", "w")
    for x in driver_list_rox:
        f1.write(str(x) + "\n")
    f1.close()
