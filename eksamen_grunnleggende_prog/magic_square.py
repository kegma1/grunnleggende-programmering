# koden er kjørbar uten syntaks-feil
# etterspurt funksjonalitet er implementert


input = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

def is_magic_square(square) -> bool: # returns True if it is a magic square
    last_sum = square[0][2] + square[1][1] + square[2][0] # the previous sum, we initialize it to the diagonal form bottom left to top right
    current_sum = square[0][0] + square[1][1] + square[2][2] # variabel to hold the sum of the current sum, initialize it to the diagonal form top left to bottom right so it can be compared with the other diagonal

    if current_sum != last_sum: # check if the diagonals are equal. if they are we continue and set current_sum to zero, otherwise we return False early(no need to check the rest)
        return False
    current_sum = 0

    for row in range(3): # check all the rows 
        for col in range(3):
            current_sum += square[row][col]
        if current_sum != last_sum:
            return False
        current_sum = 0

    for row in range(3): # check all the columns 
        for col in range(3):
            current_sum += square[col][row]
        if current_sum != last_sum:
            return False
        current_sum = 0

    return True # if we pass alle the checks we can safely say it is a magic square
    

def main():
    print(is_magic_square(input))
main()

