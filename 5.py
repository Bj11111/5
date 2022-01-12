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
st.title('彩蛋')
# uploaded_file = st.file_uploaded(" ",type = "jpg")
# if uploaded_file is not None:
#     file_bytes = np.asarray(bytearray(uploaded_file.raed()),dtype=np.uint8)
#     opencv_image = cv2.imdecode(file_bytes,1)
#     st.image(opencv_image,channels="BGR")
#     cv2.imwrite('test.jpg',opencv_image)

from keras.preprocessing.image import load_img

from tempfile import NamedTemporaryFile

st.set_option('deprecation.showfileUploaderEncoding', False)

buffer = st.file_uploader("Image here pl0x")
temp_file = NamedTemporaryFile(delete=False)
if buffer:
    temp_file.write(buffer.getvalue())
    st.write(load_img(temp_file.name))
    
