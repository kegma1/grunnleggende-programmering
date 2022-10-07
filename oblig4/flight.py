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
        pass

