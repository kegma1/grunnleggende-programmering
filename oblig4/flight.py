from datetime import datetime

class Flight:
    def __init__(self, flightNum, departureTime, arrivalTime):
        self.__flightNum = flightNum
        self.__departureTime = departureTime 
        self.__arrivalTime = arrivalTime 

    def getFlightNum(self):
        return self.__flightNum

    def getDepartureTime(self):
        return self.__departureTime

    def setDepartureTime(self, newTime):
        self.__departureTime = newTime
        return self.__departureTime

    def getArrivalTime(self):
        return self.__arrivalTime

    def setArrivalTime(self, newTime):
        self.__arrivalTime = newTime
        return self.__arrivalTime

    def getFlightTime(self):
        return (self.__arrivalTime - self.__departureTime).total_seconds() / 60.0

class Itinerary:
    def __init__(self, flights):
        self.__flights = flights

    def getTotalFlightTime(self):
        return sum([x.getFlightTime() for x in self.__flights])

    def getTotalTravelTime(self):
        start = self.__flights[0].getDepartureTime()
        end = self.__flights[-1].getArrivalTime()
        return (end - start).total_seconds() / 60.0


def main():

    flights = []
            
    flights.append(Flight("US230",
        datetime(2014, 4, 5, 5, 5, 0),
        datetime(2014, 4, 5, 6, 15, 0)))

    flights.append(Flight("US235",
        datetime(2014, 4, 5, 6, 55, 0),
        datetime(2014, 4, 5, 7, 45, 0)))

    flights.append(Flight("US237",
        datetime(2014, 4, 5, 9, 35, 0),
        datetime(2014, 4, 5, 12, 55, 0)))

    itinerary = Itinerary(flights)
    print(itinerary.getTotalTravelTime())
    print(itinerary.getTotalFlightTime())

if __name__ == "__main__":
    main()