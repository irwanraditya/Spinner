##SOAL 2 - List Spinner
def counterClockwise(input): #Buat function terlebih dahulu
    puter = [
           [input[0][2],input[1][2],input[2][2]], #menjadikan list baru dengan index ke-2 dimasing" list sebagai list pertama dari tiap" list 
           [input[0][1],input[1][1],input[2][1]], #menjadikan list baru dengan index ke-1 dimasing" list sebagai list kedua dari tiap" list 
           [input[0][0],input[1][0],input[2][0]]] #menjadikan list baru dengan index ke-0 dimasing" list sebagai list ketiga dari tiap" list 
    return puter #Return hasil dari output yang didapat

print(counterClockwise([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]))