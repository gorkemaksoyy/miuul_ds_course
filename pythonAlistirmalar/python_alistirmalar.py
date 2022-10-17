###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)


l = [1, 2, 3, 4,"String",3.2, False]
type(l)


d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)


s = {"Python", "Machine Learning", "Data Science","Python"}
type(s)



###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."

text = text.replace(",", " ").replace("."," ")
#text = text.replace("."," ")
text

text = text.upper()
space = []
new_list = []

space = [index for index,letter in enumerate(text) if letter ==" "]
'''for index, letter in enumerate(text):
    if letter == " ":
        space.append(index)'''
space
h=0
'''new_list = [text[h:index] if index-h>1 h=index+1 for index in space ]''' #list comprehension yapıları çoklu komutlar için uygun değil
for index in space:
    if index - h > 1:
        new_list.append(text[h:index])
    h = index +1 #+1 ile boşlukların listeye alınmaması sağlanır
new_list
###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.
lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.
lst[0:4]

# Adım 4: Sekizinci index'teki elemanı silin.
del lst[8]
lst
# Adım 5: Yeni bir eleman ekleyin.
lst.append("N")
lst

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.
lst.insert(8,"N")
lst


###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}



# Adım 1: Key değerlerine erişiniz.
dict.keys()


# Adım 2: Value'lara erişiniz.
dict.values()


# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"][1] = 13
dict

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict["Ahmet"] = ["Turkey", 24]
dict

# Adım 5: Antonio'yu dictionary'den siliniz.
del dict["Antonio"]
dict



###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

def tekciftayir(list):
    tek_sayilar = []
    cift_sayilar = []
    for item in list:
        if item % 2 == 0:
            cift_sayilar.append(item)
        else:
            tek_sayilar.append(item)
    return tek_sayilar, cift_sayilar

tekciftayir([2,13,18,93,22])


###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for index,ogrenci in enumerate(ogrenciler):
    if index < 3:
        print(f"Mühendislik fakültesi {index+1}. öğrenci: {ogrenci}")
    else:
        print(f"Tıp fakültesi {index-2}. öğrenci: {ogrenci}")


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

dersler = list(zip(ders_kodu, kredi, kontenjan))

for ders_listesi in dersler:
    print(f"Kredisi {ders_listesi[1]} olan {ders_listesi[0]} kodlu dersin kontenjanı {ders_listesi[2]} kişidir")

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))


name = "gorkem"
name.upper()
upper(name)
type(len("gorkem"))

numbers = range(10)
new_dict = {i:i**2 for i in numbers if i%2 == 0}
new_dict

#List ve dict comprehensions uygulamaları
import seaborn as sns
df =sns.load_dataset("car_crashes")
df.columns

new_columns = ["flag_" + columns if "ins" in columns else "no_flag_"+columns for columns in df.columns]
new_columns

my_list = ['mean', 'min', 'max', 'var']
number_list = [col for col in df.columns if df[col].dtype == ("float64" or "int64")]
my_dict = {columns:my_list for columns in df.columns if df[columns].dtype == ("float64" or "int64")}
my_dict
df[number_list].agg(my_dict)