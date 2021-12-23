# 導入 tkinter 模塊
# 從 tkinter 導入 *
# 導入 tkinter。消息框 作為 msg
# 設置窗口
根 =  Tk ()
根。幾何（'500x550'）
根。最大尺寸( 500 , 550 )
根。最小尺寸( 500 , 550 )
# 定義了一些變量
turn  =  2  # 對於 acucessig 玩家回合。如果是偶數，則玩家 1 和奇數玩家 2
board  = [ "-" , "-" , "-" ,
         "-" , "-" , "-" ,
         "-" , "-" , "-" ]
stop_list  = [] # 每當遊戲獲勝時停止的列表，該列表中附加了停止
根。配置（bg = '黃色'）

def  display_board ():
    '''該函數用於畫板'''
    打印（板[ 0 ] +  ' | '  + 板[ 1 ] +  ' | '  +板[ 2 ]）
    打印（板[ 3 ] +  ' | '  + 板[ 4 ] +  ' | '  + 板[ 5 ]）
    打印（板[ 6 ] +  ' | '  + 板[ 7 ] +  ' | '  + 板[ 8 ]）

def  check_winner ():
    '''用於檢查獲勝者的函數'''
    # 檢查行
    如果 board [ 0 ] ==  board [ 1 ] == board [ 2 ]和 board [ 0 ] != '-'：
        打印（f' { board [ 0 ] }是贏家'）
        停止列表。追加（'停止'）
    elif  board [ 3 ] ==  board [ 4 ] == board [ 5 ]和 board [ 3 ] != '-'：
        打印（f' { board [ 3 ] }是贏家'）
        停止列表。追加（'停止'）
    elif  board [ 6 ] ==  board [ 7 ] == board [ 8 ]和 board [ 6 ] != '-'：
        打印（f' { board [ 6 ] }是贏家'）
        停止列表。追加（'停止'）

    # 檢查列
    對於 我 在 範圍（3）：
        如果 board [ i ] ==  board [ i + 3 ] ==  board [ i + 6 ]並且 board [ i ] != '-'：
            打印（f' { board [ i ] } is winnner'）
            停止列表。追加（'停止'）

    # 對於對角線
    if (( board [ 0 ] ==  board [ 4 ] ==  board [ 8 ]) or ( board [ 2 ] ==  board [ 4 ] ==  board [ 6 ])) and  board [ 4 ] != '-'：
        打印（f' { board [ 4 ] }是贏家'）
        停止列表。追加（'停止'）

def  check_tie ():
    ''''檢查匹配的功能是否平局。'''
    如果 len ( stop_list ) == 0 並且 '-'  not  in  board : # len()==0 表示停止不在列表中或 '-' 不在面板中表示所有
        # 空格已填滿
        打印（'比賽是平局'）
        停止列表。追加（'領帶'）

def  button_player1（按鈕）：
    '''此功能用於改變點擊X後按鈕的樣式'''
    按鈕。更新()
    按鈕[ 'fg' ] =  '黃色'
    按鈕[ '文本' ] =  'X'
    按鈕[ 'bg' ] =  '藍色'

def  button_player2（按鈕）：
    '''該函數用於改變玩家O點擊後按鈕的樣式'''
    按鈕。更新()
    按鈕[ 'fg' ] =  '黃色'
    按鈕[ '文本' ] =  'O'
    按鈕[ 'bg' ] =  '紅色'

def  reset_button_style（按鈕）：
    '''這個功能會在遊戲重啟時清除按鈕上的所有效果'''
    按鈕。更新()
    按鈕[ 'fg' ] =  '白色'
    按鈕[ '文本' ] =  '-'
    按鈕[ 'bg' ] =  '黑色'


def  clear_list_and_reset_button_text ():
    '''此函數用於通過將所有變量設置為其初始位置來再次玩遊戲'''
    # 該函數僅在有人獲勝或比賽平局時運行
    button_list  = [ b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9 ]
    對於 我 在 範圍（9）：
        reset_button_style ( button_list [ i ]) # 重置所有按鈕的樣式
        board [ i ] =  '-'  # 再次設置 board
    印刷（板）
    turn_indicator。更新()
    turn_indicator [ 'text' ] =  'Turn: Player 1'  # 最初輪到第一個玩家
    停止列表。clear () #清空列表



def  update_board ( position , button ):
    乙1。更新()
    全球 轉向
    # 玩家 1 輪偶數
    如果 轉% 2 == 0：
        # 更新窗口上的玩家回合標籤
        turn_indicator。更新()
        turn_indicator [ 'text' ] =  '回合：玩家 2'
        if  board [ position - 1 ] ==  '-' : # 檢查玩家位置的條件是否為空。'-' 表示空
            按鈕。更新()
            button_player1 ( button ) # 點擊時調用按鈕樣式改變函數
            board [ position - 1 ] =  'X'  # 在船上更新位置
            check_winner () # 每次點擊後檢查獲勝者
            check_tie () # 每次點擊後檢查tie
            if  'stop'  in  stop_list : # 每當玩家贏得獲勝者檢查時，函數將在空列表中添加停止
                留言。showinfo ( 'Winner' , 'Congratulations .... Player 1 wins. \n Well play ' )
                打印（轉）
                clear_list_and_reset_button_text ()
            elif  'tie'  in  stop_list : # 每當 match 為 tie 時，chek for tie 函數將在空列表中添加 tie
                留言。showinfo ( 'Tie' , 'Ohh!.... The match is tie' )
                clear_list_and_reset_button_text ()
            else : # 如果什麼都沒有發生，那麼玩家轉身
                停止列表。清除()
                轉 +=  1
        else : # 如果位置不為空則顯示錯誤
            留言。showinfo ( 'Eroor!' , "請不要試圖誇大立場.." )

    # Odd 指的是第二個玩家
    elif 轉% 2 != 0 :
        # 更新玩家指示器標籤
        turn_indicator。更新()
        turn_indicator [ 'text' ] =  '回合：玩家 1'
        if  board [ position - 1 ] == '-' : # 檢查玩家位置的條件是否為空。'-' 表示空
            打印（'玩家2回合'）
            button_player2 ( button ) # 點擊時調用按鈕樣式改變函數
            board [ position - 1 ] =  'O'  # 在後台更新board上的位置
            check_winner () # 檢查獲勝者，如果有人獲勝，則此函數將在列表中添加停止
            check_tie () # 檢查領帶
            # 檢查停止或平局
            如果 在stop_list 中“停止” ： 
                留言。showinfo ( 'info' , '玩家 2 是贏家' )
                clear_list_and_reset_button_text ()
                轉+= 1
            elif  'tie' 在 stop_list 中：
                留言。showinfo ( 'Tie' , 'Ohh!.... The match is tie' )
                clear_list_and_reset_button_text ()
            else : # 如果什麼都沒有發生，那麼通過使偶數變為奇數來改變轉彎，反之亦然
                停止列表。清除()
                轉 +=  1
        其他：
            留言。showinfo ( 'Eroor!' , "請不要試圖誇大立場.." )

# 窗口的樣式從這裡開始
標籤( root , text = 'Welcome in Tic Tac Toe Game' , font = 'Arial 25 bold' , fg = 'black' , bg = 'orange' )。包（稻穀= 4）

turn_indicator  =  Label ( root , text = 'Turn: Player 1' , font = 'MVBoli 19 bold' )
turn_indicator。包()
# 第一幀
f1  = 框架（根，寬度= 450，高度= 100，bg = '黃色'）
f1。包（稻穀= 10）
b1  =  Button ( f1 , text = board [ 0 ], width = 3 , font = 'Arial 48 bold' , bg = 'black' , fg = 'white' ,浮雕= GROOVE , bd = 4 , command = lambda : update_board ( 1 , b1 ))
乙1。包（邊=左，padx = 4）
b2  =  Button ( f1 , text = '-' , width = 3 , font = 'Arial 48 bold' , bg = 'black' , fg = 'white' ,浮雕= GROOVE , bd = 4 , command = lambda : update_board ( 2 , b2 ))
乙2。包（邊=左，padx = 4）
b3  =  Button ( f1 , text = '-' , width = 3 , font = 'Arial 48 bold' , bg = 'black' , fg = 'white' ,浮雕= GROOVE , bd = 4 , command = lambda : update_board ( 3 , b3 ))
乙3。包()
# 第二幀
f2  = 框架（根，寬度= 450，高度= 100，bg = '黃色'）
f2 . 包（稻穀= 10）
b4  =  Button ( f2 , text = '-' , width = 3 , font = 'Arial 48 bold' , bg = 'black' , fg = 'white' ,浮雕= GROOVE , bd = 4 , command = lambda : update_board ( 4 , b4 ))
b4 . 包（邊=左，padx = 4）
b5  =  Button ( f2 , text = '-' , width = 3 , font = 'Arial 48 bold' , bg = 'black' , fg = 'white' ,浮雕= GROOVE , bd = 4 , command = lambda : update_board ( 5 , b5 ))
乙5。包（邊=左，padx = 4）
b6  =  Button ( f2 , text = '-' , width = 3 , font = 'Arial 48 bold' , bg = 'black' , fg = 'white' ,浮雕= GROOVE , bd = 4 , command = lambda : update_board ( 6 , b6 ))
乙6。包()
# 第三幀
f3  = 框架（根，寬度= 450，高度= 100，bg = '黃色'）
f3 . 包（稻穀= 10）
b7  =  Button ( f3 , text = '-' , width = 3 , font = 'Arial 48 bold' , bg = 'black' , fg = 'white' ,浮雕= GROOVE , bd = 4 , command = lambda : update_board ( 7 , b7 ))
乙7。包（邊=左，padx = 4）
b8  =  Button ( f3 , text = '-' , width = 3 , font = 'Arial 48 bold' , bg = 'black' , fg = 'white' ,浮雕= GROOVE , bd = 4 , command = lambda : update_board ( 8 , b8 ))
b8 . 包（邊=左，padx = 4）
b9  =  Button ( f3 , text = '-' , width = 3 , font = 'Arial 48 bold' , bg = 'black' , fg = 'white' ,浮雕= GROOVE , bd = 4 , command = lambda : update_board ( 9 , b9 ))
乙9。包()

根。主循環（）
