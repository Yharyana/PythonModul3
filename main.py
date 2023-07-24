#i = 1
#while i < 6:
#  print(i)
 # i += 1
#ista_sports=["triatrlon","bobslej","bridge","soccer"]
#index_sports=0
#while index_sports<len(lista_sports):
#    if index_sports % 2>0:
#        print(lista_sports[index_sports])
#    index_sports+=1

#lista_nums=[2137,69,420,17]
#num_sum=0
#num_index=0
#while num_index<len(lista_nums):
#    num_sum+=lista_nums[num_index]
#    num_index+=1

#print(num_sum)

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

#tez spoko zadanie na poczaktu łatwe sie wydaje a nie dokkocna
#num=0
#proby=0
#while num % 2!=0 and proby<10 or num == 0 and proby<10:
#    proby += 1
#    num = int(input("Podaj liczbe parzysta wiekszą od 0. masz 10 prób"))
#if(proby<10):
#    print("udało ci sie")
#else:
#    print(" r y searius?")

#przekombinował w  i nie dizała edit: wystaczyło uzyc spolita
#dania=input("podaj swoje uluione dania odzielajac  je przeicnkiem")
#liczba_dots=0
#liczba_dan=0
#while liczba_dots<len(dania):
#    if dania[liczba_dots]==",":
#        liczba_dan+=1
#        liczba_dots+=1
#    else:
#        liczba_dots+=1
#liczba_dan+=1
#print(liczba_dan)
#lista_dan=[0]*liczba_dan
#liczba_dots=0

#pętla for

#count=1
#seasons=["wiosna","lato","jesien","zima"]
#for season in seasons:
#    print(count,season)
#    count+=1
#seasons=["wiosna","lato","jesien","zima"]
#for count,season in enumerate(seasons,start=1):
#    print(count,season)

#zadania!

# spoko zadanie całkiem
#x=True
#oceny=""
#ocena_int=0;
#srednia=0
#suma=0;
#ilosc=0
#while x==True:
#    y=input("Podaj ocene lub jeśli skonczyłes  napisz X")
#    if y=="X":
#        x=False
#    else:
#        oceny+=y
#        ilosc+=1
#
#for i in oceny:
#    ocena_int=int(i)
#    suma+=ocena_int
#    print(i)
#srednia=suma/ilosc
#print("oto twoja srednia ",srednia)


#tel_num=input("Podaj swój numer telefonu")
#tel_num=tel_num.replace("-","").replace(" ","")
#formatted_celli=""

#for index_celli,number in enumerate(tel_num):
#    if index_celli % 3==0 and index_celli!=0:
#        formatted_celli+=" "
#        formatted_celli += number

#    else:
#        formatted_celli+=number


#print(formatted_celli)


# zebyb wypisowało tylko
#wydatki={}
#x=True#
#
#while x==True:
#    y=True#
#
#    kategoria=input("podaj kategorie lub  napisz X by wyjść")
#    if kategoria=="X":
#        x=False
#    else:
#        wydatki[kategoria]=[]
#        while y==True:
#            cena=input("opodaj ilosc jakie wydałes na owy wydatek albo nacisj Y by zakonaczy program")
#            if cena=="Y":
#                y=False
#            else:
#                cena=int(cena)
#                wydatki[kategoria].append(f"{cena} ")
#
#print(wydatki)





#ważne zadanie do zrozumienia
wydatki={}
wydatki_total=0
wydatki_total_sposob=0
x=True

while x==True:
    y=True

    kategoria=input("podaj kategorie lub  napisz X by wyjść")
    if kategoria=="X":
        x=False
    else:
        wydatki[kategoria]=[]
        while y==True:
            cena=input("opodaj ilosc jakie wydałes na owy wydatek albo nacisj Y by zakonaczy program")
            if cena=="Y":
                y=False
            else:
                cena=float(cena)
                wydatki_total+=cena
                wydatki[kategoria].append(cena)
for i in wydatki.values():
    wydatki_total_sposob+=sum(i)
print(wydatki_total_sposob)
print(wydatki_total)
procenty={}
for z,r in wydatki.items():
    katname=z
    total_w_lista=sum(r)
    procenty[katname]=total_w_lista*100/wydatki_total
    print(procenty[katname])
mi=None
mi_p=0

for c,p in procenty.items():
    if p>mi_p:
        mi_p=p
        mi=c

print(f" najwiecje wydajesz na  {mi} to jest {mi_p} %")