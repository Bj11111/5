import random
# import cv2
# import numpy as np
import streamlit as st

class Die:
    def __init__(self, sides):
        self.sides = sides
        self.keep = False
        self.save_value()

    def save_value(self):
        self.value = self.roll()

    def roll(self):
        return random.randint(1, self.sides)

st.title("TENZI 天子")

if 'dice' not in st.session_state:
    st.session_state.dice = []

NUM_DICE = 10
NUM_SIDES = 6
if st.button("自我挑戰"):
    if len(st.session_state.dice) == 0:
        for idx in range(NUM_DICE):
            st.session_state.dice.append(Die(NUM_SIDES))
    else:
        for idx, die in enumerate(st.session_state.dice):
            if not die.keep:
                st.session_state.dice[idx].save_value()

current_value = 0
has_won = False
if len(st.session_state.dice) > 0:
    current_value = st.session_state.dice[0].value
    has_won = True
for idx, die in enumerate(st.session_state.dice):
    die.keep = st.checkbox(str(die.value), key=str(idx))
    if die.value != current_value:
        has_won = False
        

if has_won:
    st.write("你贏啦~!!")
    st.balloons()
    '''
    ## 謝謝來玩 請再次光臨!
    ## 如果想再玩一次 請按F5!
    ## 祝大家都可以all pass開心過寒假
    '''
if st.button('帥哥'):
   st.image("https://scontent.xx.fbcdn.net/v/t1.15752-9/p206x206/271439506_408933894191183_71515324726547938_n.jpg?_nc_cat=103&ccb=1-5&_nc_sid=aee45a&_nc_ohc=SkRYdAoBUCYAX98dbDa&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVIxzcU3KzZN4112mwDNgHjbSJC6eneygMfDYRYDymGJnQ&oe=6204F2D0")
