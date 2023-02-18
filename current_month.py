'''module that returns name of current month as string
to use it as identifier of curren sheet'''


from datetime import date

current_month_decimal=date.today().month

all_month = {1: 'Январь',
            2: 'Февраль',
            3: 'Март',
            4: 'Апрель',
            5: 'Май',
            6: 'Июнь',
            7: 'Июль',
            8: 'Август',
            9: 'Сентрябрь',
            10: 'Октябрь',
            11: 'Ноябрь',
            12: 'Декабрь'}

current_month = all_month[current_month_decimal]

print(current_month)

