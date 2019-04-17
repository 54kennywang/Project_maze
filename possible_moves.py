class Play:
    @staticmethod
    def possible_moves(mp, weight, a, b, visited):
        temp = []
        # energies = []
        if (a == mp.sx - 1) or (a == 0): # no up
            right = (a + 1, b)
            if (a + 1 != mp.sx) and (right not in visited):
                right_energy = weight(mp, (a, b), right)
                r = (right_energy, a + 1, b)
                temp.append(r)
                # energies.append(right_energy)
            down = (a, b + 1)
            if (b + 1 != mp.sy) and (down not in visited):
                down_energy = weight(mp, (a, b), down)
                d = (down_energy, a, b + 1)
                temp.append(d)
                # energies.append(down_energy)
            left = (a - 1, b)
            if (a - 1 != -1) and (left not in visited):
                left_energy = weight(mp, (a, b), left)
                l = (left_energy, a - 1, b)
                temp.append(l)
                # energies.append(left_energy)
        elif (b == mp.sy - 1) or (b == 0): # no left
            right = (a + 1, b)
            if (a + 1 != mp.sx) and (right not in visited):
                right_energy = weight(mp, (a, b), right)
                r = (right_energy, a + 1, b)
                temp.append(r)
                # energies.append(right_energy)
            down = (a, b + 1)
            if (b + 1 != mp.sy) and (down not in visited):
                down_energy = weight(mp, (a, b), down)
                d = (down_energy, a, b + 1)
                temp.append(d)
                # energies.append(down_energy)
            up = (a, b - 1)
            if (b - 1 != -1) and (up not in visited):
                up_energy = weight(mp, (a, b), up)
                u = (up_energy, a, b - 1)
                temp.append(u)
                # energies.append(up_energy)
        else: # all
            right = (a + 1, b)
            if (a + 1 != mp.sx) and (right not in visited):
                right_energy = weight(mp, (a, b), right)
                r = (right_energy, a + 1, b)
                temp.append(r)
                # energies.append(right_energy)
            down = (a, b + 1)
            if (b + 1 != mp.sy) and (down not in visited):
                down_energy = weight(mp, (a, b), down)
                d = (down_energy, a, b + 1)
                temp.append(d)
                # energies.append(down_energy)
            left = (a - 1, b)
            if (a - 1 != -1) and (left not in visited):
                left_energy = weight(mp, (a, b), left)
                l = (left_energy, a - 1, b)
                temp.append(l)
                # energies.append(left_energy)
            up = (a, b - 1)
            if (b - 1 != -1) and (up not in visited):
                up_energy = weight(mp, (a, b), up)
                u = (up_energy, a, b - 1)
                temp.append(u)
                # energies.append(up_energy)
        return temp
        '''
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
        '''

        ''' no special case        
        right = (a + 1, b)
        if (a + 1 != mp.sx) and (right not in visited):
            right_energy = weight(mp, (a, b), right)
            r = (right_energy, a + 1, b)
            temp.append(r)
            # energies.append(right_energy)
        down = (a, b + 1)
        if (b + 1 != mp.sy) and (down not in visited):
            down_energy = weight(mp, (a, b), down)
            d = (down_energy, a, b + 1)
            temp.append(d)
            # energies.append(down_energy)
        left = (a - 1, b)
        if (a - 1 != -1) and (left not in visited):
            left_energy = weight(mp, (a, b), left)
            l = (left_energy, a - 1, b)
            temp.append(l)
            # energies.append(left_energy)
        up = (a, b - 1)
        if (b - 1 != -1) and (up not in visited):
            up_energy = weight(mp, (a, b), up)
            u = (up_energy, a, b - 1)
            temp.append(u)
            # energies.append(up_energy)
        return temp

        '''

    def findPath_helper(mp, weight):
        visited = []
        energies = {}
        pred = {}
        for i in range(0, mp.sx):
            for j in range(0, mp.sy):
                energies[(i, j)] = float("inf")
        energies[(0, 0)] = 0
        while True:
            print (len(energies))
            (min_cell, min_val) = min(energies.items(), key=lambda k: k[1])
            # if (float(min_val) == float("inf")):
            #     break 
            if (min_cell == (mp.sx-1, mp.sy-1)):
                result = min_val
                break
            del energies[min_cell]
            visited.append(min_cell)
            options = Marcher.possible_moves(mp, weight, min_cell[0], min_cell[1], visited)
            for i in options:
                if ((min_val + i[0]) < energies[(i[1], i[2])]):
                    energies[(i[1], i[2])] = float(min_val + i[0])
                    pred[(i[1], i[2])] = min_cell
        mp.path.append((mp.sx-1, mp.sy-1))
        p = pred[(mp.sx-1, mp.sy-1)]
        while (p != (0, 0)):
            mp.path.insert(0, p)
            p = pred[p]
        mp.path.insert(0, (0, 0))
        return result