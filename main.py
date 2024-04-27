import math

boy=[171,165,185,180,160,172,173,175,180,170]
kilo=[70,84,70,87,55,90,73,60,83,50]
tur=["normal","kilolu","zayıf","normal","normal","kilolu","normal","zayıf","normal","zayıf"]

b=float(input("bir boy giriniz:"))
o=float(input("bir kilo giriniz:"))
k=int(input("bir k değeri giriniz:"))
#öklid uzaklığı hesaplama ve boş diziye ekleme
dizi={}
for i in range(len(boy)):
    bfark=boy[i]-b
    ofark=kilo[i]-o
    u=math.sqrt(pow(bfark,2)+pow(ofark,2))
    dizi.update({i:u})
    
print(dizi)    
    
diziSirala={k: v for k, v in sorted(dizi.items(), key=lambda item: item[1])}
print(diziSirala)

for i in diziSirala:
    print(boy[i],"  ",kilo[i],"  ",i,"  ",tur[i],"  ",diziSirala[i])
    
dizi_list=list(diziSirala)


k_list=[]
for i in range(k):
    k_list.append(tur[dizi_list[i]])
    
print(k_list)    
normal=zayif=kilolu=0

normal=k_list.count("normal")
zayif=k_list.count("zayıf")
kilolu=k_list.count("kilolu")

if(normal>zayif and normal>kilolu):
    print("sınıflandırma sonucu= normal ")
elif(zayif>normal and zayif>kilolu):
    print("sınıflandırma sonucu= sayıf")
else:
    print("sınıflandırma sonucu= kilolu")    
    
        
   