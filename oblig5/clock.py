class Clock:
    __days_in_months = [31,  28,  31,  30,  31,  30,  31,  31,  30,  31,  30,  31]

    def __init__(self, year=0, month=0, day=0, hour=0, min=0, sec=0):
        self.set_clock(year, month, day, hour, min, sec)

    def __get_month(self):
        days = self.__days_in_months[self.__month - 1]
        is_leap_year = self.__year % 4 == 0
        if self.__month == 2 and is_leap_year:
            days += 1
        return days


    def inc_sec(self): 
        new_sec = self.__sec + 1
        if new_sec < 60:
            self.__sec = new_sec
        else:
            self.__sec = 0
            self.inc_min()


    def inc_min(self): 
        new_min = self.__min + 1
        if new_min < 60:
            self.__min = new_min
        else:
            self.__min = 0
            self.inc_hour()


    def inc_hour(self): 
        new_hour = self.__hour + 1
        if new_hour < 24:
            self.__hour = new_hour
        else:
            self.__hour = 0
            self.inc_day()


    def inc_day(self):
        new_day = self.__day + 1
        if new_day < self.__get_month():
            self.__day = new_day
        else:
            self.__day = 1
            self.inc_month()


    def inc_month(self):
        new_month = self.__month + 1
        if new_month <= 12:
            self.__month = new_month
        else:
            self.__month = 1
            self.inc_year()


    def inc_year(self):
        self.__year += 1


    def set_clock(self, year, month, day, hour, min, sec):
        self.__year = year if year >= 0 else 0
        self.__month = month if 0 < month <= 12 else 1
        self.__day = day if 0 < day <= self.__get_month() else 1
        self.__hour = hour if 0 <= hour < 24 else 0
        self.__min = min if 0 <= min < 60 else 0
        self.__sec = sec if 0 <= sec < 60 else 0


    def __str__(self):
        return f"{self.__year:04}-{self.__month:02}-{self.__day:02} {self.__hour:02}:{self.__min:02}:{self.__sec:02}"

x = Clock(2021, 1, 30, 23, 59, 59)
x.inc_sec()
print(x)