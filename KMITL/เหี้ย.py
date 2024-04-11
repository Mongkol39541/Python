road1 = { "2": [209, 1], "3": [141, 1], "4": [60, 1], "5": [36, 1] }
road2 = { "1": [209, 1], "3": [160, 1], "4": [150, 1], "5": [184, 1] }
road3 = { "1": [141, 1], "2": [160, 1], "4": [168, 1], "5": [202, 1] }
road4 = { "1": [60, 1], "2": [150, 1], "3": [168, 1], "5": [34, 1] }
road5 = { "1": [36, 1], "2": [184, 1], "3": [202, 1], "4": [34, 1] }
roads = [road1, road2, road3, road4, road5]
city_distances = [1, 2, 3, 4, 5]
exp, lpha, beta = 0.25, 1, 2
time = 0
while len(set(city_distances)) != 1:
    route, distances = [], []
    same = { "1->2": 0, "1->3": 0, "1->4": 0, "1->5": 0, "2->3": 0, "2->4": 0, "2->5": 0, "3->4": 0, "3->5": 0, "4->5": 0 }
    for city in range(len(roads)):
        loop, indexs, start = len(roads) - 1, [str(city + 1)], roads[city]
        distance, i = 0, city + 1
        for _ in range(loop):
            p, vals = [0, 0, 0, 0], []
            inp, asix = 0, 0
            for j in start.keys():
                if j not in indexs:
                    vals.append(j)
                    inp += (1 / (start[j][0] ** lpha)) * (start[j][1] ** beta)
                    p[asix] = (1 / (start[j][0] ** lpha)) * (start[j][1] ** beta)
                    asix += 1
            p = [val / inp for val in p]
            index = vals[p.index(max(p))]
            indexs.append(index)
            distance += start[index][0]
            start = roads[int(index) - 1]
            if i < int(index):
                same[f"{i}->{int(index)}"] += 1
            else:
                same[f"{int(index)}->{i}"] += 1
            i = int(index)
        distance += roads[city][index][0]
        if city + 1 < i:
            same[f"{city + 1}->{i}"] += 1
        else:
            same[f"{i}->{city + 1}"] += 1
        indexs.append(str(city + 1)), route.append(indexs), distances.append(distance)
    time += 1
    city_distances = distances.copy()
    for index in range(len(route)):
        print(f"มดตัวที่ {index + 1} เดินจาก", " --> ".join(map(str, route[index])), f"ระยะทางทั้งหมดที่ใช้เท่ากับ {distances[index]}")
    i = 0
    print("")
    print("Update ค่าฟีโรโมน")
    for road in roads:
        i += 1
        for k in road.keys():
            if i < int(k):
                val_old = road[k][1]
                road[k][1] = round((1 - exp) * road[k][1] + (1 / road[k][0]) * same[f"{i}->{k}"], 4)
                print(f"เส้นทาง {i} --> {k} จาก {val_old} เป็น {road[k][1]}")
            if i > int(k):
                road[k][1] = round((1 - exp) * road[k][1] + (1 / road[k][0]) * same[f"{k}->{i}"], 4)
    print("")
    print("----------------------------------------")
    print("")
print("จำนวนครั้งที่มดเดิน", time, "ครั้ง")