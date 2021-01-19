
# =============================================================================
# 建立棋盤
# 建立座標
# ======
# O|O|X
# ======
# X|O|X
# ======
# O|X|O
# ======
# 判斷輸贏
# =============================================================================
import random
checkerboard=['0','1','2',
              '3','4','5',
              '6','7','8']
check=[0,0,0,0,0,0,0,0,0]

oblique=0#如果不是斜線就會報錯
endcode=0
winhorizontal=0
winstraight=0
#================================================input
class InputError(Exception):
    pass
def inp():
    try:
        result = int(input("請輸入0~8:"))#猜密碼
        if checkerboard[result]=='O' or checkerboard[result]=='X' :
            raise InputError()
        return result
    except InputError:
        print("輸入錯誤")
        return inp()
    except ValueError:
        return inp()
#================================================判斷
#================================================checkboard
def draw():
    for i in range(0,9,3): 
        print("\t",checkerboard[i],"\t",checkerboard[i+1],"\t",checkerboard[i+2],"\t")
    print("_____________________") 


#================================================主程式
while True:
    endcode+=1
#================================================確認條件    
    for i in range(0,9,3):
        winhorizontal=check[i]+check[i+1]+check[i+2]
        if winhorizontal ==3 or winhorizontal== -3 :
            endcode=10
            break
    for i in range(0,3,1):
        winstraight = check[i]+check[i+3]+check[i+6]  
        if  winstraight ==3 or  winstraight== -3 :
            endcode=10
            break
    if check[4]+check[0]+check[8]==3 or check[4]+check[2]+check[6]==3:
        oblique=1 
        endcode=10
    elif check[4]+check[0]+check[8]==-3 or check[4]+check[2]+check[6]==-3:
        oblique=-1 
        endcode=10
#================================================建立棋盤            
    draw()
#================================================    
    if(endcode%2==1):
        move = inp()
        checkerboard[move]='O'    
        check[move]=1
    else:
        while True:
            computermove = random.randint(0,8)#檢查點
            if (checkerboard[computermove]!='O'and checkerboard[computermove]!='X' )or endcode==10:          
                break
        checkerboard[computermove]='X'     
        check[computermove]=-1
    if endcode==10 :
        break
#================================================判斷誰贏
if winhorizontal ==3 or winstraight==3 or oblique==1 :
    print("player win")
elif winhorizontal ==-3 or winstraight==-3 or oblique==-1:
    print("computer win")
else :
    print("no winer")