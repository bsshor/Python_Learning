'''
提示输入需要购买的苹果的重量(斤),
然后提示输入每斤的价格,
请计算应支付的总价,
并打印提示输出
'''

x = input('请输入要购买的苹果质量，单位斤:')
y = input('请输入每斤价格： ')
c = int(x) * int(y)
print('金额：', c)
