class ChooseList(list):


    def __init__(self, str_):

        self.extend(str_.split())
        self.all_members_change_num(-1)

    def all_members_change_num(self, num):

        for s in range(len(self)):
            self[s] = int(self[s]) + num

class AnsList(list):


    def init_jagged_list(self, col_list):

        self.clear()
        for i in col_list:
            new_list = []
            for j in range(i):
                new_list.append(0)
            self.append(new_list)

    def init_normal_list(self, row, col):

        self.clear()
        for i in range(row):
            new_list = []
            for j in range(col):
                new_list.append(0)
            self.append(new_list)
    
    def clear(self):
        del self[:]

    def choices_put_in(self, choose_list):

        out_of_range = False
        for i in range(len(choose_list)):
            if 0 <= choose_list[i] < len(self[i]):
                self[i][choose_list[i]] += 1
            else:
                out_of_range = True
        if out_of_range:
            raise IndexError