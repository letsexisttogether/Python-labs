import os
import sys

def FloatValueEnter(msg):
    """Enter a value
    and check if the value entered is float
    msg - a message of entering
    :return: Entered float value
    """
    while True:
        floatVal = input(msg)
        # check whether the entered value is float
        try:
            taker = float(floatVal)
        except ValueError:
            continue
        else:
            return float(floatVal)


def IntValueEnter(msg):
    """Enter a value
      and check if the value entered is int
      msg - a message of entering
      minVal - min acceptible value, as a default set to 1
      maxVal - max acceptible value, as a default set to 2000
      :return: Entered int value
      """
    while True:
        intVal = input(msg)
        # check whether the entered value is float
        try:
            taker = int(intVal)
        except ValueError:
            continue
        else:
            return int(intVal)


def BoolValueEnter(msg):
    """The function is only created to simplify
    entering a bool value
    msg - a message of entering
    :return: True or False
    """
    while True:
        strVal = input(msg)
        # check whether the entered value is 'Так' or 'Ні'
        if strVal != 'Так' and strVal != 'Ні':
            continue
        if strVal == 'Так':
            return True
        return False


def MenuSelector(msg, minVal, maxVal):
    """Helps to catch errors while choosing
    a menu item
    msg - entering message
    minVal - min acceptible value
    maxVal - max acceptible value
    :return: Selected menu item
    """
    while True:
        menuVal = IntValueEnter(msg)
        if menuVal < minVal or menuVal > maxVal:
            continue
        return menuVal

def MakeConsoleClean():
    clearCommand = 'clear' # defualt command
    if os.name in ('nt', 'dos'): # if the program is run on windows
        clearCommand = 'cls'
    os.system(clearCommand) # make the console clear

class Passport:
    def __init__(self, newPassportID : int, newName : str, newSurname : str, newPatronymic : str,
                 newCertificateCOVID19 : bool, newGender : str, newBirthDate : str):
        """
        The constuctor of the class
        to create and initialise fields
        of a Passport object
        """
        self.passportID = newPassportID
        self.name = newName
        self.surname = newSurname
        self.patronymic = newPatronymic
        self.certificateCOVID19 = newCertificateCOVID19
        self.gender = newGender
        self.birthDate = newBirthDate
    def __str__(self):
        """
        :return Values of all fields of the object:
        """
        return 'ПІБ: %s %s %s, дата народження: %s \n    Номер паспорта -- %s. Гендер -- %s. Сертифікат вакцинації COVID-19 -- %s\n    ' % (
                self.surname, self.name, self.patronymic, self.birthDate,
                self.passportID, self.gender, self.certificateCOVID19)


class Passanger:
    def __init__(self, newTicketNum : int, newSeatType : str, newPassport : Passport):
        """
        The constuctor of the class
        to create and initialise fields
        of a Passanger object
        """
        self.ticketNum = newTicketNum
        self.seatType = newSeatType
        self.passport = newPassport

    def __str__(self):
        """
        :return Values of all fields of the object:
        """
        return  str(self.passport) + 'Номер квитка -- %s, тип каюти -- %s' % (self.ticketNum, self.seatType)


class Liner:
    def __init__(self, newLinerID : int, newLinerName : str, newMaxSpeed : float, newLength : float, newWidth : float):
        """
        The constuctor of the class
        to create and initialise fields
        of a Passanger object
        """
        self.linerID = newLinerID
        self.linerName = newLinerName
        self.maxSpeed = newMaxSpeed
        self.length = newLength
        self.width = newWidth
        self.listPassangers = []

    def AddPassanger(self, aPassanger : Passanger):
        """
        Method to add new passanger
        to passangers' list
        aPassanger - object to add
        :return None:
        """
        if self.find_passanger(aPassanger.ticketNum) == -1:
            self.listPassangers.append(aPassanger)
        else:
            print('Вибачте, пасажир з таким квитком вже зайшов на борт')

    def DeletePassanger(self, aTicketNum : int):
        """
        Method to delete a selected passanger
        by their ticket number
        aTicketNum - ticket number of the passanger
        which are tried to delete
        :return: None
        """
        delPassID = self.find_passanger(aTicketNum)
        if delPassID != -1:
            self.listPassangers.pop(delPassID)
        else:
            print('Вибачте, такого пасажира немає')

    def ChangePassanger(self, aName : str, aSurname : str, aPatronymic : str, newTicketNum : int, newSeatType : str):
        """
        Changes ticket number and seat type
        of a passanger, which is found by their name,
        surname and patronymic
        :return: None
        """
        defPassID = self.find_passanger_full_name(aName, aSurname, aPatronymic)
        if defPassID != -1:
            self.listPassangers[defPassID].ticketNum = newTicketNum
            self.listPassangers[defPassID].seatType = newSeatType

    def find_passanger(self, aTicketNum : int):
        """
        Finds passanger by their ticket number
        aTicketNum - ticket number of the passanger
        which are tried to find
        :return: index of passanger's place or exception code
        """
        for i in range(len(self.listPassangers)):
            if self.listPassangers[i].ticketNum == aTicketNum:
                return i
        else:
            return -1 # exception code

    def find_passanger_full_name(self, aName: str, aSurname: str, aPatronymic: str):
        """
        Finds passanger by their ticket number
        aTicketNum - ticket number of the passanger
        which are tried to find
        aName - name to find a person by
        aSuranem - surname to find a person by
        aPatronymic - patronymic to find a person by
        :return: index of passanger's place or exception code
        """
        for i in range(len(self.listPassangers)):
            if self.listPassangers[i].passport.name == aName and \
                    self.listPassangers[i].passport.surname == aSurname and \
                    self.listPassangers[i].passport.patronymic == aPatronymic:
                return i
        else:
            return -1  # exception code

    def __str__(self):
        """
        :return: Values of all of the obect's fields
        """
        return "%s. Лайнер: %s\n   Ширина -- %s, Довжина -- %s\n   Максимальна швидкість -- %s (вузлів)" \
               % (self.linerID, self.linerName, self.width, self.length, self.maxSpeed)


class Route:
    def __init__(self, newRouteID : int, newDepartureDateTime : str, newArrivalDateTime : str, newPort_1 : str, newPort_2 : str):
        """
        The constructor of the class
        to craete and initialise fields
        of a Route object
        """
        self.routeID = newRouteID
        self.departureDateTime = newDepartureDateTime
        self.arrivalDateTime = newArrivalDateTime
        self.port_1 = newPort_1
        self.port_2 = newPort_2
        self.listLiners = []

    def GetLiner(self, aLinerID : int):
        """
        :return: Liner by its ID, if such one existst
        """
        foundID = self.find_liner(aLinerID)
        if foundID != -1:
            return self.listLiners[foundID]
        else:
            print('Вибачте, лайнеру з таким ID не існує')
            return Liner(0, 'None', 0.0, 0.0, 0.0)

    def AddLiner(self, newLiner : Liner):
        """
        Method to add new liner
        to route's liners list
        newLiner - object of class Liner
        whick is tried to add
        :return: None
        """
        if self.find_liner(newLiner.linerID) == -1:
            self.listLiners.append(newLiner)
        else:
            print('Вибачте, лайнер з таким ID: %s вже існує\n', newLiner.linerID)

    def DeleteLiner(self, deleteLinerID):
        """
        Method to delete liner
        by its ID
        deleteLinerID - ID to delete a liner by
        :return: None
        """
        foundID = self.find_liner(deleteLinerID)
        if self.find_liner(deleteLinerID) != -1:
            self.listLiners.pop(foundID)
        else:
            print('Вибачте, на цьому мартшуті такого лайнеру немає')

    # The method is only used in class, as it's private the name starts with a lowercase letter
    def find_liner(self, linerSearchID : int):
        """
        Finds passanger by their ticket number
        aTicketNum - ticket number of the passanger
        which are tried to find
        :return: index of passanger's place or exception code
        """
        for i in range(len(self.listLiners)):
            if self.listLiners[i].linerID == linerSearchID:
                return i
        else:
            return -1 # exceprion code

    def __str__(self):
        """
        :return: Values of all of the obect's fields
        """
        return "Маршрут номер %s\nПорта та час відправки: %s %s\nПорт та час прибуття: %s %s" % (
            self.routeID, self.port_1, self.departureDateTime, self.port_2, self.arrivalDateTime)


def main():
    # Filling list of routes with initial values
    listRoutes = [
        Route(1, '16.30 04.05.22', '17.00 - 08.05.22', 'Майамі, США', 'о. Роатан, Гондурас'),
        Route(2, '18.00 22.05.22', '07.00 27.05.22', 'Барселона, Іспанія', 'Неаполь, Італія'),
        Route(3, '17.00 22.05.22', '10.00 27.05.22', 'Венеція (Равенна), Італія', 'Аргостоліон, Греція'),
        Route(4, '17.00 05.06.22', '06.00 09.06.22', "Рим (Чівітавек`я), Італія", 'о. Міконос, Греція')
    ]

    # Giving each created route some liners, not to make them sad
    listRoutes[0].AddLiner(Liner(1, 'Wonder of the Seas', 25, 363, 66))
    listRoutes[0].AddLiner(Liner(2, 'Symphony of the Seas', 22.6, 363, 66))
    listRoutes[1].AddLiner(Liner(3, 'Celebrity Edge', 22, 306, 39))
    listRoutes[2].AddLiner(Liner(4, 'Dream of the seas', 19, 325, 42))
    listRoutes[3].AddLiner(Liner(5, 'Pirates of the Caribbean', 25, 348, 49))

    # Filling liners with passangers
    listRoutes[0].GetLiner(1).AddPassanger(Passanger(315, "Ocean view",
        Passport(319067000, 'Анастасія', 'Лінчук', 'Вадимівна', True, 'Ж', '03.05.2003')))
    listRoutes[0].GetLiner(1).AddPassanger(Passanger(314, "Cabin with balcony",
        Passport(279200780, 'Олександр', 'Черненко', 'Євгенович', True, 'Ч', '21.01.2001')))
    listRoutes[0].GetLiner(2).AddPassanger(Passanger(104, "Suite",
        Passport(190046124, 'Інна', 'Лінчук', 'Леонідівна', False, 'Ж', '25.10.1976')))
    listRoutes[0].GetLiner(2).AddPassanger(Passanger(103, "Deluxe suite",
        Passport(283451900, 'Вадим', 'Богданюк', 'Валентинович', False, 'Ч', '04.07.1999')))
    listRoutes[1].GetLiner(3).AddPassanger(Passanger(207, "Cabin with balcony",
        Passport(169800381, 'Євгеній', 'Філімоненков', 'Володимирович',  True, 'Ч', '12.07.2006')))
    listRoutes[1].GetLiner(3).AddPassanger(Passanger(198, "Ocean view",
        Passport(290015698, 'Олена', 'Фесік', 'Ігорівна', True, 'Ж', '01.01.1989')))
    listRoutes[2].GetLiner(4).AddPassanger(Passanger(89, "Ocean view",
        Passport(109345871, 'Антон', 'Цапков', 'Ігорович',  False, 'Ч', '09.06.2005')))
    listRoutes[2].GetLiner(4).AddPassanger(Passanger(109, "Suite",
        Passport(180000000, 'Володимир', 'Бондаренко', 'Володимирович', True, 'Ч', '19.05.1995')))
    listRoutes[3].GetLiner(5).AddPassanger(Passanger(199, "Suite",
        Passport(230987039, 'Валерія',  'Сава', 'Артуровна', True, 'Ж', '20.09.1997')))
    listRoutes[3].GetLiner(5).AddPassanger(Passanger(10, "Deluxe suite",
        Passport(195037689, 'Олександр',  'Михайлик', 'Сергійович', False, 'Ч', '10.07.1989')))
    listRoutes[3].GetLiner(5).AddPassanger(Passanger(101, "Cabin with balcony",
        Passport(395019878, 'Федір', 'Сліпченко', 'Миколайович', True, 'Ч', '08.12.1990')))
    listRoutes[3].GetLiner(5).AddPassanger(Passanger(301, "Cabin with balcony",
        Passport(167590000, 'Надія', 'Глушко', 'Вікторівна', True, 'Ж', '06.08.1989')))

    while True:
        MakeConsoleClean()
        # Menu
        choice = MenuSelector('Меню:\n1. Вивести маршрут та лейнери, що по ньому плавають\n'
              '2. Вивести лайнер та інформацію про пасажирів\n3. Додати нового пасажира\n'
              '4. Видалити пасажира\n5. Додати лайнер\n6. Видалити лайнер\n7. Змінити номер та тип квитка пасажира\n'
              '8. Вихід\n\nОберіть пункт меню: ', 1, 8)

        # Print every sigle route and its liners
        if choice == 1:
            for route in listRoutes:
                print(str(route) + '\n')
                for liner in route.listLiners:
                    print("   ", str(liner))
                print("")

        # Printing each liner and its passangers
        if choice == 2:
            # Looking through every known route
            for route in listRoutes:
                # Looking through each liner in route
                for liner in route.listLiners:
                    print (str(liner) + '\n')
                    for passanger in liner.listPassangers:
                        print("   ", str(passanger))
                    print("")

        # Add new passanger to a liner
        if choice == 3:
            # Entering values of passanger, which is being add
            passangerToAdd = Passanger(IntValueEnter('Введіть номер квитка: '),
                input('Введіть тип каюти: '),
                Passport(IntValueEnter('Введіть ID паспорта: '),
                input("Введіть ім`я людини: "),
                input('Введіть прізвище людини: '),
                input("Введіть ім'я-побатькові людини: "),
                BoolValueEnter('Чи є у людини сертефікат COVID 19(Так / Ні): '),
                input('Введіть стать людини: '),
                input('Введіть дату народження людини: ')))

            # Choose which route the passanger wants to take
            routeStr = 'Список маршрутів:\n'
            # Going through each route by its index
            # in list of routes
            for i in range(len(listRoutes)):
                routeStr += str(i + 1) + '. ' + str(listRoutes[i]) + '\n'
            # Selecting a route by its position
            findRouteIndex = MenuSelector(routeStr, 1, len(listRoutes))
            routeStr += '\nОберіть маршрут: '

            # Choose which liner is the most attractive to the passanger
            linerStr = 'Список лайнерів:\n'
            for i in range(len(listRoutes[findRouteIndex - 1].listLiners)):
                linerStr += str(i + 1) + '. ' \
                    + listRoutes[findRouteIndex - 1].listLiners[i].linerName
            linerStr += '\nОберіть лайнер: '
            # Selecting a liner by its position
            findLinerIndex = MenuSelector(linerStr, 1, len(listRoutes[findRouteIndex].listLiners))
            listRoutes[findRouteIndex - 1].listLiners[findLinerIndex - 1].AddPassanger(passangerToAdd)

        # Delete a passanger from the liner
        if choice == 4:
            listAllLiners = []
            linerStr = 'Оберіть лайнери: \n'
            # Getting all liners together
            for route in listRoutes:
                # Looking through all liner
                # in route's listLiners
                for liner in route.listLiners:
                    linerStr += str(len(listAllLiners) + 1) \
                        + '. ' + str(liner) + '\n'
                    listAllLiners.append(liner)

            findLinerIndex = MenuSelector(linerStr, 1, len(listAllLiners))
            # Getting all passangers of the selected liner
            print('Всі пасажири: ')
            for passanger in listAllLiners[findLinerIndex - 1].listPassangers:
                print(str(passanger))
            # Entering ticket number to find a passanger by
            passangerTicketNum = IntValueEnter('Введіть номер квитка пасажира: ')
            listAllLiners[findLinerIndex - 1].DeletePassanger(passangerTicketNum)

        # Add new liner to a route
        if choice == 5:
            linerToAdd = Liner(IntValueEnter('Введіть ID лайнеру: '), input('Введіть назву лайнеру: '),
                FloatValueEnter('Введіть максимальну швидкість корабля: '),
                FloatValueEnter('Введіть довжина корабля: '),
                FloatValueEnter('Введіть ширину корабля: '))
            routeStr = ""
            for i in range(len(listRoutes)):
               routeStr += str(i + 1) + '. ' + str(listRoutes[i]) + '\n'
            # Selecting route by its number
            # in listRoutes
            findRouteID = MenuSelector(routeStr, 1, 4)
            listRoutes[findRouteID - 1].AddLiner(linerToAdd)

        # Delete a liner with all his passangers from a route
        if choice == 6:
            # Searching a route
            routeStr = 'Оберіть маршрут:\n'
            for i in range(len(listRoutes)):
                routeStr += str(i + 1) + '. ' + str(listRoutes[i]) + '\n'
            findRouteIndex = MenuSelector(routeStr, 1, len(listRoutes))
            # Selecting a liner by its ID (liner number)
            for liner in listRoutes[findRouteIndex - 1].listLiners:
                print(str(liner))
            linerToDeleteID = IntValueEnter('Введіть ID лайнера: ')
            listRoutes[findRouteIndex - 1].DeleteLiner(linerToDeleteID)

        # Change ticket number and its type of selected passanger
        # by his name, surname and partonymic
        if choice == 7:
            # Entring name, surname and patronymic
            # of a person to find them by
            newPassangerName = input("Введіть ім'я пасажира: ")
            newPassangerSurname = input('Введіть прізвище пасажира: ')
            newPassangerPatronymic = input("Введіть ім'я-побатькові пасажира: ")
            for route in listRoutes:
                for liner in route.listLiners:
                    for passanger in liner.listPassangers:
                        if passanger.passport.name == newPassangerName \
                            and passanger.passport.surname == newPassangerSurname \
                            and passanger.passport.patronymic == newPassangerPatronymic:
                                liner.ChangePassanger(newPassangerName, newPassangerSurname, newPassangerPatronymic,
                                    IntValueEnter('Введіть новий номер квитка: '),
                                    input('Введіть новий тип місця пасажира: '))

        # Exit
        if choice != 8: # if something else than 'Exit' is selected
            # print pause
            input("\nНатисніть будь-яку клавішу для продовження\n")
        else:
           break;

if __name__ == "__main__":
    main()
