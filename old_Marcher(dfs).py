#################################################################
#                                                               #
#    Define any helper functions you need in this file only.    #
#    All classes/hepler functions should be subclass of         #
#    Marcher, do not include any code outside that scope.       #
#                                                               #
#    You cannot include any additional libraries                #
#    If you need something that Python doesn't                  #
#    have natively - implement it.                              #
#                                                               #
#    Make sure you take a look at Map.py to get familiar        #
#    with how the image is loaded in and stored, you will       #
#    need this to implement your solution properly.             #
#                                                               #
#    A few test cases are provided in Test.py. You can test     #
#    your code by running                                       #
#               python3 Test.py                                 #
#    in the directory where the files are located.              #
#                                                               #
#################################################################


class Marcher:

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
                if (i[2] == 191):
                    print (options)
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
                print ()
                # time.sleep(0.0001)
                if (i[1] == (mp.sx - 1)) and (i[2] == (mp.sy - 1)):
                    return energy
                # x = Marcher.findPath_helper(mp, weight, energy, i[1], i[2], a, b)
                if (left > 30) or (up > 30):
                    del mp.path[-1]
                    energy = energy - i[0]
                    left = 20
                    up = 20
                    '''
                    if (is_left == True): 
                        left = left - 1
                        is_left = False
                    if (is_up == True):
                        up = up - 1
                        is_up = False
                    '''
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


    @staticmethod
    # def possible_moves(mp, weight, a, b, lx, ly):
    def possible_moves(mp, weight, a, b):
        temp = []
        # possible = False # has to have right or down
        energies = []
        if (a == mp.sx - 1) or (a == 0): # no up
            right = (a + 1, b)
            # if (a + 1 != mp.sx) and right != (lx, ly) and (right not in mp.path):
            if (a + 1 != mp.sx) and (right not in mp.path):
                # possible = True
                right_energy = weight(mp, (a, b), right)
                r = (right_energy, a + 1, b)
                temp.append(r)
                energies.append(right_energy)
            down = (a, b + 1)
            # if (b + 1 != mp.sy) and down != (lx, ly) and (down not in mp.path):
            if (b + 1 != mp.sy) and (down not in mp.path):
                # possible = True
                down_energy = weight(mp, (a, b), down)
                d = (down_energy, a, b + 1)
                temp.append(d)
                energies.append(down_energy)
            left = (a - 1, b)
            # if (a - 1 != -1) and left != (lx, ly) and (left not in mp.path):
            if (a - 1 != -1) and (left not in mp.path):
                left_energy = weight(mp, (a, b), left)
                l = (left_energy, a - 1, b)
                temp.append(l)
                energies.append(left_energy)
        elif (b == mp.sy - 1) or (b == 0): # no left
            right = (a + 1, b)
            # if (a + 1 != mp.sx) and right != (lx, ly) and (right not in mp.path):
            if (a + 1 != mp.sx) and (right not in mp.path):
                # possible = True
                right_energy = weight(mp, (a, b), right)
                r = (right_energy, a + 1, b)
                temp.append(r)
                energies.append(right_energy)
            down = (a, b + 1)
            # if (b + 1 != mp.sy) and down != (lx, ly) and (down not in mp.path):
            if (b + 1 != mp.sy) and (down not in mp.path):
                # possible = True
                down_energy = weight(mp, (a, b), down)
                d = (down_energy, a, b + 1)
                temp.append(d)
                energies.append(down_energy)
            up = (a, b - 1)
            #if (b - 1 != -1) and up != (lx, ly) and (up not in mp.path):
            if (b - 1 != -1) and (up not in mp.path):
                up_energy = weight(mp, (a, b), up)
                u = (up_energy, a, b - 1)
                temp.append(u)
                energies.append(up_energy)
        else: # all
            right = (a + 1, b)
            # if (a + 1 != mp.sx) and right != (lx, ly) and (right not in mp.path):
            if (a + 1 != mp.sx) and (right not in mp.path):
                # possible = True
                right_energy = weight(mp, (a, b), right)
                r = (right_energy, a + 1, b)
                temp.append(r)
                energies.append(right_energy)
            down = (a, b + 1)
            # if (b + 1 != mp.sy) and down != (lx, ly) and (down not in mp.path):
            if (b + 1 != mp.sy) and (down not in mp.path):
                # possible = True
                down_energy = weight(mp, (a, b), down)
                d = (down_energy, a, b + 1)
                temp.append(d)
                energies.append(down_energy)
            left = (a - 1, b)
            # if (a - 1 != -1) and left != (lx, ly) and (left not in mp.path):
            if (a - 1 != -1) and (left not in mp.path):
                left_energy = weight(mp, (a, b), left)
                l = (left_energy, a - 1, b)
                temp.append(l)
                energies.append(left_energy)
            up = (a, b - 1)
            #if (b - 1 != -1) and up != (lx, ly) and (up not in mp.path):
            if (b - 1 != -1) and (up not in mp.path):
                up_energy = weight(mp, (a, b), up)
                u = (up_energy, a, b - 1)
                temp.append(u)
                energies.append(up_energy)
        # if (possible == False):
        #     return []
        if (len(temp) == 0) or (len(temp) == 1):
            return temp
        elif (len(temp) == 2):
            if(temp[0][0] <= temp[1][0]):
                return temp
            else:
                result = []
                result.append(temp[1])
                result.append(temp[0])
                return result
        else:
            first = min(energies)
            energies.remove(first)
            second = min(energies)
            # third = max(energies)
            result = []
            for i in temp:
                if (i[0] == first):
                    result.append(i)
                    temp.remove(i)
                    break
            if (temp[0][0] == second):
                result.append(temp[0])
                result.append(temp[1])
                return result
            else:
                result.append(temp[1])
                result.append(temp[0])
                return result
    #######################################################

    @staticmethod
    def all_colour_weight(mp, a, b):
        """
        Input:
            mp : a Map object that represents the image
            a, b : There are both 2-tuples, containing the (x,y) coordinates for the two pixels between
                    which you want to find the energy for a step.


        Requirements:

            Define your own weight function here so that when "25colours.ppm" is run with this function, 
            the least-energy path in the image satisfies the following constraints:

                (1) The least energy path must visit every one of the 25 colours in the graph. The order 
                    in which the path visits these colours does *not* matter, as long as it visits them all. 
                    Be careful - missing even one colour will result in 0 for this function.

                (2) The path can stay on one colour for as many steps as necessary, however once the path 
                    leaves a colour, it can NEVER go through another pixel of the same colour again.
                    (Said in another way, it can only enter/exit each coloured box once)

                (3) For any two given pixels, the energy required to step between them *must* be non-negative.
                    If you have negative energies, this function may not work as intended.

            There is no restriction on path length, it can be as long or as short as needed - as long as it 
            satisfies the conditions above. Also, the amount of energy to step from 'a' to 'b' does not have to be
            the same as the energy to step from 'b' to 'a'. This is up to you.

        Important Note: This weight function will NOT be tested with your solution to the first part of the
                        question. This will be passed into my code and should still produce the results as above,
                        so do not try to change your findPath() method to help with this.

                        This function will be tested ONLY on the specified image, so you do not have to worry
                        about generalizing it. Just make sure that it does not depend on anything else in your
                        code other than the arguments passed in.


        How to test:    Use the 'outputGradient' and 'outputPath' methods in Map to help you debug. Displaying
                        the path will be useful to start, as it will give you a general idea of what the least-
                        energy path looks like, but you will also want to display the gradient to make sure that 
                        there are no colours repeated! (This should be obvious visually if it is the case)

        """

        return 1    # <-- Replace this!