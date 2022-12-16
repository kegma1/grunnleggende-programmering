# koden er kjørbar uten syntaks-feil
# etterspurt funksjonalitet er implementert
# det sto ikke i oppgaven at den skal sjekke om det dag eller måned er rett, den vil feile hvis du ikke skriver inn måneden rett.

def which_season(month: str, day: int) -> str:
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_number = months.index(month) + 1

    if month_number in range(1, 4):
        if month_number == 3 and day >= 20:
            return "Spring"
        return "Winter"
    elif month_number in range(4, 7):
        if month_number == 6 and day >= 21:
            return "Summer"
        return "Spring"
    elif month_number in range(7, 10):
        if month_number == 9 and day >= 22:
            return "Fall"
        return "Summer"
    elif month_number in range(10, 13):
        if month_number == 12 and day >= 21:
            return "Winter"
        return "Fall"

def main():
    user_month = input("Enter the name of the month: ")
    user_day = int(input("Enter the day number: "))
    season = which_season(user_month, user_day)
    print(f"{user_month} {user_day} is in {season}")
main()