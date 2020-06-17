import math

uniques = []
final_list = []
input_list = list(range(1, 1000))
for number in input_list:
    raw_divided_number_3 = int(number)/3
    raw_divided_number_5 = int(number)/5
    clean_divided_number_3 = math.trunc(raw_divided_number_3)
    clean_divided_number_5 = math.trunc(raw_divided_number_5)
    difference_3 = raw_divided_number_3 - clean_divided_number_3
    difference_5 = raw_divided_number_5 - clean_divided_number_5
    if difference_3 == 0:
        final_list.append(number)
    if difference_5 == 0:
        final_list.append(number)

for number in final_list:
    if number not in uniques:
        uniques.append(number)
summed_value = sum(uniques)
print(str(uniques) + ' uniques')
#print(str(final_list) + ' final list')
print(str(summed_value) + ' summed value')



