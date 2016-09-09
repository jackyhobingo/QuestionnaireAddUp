import os
def clear_window():
    if "nt" in os.name:
        os.system("cls")
    elif "posix" in os.name:
        os.system("clear")
