import matplotlib.pyplot as plt

test_arr = [(0, 10), (1, 20), (2, 30), (3, 40)]

def return_graph(arr) :

    x = []
    y = []

    for tup in arr :
        x.append(tup[0])
        y.append(tup[1])

    plt.plot(x, y)
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Graphic function')
    plt.show()

    return None

return_graph(test_arr)