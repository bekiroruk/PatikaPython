2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
         
     
         
#CODE
         
input = [[1, 2], [3, 4], [5, 6, 7]]
new_l = []
         
def reverse(x):
    for i in x:
        if isinstance(i,list):
            reverse(i)
        else:
            new_l.append(i)
    return new_l[::-1]
         
print(reverse(input)
