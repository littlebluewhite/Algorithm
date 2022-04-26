# ex12_5.py
def hanoi(n, src, dst, aux):
    ''' 河內塔 '''
    if n == 1:                                  # 河內塔終止條件
        print('移動圓盤 {} 從 {} 到 {}'.format(n, src, dst))
    else:
        hanoi(n - 1, src, aux, dst)
        print('移動圓盤 {} 從 {} 到 {}'.format(n, src, dst))
        hanoi(n - 1, aux, dst, src)
             
n = eval(input('請輸入圓盤數量 : '))
hanoi(n, 'A', 'B', 'C')







      



    


































def my_function(n, src, dst, aux):
    if n == 1:
        print(f"移動圓盤 {n} 從 {src} 到 {dst}")
    else:
        my_function(n-1, src, aux, dst)
        print(f"移動圓盤 {n} 從 {src} 到 {dst}")
        my_function(n-1, aux, dst, src)

print("--------------------------------------------")
my_function(4, "A", "B", "C")