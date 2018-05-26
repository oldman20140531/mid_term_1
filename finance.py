# -*- coding: utf-8 -*-
import time

# 初始化资产表
crt_time = time.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')
try:
    with open('zichan.txt', encoding='utf8') as f1:
        zc = f1.readlines()
    last_rec = zc[-1].split()
    crt_zc = eval(last_rec[1])
    crt_fz = eval(last_rec[2])
    crt_jzc = eval(last_rec[3])
except Exception:
    zc = []
    zc.append('结算日期 资产/w 负债/w 净资产/w\n')
    zc.append('%s 0 0 0\n' % crt_time)
    with open('zichan.txt', 'w', encoding='utf8') as f1:
        f1.writelines(zc)
    crt_zc = 0
    crt_fz = 0
    crt_jzc = 0
    print('没有找到资产负债表！已创建新表。')
# 初始化流水账单
try:
    with open('liushui.txt', encoding='utf8') as f2:
        ls = f2.readlines()
except FileNotFoundError:
    ls = []
    ls.append('交易对象 收入/w 支出/w 应收账款/w 应付账款/w 交易日期\n')
    with open('liushui.txt', 'w', encoding='utf8') as f2:
        f2.writelines(ls)
    print('没有找到流水账单！已创建新表。')


# 记账模块
def jizhang():
    global zc
    global ls
    global crt_jzc
    global crt_zc
    global crt_fz
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
        zc[-1] = '%s %.2f %.2f %.2f\n' % (crt_time, crt_zc, crt_fz, crt_jzc)
    else:
        zc.append('%s %.2f %.2f %.2f\n' % (crt_time, crt_zc, crt_fz, crt_jzc))
    ls.append('%s %.2f %.2f %.2f %.2f %s\n' % (t_cpny, income, expend, receiv, payabl, crt_time))
    print('交易已记录\n当前资产状况：\n')
    print('最新资产：%.2f万\n最新负债：%.2f万\n最新净资产：%.2f万\n' % (crt_zc, crt_fz, crt_jzc))


# 查账模块
def chazhang():
    print('查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最新资产负债状况\n')
    qry = input('请选择服务：')
    if qry == '1':
        print(ls[0])
        for i in ls[-10:]:
            if i != ls[0]:
                print(i)
    elif qry == '2':
        q_cpny = input('请输入公司名：')
        c = 0
        print(ls[0])
        for i in ls:
            if q_cpny in i.split():
                print(i)
                c += 1
        print('与%s共%d笔交易\n' % (q_cpny, c))
    elif qry == '3':
        print('最新资产：%.2f万\n最新负债：%.2f万\n最新净资产：%.2f万\n最后更新时间：%s\n' % (crt_zc, crt_fz, crt_jzc, crt_time))
    else:
        print('输入错误！返回上级菜单。')


# 记录模块
def sav():
    with open('zichan.txt', 'w', encoding='utf8') as s1:
        s1.writelines(zc)
    with open('liushui.txt', 'w', encoding='utf8') as s1:
        s1.writelines(ls)


while True:
    sle = input('1.查账；2.记账；3.退出\n')
    if sle == '2':
        jizhang()
        sav()
    elif sle == '1':
        chazhang()
        sav()
    elif sle == '3':
        sav()
        break
    else:
        print('输入错误，请重新输入！')
