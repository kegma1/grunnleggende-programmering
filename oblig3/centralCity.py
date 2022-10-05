from cgitb import small
from math import sqrt
from operator import indexOf

def dist(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def indexOfMin(lst):
    (_, index) = min((x, i) for (i, x) in enumerate(lst))
    return index


def main():
    userInput = [float(x) for x in input("Enter the coordinates of the cities: ").split(" ")]
    assert len(userInput) % 2 == 0, "not enough points"
    cities = [(userInput[i], userInput[i + 1]) for i in range(0, len(userInput), 2)]
    citiesDistance = []
    for city in cities:
        distances = []
        for other in cities:
            distances.append(dist(city, other))
        citiesDistance.append(sum(distances) / (len(distances) - 1))
    centralIndex = indexOfMin(citiesDistance)

    print(f"The central city is at {cities[centralIndex]}")


if __name__ == "__main__":
    main()