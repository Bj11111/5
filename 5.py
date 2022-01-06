import streamlit as st
import random as rnd

st.set_page_config(
    "Guessing Game"
)

if 'number' not in st.session_state:
    st.session_state.number = None
if 'number_from' not in st.session_state:
    st.session_state.number_from = None
if 'number_to' not in st.session_state:
    st.session_state.number_to = None
if 'number_of_guesses' not in st.session_state:
    st.session_state.number_of_guesses = None
if 'passed1' not in st.session_state:
    st.session_state.passed1 = False
if 'end' not in st.session_state:
    st.session_state.end = False
if 'name' not in st.session_state:
    st.session_state.name = False


if not st.session_state.name:
   st.session_state.name = st.text_input("你好! 叫什麼名字?")

if st.session_state.name and (not st.session_state.passed1):
    with st.form("form1"):
        st.session_state.number_of_guesses = st.number_input(
            f'{st.session_state.name.capitalize()} 你覺得自己有多幸運\
                 ? 你想猜多少呢?',
            min_value=1,
            max_value=10,
            value=5
        )
        st.session_state.number_from = st.number_input(
            '範圍選擇最小的數字，您希望它是多少?',
            min_value=1,
            max_value=100
        )
        st.session_state.number_to = st.number_input(
            '範圍選擇最大的數字，您希望它是什麼\
                 是？',
            min_value=2,
            max_value=100
        )
        submitted1 = st.form_submit_button("自我挑戰")

    # need to validate user inputs
    if submitted1:
        if not (st.session_state.number_to > st.session_state.number_from):
            st.error('抱歉，最大的數字必須大於\
                    最小的!')
        else:
            st.session_state.passed1 = True
            # the number generation has to be outside of guessing form,
            # otherwise it keeps generating a new number
            st.session_state.number = rnd.randint(
                st.session_state.number_from, st.session_state.number_to)

if st.session_state.passed1 and (not st.session_state.end):
    f'Well, {st.session_state.name} 在數字\
         之間 {st.session_state.number_from} and\
              {st.session_state.number_to}.'

    with st.form("form2"):
        guess = st.number_input(
            '',
            min_value=1,
            max_value=100
        )
        submitted2 = st.form_submit_button("自我挑戰")

    if submitted2:
        st.session_state.number_of_guesses -= 1
        st.info(f" {st.session_state.number_of_guesses} 次機會")
        if guess < st.session_state.number_from \
                or guess > st.session_state.number_to:
            st.warning("超出範圍, FOOL!")
        elif guess < st.session_state.number:
            st.warning("比密碼小!")
        elif guess > st.session_state.number:
            st.warning("比密碼大!")
        else:
            st.success("挑戰成功")
            st.session_state.end = True

        if st.session_state.number_of_guesses == 0:
            st.error(f"輸了喔 數字是\
                 {st.session_state.number}")
            st.session_state.end = True

if st.session_state.end:
    '''
    # Thanks for playing!
    ## Refresh the page if you wish to play again!
    '''
