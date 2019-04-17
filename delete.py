# from possible_moves import Play
# from Map import Map

# a = float("inf")
# b = [3.3, 4, float("inf")]
# print (max(b) == float("inf"))


# energies = {}
# print (bool(energies))
# for i in range(0, 3):
#     for j in range(0, 3): 
#         energies[(i, j)] = float(i + j)
# print (energies)
# print (energies[(1, 1)])

# print ((2, 2) in energies.keys())

# (x, y) = max(energies.items(), key=lambda k: k[1])
# print ()
# print (x)
# print (y)
# del energies[x]
# print ()
# print (energies)

# print ("---------------------")

# # possible_moves(mp, weight, a, b, visited)
# def similar_colour(mp, a, b):
#     pa = mp.pixels[a]
#     pb = mp.pixels[b]
#     dst = (pa[0]-pb[0])**2 + (pa[1]-pb[1])**2 + (pa[2]-pb[2])**2
#     return (dst ** 0.5 + 0.01)

# inp = Map("images/water.ppm")
# visited = [(197, 18)]
# options = Play.possible_moves(inp, similar_colour, 197, 19, visited)
# print (options)


# map = [(10, (5, 5)), (8, (4, 4)), (6, (3, 3))]
# map.sort()
# haha = [((1, 4), 8), ((2, 2), 9), ((5, 5), 10)]
# # haha.sort()
# print (haha[1][1])


glo = [1, 2, 3]

class haha:
        # global glo
        @staticmethod
        def p(a):
                temp = a[0]
                a[0] = a[1]
                a[1] = temp
                # return temp, b

        @staticmethod
        def xx():
                a = [(1, 1), (2, 2)]
                # b = 5
                # print (a.index((1,1)))
                haha.p(a)
                # print (x)
                # print (y)
                print (a)

if __name__ == "__main__":
#     haha.xx()
        a = [-1, 5]
        print (a)
        b = a.pop()
        a.append(b)
        print (a)




