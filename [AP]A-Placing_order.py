'''
Description:
    美团在吃喝玩乐等很多方面都给大家提供了便利。最近又增加了一项新业务：小象生鲜。这是新零售超市，你既可以在线下超市门店选购生鲜食品，也可以在手机App上下单，最快30分钟就配送到家。
    新店开张免不了大优惠。我们要在小象生鲜超市里采购n个物品，每个物品价格为ai，有一些物品可以选择八折优惠（称为特价优惠）。
    有m种满减优惠方式，满减优惠方式只有在所有物品都不选择特价优惠时才能使用，且最多只可以选择最多一款。
    每种满减优惠描述为(bi,ci)，即满bi减ci（当消费>=bi时优惠ci）。
    求要买齐这n个物品（必须一单买齐），至少需要多少钱（保留两位小数）。

Input description:
    第一行，两个整数n,m。
    接下来n行，每行一个正整数ai，以及一个0/1表示是否可以选择特价优惠（1表示可以）。
    接下来m行，每行两个正整数bi,ci，描述一款满减优惠。
    
    1 <= n,m <=10
    1 <= ai <= 100
    1 <= ci < bi <= 1000
    
Output description:
    一行一个实数，表示至少需要消耗的钱数（保留恰好两位小数）。
    
Examples:
    I input:               II input:
        2 1                     2 2
        6 1                     6 1     
        10 1                    10 1
        12 2                    5 1    
    output:                     16 6
        12.80                 output:
                                10.0

'''

n_m_input = list(map(int, input().split(' ')))  # 第一行输入
n, m = n_m_input[0], n_m_input[1]
total_price, discount_price = 0, 0
for i in range(n):
    l = list(map(int, input().split(' ')))
    p, d = l[0], l[1]
    total_price += p
    p1 = [0.8 * p, p][d != 1]
    discount_price += p1
a = []
for j in range(m):
    l = list(map(int, input().split(' ')))
    t, dis = l[0], l[1]
    if total_price >= t:
        a.append(total_price - dis)

a = sorted(a)
print("%.2f" % [a[0], discount_price][a[0] > discount_price])

# print(total_price, discount_price)
