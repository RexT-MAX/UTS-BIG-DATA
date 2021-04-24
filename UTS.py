import nltk
raw_input = input

nama = ("Aldorei Praka")
nim = ("04119006")
prodi =("Sistem Komputer")
print ("Nama  = " + nama)
print ("NIM   = " + nim)
print ("Prodi = " + prodi)

print ("")
print("")
kata = raw_input("Masukan kata-katamu =")

hasil = nltk.word_tokenize(kata)
print("")
print(hasil)