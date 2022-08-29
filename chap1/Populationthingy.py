START_POPULATION = 312032486
SECONDS_IN_A_YEAR = 60*60*24*365

yearlyNumbersOfBirths = SECONDS_IN_A_YEAR // 7

yearlyNumbersOfImmigrants = SECONDS_IN_A_YEAR // 45

yearlyNumbersOfDeaths = SECONDS_IN_A_YEAR // 13

#Year 1
yearOne = (START_POPULATION + (yearlyNumbersOfBirths + yearlyNumbersOfImmigrants - yearlyNumbersOfDeaths))
print("Year 1",yearOne)
for year in range(2, 5):
    yearOne = (yearOne + (yearlyNumbersOfBirths + yearlyNumbersOfImmigrants - yearlyNumbersOfDeaths))
    print(f'year {year} {yearOne}')

