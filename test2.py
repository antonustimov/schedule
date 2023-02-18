from pprint import pprint
import pickle

with open('test_sheet.pkl', 'rb') as f:
    sheet = pickle.load(f)
new_dict ={}
counter = 1
for i in sheet:
    new_dict[counter] = []
    if i['Смены'] != '' and i['Смены'] !=0:
        new_dict[counter].append(i)

pprint(new_dict)
