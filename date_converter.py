import re

days_to_words = {"1":"перв",
                 "01":"перв",
                 "2":"втор",
                 "02":"втор",
                 "03":"трет",
                 "3":"трет",
                 "4":"четверт",
                 "04":"четверт",
                 "05":"пят",
                 "5":"пят",
                 "6":"шест",
                 "06":"шест",
                 "07":"седьм",
                 "7":"седьм",
                 "8":"восьм",
                 "08":"восьм",
                 "09":"девят",
                 "9":"девят",
                 "10":"десят",
                 "11":"одиннадцат",
                 "12":"двенадцат",
                 "13":"тринадцат",
                 "14":"четырнадцат",
                 "15":"пятнадцат",
                 "16":"шестнадцат",
                 "17":"семнадцат",
                 "18":"восемнадцат",
                 "19":"девятнадцат"}

digits = {2:"двадцать",
          3:"тридацть",
          4:"сорок",
          5:"пятьдесят",
          6:"шестьдесят",
          7:"семьдесят",
          8:"восемьдесят",
          9:"девяносто"}

months = {"1":"января",
          "01":"января",
          "02":"февраля",
          "2":"февраля",
          "3":"марта",
          "03":"марта",
          "04":"апреля",
          "4":"апреля",
          "5":"мая",
          "05":"мая",
          "06":"июня",
          "6":"июня",
          "7":"июля",
          "07":"июля",
          "08":"августа",
          "8":"августа",
          "9":"сентября",
          "09":"сентября",
          "10":"октября",
          "11":"ноября",
          "12":"декабря"}

thousands = {0:"",
             1:"тысяча",
             2:"две тысячи",
             3:"три тысячи"}

centuries = {0:"",
             1:"сто",
             2:"двести",
             3:"триста",
             4:"четыреста",
             5:"пятьсот",
             6:"шестьсот",
             7:"семьсот",
             8:"восемьсот",
             9:"девятьсот"}

DATE = re.compile("([0-9]{,2} (январ|феврал|март|апрел|ма|июн|июл|август|сентябр|октябр|ноябр|декабр).)")
FULL_DATE = re.compile("([0-9]{,2} (январ|феврал|март|апрел|ма|июн|июл|август|сентябр|октябр|ноябр|декабр). [0-9]{,4} ?(год.|г.)?)")
NUMERIC_DATE = re.compile("[0-9]{1,2}[\.\/-][0-9]{1,2}[\.\/-][0-9]{2,4}")

text = input()
dates = re.findall(FULL_DATE, text)
dates += re.findall(DATE, text)
numeric_dates = re.findall(NUMERIC_DATE, text)

for i in dates:
    YEAR = re.compile("[0-9]{4}")
    match = YEAR.search(i[0])
    if match:
        year_in_numbers = int(match.group(0))
        first_symb = year_in_numbers//1000
        sec_symb = (year_in_numbers - 1000 * first_symb)//100
        last_years = year_in_numbers - first_symb * 1000 - sec_symb * 100
        if last_years <= 19:
            year_in_letters = thousands[first_symb] + " " + centuries[sec_symb] + " " + days_to_words[str(last_years)]
        else:
            if last_years%10 == 0:
                year_in_letters = thousands[first_symb] + " " + centuries[sec_symb] + " " + digits[last_years//10]
            else:
                year_in_letters = thousands[first_symb] + " " + centuries[sec_symb] + " " + digits[last_years//10] + " " + days_to_words[str(last_years%10)]
            
        if match.group(0)[-1] == "3":
            year_in_letters += "ьего"
        else:
            year_in_letters += "ого"
        text = re.sub(match.group(0), year_in_letters, text)
        
    DAY = re.compile("[0-9]{,2}")
    match2 = DAY.search(i[0])
    if match2.group(0):
        if match2.group(0) == "3":
            text = re.sub(match2.group(0), days_to_words[match2.group(0)] + "ье", text)
        else:
            text = re.sub(match2.group(0), days_to_words[match2.group(0)] + "ое", text)

for k in numeric_dates:
    date_in_symb = k.split(".")

    '''определение года'''
    year_in_numbers = int(date_in_symb[2])
    first_symb = year_in_numbers//1000
    sec_symb = (year_in_numbers - 1000 * first_symb)//100

    last_years = year_in_numbers - first_symb * 1000 - sec_symb * 100
    if last_years <= 19:
        year_in_letters = thousands[first_symb] + " " + centuries[sec_symb] + " " + days_to_words[str(last_years)]
    else:
        if last_years%10 == 0:
            year_in_letters = thousands[first_symb] + " " + centuries[sec_symb] + " " + digits[last_years//10]
        else:
            year_in_letters = thousands[first_symb] + " " + centuries[sec_symb] + " " + digits[last_years//10] + " " + days_to_words[str(last_years%10)]

    if date_in_symb[2][-1] == "3":
        year_in_letters += "ьего года"
    else:
        year_in_letters += "ого года"

    if int(date_in_symb[0]) <= 19:
        day = days_to_words[date_in_symb[0]]
    else:
        if int(date_in_symb[0])%10 == 0:
            day = digits[int(date_in_symb[0])//10]
        else:
            day = digits[int(date_in_symb[0])//10] + " " + days_to_words[str(int(date_in_symb[0])%10)]

    '''проверка на порядок элементов в дате (русский VS американский)'''
    if int(date_in_symb[1]) <= 12:
        if date_in_symb[0] == "3":
            date_in_symb = " ".join([day + "ье", months[date_in_symb[1]], year_in_letters])
        else:
            date_in_symb = " ".join([day + "ое", months[date_in_symb[1]], year_in_letters])
    else:
        if date_in_symb[0] == "3":
            date_in_symb = " ".join([day + "ье", months[date_in_symb[0]], year_in_letters])
        else:
            date_in_symb = " ".join([day + "ое", months[date_in_symb[0]], year_in_letters])

    text = re.sub(k, date_in_symb, text)

print (text)
