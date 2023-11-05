#Uzatilgan Habarlar
import telebot
from Rassom import rasim
from Chat import chat
import requests

bot = telebot.TeleBot("6245763374:AAEmPS_k1hn34D1jZ1EhZ1KnYd8hZE-aBcM")
hammagajonat=False

try:
	mavjud_id=open('idlar.txt','r')
	mavjud_id.close()
	mavjud_id = open('malumotlar.txt', 'r')
	mavjud_id.close()
except:
	mavjud_id=open("idlar.txt",'w')
	mavjud_id.close()
	mavjud_id = open("malumotlar.txt", 'w')
	mavjud_id.close()

@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message, """Foydalanish qoʻllanmasi:\nChat: Sizni qiziqtirgan savol\nRasm: Koʻrmoqchi boʻlgan rasmingiz""")
	user = message.from_user

	ismi = str(user.first_name)
	fnomi = str(user.username)
	# tel = user.contact.phone_number if user.contact else None

	malumotlar=open("malumotlar.txt",'a')
	idlar=open("idlar.txt",'a')
	mavjud_id=open('idlar.txt','r')
	mavjud_idlar=mavjud_id.read().split("\n")
	# print(user)
	if not str(message.chat.id) in mavjud_idlar:
		# print(f"{ismi} {fnomi} {message.chat.id}")
		try:
			malumotlar.write(f"{ismi}    @{fnomi}    {message.chat.id}\n")
		except:
			malumotlar.write(f"Ismida xatolik    @{fnomi}    {message.chat.id}\n")
		idlar.write(f"{message.chat.id}\n")
	mavjud_id.close()
	idlar.close()
	malumotlar.close()

@bot.message_handler(func=lambda message: message.text and message.text.lower().startswith("rasm:"))
def rasm_handler(message):
	bot.reply_to(message, "Buyuruq qabul qilindi. Javobni olish ozgina vaqt olish mumkin.")
	try:
		rasm_url = rasim(message.text.split(":")[1])
		with open("image2.jpg", "wb") as file:
			response = requests.get(rasm_url)
			file.write(response.content)
		photo = open("image2.jpg", "rb")
		bot.send_photo(message.chat.id, photo, message.text.split(":")[1])

	except:
		bot.reply_to(message, "Natija olish uchun aniqroq yozing")

@bot.message_handler(func=lambda message: message.text and message.text.lower().startswith("chat:"))
def chat_handler(message):
	try:
		response = chat(message.text.split(":")[1])
		bot.reply_to(message, response)
	except:
		bot.reply_to(message,  "Natija olish uchun aniqroq yozing.")

@bot.message_handler(func=lambda message: hammagajonat and message.chat.id==1864080124)
def chat_handler(message):
	print("HJ ishga tushdi")
	mavjud_id=open('idlar.txt','r')
	mavjud_idlar=mavjud_id.read().split("\n")
	xabar=message.text

	for i in mavjud_idlar:
		try:	
			bot.send_message(i,xabar)
		except:
			bot.send_message("1864080124","Xammaga habar jo'natildi")
@bot.message_handler(func=lambda message: (message.chat.id==1864080124))
def boshqaruvchi(message):
	global hammagajonat, habar
	if message.text.lower()=="idlar" or message.text.lower()=='/idlar':	
		mavjud_id=open('malumotlar.txt','r')
		try:	
			bot.send_message("1864080124",mavjud_id.read())
		except:
			bot.send_message("1864080124","Malumotlar bazasida IDlar mavjud emas")
		mavjud_id.close()
	elif message.text.lower()=="hammaga jo'nat" or message.text.lower()=="hammaga jonat" or message.text.lower()=="hammaga jo'nat rejimi" or message.text.lower()=="hammaga jonat rejimi" or message.text.lower()=="/hj":
		if hammagajonat:
			hammagajonat=False
			bot.unpin_chat_message("1864080124", habar)
			bot.send_message('1864080124', "Hammaga jo'natish rejimi o'chirildi")
		else:
			hammagajonat=True
			habar = bot.send_message('1864080124', "Hammaga jo'natish rejimi ishga tushdi")
			habar = habar.message_id
			bot.pin_chat_message("1864080124", habar)
		# print(hammagajonat and message.chat.id==1864080124)

bot.polling()
print("Tugadi")