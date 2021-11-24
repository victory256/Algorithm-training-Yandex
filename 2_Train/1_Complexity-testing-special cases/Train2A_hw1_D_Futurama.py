def swoap_heroes(a, b):
    print(a, b)
    mas_heroes[a], mas_heroes[b] = mas_heroes[b], mas_heroes[a]
    return mas_heroes[b]


with open('ДЗ1_D_Футурама_008.txt', 'r') as f:
    n_heroes, kol_perest = map(int, f.readline().split())
    mas_heroes = list(range(n_heroes + 1))
    for _ in range(kol_perest):
        heroes_1, heroes_2 = map(int, f.readline().split())
        mas_heroes[heroes_1], mas_heroes[heroes_2] = mas_heroes[heroes_2], mas_heroes[heroes_1]
f.close()

print(mas_heroes)
for i in range(1, 10):  # n_heroes-1):
    print("i=", i)
    if mas_heroes[i] != i:
        now = i
        kol = 0
        while mas_heroes[now] != now and kol < 5 and mas_heroes[now] != i:
            kol += 1
            now = swoap_heroes(now, n_heroes - 1)
            print(mas_heroes, "now=", now, "i=", i, mas_heroes[now])
            print(now != n_heroes, mas_heroes[now] != i)
        if now != n_heroes:
            now = swoap_heroes(now, n_heroes)
            print(mas_heroes, now, i, mas_heroes[now])
            now = swoap_heroes(now, n_heroes)
            print(mas_heroes, now, i, mas_heroes[now])
        if mas_heroes[n_heroes - 1] < n_heroes - 1:
            now = mas_heroes[n_heroes - 1]
            now = swoap_heroes(now, n_heroes - 1)
            print(mas_heroes, now, i, mas_heroes[now])
if mas_heroes[n_heroes] != n_heroes:
    now = swoap_heroes(n_heroes - 1, n_heroes)
    print(mas_heroes, now, i, mas_heroes[now])
