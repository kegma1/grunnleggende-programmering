# koden er kjørbar uten syntaks-feil
# etterspurt funksjonalitet er implementert

class Container:  
    def __init__(self, maxWeight = 10):
        self.maxWeight = maxWeight
        self.totalWeight = 0
        self.objects = []   

    def addItem(self, weight):
        new_weight = self.totalWeight + weight
        if new_weight > self.maxWeight:
            return False
        self.objects.append(weight)
        self.totalWeight = new_weight
        return True

    def __str__(self):
        return " ".join([str(s) for s in self.objects])

def main():
    item_weights = input("Gi inn vekter på gjenstandene: ").split(" ")
    for i in range(len(item_weights)):
        item_weights[i] = int(item_weights[i])
    item_weights.sort()
    containers = [Container()]
    i = 0;

    while len(item_weights) > 0:
        current_item = item_weights.pop()
        if not containers[i].addItem(current_item):
            item_weights.append(current_item)
            if len(containers) - 1 == i:
                containers.append(Container())
                i = 0
            else:
                i += 1
        else:
            i = 0

    for (i, c) in enumerate(containers):
        print(f"Container {i + 1} inneholder gjenstander med vektene {c} ")
main()
