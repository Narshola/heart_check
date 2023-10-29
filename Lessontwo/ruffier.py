#from main import p1, p2, p3, age

''' Модуль для расчета результатов пробы Руфье.


Сумма измерений пульса в трех попытках (до нагрузки, сразу после и после короткого отдыха)
в идеале должна быть не более 200 ударов в минуту.
Мы предлагаем детям измерять свой пульс на протяжении 15 секунд,
и приводим результат к ударам в минуту умножением на 4:
   S = 4 * (P1 + P2 + P3)
Чем дальше этот результат от идеальных 200 ударов, тем хуже.
Традиционно таблицы даются для величины, делённой на 10.
Индекс Руфье  
   IR = (S - 200) / 10
оценивается по таблице в соответствии с возрастом:
       7-8             9-10                11-12               13-14               15+ (только для подростков!)
отл.    6.4 и менее    4.9 и менее       3.4 и менее         1.9 и менее               0.4 и менее
хор.    6.5 - 11.9     5 - 10.4          3.5 - 8.9           2 - 7.4                   0.5 - 5.9
удовл.  12 - 16.9      10.5 - 15.4       9 - 13.9            7.5 - 12.4                6 - 10.9
слабый  17 - 20.9      15.5 - 19.4       14 - 17.9           12.5 - 16.4               11 - 14.9
неуд.   21 и более     19.5 и более      18 и более          16.5 и более              15 и более


для всех возрастов результат "неуд" отстоит от "слабого" на 4,
тот от "удовлетворительного" на 5, а "хороший" от "уд" - на 5.5
поэтому напишем функцию ruffier_result(r_index, level), которая будет получать
рассчитанный индекс Руфье и уровень "неуд" для возраста тестируемого, и отдавать результат'''

txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''нет данных для такого возраста'''
txt_res = []
txt_res.append('''низкая.
Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная.
Обратитесь к врачу!''')
txt_res.append('''средняя.
Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
выше среднего''')
txt_res.append('''
высокая''')

def index(p1, p2, p3):
    return (4 * (p1 + p2 + p3) - 200) / 10

def neud_level(age):
    normal_age = (min(age, 15) - 7) // 2
    result = 21 - normal_age * 1.5
    return result

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level -= 4
    if r_index >= level:
        return 1
    level -= 5
    if r_index >= level:
        return 2
    level -= 5.5
    if r_index >= level:
        return 3
    return 4
    
def test(p1, p2, p3, age):
    final_str = txt_index + str(index(p1, p2, p3)) + '\n' + txt_workheart + txt_res[ruffier_result(index(p1, p2, p3), neud_level(age))]
    return final_str