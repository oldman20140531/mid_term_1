# -*- coding: utf-8 -*-

# 读文件
with open('report.txt', encoding='utf8') as f:
    rpt = f.readlines()

# 创建表头、科目平均分行
result = []
result.append('名次 '+rpt[0].strip('\n')+' 总分 平均分\n')
avg_c = ['平均', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sort_st = []
# 遍历文件每行，生成每个学生的成绩列表stu计算总分
for s in rpt[1:]:
    sum_st = 0
    stu = [eval(x) for x in s.split()[1:]]
    for i in range(len(stu)):
        # 科目总分累加
        avg_c[i+1] += stu[i]
        # 学生总分累加
        sum_st += stu[i]
        # 替换不及格分数
        if stu[i] < 60:
            stu[i] = '不及格'
    # 将学生成绩插入姓名和统计结果一并写入sort_st列表待排序
    stu.insert(0, s.split()[0])
    stu.append(sum_st)
    stu.append(int(sum_st/len(stu)))
    sort_st.append(stu)
# 计算各科目平均分写入result
for x in range(1, len(avg_c[:-2])):
    avg_c[x] = int(avg_c[x]/(len(rpt)-1))
avg_c[-2] = int(sum(avg_c[1:-2]))
avg_c[-1] = int(avg_c[-2]/len(avg_c[1:-2]))
result.append('0 '+' '.join([str(x) for x in avg_c])+'\n')
# 排序并将学生成绩表写入result
sort_st = sorted(sort_st, key=lambda x: x[-2], reverse=True)
n = 0  # n为名次序列
for l in sort_st:
    n += 1
    result.append(str(n)+' '+' '.join([str(x) for x in l])+'\n')
# 生成统计文件
with open('result.txt', 'w', encoding='utf8') as r:
    r.writelines(result)
