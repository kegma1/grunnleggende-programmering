# koden er kjørbar uten syntaks-feil
# etterspurt funksjonalitet er implementert

def gen_seq(n):
    seq = [n]
    while seq[len(seq) - 1] != 1:
        last = seq[len(seq) - 1]
        if last % 2 == 0:
            seq.append(last // 2)
        else:
            seq.append(last * 3 + 1)
    return seq

def main():
    while True:
        n = int(input("Starting number : "))
        if n <= 0:
            break
        seq = gen_seq(n)

        for i in range(1, len(seq)):
            print(seq[i])
        print(f"Finished with start = {n} in {len(seq) - 1} iterations")
main()