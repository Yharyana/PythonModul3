i = 1
while i < 6:
  print(i)
  i += 1
lista_sports=["triatrlon","bobslej","bridge","soccer"]
index_sports=0
while index_sports<len(lista_sports):
    if index_sports % 2>0:
        print(lista_sports[index_sports])
    index_sports+=1

lista_nums=[2137,69,420,17]
num_sum=0
num_index=0
while num_index<len(lista_nums):
    num_sum+=lista_nums[num_index]
    num_index+=1

print(num_sum)

#zadania
tel_num=input("Podaj swój numer telefonu")
tel_num=tel_num.replace("-","").replace(" ","")
formatted_celli=""
index_celli=0
while index_celli
