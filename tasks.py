# task 1 
# Foydalanuvchidan matn qabul qiling , unda "gaz" , "svet", "yo'q" kabi so'zlar ishtirok etganmi yoki yo'qmi aniqlang va ular sonini har birini alohida hisoblab boring so'zlar register turi yoki boshqa qoshimchalar bilan kelishi mumkin bularni ham inobatga oling

# Gaz yo'q ekan lekin svet bor svetamuzika

# gaz = 1
# svet = 2
# text = "Gaz yo'q ekan lekin svet bor svetamuzika gazini bos"
# gaz = 0
# svet = 0
# no = 0
# for t in text.split(" "):
#     if t.lower() == "gaz" or "gaz" in t.lower():
#         gaz += 1
#     if t.lower() == "svet" or "svet" in t.lower():
#         svet += 1
#     if t.lower() == "yo'q":
#         no += 1
# print(f"\ngaz={gaz}\nsvet={svet}\nno={no}")

# task 2 
# quyidagi shartlarni tekshirib parol togri yoki notogriligini aniqlaydigan dastur tuzing
# password:
#     - minimum 6 ta belgi 
#     - kamida bitta katta harf 
#     - kamida bitta maxsus belgi (/,\,@,/,_,-)

# v = "Salom#Qalesan#Alik#"
# l = len(v)
# card = "8600 1600 2530 1535"
# c = 0
# result = ""

# for n in card.split(" "):
#     if c == 3:
#         result += n 
#     else:
#         result += "**** "
#         c += 1
# print(result)

# task 3 
# n soni berilgan (30 > n > 0) 0 dan n gacha bo'lgan sonlarni orasida probellar bilan chiqaring agar son toq bo'lsa bitta probel bilan uni keyingi son orasini belgilaysiz agar juft bo'lsa 2 ta probel bilan. misol : 0  1 2  3 4  5

# task 4 
# 1 dan  500 gacha sanab barcha 7 sonlarini alohida massivga yozing;
# Masalan nums = [7,17,27……]

# sevens = []
# for i in range(1,501):
#     if "7" in str(i):
#         sevens.append(i)
# print(sevens)

# print([x for x in range(1,501) if "7" in str(x)])

# task 5
# import random
# user = {
#     "name":"Mike Dean",
#     "key_number":"*****"
# }
#  Ushbu dict  uchun key_number maydoniga name maydoni qiymati uzunligida 1 dan 50 gacha bo’lgan sonlardan tasodifiy sonlar hosil qiling
# key_nums = ""
# for i in range(len(user["name"])):
#     n = random.randint(1,9)
#     key_nums += str(n)
# user["key_number"] = key_nums

# print(user) # {'name': 'Mike Dean', 'key_number': '986572342'}

# task 6 
# Berilgan massivdan sonlarni bir xillarini olib tashlab faqat sanoqdagi ketma-ket sonlarni qoldiring
# Masalan arr = [1,5,6,1,8,5,9]  Output/Javob arr = [1,5,6,8,9]
# Sizga berilgan Massiv bu >> arr = [2,6,6,4,7,8,2,9,7,1,9]

# task 7 

# Kinoteatrda 15 ta qator  bor har bir qatorda 20 tadan o'rin bor. O'rindiqlar seriya raqamlangan
# misol : A12 A bu yerda qator tartib harfi 12 esa  o’rindiq tartib raqami siz foydalanuvchi kiritgan seriya raqamiga qarab o’rindiq qaysi qatorda joylashganini topishingiz kerak. Bundan tashqari random shaklda o’rindiqlar band qilinadi , Kinoteatr 50% ga to’ldiriladi siz foydalanuvchi kiritgan o’rindiq band yoki bosh ekanini chiqarishingiz kerak.

# task 8 
# 9 qavatli uyda 3-ta podyezd bor har bir qavatda 6 tadan kvartira bor. Foydalanuvchi kvartira raqamini kiritsa siz topishingiz kerak;
# (kvartiralar raqamlari 1-chi qavatdan 1-podyezdan boshlanadi : 1-kv , 1-podyezd 1-etaj)
# Kvartira qaysi qavatda ekanini
# Kvartira qaysi podyezdda ekanini



# task 9 
# Istalgan turdagi elementlari mavjud bolgan massivdan faqat sonlarini topib ularni yigindisini hisoblovchi dastur tuzing (Faqat musbat sonlar hisoblanadi)
# l = [True , 1 , 0.3, "one", ["1","uu"]]
# output: 1.3 


# task 10 
# Qiymatlarida butun sonlar berilgan  2 ta dict mavjud siz dictlarda bir xil qiymatga ega elementlarni boshqa random sonlarga almashtirishingiz kerak 
# input:
# a = {"a":5,"b":3}
# b = {"a":2,"b":1, "c":3}
# # output:
# a = {"a":5,"b":8}
# b = {"a":2,"b":6}

# task 11 
# Odil har kuni muntazam 9 soatdan uxlashni reja qilgan. Siz uning uchun u soat nechida uxlashga yotsa roppa rosa 9 soatdan keyin soat nechi bo’lishini hisoblaydigan dastur yozishingiz kerak. Agar Tohir soat 22:00 da uhlashga yotsa demak uyg’onganida soat 07:00 bo’lishini ko’rsatishingiz kerak.
# Kirish : ‘22:00’
# Chiqish : ‘07:00’
# st = "21:30"
# print(abs(9-(24 - int(st.split(":")[0]))) ,":", int(st.split(":")[1])) 

# task 12
# Abdulloh ni Asaka Bank da har oy kirim X mln puli bor va davlatga shu daromad pullaridan 12% daromad solig’i to’lashi kerak. Abdulloh bu yilning 5- oyda davlatimizga qancha soliq to’lashini hisoblang.// x=int(input())