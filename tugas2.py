

def faktorial(n):        
    #nama fungsinya faktorial dengan parameter n
    # def=mendefinisikan  sebuah fungsi dan memiliki argumen(parameter)
    if n == 0:
        return 1
    else:               #pada kondisi lainya 
        faktor=n * faktorial(n-1)     #rumus
        return faktor
    
# input dari pengguna
bilangan = int(input("memasukan bilangan positif : "))

# memeriksa apakah bilangan positif
if bilangan < 0:
    print("faktorial hanya didefinisikan untuk bilangan positif")
else:
    hasil = faktorial(bilangan)
    print(f"faktorial dari" ,bilangan, "adalah", hasil)
