import sys

menu ={'아이스아메리카노':3000}
prompt = '''
-----------------------------------------------
1.메뉴추가 2.메뉴수정 3.메뉴삭제 4.메뉴목록 5.종료
-----------------------------------------------
'''
while True:
    in1 = input(prompt)

    if in1 == '1':
        in2 = input('추가할 메뉴 입력>>>')
        price = int(input('가격 >>>'))
        if menu.get(in2) :
            print('이미 존재하는 메뉴입니다.')
        else :
            menu[in2]=price
            print(f'{in2}메뉴 가격{price:,}로 입력되었습니다.')
    elif in1 =='2':
        pass
    elif in1 =='3':
        pass
    elif in1 =='4':
        pass
    elif in1 =='5':
        sys.exit()
    else:
        print('메뉴선택을 정확히 해주세요')