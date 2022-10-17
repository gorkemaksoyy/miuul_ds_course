
#############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
#############################################

#############################################
# İş Problemi
#############################################
# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler oluşturup bu segmentlere göre yeni gelebilecek müşterilerin şirkete
# ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

# Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.


#############################################
# Veri Seti Hikayesi
#############################################
# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu ürünleri satın alan kullanıcıların bazı
# demografik bilgilerini barındırmaktadır. Veri seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı tablo
# tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir kullanıcı birden fazla alışveriş yapmış olabilir.

# Price: Müşterinin harcama tutarı
# Source: Müşterinin bağlandığı cihaz türü
# Sex: Müşterinin cinsiyeti
# Country: Müşterinin ülkesi
# Age: Müşterinin yaşı

################# Uygulama Öncesi #####################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17

################# Uygulama Sonrası #####################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#############################################
# PROJE GÖREVLERİ
#############################################

#############################################
# GÖREV 1: Aşağıdaki soruları yanıtlayınız.
#############################################

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd
kts = pd.read_csv("VeriGorsellestirme_KesifciVeriAnalizi/Kural Tabanl─▒ S─▒n─▒fland─▒rma/persona.csv")
kts.head()
kts.info()
# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
kts.SOURCE.nunique()
kts.SOURCE.value_counts()
# Soru 3: Kaç unique PRICE vardır?
kts.PRICE.nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
kts.PRICE.value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
kts.COUNTRY.value_counts()



# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
kts.groupby("COUNTRY").agg({"PRICE":"sum"})



# Soru 7: SOURCE türlerine göre göre satış sayıları nedir?
kts.SOURCE.value_counts()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
kts.groupby("COUNTRY").agg({"PRICE":"mean"})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
kts.groupby("SOURCE").agg({"PRICE":"mean"})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
kts.groupby(["COUNTRY","SOURCE"]).agg({"PRICE":"mean"})

#############################################
# GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################
kts.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"})

#############################################
# GÖREV 3: Çıktıyı PRICE'a göre sıralayınız.
#############################################
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE'a uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.
agg_df = kts.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"mean"})\
    .sort_values("PRICE",ascending=False)
agg_df

#############################################
# GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.
# İpucu: reset_index()
agg_df.reset_index(inplace=True)
agg_df


#############################################
# GÖREV 5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.
#############################################
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici olacağını düşündüğünüz şekilde oluşturunuz.
# Örneğin: '0_18', '19_23', '24_30', '31_40', '41_70'
age_categories = [0,18,23,30,40,70]
kts["AGE_CAT"] = pd.cut(kts["AGE"], age_categories, labels=["0_18","19_23","24_30","31_40","41_70"])
kts.AGE_CAT
[kts[col] for col in kts]
kts.info()
#############################################
# GÖREV 6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################
# customers_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.
# Dikkat!
# list comp ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.
kts["customers_level_based"] = ""

#[kts["customers_level_based"].values[index] = str(kts.COUNTRY[index]) + \
#                                                 "_" + str(kts.SOURCE[index]) + "_" + \
#                                                 str(kts.SEX[index]) + "_" + str(kts.AGE_CAT[index]) for index in range(len(kts.AGE))]

for index in range(len(kts.AGE)):
    kts["customers_level_based"].values[index] = str(kts.COUNTRY[index]) + \
                                                 "_" + str(kts.SOURCE[index]) + "_" + \
                                                 str(kts.SEX[index]) + "_" + str(kts.AGE_CAT[index])
kts["customers_level_based"]

segmentation = kts.groupby("customers_level_based").agg({"PRICE":"mean"}).sort_values("PRICE", ascending=False).reset_index()
segmentation
#############################################
# GÖREV 7: Yeni müşterileri (USA_ANDROID_MALE_0_18) segmentlere ayırınız.
#############################################
# PRICE'a göre segmentlere ayırınız,
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz,
# segmentleri betimleyiniz,
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], q=4, labels=["A","B","C","D"])
agg_df.head()
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean","min", "max", "sum"]})
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], age_categories, labels=["0_18","19_23","24_30","31_40","41_70"])

#############################################
# GÖREV 8: Yeni gelen müşterileri sınıflandırınız ne kadar gelir getirebileceğini tahmin ediniz.
#############################################
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
predicted_segment_1 = agg_df.loc[(agg_df["SOURCE"] == "android")&(agg_df["COUNTRY"] == "tur")&
           (agg_df["AGE_CAT"] == "31_40")&(agg_df["SEX"] == "female")]["SEGMENT"].mode()[0]
predicted_segment_1
predicted_value_1 = agg_df.loc[(agg_df["SOURCE"] == "android")&(agg_df["COUNTRY"] == "tur")&
           (agg_df["AGE_CAT"] == "31_40")&(agg_df["SEX"] == "female")].agg({"PRICE":["mean"]})
predicted_value_1
predicted_value_1_alt = segmentation["PRICE"].loc[segmentation["customers_level_based"] == "tur_android_female_31_40"]
predicted_value_1_alt
# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?
predicted_segment_2 = agg_df.loc[(agg_df["SOURCE"] == "ios")&(agg_df["COUNTRY"] == "fra")&
           (agg_df["AGE_CAT"] == "31_40")&(agg_df["SEX"] == "female")]["SEGMENT"].mode()[0]
predicted_segment_2
predicted_value_2 = agg_df.loc[(agg_df["SOURCE"] == "ios")&(agg_df["COUNTRY"] == "fra")&
           (agg_df["AGE_CAT"] == "31_40")&(agg_df["SEX"] == "female")].agg({"PRICE":["mean"]})
predicted_value_2
predicted_value_2_alt = segmentation["PRICE"].loc[segmentation["customers_level_based"] == "fra_ios_female_31_40"]
predicted_value_2_alt