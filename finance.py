# -*- coding: utf-8 -*-
import time

# 初始化资产表
try:
    with open('zichan.txt', encoding='utf8') as f1:
        zc = f1.readlines()
        last_rec = zc[-1].split()
        crt_zc = eval(last_rec[1])
        crt_fz = eval(last_rec[2])
        crt_jzc = eval(last_rec[3])
except FileNotFoundError:
    print('没有找到资产负债表！已创建新表。')
    f1 = open('zichan.txt', 'w', encoding='utf8')
    f1.close()
    zc = []
    zc.append('结算日期 资产/w 负债/w 净资产/w\n')
    crt_zc = 0
    crt_fz = 0
    crt_jzc = 0

# 初始化流水账单
try:
    with open('liushui.txt', encoding='utf8') as f2:
        ls = f2.readlines()
except FileNotFoundError:
    print('没有找到流水账单！已创建新表。')
    f2 = open('liushui.txt', 'w', encoding='utf8')
    f2.close()
    ls = []
    ls.append('交易对象 收入/w 支出/w 应收账款/w 应付账款/w 交易日期\n')

def jizhang():
    crt_time = time.strftime('%Y年%m月%d日', time.localtime())
    print('记账模式\n')
    t_cpny = input('交易对象：')
    income = eval(input('收入/万：'))
    expend = eval(input('支出/万：'))
    receiv = eval(input('应收账款/万：'))
    payabl = eval(input('应付账款/万：'))
    crt_zc = crt_zc + income - expend
    crt_fz = crt_fz + payabl - receiv
    crt_jzc = crt_zc - crt_fz
    if crt_time == last_rec[0]:
        zc[-1] = '%s %.2f %.2f %2f' % (crt_time, crt_zc, crt_fz, crt_jzc)
    else:
        zc.append('%s %.2f %.2f %2f' % (crt_time, crt_zc, crt_fz, crt_jzc))



