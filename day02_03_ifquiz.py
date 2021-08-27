price = int(input('상품금액 >>>'))
money = int(input('상품대금 >>>'))

change = price - money

if change<0:
    m1 = change //10000
    m2 = (change - 10000*m1) // 5000
    m3 = (change - 10000*m1 -5000*m2) // 1000
    m4 = (change - 10000*m1 -5000*m2-1000*m3) //500
    m5 = (change - 10000*m1 - 5000*m2 - 1000*m3 - 500*m4) //100
    m6 = (change - 10000*m1 - 5000*m2 - 1000*m3 - 500*m4 - 100*m5) //50
    m7 = (change - 10000*m1 - 5000*m2 - 1000*m3 - 500*m4 - 100*m5 - 50*m6) //10
    print(f'만원권{m1}장, 오천원권{m2}장, 천원권{m3}장, 오백원{m4}, 백원{m5}, 오십원{m6}개, 십원{m7}개')
