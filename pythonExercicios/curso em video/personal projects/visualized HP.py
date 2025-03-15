C = {'': '\033[m',
     'voidHP': '\033[38;2;0;0;0m',
     'emptyHP': '\033[38;2;75;75;75m',
     'emptylowHP': '\033[38;2;200;100;100m',
     'lowHP': '\033[38;2;200;200;100m',
     'HP': '\033[38;2;100;200;100m',
     'overHP': '\033[38;2;175;255;175m'}  # Color

voidHP = f'{C["voidHP"]}█{C[""]}'
emptyHP = f'{C["emptyHP"]}█{C[""]}'
emptylowHP = f'{C["emptylowHP"]}█{C[""]}'
lowHP = f'{C["lowHP"]}█{C[""]}'
HP = f'{C["HP"]}█{C[""]}'
overHP = f'{C["overHP"]}█{C[""]}'


while True:
    health = ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']
    healthStatus = 'healthy'
    hp = int(input('hp: >'))
    void = int(input('void: >'))
    if hp == -1:
        break
    print('\n\n')
    if hp > 13:
        hp = 13
    if void > 10:
        void = 10
    for c in range(0, hp):   # deal health
        if 'empty' in health:
            health.remove('empty')
            health.insert(0, 'health')
        else:
            health.append('overhealth')

    if void > 0:
        while len(health) > 10:
            health.pop()
    for c in range(0, void):
        health.pop()
    for c in range(0, void):
        health.append('voidHP')

    if health.count('overhealth') > 0:
        healthStatus = 'Overhealth'
    if 4 < health.count('health') <= 8:
        healthStatus = 'hurt'
    if 2 < health.count('health') <= 4:         # between 2 and 4
        healthStatus = 'Low Health'
        for c in range(0, len(health)):
            if 'health' in health:
                health.remove('health')
                health.insert(0, 'lowHP')
    elif 0 < health.count('health') <= 2:           # between 2 or 0
        healthStatus = 'Critical Health'
        for c in range(0, len(health)):
            if 'health' in health:
                health.remove('health')
                health.insert(0, 'lowHP')
            elif 'empty' in health:
                health.insert(health.index('empty'), 'emptylowHP')
                health.remove('empty')
    elif health.count('health') <= 0:           # 0 hp
        healthStatus = '\033[7;30;48;2;255;0;0mDEAD\033[0m'
        for c in range(0, len(health)):
            health.pop()
            health.insert(0, 'voidHP')


    print(health)
    for c in range(0, len(health)):   # read health[] and then print
        if health[c] == 'lowHP':
            print(lowHP, end='')
        elif health[c] == 'emptylowHP':
            print(emptylowHP, end='')
        elif health[c] == 'health':
            print(HP, end='')
        elif health[c] == 'empty':
            print(emptyHP, end='')
        elif health[c] == 'overhealth':
            print(overHP, end='')
        elif health[c] == 'voidHP':
            print(voidHP, end='')
        else:
            print('error')
    print()  # prevent end='' problem
    print(healthStatus, 'VOID' if void > 0 else '')

# print(color)
# print('█', end='')
# print(removecolor)
