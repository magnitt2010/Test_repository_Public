money = int(input("Введите сумму вклада :"))
per_cent = {'ТКБ':5.6, 'СКБ':5.9, 'ВТБ':4.28, 'СБЕР':4.0}
TKB = int((per_cent["ТКБ"])*(money/100))
CKB = int((per_cent["СКБ"])*(money/100))
VTB = int((per_cent["ВТБ"])*(money/100))
SBER = int((per_cent["СБЕР"])*(money/100))
deposit = {"ТКБ":TKB, 'СКБ':CKB, 'ВТБ':VTB, 'СБЕР':SBER}
print("Депозит:", deposit)

max_val = max(deposit.values())
print("Максимальный депозит:", max_val)