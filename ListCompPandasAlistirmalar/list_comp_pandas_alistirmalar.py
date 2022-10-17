
##################################################
# List Comprehensions
##################################################
#NOTLAR: Pandas series ile  numpy array farkı pandas'daki ixdex'ler
#set ile numpy'a bir giriş olursa içerdeki veri tipine uyum sağlar, apend yaparsak, içerdekiler gelene uyum sağlar,
#mesela içerde hep integer varken float gelirse set ile, float'ı int'e çevirir, append ile hepsi float olur
# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()
df.total
df[total]
df["total"].dtype
str(df["total"].dtype)
["NUM_" + column.upper() if df[column].dtype != "O"
 else column.upper() for column in df.columns]   #"O" ile kategorik tüm değişkenleri ifade edebiliriz (bool hariç!)

["NUM_" + column.upper() if str(df[column].dtype) not in ["bool", "object", "category"]
 else column.upper() for column in df.columns]

['NUM_' + columns.upper() if (df[columns].dtype == 'float' or df[columns].dtype == 'int')
 else columns.upper() for columns in df.columns]   #int32 veya int 64 gibi farklılıklar olabilir, en sağlam çözüm ilk seçenek

['NUM_' + i.upper() if df[i].dtype != "O"
 else i.upper() for i in df]   #bunu yapma çünkü tüm dataframe üzerinden döngü olacağı için computation time uzun sürer

for i in df.head(10):
    print(i)
    print(df[i].dtype)
# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin
# isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']
[column.upper() + "_FLAG" if "no" not in column else column.upper() for column in df.columns]

[column.upper() if "no" in column else column.upper() + "_FLAG" for column in df.columns]
#find metodu ile de çözülebilir
# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################

og_list = ["abbrev", "no_previous"]

# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#

new_columns = [columns for columns in df.columns if columns not in og_list]
new_columns
new_df = df[new_columns]
new_df.head()
df.head()





##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################

titanic = sns.load_dataset("titanic")
titanic.head()
#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

titanic["sex"].value_counts()


#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################
titanic.nunique()    # en güzel yöntem

titanic["sex"].unique()    #unique fonksiyonu pandas series üzerinden çalışıyor fakat nunique dataframe üzerinden çalışıyor

pd.DataFrame(index= titanic.columns, data=[titanic[columns].nunique() for columns in titanic.columns])

titanic[[columns for columns in titanic.columns]].nunique()

for columns in titanic.columns:
    print(columns, titanic[columns].nunique())


#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

titanic.pclass.unique()


#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

titanic[["pclass", "parch"]].nunique()


#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

titanic[["embarked"]].info()
titanic["embarked"] = titanic['embarked'].astype("category")   #atama yapmazsak astype değişmez!
titanic[["embarked"]].info()

titanic["embarked"] = pd.Categorical(titanic.embarked)
titanic[["embarked"]].info()

#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

titanic[titanic["embarked"] == "C"].head()      #loc yapısı olmadan da filtreleme yapılabiliyor
titanic.loc[titanic["embarked"] == "C", :].head()

#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

titanic[titanic["embarked"] != "S"].head()
titanic.loc[titanic["embarked"] != "S", :]

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

titanic[(titanic["age"] < 30) & (titanic["sex"] == "female")].head()
titanic.loc[(titanic["age"] < 30) & (titanic["sex"] == "female")].head()

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

titanic[(titanic["fare"] > 500)  | (titanic["age"] > 70)].head()
titanic.loc[(titanic["fare"] > 500)  | (titanic["age"] > 70)]

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

titanic.isnull().sum()


#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

titanic.drop("who", axis=1, inplace=True).head()
titanic.head()

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

titanic[["deck"]].info()
titanic["deck"].value_counts().idxmax()
titanic["deck"].value_counts()
titanic["deck"].mode()[0]   #alternatif yöntem  (daha yaygın,  tavsiye edilen)
titanic["deck"].fillna(titanic["deck"].mode()[0], inplace=True)
titanic.deck
titanic["deck"].value_counts()


#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

titanic["age"].median()
titanic["age"] = titanic.age.fillna(titanic["age"].median())
titanic.age.isnull().sum()
#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################
titanic.groupby(["pclass", "sex"]).agg({"survived":["sum","count","mean"]})

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################



def new_column1(dataframe):
    dataframe["age_flag"] = [1 if index < 30 else 0 for index in dataframe["age"]]

new_column1(titanic)
titanic.head()
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset("titanic")

titanic["age_flag"] = titanic["age"]
titanic["age_flag"] = titanic.loc[:, "age_flag"].apply(lambda x: 1 if x<30 else 0)
titanic.head()

titanic["age_flag"] = titanic.age.apply(lambda x: 1 if x<30 else 0)
titanic.head()

def new_column(age):
    if age < 30:
        return 1
    else:
        return 0

titanic["age_flag"] = titanic.loc[:, "age"].apply(new_column)
titanic.head()
#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

import pandas as pd
import seaborn as sns

tips = sns.load_dataset("Tips")
tips.info()

#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

tips.groupby("time").agg({"total_bill":["sum","min","max", "mean"]})

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

tips.groupby(["day","time"]).agg({"total_bill":["sum","min","max", "mean"]})

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################
#aşağıdaki kodda and komutunun iki tarafındaki girdilerin parantezle kapatılması önemli!
tips.loc[(tips["sex"] == "Female") & (tips["time"] == "Lunch")].groupby(["day"]).agg({"total_bill": ["sum", "min", "max", "mean"],
                                                                                         "tip": ["sum", "min", "max", "mean"]})

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

tips.loc[(tips["size"] < 3) & (tips["total_bill"] > 10), ["total_bill"]].mean()
tips.loc[(tips["size"] < 3) & (tips["total_bill"] > 10)].agg({"total_bill": "mean"})

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

tips["total_bill_tip_sum"] = tips["total_bill"] + tips["tip"]
tips["total_bill_tip_sum"]
tips.head()

#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

tips.sort_values("total_bill_tip_sum", ascending=False, inplace=True)
new_tips = tips.head(30)
new_tips.head()
new_tips.reset_index()

def alternating(string):  #alternating isimli fonk. tanımlanmış, içerisine string isimli bir parametre girilmesi isteniyor
    new_string = ""       #new_string isimli boş string tipinde bir değişken tanımlanmış

    for string_index in range(len(string)): #kullanıcı tarafından girilecek string argümanındaki karakter sayısı kadar dönecek bir loop
        if string_index % 2 == 0:           #string argümanındaki i.karakterin index'i çiftse bir alttaki işlemi yap değilse else'den devam et
            new_string += string[string_index].upper()   #new_string isimli boş değişkenimize, girdiğimiz argümanın 2'ye bölünen indekslerindeki harflerin büyüğünü yazdır
        else:
            new_string += string[string_index].lower()  #new_string isimli boş değişkenimize, girdiğimiz argümanın 2'ye bölünmeyen indekslerindeki harflerin küçüğünü yazdır

    print(new_string)        #for loop tamamlandıktan sonra yukarı belirtilen koşullara göre oluşacak new_string değişkenini yazdır

# enumerate ile yaz:
def alternating(string):
    new_string = ""
    for index,character in string:
        if index % 2 == 0:
            new_string += character.upper()
        else:
            new_string += character.lower()

    print(new_string)

new_string = 'BASARIHERGUNTEKRARLANANKUCUKCABALARINTOPLAMIDIR'

letter_index = 0
slide = 5
part_length = 10
letter_index_dict = {}
letter_index_list = []
frequent_letters = ""
ten_letter_words = []

#5'er 5'er kayarak 10 harfli kelimeleri listeye alır ve yazdırır
for harf in range(0, len(new_string), slide):
    if len(new_string) >= letter_index + part_length:
        ten_letter_words.append(new_string[letter_index:letter_index + part_length])
        print(ten_letter_words[-1])
    letter_index = letter_index + 5
#10 harfli kelimelerde en çok tekrarlanan harfleri bulur
for words in ten_letter_words:
    for letters in words:
        if letters in letter_index_dict:
            letter_index_dict[letters] += 1
        else:
            letter_index_dict[letters] = 1
    letter_index_list = sorted(list(zip(letter_index_dict.values(), letter_index_dict.keys())),reverse=True)   #set ile yapmak daha mantıklı!
    frequent_letters += letter_index_list[0][1]

    for index, thing in enumerate(letter_index_list):
        if index == 0:
            continue
        elif thing[0] == letter_index_list[0][0]:
            frequent_letters += thing[1]
        else:
            break

    print(frequent_letters)
    letter_index_dict = {}
    letter_index_list = []
    frequent_letters = ""

import seaborn as sns
df = sns.load_dataset("titanic")
df["sex"].describe([0.25, 0.50, 0.75])


