from constraint import *



def check_day(day):
    """
       returns true if day is a workday, false otherwise
       :param :
       :return : path to end node
       """

    if 0 < int(day) < 6:

        return True
    else:

        return False


def check_record_presence(list):
    print("insert day as integer: \n1:Monday\n2:Tuesday\n3:Wednesday\n4:Thursday\n5:Friday\n")
    day = input("day: \n")
    if check_day(day) is False:
        print("Wrong day format")
        exit(0)

    print("insert time in the following format: [HH].[MM], between 08:00 and 20:00\n")
    time = input("time: \n")
    hour = format_time(time)
    name = input("films in catalogue: \n \n[godfather, godfather II, Godfather III, Dune, Toy Story, Goodfellas, Toy Story 2 \n"
                 " Toy Story 2, Terminator 2, Pretty woman, Ghost, Forrest Gump, Narnia, GoldenEye, Jumanji \n"
                 " Call me by your name (2017), Fury (2014), Insidious (2010), Dark Knight (2008), ran (1985),\n"
                 " Star Wars: Episode IV - A New Hope (1977), Star Wars: Episode V, Star Wars: Episode VI, Matrix, The (1999)]\n\n")
    id = name_to_id(name)

    day += ','
    hour += ','
    id += '}'

    for element in list:

        strings = str(element)
        strings = strings.split(' ')

        if (day == strings[1]) and (hour == strings[3]) and (id == strings[5]):
            return True

    return False


def name_to_id(name):
    if name == 'godfather':
        return '858'
    elif name == 'godfather II':
        return '1221'
    elif name == 'Godfather III':
        return '2023'
    elif name == 'Dune':
        return '2021'
    elif name == 'Toy Story':
        return '1'
    elif name == 'Goodfellas':
        return '1213'
    elif name == 'Toy Story 2':
        return '3114'
    elif name == 'Terminator':
        return '1240'
    elif name == 'Terminator 2':
        return '589'
    elif name == 'Pretty woman':
        return '597'
    elif name == 'Ghost':
        return '587'
    elif name == 'Forrest Gump':
        return '356'
    elif name == 'Narnia':
        return '41556'
    elif name == 'GoldenEye':
        return '10'
    elif name == 'Jumanji':
        return '2'
    elif name == 'Call me by your name (2017)':
        return '168492'
    elif name == 'Fury (2014)':
        return '115210'
    elif name == 'Insidious (2010)':
        return '85788'
    elif name == 'Dark Knight (2008)':
        return '58559'
    elif name == 'ran (1985)':
        return '1217'
    elif name == 'Star Wars: Episode IV - A New Hope (1977)':
        return '260'
    elif name == 'Star Wars: Episode V':
        return '1196'
    elif name == 'Star Wars: Episode VI':
        return '1210'
    elif name == 'Matrix, The (1999)':
        return '2571'
    else:
        return 'id not found'


def format_time(time):
    hour = time.split('.')
    mins = int(hour[1])
    hour = int(hour[0])

    if hour > 23 or hour < 0:
        print('Invalid time')
        exit(0)
    elif (hour > 20 or hour < 8) or (hour == 20 and mins > 0):
        print('shop closed')
        exit(0)
    else:
        return str(hour)


if __name__ == "__main__":

    problem = Problem()
    problem.addVariable("Day", [1, 2, 3, 4, 5])
    problem.addVariable("Time", [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    problem.addVariable("Id_Film", [858, 1221, 2023, 1, 2021, 1213, 3114, 1240, 589, 597, 587, 356,
                                    41556, 10, 2, 168492, 115210, 85788, 58559, 1217, 260, 1196, 1210, 2571])

    # lunedì
    problem.addConstraint(lambda Day, Time, Id_Film:
                          (Day == 1 and 8 <= Time <= 10 and Id_Film != 58559
                           and Id_Film != 1217 and Id_Film != 260 and Id_Film != 1196 and Id_Film != 1210
                           and Id_Film != 2571 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                           and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                          or (Day == 1 and 10 <= Time <= 12 and Id_Film != 858
                              and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                              and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                              and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                          or (Day == 1 and 12 <= Time <= 14 and Id_Film != 41556
                              and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                              and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                              and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                          or (Day == 1 and 14 <= Time <= 16 and Id_Film != 41556
                              and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                              and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                              and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                          or (Day == 1 and 16 <= Time <= 18 and Id_Film != 858
                              and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                              and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                              and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                          or (Day == 1 and 18 <= Time <= 20 and Id_Film != 58559
                              and Id_Film != 1217 and Id_Film != 260 and Id_Film != 1196 and Id_Film != 1210
                              and Id_Film != 2571 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                              and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                          or (Day == 2 and 8 <= Time <= 10 and Id_Film != 41556
                              and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                              and Id_Film != 85788 and Id_Film != 858 and Id_Film != 1221 and Id_Film != 2023
                              and Id_Film != 1 and Id_Film != 2021 and Id_Film != 1213)
                          or (Day == 2 and 10 <= Time <= 12 and Id_Film != 41556
                              and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                              and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                              and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                          or (Day == 2 and 12 <= Time <= 14 and Id_Film != 41556
                              and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                              and Id_Film != 85788 and Id_Film != 858 and Id_Film != 1221 and Id_Film != 2023
                              and Id_Film != 1 and Id_Film != 2021 and Id_Film != 1213
                              or (Day == 2 and 14 <= Time <= 16 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                                  and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                              or (Day == 2 and 16 <= Time <= 18 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                                  and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                              or (Day == 2 and 18 <= Time <= 20 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 3 and 8 <= Time <= 10 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                                  and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                              or (Day == 3 and 10 <= Time <= 12 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 3 and 12 <= Time <= 14 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                                  and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                              or (Day == 3 and 14 <= Time <= 16 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                                  and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                              or (Day == 3 and 16 <= Time <= 18 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 858 and Id_Film != 1221 and Id_Film != 2023
                                  and Id_Film != 1 and Id_Film != 2021 and Id_Film != 1213)
                              or (Day == 3 and 18 <= Time <= 20 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 4 and 8 <= Time <= 10 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 4 and 10 <= Time <= 12 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 858 and Id_Film != 1221 and Id_Film != 2023
                                  and Id_Film != 1 and Id_Film != 2021 and Id_Film != 1213)
                              or (Day == 4 and 10 <= Time <= 12 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 4 and 12 <= Time <= 14 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 4 and 14 <= Time <= 16 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 4 and 16 <= Time <= 18 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 4 and 18 <= Time <= 20 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                                  and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                              or (Day == 5 and 8 <= Time <= 10 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 5 and 10 <= Time <= 12 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                                  and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                              or (Day == 5 and 12 <= Time <= 14 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 5 and 14 <= Time <= 16 and Id_Film != 858
                                  and Id_Film != 1221 and Id_Film != 2023 and Id_Film != 1 and Id_Film != 2021
                                  and Id_Film != 1213 and Id_Film != 3114 and Id_Film != 1240 and Id_Film != 589
                                  and Id_Film != 597 and Id_Film != 587 and Id_Film != 356)
                              or (Day == 5 and 16 <= Time <= 18 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 58559 and Id_Film != 1217 and Id_Film != 260
                                  and Id_Film != 1196 and Id_Film != 1210 and Id_Film != 2571)
                              or (Day == 5 and 18 <= Time <= 20 and Id_Film != 41556
                                  and Id_Film != 10 and Id_Film != 2 and Id_Film != 168492 and Id_Film != 115210
                                  and Id_Film != 85788 and Id_Film != 858 and Id_Film != 1221 and Id_Film != 2023
                                  and Id_Film != 1 and Id_Film != 2021 and Id_Film != 1213)
                              ))

    if check_record_presence((problem.getSolutions())):
        print("The film is available to rent")
    else:
        print("The film is not available to rent")
