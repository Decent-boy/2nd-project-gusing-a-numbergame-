import time
import random
from sty import RgbFg,fg,Style,rs
fg.mango=Style(RgbFg(255, 165, 0))
fg.peach=Style(RgbFg(255, 229, 0,))
fg.postal_orange=Style(RgbFg(250, 200, 152))
# fg.mango=Style(RgbFg(255, 165, 0))
score=0
try:
    name=input(f"{fg.black} Enter Your Name:{fg.rs}")
    age=int(input(f"{fg.black} Enter Your Age: {fg.rs}"))
    if age>=15 and age<=60:
        print(f"{fg.li_green}Loding.....{fg.rs}")
        time.sleep(3)
        print(f"{fg.mango}________WellCome {name} to gusing Game_______{fg.rs}")
    else:
        print(f"{fg.li_green}Loding.....{fg.rs}")
        time.sleep(3)
        print(f"{fg.mango}You Can't Play This Game\n_________Sorry_________{fg.rs}")
        quit()
except ValueError:
    print(f"{fg.li_green}Loding.....{fg.rs}")
    time.sleep(3)
    print(f"{fg.li_red}___Error___{fg.rs}")

choice_value=input(f"{fg.black}Insert a value where you wanted to play it: {fg.rs}")
if choice_value.isdigit():
    choice_value=int(choice_value)

    random_number=random.randint(0,choice_value)
if choice_value<=0:
    print(f"{fg.li_green}Loding.....{fg.rs}")
    time.sleep(3)
    print(f"{fg.postal_orange}You must choss up to 0.{fg.rs}")
    quit()
else:
    pass

while True:
    score+=1
    user_guse=input(f"{fg.black}Let's make a guse and Type Q for (quit): {fg.rs}")
    if user_guse.lower().strip()=="q":
        print(f"{fg.li_green}Loding.....{fg.rs}")
        time.sleep(3)
        print(f"{fg.postal_orange}Done!{fg.rs}")
        quit()
    if user_guse.isdigit():
        user_guse=int(user_guse)
        if user_guse==random_number:
            print(f"{fg.li_green}Loding.....{fg.rs}")
            time.sleep(3)
            print(f"{fg.postal_orange}You got it\nConguraulation.......{fg.rs}")
            score+=1
            print(f"{fg.green}you got score {score}{fg.rs}")
            break
        elif user_guse>random_number:
            print(f"{fg.li_green}Loding.....{fg.rs}")
            time.sleep(3)
            print(f"{fg.peach}You should guse low.{fg.rs}")
        elif user_guse<random_number:
            print(f"{fg.li_green}Loding.....{fg.rs}")
            time.sleep(3)
            print(f"{fg.peach}You should guse high.{fg.rs}")
        else:
            print(f"{fg.li_green}Loding.....{fg.rs}")
            time.sleep(3)
            print(f"{fg.peach}guse under the chouse value.{fg.rs}")
    else:
        print(f"{fg.li_green}Loding.....{fg.rs}")
        time.sleep(3)
        print(f"{fg.li_red}Invalid{fg.rs}")

