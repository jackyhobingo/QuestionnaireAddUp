from list_type import AnsList, ChooseList

class Questionnaire(object):


    def __init__(self):

        self.ans_list = AnsList()
        self.setting()
        self.start()
        self.show_ans()
        self.write_ans()
        print("程式執行結束")

    def setting(self):

        print("問卷設定開始~")
        while True:
            jagged = input("每題答案數量相同嗎(0:不同, 1:相同): ")
            if '0' in jagged and '1' not in jagged:
                self.jagged = True
                break
            elif '1' in jagged and '0' not in jagged:
                self.jagged = False
                break
            else:
                print('輸入錯誤 請重新輸入')

        if self.jagged:
            while True:
                try:
                    col_list = input("(e.g. 2 4 7 代表有三題 分別有 2個 4個 7個選項)\n請輸入各題選項數量: ").split()
                    col_list = [int(col) for col in col_list]
                    self.ans_list.init_jagged_list(col_list)
                    break
                except ValueError:
                    print("輸入錯誤 請重新輸入")

        else:
            while True:
                try:
                    num = int(input("請輸入題目數量: "))
                    if num < 1:
                        raise ValueError
                    types = int(input("請輸入答案種類數量: "))
                    if types < 1:
                        raise ValueError
                    self.ans_list.init_normal_list(row=num, col=types)
                    break
                except ValueError:
                    print("輸入錯誤 請重新輸入")


    def start(self):

        print("問卷統計開始~")
        while True:
            try:
                input_str = input("請輸入受測者的選擇(完成請輸入Q): ")
                if 'q' in input_str or 'Q' in input_str:
                    break
                choose_list = ChooseList(input_str)
                self.ans_list.choices_put_in(choose_list)
            except ValueError :
                print("輸入錯誤，請重新輸入。")
            except IndexError:
                print("輸入範圍外不列入計算。")
            finally:
                print(self.ans_list)

    def show_ans(self):

        print("顯示結果")
        for ans in self.ans_list:
            print(ans)
    
    def write_ans(self):

        print("即將寫入檔案")
        f_name = input("輸入檔名或是按下Enter取消寫入: ")
        
        if f_name:
            with open(f_name+'.txt', 'a') as f :
                print("正在寫入",f_name+'.txt')
                for ans in self.ans_list:
                    print(ans, file=f)
                print("寫入",f_name+'.txt 成功')
        else:
            print("取消寫入")