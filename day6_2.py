def fishDict(filename):
    fish_dict = {}
    with open(filename) as f:
        fishes = f.readline().split(',')
    for i in range(len(fishes)):
        fishes[i] = int(fishes[i])
    for timer in fishes:
        if timer not in fish_dict:
            fish_dict[timer] = 0
        fish_dict[timer] += 1
    return fish_dict

def countFish(fish_dict, days):
    current_fish = fish_dict.copy()
    multiply_period = 7
    new_fish_timer = 8
    while days > 0:
        new_fish = {}
        for timer, count in current_fish.items():
            timer -= 1
            if timer == -1:
                if new_fish_timer not in new_fish:
                    new_fish[new_fish_timer] = 0
                new_fish[new_fish_timer] += count
                timer = multiply_period - 1
            if timer not in new_fish:
                new_fish[timer] = 0
            new_fish[timer] += count
        current_fish = new_fish.copy()
        days -= 1
    fish_count = list(current_fish.values())
    total = sum(fish_count)
    return total

fish_dict = fishDict('input1206.txt')
total_fish = countFish(fish_dict, 256)
print(total_fish)
