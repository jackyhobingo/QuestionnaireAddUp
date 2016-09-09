class ListAction(object):


    @classmethod
    def int_list(cls, list_):
        return [int(x) for x in list_]

    @classmethod
    def str_list_to_list(cls, str_list):
        return cls.int_list(str_list.strip().strip('[').strip(']').split(', '))

    @classmethod
    def lists_sum(cls, *lists):
        result = type(lists[0])()
        for t in zip(*lists):
            if type(t[0]) == int:
                result.append(sum(t))
            elif type(t[0]) == list:
                result.append(cls.lists_sum(*t))
        return result

    @classmethod
    def to_persents(cls, list_, how_many_after_dot):
        s = sum(list_)
        return [round(item / s, how_many_after_dot) for item in list_]

class ChooseList(list):


    def __init__(self, str_):

        self.extend(str_.split())
        self.all_members_change_num(-1)

    def all_members_change_num(self, num):

        for s in range(len(self)):
            self[s] = int(self[s]) + num

class AnsList(list):


    def clear(self):
        del self[:]

    def init_normal_list(self, row, col):

        self.clear()
        for i in range(row):
            new_list = []
            for j in range(col):
                new_list.append(0)
            self.append(new_list)

    def init_jagged_list(self, col_list):

        self.clear()
        for i in col_list:
            new_list = []
            for j in range(i):
                new_list.append(0)
            self.append(new_list)

    def extend_readlines(self, readlines):
    
        self.clear()
        list_ = [ListAction.str_list_to_list(x) for x in readlines]
        self.extend(list_)

    def add(self, another_ans_list):
    
        new_list = ListAction.lists_sum(self, another_ans_list)
        self.clear()
        self.extend(new_list)

    def choices_put_in(self, choose_list):

        out_of_range = False
        for i in range(len(choose_list)):
            if 0 <= choose_list[i] < len(self[i]):
                self[i][choose_list[i]] += 1
            else:
                out_of_range = True
        if out_of_range:
            raise IndexError

    def choices_put_out(self, choose_list):
        for i in range(len(choose_list)):
            if 0 <= choose_list[i] < len(self[i]):
                self[i][choose_list[i]] -= 1

    def get_persents(self, how_many_after_dot):
        if len(self) != 0:
            presents_ans_list = AnsList()
            for list_ in self:
                presents_ans_list.append(ListAction.to_persents(list_, how_many_after_dot))
            return presents_ans_list
        else:
            raise ValueError
