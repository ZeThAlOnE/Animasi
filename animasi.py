# module
from os import system
from time import sleep

# program
def logo():
   print("""

    \33[5;31m_    _   _ ___ __  __    _    ____ ___\33[5;31m 
   \33[5;31m/ \  | \ | |_ _|  \/  |  / \  / ___|_ _|\33[5;31m
  \33[5;31m/ _ \ |  \| || || |\/| | / _ \ \___ \| |\33[5;31m 
 \33[5;31m/ ___ \| |\  || || |  | |/ ___ \ ___) | |\33[5;31m 
\33[5;31m/_/   \_\_| \_|___|_|  |_/_/   \_\____/___|\33[5;31m   \33[5;37m ByZETH|ALONE \33[5;37m
""")

   print("""\33[5;33m<> Author : Mr.ZETH
<> Team   : NTB CYBER TEAM
<> Github : https://github.com/ZeThAlOnE  \33[5;33m
""")

logo()

def menu():
   print("""{1} Animasi Cmatrix
{2} Animasi Kereta
{3} Animasi Ranger
{4} Animasi Api
{5} Animasi Htop
{6} Install Module Animasi Terlebih Dahulu
{7} Keluar
""")

   pil = input("     Masukkan pilihan anda : ")
   if pil =="1":
     sleep(1)
     system("cmatrix")
     print("""\33[5;31m
          _                 _ 
 ___  ___| | ___  ___  __ _(_)
/ __|/ _ \ |/ _ \/ __|/ _` | |
\__ \  __/ |  __/\__ \ (_| | |
|___/\___|_|\___||___/\__,_|_|\33[5;31m
""")

   if pil =="2":
     sleep(1)
     system("sl")
     print("""\33[5;33m
          _                 _ 
 ___  ___| | ___  ___  __ _(_)
/ __|/ _ \ |/ _ \/ __|/ _` | |
\__ \  __/ |  __/\__ \ (_| | |
|___/\___|_|\___||___/\__,_|_|\33[5;33m
""")

   if pil =="3":
     sleep(1)
     system("ranger")
     print("""\33[5;34m
          _                 _ 
 ___  ___| | ___  ___  __ _(_)
/ __|/ _ \ |/ _ \/ __|/ _` | |
\__ \  __/ |  __/\__ \ (_| | |
|___/\___|_|\___||___/\__,_|_|\33[5;34m
""")

   if pil =="4":
     sleep(1)
     system("cacafire")
     print("""\33[5;35m
          _                 _ 
 ___  ___| | ___  ___  __ _(_)
/ __|/ _ \ |/ _ \/ __|/ _` | |
\__ \  __/ |  __/\__ \ (_| | |
|___/\___|_|\___||___/\__,_|_|\33[5;35m
""")

   if pil =="5":
     sleep(1)
     system("htop")
     print("""\33[5;36m
          _                 _ 
 ___  ___| | ___  ___  __ _(_)
/ __|/ _ \ |/ _ \/ __|/ _` | |
\__ \  __/ |  __/\__ \ (_| | |
|___/\___|_|\___||___/\__,_|_|\33[5;36m
""")

   if pil =="6":
     sleep(1)
     system("pkg install cmatrix && pkg install sl && pkg install ranger && pkg install libcaca && pkg install htop")
     print("""\33[5;37m
          _                 _ 
 ___  ___| | ___  ___  __ _(_)
/ __|/ _ \ |/ _ \/ __|/ _` | |
\__ \  __/ |  __/\__ \ (_| | |
|___/\___|_|\___||___/\__,_|_|\33[5;37m
""")

   if pil =="7":
     sleep(1)
     system("")
     print("""\33[5;35m
 _                    __   __          
| |    _____   _____  \ \ / /__  _   _ 
| |   / _ \ \ / / _ \  \ V / _ \| | | |
| |__| (_) \ V /  __/   | | (_) | |_| |
|_____\___/ \_/ \___|   |_|\___/ \__,_|\33[5;35m
""")

menu()





