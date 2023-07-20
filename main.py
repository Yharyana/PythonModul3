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

#bardzo spoko zadanie jestem dumny ze je zrobiłem

#tel_num=input("Podaj swój numer telefonu")
#tel_num=tel_num.replace("-","").replace(" ","")
#formatted_celli=""
#index_celli=0
#while index_celli<len(tel_num):
#    if index_celli % 3==0 and index_celli!=0:
#        formatted_celli+=" "
#        formatted_celli += tel_num[index_celli]
#        index_celli+=1
#    else:
#        formatted_celli+=tel_num[index_celli]
#        index_celli+=1
#
#print(formatted_celli)

num=0
proby=0
while num % 2!=0 and proby<10 or num == 0 and proby<10:
    proby += 1
    num = int(input("Podaj liczbe parzysta wiekszą od 0. masz 10 prób"))
if(proby<10):
    print("udało ci sie")
else:
    print(" r y searius?")

