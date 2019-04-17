@staticmethod
    def findPath(mp, weight):
        """
        Input: 
            mp - This is a Map object representing the image you are working on. Look at the Map
                class to see details on how we are representing the data.

            weight - This is the weight **function**. You are supposed to use this to find the energy
                required for each step by the Pixel Marcher. This function should be called like this:

                      weight(mp, (x,y), (a, b))

                to find the energy needed to step from pixel (x,y) to pixel (a,b). Note that
                this function may return a value for *any* pair of pixels, and it is your job
                to only be consider valid steps (More on this below). In general this returns a float.

                The return value of this function will always be non-negative, and it is not necessarily
                the case that weight(mp, a, b) = weight(mp, b, a).

        Requirements: 
            Your objective is to find the least-energy path from pixel (0,0) to pixel(sx-1, sy-1), along
            with the amount of energy required to traverse this path. Here, sx and sy are the x and y 
            dimensions of the image. (These are stored in 'mp')

            From each pixel, it is possible to step to at most 4 other pixels, namely the ones on it's top, 
            right, bottom and left. All of these steps may require different amounts of energy, and you have 
            to use the given weight function to compute these.

            Note: When going through your neighbours, always go through them in the following order for the sake
                of this assignment: TOP, RIGHT, BOTTOM, LEFT (Start at the top and go clockwise).


                                                        (x, y-1)
                                                            ^
                                                            |
                                        (x-1, y) <------ (x, y) ------> (x+1, y)
                                                            |
                                                            v
                                                        (x, y+1)


            Always doing it in this order will ensure consistency if there are multiple least-energy paths.

            Once you find this path, you need to store all the nodes along it in mp.path[], ensuring that 
            the (0,0) is the first element in the array, (sx-1, sy-1) is the last, and all the remaining
            elements are in order.

            Your function additionally needs to return the total energy required for the least-energy path 
            you have found. You will be graded on this since the cost a least-energy path is unique and must 
            match the expected answer.

        You are NOT allowed to import any additional libraries. All code must be your own.      

        """
        mp.path.append((0, 0))
        # result = Marcher.findPath_helper(mp, weight, 0, 0, 0, 0, -1)
        result = Marcher.findPath_helper(mp, weight, 0, 0, 0, 0, 0)
        return result  # <-- Replace this with the cost of the least-energy path

    #######################################################
    # delete import time
    @staticmethod
    # def findPath_helper(mp, weight, energy, a, b, lx, ly):
    def findPath_helper(mp, weight, energy, a, b, left, up):
        # options = Marcher.possible_moves(mp, weight, a, b, lx, ly)
        options = Marcher.possible_moves(mp, weight, a, b)
        is_left = False
        is_up = False
        if (len(options) != 0):
            for i in options:
                energy = energy + i[0]
                mp.path.append((i[1], i[2]))
                #####################
                if (i[1] < a): # left move by 1
                    left = left + 1
                    is_left = True
                if (i[2] < b): # up move by 1
                    up = up + 1
                    is_up = True
                #####################
                print (mp.path)
                # time.sleep(0.0001)
                if (i[1] == (mp.sx - 1)) and (i[2] == (mp.sy - 1)):
                    return energy
                # x = Marcher.findPath_helper(mp, weight, energy, i[1], i[2], a, b)
                if (left > 30) or (up > 30):
                    del mp.path[-1]
                    energy = energy - i[0]
                    if is_left == True: 
                        left = left - 1
                    if is_up == True:
                        up = up - 1
                else:
                    x = Marcher.findPath_helper(mp, weight, energy, i[1], i[2], left, up)
                    if x != -1:
                        return x
                    else:
                        del mp.path[-1]
                        energy = energy - i[0]
            return -1
        else:
            return -1