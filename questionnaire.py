from list_type import AnsList, ChooseList
from clear_window import clear_window
import os

class Questionnaire(object):


    def __init__(self):
        
        self.NEW_COUNT = 1
        self.READ_FROM_FILE = 2
        self.OUTPUT = 3
        self.OUTPUT_PERSENTS = 4
        self.SUM = 5
        self.END_PROGRAME = 6
        self.selection_range = range(self.NEW_COUNT, self.END_PROGRAME + 1)

    def show_selection_panel(self):
        
        print("請問現在要做什麼")
        print('{}: 新問卷統計'.format(str(self.NEW_COUNT)))
        print('{}: 從檔案讀取問卷'.format(str(self.READ_FROM_FILE)))
        print('{}: 顯示與輸出問卷'.format(str(self.OUTPUT)))
        print('{}: 顯示與輸出問卷百分比'.format(str(self.OUTPUT_PERSENTS)))
        print('{}: 問卷資料相加'.format(str(self.SUM)))        
        print('{}: 結束程式'.format(str(self.END_PROGRAME)))

    def run(self):

        while True:
            self.show_selection_panel()
            # start select
            try:
                i = int(input(": "))
                if i not in self.selection_range:
                    raise ValueError
                if i == self.END_PROGRAME:
                    break
                clear_window()
                self.select(i)
            except TypeError:
                clear_window()
                print("輸入錯誤！請重新輸入。")                
                continue
            except ValueError:                
                clear_window()
                print("輸入範圍錯誤！請重新輸入。") 
                continue
            except AttributeError:
                print("輸入錯誤！目前未有問卷資料。")
        
        print("程式結束")

    def select(self, selection):
        
        if selection == self.NEW_COUNT:
            self.new_count()
        elif selection == self.READ_FROM_FILE:
            self.anslist = self.read_anslist_from_file()
            self.show_on_monitor(self.anslist)
        elif selection == self.OUTPUT:
            self.output(self.OUTPUT)
        elif selection == self.OUTPUT_PERSENTS:
            self.output(self.OUTPUT_PERSENTS)
        elif selection == self.SUM:
            self.anslist.add(self.read_anslist_from_file())
            self.show_on_monitor(self.anslist)
        else:
            raise ValueError


    def output(self, output_type):
        
        if len(self.anslist) != 0:
            while True:
                try:
                    output_info = self.anslist
                    if output_type == self.OUTPUT_PERSENTS:
                        point = int(input("請問要擷取到小數點後幾位(0~10): "))                    
                        output_info = self.anslist.get_persents(point)
                    self.show_on_monitor(output_info)
                    self.write_to_file(output_info)
                    break
                except ValueError:
                    print("輸入錯誤 請重新輸入")
        else:
            print("目前無任何可輸出之資訊")

    def new_count(self):
        self.anslist = AnsList()
        self.new_count_setting()
        self.new_count_start()
        print("新統計執行結束")
        self.show_on_monitor(self.anslist)

    def new_count_setting(self):

        print("新問卷設定開始~")
        while True:
            jagged = input("每題答案數量相同嗎(0:不同, 1:相同): ")
            if '0' in jagged and '1' not in jagged:
                self.jagged = True
                break
            elif '1' in jagged and '0' not in jagged:
                self.jagged = False
                break
            else:
                print('輸入錯誤，請重新輸入。')

        if self.jagged:
            while True:
                try:
                    col_list = input("(e.g. 2 4 7 代表有三題 分別有 2個 4個 7個選項)\n請輸入各題選項數量: ").split()
                    col_list = [int(col) for col in col_list]
                    self.anslist.init_jagged_list(col_list)
                    break
                except ValueError:
                    print("輸入錯誤，請重新輸入。")

        else:
            while True:
                try:
                    num = int(input("請輸入題目數量: "))
                    if num < 1:
                        raise ValueError
                    types = int(input("請輸入答案種類數量: "))
                    if types < 1:
                        raise ValueError

                    self.anslist.init_normal_list(row=num, col=types)
                    break
                except ValueError:
                    print("輸入錯誤 請重新輸入")

    def new_count_start(self):

        print("新問卷統計開始~")
        self.add_list = []
        while True:

            try:
                input_str = input("請輸入受測者的選擇(C:取消前一次選擇 Q:完成): ")
                if 'q' in input_str or 'Q' in input_str:
                    break
                if 'c' in input_str or 'C' in input_str:
                    if self.add_list:
                        choose_list = self.add_list.pop()    
                        self.anslist.choices_put_out(choose_list)
                    else:
                        raise ValueError
                else:
                    choose_list = ChooseList(input_str)
                    self.add_list.append(choose_list)
                    self.anslist.choices_put_in(choose_list)
            except ValueError :
                print("輸入錯誤，請重新輸入。")
            except IndexError:
                print("輸入範圍外不列入計算。")
            finally:
                print(self.anslist)

    def show_on_monitor(self, anslist):

        print("顯示目前問卷")
        for ans, i in zip(anslist, range(1, len(anslist)+1)):
            print(i,":", ans)

    def read_anslist_from_file(self):
        while True:
            try:
                f_name = input("請輸入要讀取的檔案名稱: ")
                new_anslist = AnsList()
                with open(f_name, 'r') as f:
                    readlines = f.readlines()
                    new_anslist.extend_readlines(readlines)
                    return new_anslist
                    break
            except FileNotFoundError:
                print("檔案名稱錯誤，請重新輸入檔名。")

    
    def write_to_file(self, anslist):

        print("即將寫入檔案")
        f_name = input("輸入檔名或是按下Enter取消寫入: ")
        if os.path.exists(f_name):
            check = input("檔案已經存在，是否覆蓋(Y/N): ")
            if 'y' not in check and 'Y' not in check or 'n' in check or 'N' in check:
                f_name = ''

        if f_name:
            with open(f_name, 'w') as f :
                print("正在寫入",f_name)
                i = len(anslist)
                for ans in anslist:
                    print('.'* (40 // i), end='')
                    print(ans, file=f)
                print('Finish')
                print("寫入", f_name, '成功')
        else:
            print("取消寫入")
