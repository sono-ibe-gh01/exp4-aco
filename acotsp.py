import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import animation, rc


def read_problem(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()

    i = 0
    check = True
    while check:
        if 'NAME' in lines[i]:
            name = lines[i].split(":")[1]
        if 'DIMENSION' in lines[i]:
            num_cities = int(lines[i].split(":")[1])
        if 'NODE' in lines[i]:
            check = False
        i += 1

    pos_cities = []
    j = 0
    while i < len(lines):
        sp = lines[i].split()
        if len(sp) < 3:
            break
        pos_cities.append([float(sp[1]), float(sp[2])])
        i += 1
        j += 1

    assert j == num_cities

    dist_cities = [[0] * num_cities for i in range(num_cities)]

    for c1 in range(num_cities):
        for c2 in range(num_cities):
            dist_cities[c1][c2] = \
                math.sqrt(
                    pow(pos_cities[c1][0] - pos_cities[c2][0], 2)
                    + pow(pos_cities[c1][1] - pos_cities[c2][1], 2))


    return name, num_cities, pos_cities, dist_cities


def view_problem(pos_cities):
    FIGSIZE = (4.5, 4.5)
    plt.figure(figsize=FIGSIZE)
    plt.scatter([p[0] for p in pos_cities], [p[1] for p in pos_cities])
    plt.show()


def view_tours(pos_cities, tours, names, info):
    fig_save_dir = f'./figs_{info[0].strip()}'
    Path(fig_save_dir).mkdir(exist_ok=True)
    plt.close('all')
    FIGSIZE = (15, 4.5)
    fig = plt.figure(figsize=FIGSIZE)

    for i in range(min(3, len(tours))):
        ax = fig.add_subplot(1, 3, i + 1, title=names[i])
        ax.scatter([p[0] for p in pos_cities], [p[1] for p in pos_cities])
        plot_tour(ax, pos_cities, tours[i])

    plt.savefig(f'{fig_save_dir}/{info[1]}.jpg')
    plt.pause(0.2)


def view_pheromones_and_tours(pos_cities, tau, tours, names, info):
    fig_save_dir = f'./figs_{info[0].strip()}'    # 保存用dirの名前
    Path(fig_save_dir).mkdir(exist_ok=True)    # dir作成
    plt.close('all')    # 前のwindowを削除する
    FIGSIZE = (15, 4.5)
    fig = plt.figure(figsize=FIGSIZE)

    ax = fig.add_subplot(131, title='Pheromone map')
    ax.scatter([p[0] for p in pos_cities], [p[1] for p in pos_cities])
    plot_pheromone_map(ax, pos_cities, tau)

    for i in range(min(2, len(tours))):
        ax = fig.add_subplot(1, 3, i + 2, title=names[i])
        ax.scatter([p[0] for p in pos_cities], [p[1] for p in pos_cities])
        plot_tour(ax, pos_cities, tours[i])

    # plt.show()    # showしている間は処理がブロックされる
    plt.savefig(f'{fig_save_dir}/{info[1]}.jpg')    # figを保存
    plt.pause(0.05)    # 少し待って処理を再開

def plot_tour(fig, pos_cities, tour):
    x1 = []
    x2 = []
    for c in range(len(tour)):
        x1.append(pos_cities[tour[c]][0])
        x2.append(pos_cities[tour[c]][1])

    fig.plot(x1, x2, color='gray', linestyle='dashed')


def plot_pheromone_map(fig, pos_cities, tau):
    #    ax = fig.add_subplot(1, 1, 1)
    #  fig.subplots_adjust(bottom=0.15)

    #  plt.scatter(data[:,0], data[:,1])

    #    fig.plot(pos_cities[:len(tour),0], pos_cities[:len(tour),1], color='gray', linestyle='dashed')
    num_cities = len(pos_cities)
    for c1 in range(num_cities):
        for c2 in range(num_cities):
            fig.plot(
                [pos_cities[c1][0], pos_cities[c2][0]],
                [pos_cities[c1][1], pos_cities[c2][1]],
                color='pink', alpha = 0.5,
                linewidth=max(0, math.log(tau[c1][c2], 7)))     # 　フェロモンマップが見づらい場合は底を調整


def sort(tours, len_tours):
    z = zip(len_tours, tours)
    z_sorted = sorted(z)
    tours = []
    len_tours = []
    for l, t in z_sorted:
        tours.append(t)
        len_tours.append(l)

    return tours, len_tours


def output_log_file(name, log_best_len_tour):
    with open("./log_" + name.strip() + ".csv", mode='w') as f:
        i = 0
        for l in log_best_len_tour:
            f.write("{}, {}\n".format(i + 1, l))
            i += 1


def get_average_dist(dist_cities):
    return sum([sum(i) for i in dist_cities]) / pow(len(dist_cities), 2.0)
