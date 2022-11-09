class Menu:
    def __init__(self, cs) -> None:
        self.choices = cs
    

    def getChoice(self):
        while True:
            for i in range(1, len(self.choices) + 1):
                print(f"{i} - {self.choices[i - 1]}")
            else:
                i += 1
                print(f"{i} - Exit")
            try:
                option = int(input("Enter your choice: "))
                if option > i or option <= 0:
                    raise ""
                return option
            except:
                print(f'\n*** Wrong input. Please enter a NUMBER ***\n')



def main():
    choices = ['Første valg', 'Andre valg', 'Tredje valg, Exit valget under lages automatisk']
    menu = Menu(choices)
    print("Valg gitt = ", menu.getChoice())

main()