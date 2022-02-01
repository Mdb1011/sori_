from re import findall
from rubika.client import Bot
from requests import get
from rubika.encryption import encryption
from rubika.tools import Tools
import requests
import time
import random
import colorama
import os
os.system("clear")
print("\033[33m bot is runing.........")
nam = "u0D5lXz0bcc92aa5b6b65c858c3d9fec"
bot = Bot("mgomyvhxwldtozjueniimlnwfcfawxjw")
target = "g0BMyaq06dd2ab6b5df08db0b2ffa0a2"

def hasInsult(msg):
	swData = [False,None]
	for i in open("dontReadMe.txt").read().split("\n"):
		if i in msg:
			swData = [True, i]
			break
		else: continue
	return swData

def hasAds(msg):
	links = list(map(lambda ID: ID.strip()[1:],findall("@[\w|_|\d]+", msg))) + list(map(lambda link:link.split("/")[-1],findall("rubika\.ir/\w+",msg)))
	joincORjoing = "joing" in msg or "joinc" in msg

	if joincORjoing: return joincORjoing
	else:
		for link in links:
			try:
				Type = bot.getInfoByUsername(link)["data"]["chat"]["abs_object"]["type"]
				if Type == "Channel":
					return True
			except KeyError: return False

# static variable
answered, sleeped, retries = [], False, {}

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		open("id.txt","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if hasInsult(msg.get("text"))[0] and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif hasAds(msg.get("text")) and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])

					elif "forwarded_from" in msg.keys() and bot.getMessagesInfo(target, [msg.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!stop" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("!ban") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(guid, "🚫 کاربر عزیز به دلیل رعایت نکردن قوانین گروه شما از گروه حذف شدید\n\n @sori_bot", message_id=msg.get("message_id"))
								bot.block(guid)
								
							else :
								bot.sendMessage(target, "❎", message_id=msg.get("message_id"))
					
						except IndexError:
							bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
							bot.sendMessage(target, "✅", message_id=msg.get("message_id"))
							
					
					elif msg.get("text").startswith("!send") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], ""+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))
					
					
					elif msg.get("text") == "خوبی" and msg.get("author_object_guid") :
						bot.sendMessage(target, "آره عشقم تو چطوری ؟", message_id=msg.get("message_id"))
					elif msg.get("text") == "هعب" and msg.get("author_object_guid") :
						bot.sendMessage(target, "اری هعب", message_id=msg.get("message_id"))
					elif msg.get("text") == "سلام" and msg.get("author_object_guid") :
						bot.sendMessage(target, "سلام عشقم چطوری 🥰❤", message_id=msg.get("message_id"))
					elif msg.get("text") == "خوبم" and msg.get("author_object_guid") :
						bot.sendMessage(target, "شکر خدا😍😁", message_id=msg.get("message_id"))
					elif msg.get("text") == "چه خبر" and msg.get("author_object_guid") :
						bot.sendMessage(target, "برف اومده تا کمر😲", message_id=msg.get("message_id"))
					elif msg.get("text") == "نه" and msg.get("author_object_guid") :
						bot.sendMessage(target, "جهنم", message_id=msg.get("message_id"))
					elif msg.get("text") == "چطوری" and msg.get("author_object_guid") :
						bot.sendMessage(target, "هعی یه نفسی میاد و میره😇", message_id=msg.get("message_id"))
					elif msg.get("text") == "بی ادب" and msg.get("author_object_guid") :
						bot.sendMessage(target, "چیکا کنم ممد یادم داده😕\n\n ☎اینم آیدیش: \n📢 @mamal_fi", message_id=msg.get("message_id"))
					elif msg.get("text") == "زر نزن" and msg.get("author_object_guid") :
						bot.sendMessage(target, "تو بزن😕", message_id=msg.get("message_id"))
					elif msg.get("text") == "باش" and msg.get("author_object_guid") :
						bot.sendMessage(target, "آفرین بیا موزتو بگیر برو تو قفست🍌", message_id=msg.get("message_id"))
					elif msg.get("text") == "کونی" and msg.get("author_object_guid") :
						bot.sendMessage(target, "لاپات بستنی نونی🙅😂", message_id=msg.get("message_id"))
					elif msg.get("text") == "هعی" and msg.get("author_object_guid") :
						bot.sendMessage(target, "لوله گاز👌", message_id=msg.get("message_id"))
					elif msg.get("text") == "فعلا" and msg.get("author_object_guid") :
						bot.sendMessage(target, "نرو بدون تو شبم سیاهه سیاهه🌚🌝", message_id=msg.get("message_id"))
					elif msg.get("text") == "بای" and msg.get("author_object_guid") :
						bot.sendMessage(target, "نرو برنج خیس کردم🍚", message_id=msg.get("message_id"))
					elif msg.get("text") == "مرسی" and msg.get("author_object_guid") :
						bot.sendMessage(target, "خاله خرسی🌝", message_id=msg.get("message_id"))
					elif msg.get("text") == "خودتو معرفی کن" and msg.get("author_object_guid") :
						bot.sendMessage(target, "سوری هستم نفس شما \n یه عقابه سینگل👸", message_id=msg.get("message_id"))
					elif msg.get("text") == "سوری" and msg.get("author_object_guid") :
						bot.sendMessage(target, "جانم جیگر طلام??", message_id=msg.get("message_id"))
					elif msg.get("text") == "چند سالته" and msg.get("author_object_guid") :
						bot.sendMessage(target, "من قصد ازدواج ندارم مزاحم نشو😏", message_id=msg.get("message_id"))
					elif msg.get("text") == "رل میخام" and msg.get("author_object_guid") :
						bot.sendMessage(target, "من تورو دیشب در ماه دیدم😮", message_id=msg.get("message_id"))
					elif msg.get("text") == "حوصلم" and msg.get("author_object_guid") :
						bot.sendMessage(target, "بگو ممد", message_id=msg.get("message_id"))
					elif msg.get("text") == "ممد" and msg.get("author_object_guid") :
						bot.sendMessage(target, "قربون عمت😂😍", message_id=msg.get("message_id"))
					elif msg.get("text") == "گدرت" and msg.get("author_object_guid") :
						bot.sendMessage(target, "کاکتوس اعتماد بنفس تورو داشت سالی دوباره موز میداد😟", message_id=msg.get("message_id"))
					elif msg.get("text") == "خاک" and msg.get("author_object_guid") :
						bot.sendMessage(target,("message_id"))
					elif msg.get("text") == "رل پی" and msg.get("author_object_guid") :
						bot.sendMessage(target, "برو به درگاه الهی توبه کن،کافر🧕", message_id=msg.get("message_id"))
					elif msg.get("text") == "سیلام" and msg.get("author_object_guid") :
						bot.sendMessage(target, "مثل آدم بگو سلام این ادا اطفار ها چیه😐", message_id=msg.get("message_id"))
					elif msg.get("text") == "ربات" and msg.get("author_object_guid") :
						bot.sendMessage(target, "ربات عمته من،گدرتمندم😽", message_id=msg.get("message_id"))
					elif msg.get("text") == "ممنان" and msg.get("author_object_guid") :
						bot.sendMessage(target, "خیر ممه و نان😎", message_id=msg.get("message_id"))
					elif "ممل" in msg.get("text"):
						bot.sendMessage(target, "از عشقم غیبت نکن", message_id=msg.get("message_id"))
					elif "سوری جون" in msg.get("text"):
						bot.sendMessage(target, "با من کاری داشتید\nآخه صدام زدید😁", message_id=msg.get("message_id"))
					elif "چجور" in msg.get("text"):
						bot.sendMessage(target, "بایا کن😕", message_id=msg.get("message_id"))
					elif "رلم" in msg.get("text"):
						bot.sendMessage(target, "رل رل نکن من قصد ازدواج ندارم \nمن عاشق مملم😶", message_id=msg.get("message_id"))
					elif "بریم" in msg.get("text"):
						bot.sendMessage(target, "کجایی لوکیشن بده بیام بالاسرت👩", message_id=msg.get("message_id"))
					elif "https://rubika.ir/joinc" in msg.get("text"):
						bot.deleteMassages(target, message_id=msg.get("message_id"))
					elif "بات" in msg.get("text"):
						bot.sendMessage(target, "اوسگل جامعه اسمم سوریه😑", message_id=msg.get("message_id"))
					elif "دوست دارم" in msg.get("text"):
						bot.sendMessage(target, "من اصلا😇", message_id=msg.get("message_id"))
					elif "اصل بده" in msg.get("text"):
						bot.sendMessage(target, "سوری ام", message_id=msg.get("message_id"))
					elif msg.get("text") == "فدات" and msg.get("author_object_guid") :
						bot.sendMessage(target, "نشی گلم👀✌", message_id=msg.get("message_id"))
					elif msg.get("text") == "صلام" and msg.get("author_object_guid") :
						bot.sendMessage(target, "مثل آدم بگو سلام😐", message_id=msg.get("message_id"))
					elif msg.get("text") == "😐" and msg.get("author_object_guid") :
						bot.sendMessage(target, "چیه پوکر میدی هی", message_id=msg.get("message_id"))
					elif msg.get("text") == "😂" and msg.get("author_object_guid") :
						bot.sendMessage(target, "رو آب بخندی", message_id=msg.get("message_id"))
					elif msg.get("text") == "💔" and msg.get("author_object_guid") :
						bot.sendMessage(target, "چیه رلت بت خیانت کرده😕", message_id=msg.get("message_id"))
					elif msg.get("text") == "چه خبر؟" and msg.get("author_object_guid") :
						bot.sendMessage(target, "دسته تبر\n تو کون آدم بی خبر😬", message_id=msg.get("message_id"))
					elif msg.get("text") == "اره" and msg.get("author_object_guid") :
						bot.sendMessage(target, "هعی چی بگم", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "لینک" and msg.get("author_object_guid") :
						linkgp = bot.getGroupLink(target)
						bot.sendMessage(target, linkgp, message_id=msg.get("message_id"))
					elif msg.get("text") == "اپدیت" and msg.get("author_object_guid") :
						bot.getChatUpdate(target)
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))
					elif msg.get("text") == "قوانین" and msg.get("author_object_guid") :
						bot.sendMessage(target, "1.Pv📛نرو\n\n 2.Link😡نذار\n\n 3.Dava💪نڪن\n\n 4.Tohin🚫نڪن\n\n 5.Chat💬بڪن\n\n 6.Harfaie🔞نذار\n\n 7.Add👫بڪن\n\n 8.Bijanbei😒نیاتو\n\n 9.Shakh🐃نشو\n\n 10.Left🏃نده", message_id=msg.get("message_id"))
					elif msg.get("text") == "سازندت" and msg.get("author_object_guid") :
						bot.sendMessage(target, "📞 جهت پشتیبانی و رزرو ربات 📞 \n\n📱 @mamal_fi \n\n📱 @DISCORD_ANC \n\n📟جهت هرگونه سوال انتقاد و پیشنهاد میتوانید با پشتیبانی در ارتباط باشید📟", message_id=msg.get("message_id"))
					elif msg.get("text") == "خش" and msg.get("author_object_guid") :
						bot.sendMessage(target, "همچنین", message_id=msg.get("message_id"))
					elif msg.get("text") == "س" and msg.get("author_object_guid") :
						bot.sendMessage(target, "ببین چی گزاشته داخل کانالش😶💦\n\n/Dmxxm‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌")
					elif msg.get("text") == "/Dmxxm" and msg.get("author_object_guid") :
						bot.sendMessage(target, "جقی یافت شد👅😂😄", message_id=msg.get("message_id"))
					elif msg.get("text") == "موز" and msg.get("author_object_guid") :
						bot.sendMessage(target, "🍌", message_id=msg.get("message_id"))
					elif msg.get("text") == "ممنون" and msg.get("author_object_guid") :
						bot.sendMessage(target, "سیب میقولی؟🍎", message_id=msg.get("message_id"))
					elif msg.get("text") == "خیر" and msg.get("author_object_guid") :
						bot.sendMessage(target, "خو چی کنم😕", message_id=msg.get("message_id"))
					elif msg.get("text") == "تزگ" and msg.get("author_object_guid") :
						bot.sendMessage(target, "نگو تزگ بگو سینا👌", message_id=msg.get("message_id"))
					elif msg.get("text") == "هیچی" and msg.get("author_object_guid") :
						bot.sendMessage(target, "نخود چی ", message_id=msg.get("message_id"))
					elif msg.get("text") == "هیق" and msg.get("author_object_guid") :
						bot.sendMessage(target, "گریه نکن زار زار \nمیبرمت بازار👶", message_id=msg.get("message_id"))
					elif msg.get("text") == "dolar" and msg.get("author_object_guid") :
						r = requests.get('https://api.tgju.online/v1/data/sana/json')
						s = r.json()['sana']['data'][0]['p']
						bot.sendMessage(target, s, message_id=msg.get("message_id"))
					elif msg.get("text") == "ساخت پسورد" and msg.get("author_object_guid") :
						x = requests.get('http://api.codebazan.ir/password/?length=20').text
						bot.sendMessage(target, x, message_id=msg.get("message_id"))
					elif msg.get("text") == "proxy list" and msg.get("author_object_guid") :
						x = requests.get('https://api.codebazan.ir/mtproto/json')
						x.json()['tedad']
						bot.sendMessage(target, "✔"+ x, message_id=msg.get("message_id"))
					
					
						bot.sendMessage(target, x, message_id=msg.get("message_id"))
					elif msg.get("text") == "ذکر امروز" and msg.get("author_object_guid") :
						f = requests.get('http://api.codebazan.ir/zekr/').text
						bot.sendMessage(target, f, message_id=msg.get("message_id"))
					elif msg.get("text") == "تاریخ" and msg.get("author_object_guid") :
						fk = requests.get('http://api.codebazan.ir/time-date/?td=all').text
						bot.sendMessage(target,"📟⏰"+ fk, message_id=msg.get("message_id"))
					elif msg.get("text") == "داستان" and msg.get("author_object_guid") :
						fsk = requests.get('http://api.codebazan.ir/dastan/').text
						bot.sendMessage(target, fsk, message_id=msg.get("message_id"))
					elif msg.get("text") == "دیالوگ" and msg.get("author_object_guid") :
						fjk = requests.get('http://api.codebazan.ir/dialog/').text
						bot.sendMessage(target,"🌺"+fjk+"🍃", message_id=msg.get("message_id"))
					elif msg.get("text") == "دانستنی" and msg.get("author_object_guid") :
						mk = requests.get('http://api.codebazan.ir/danestani/').text
						bot.sendMessage(target,"🌀"+mk, message_id=msg.get("message_id"))
					elif 'server' in msg.get("text"):
						bot.sendMessage(target, "لینک پروکسی شما👆\n برای استفاده لینک را کپی کرده و در پیام های ذخیره تلگرام خودتان الصاق کنیدوبعد روی لینک کلیک نمایید☑", message_id=msg.get("message_id"))
					elif msg.get("text") == "سوری جون" and msg.get("author_object_guid") :
						bot.sendMessage(target, "جان سوری", message_id=msg.get("message_id"))
					elif msg.get("text") == "سوری عشقم" and msg.get("author_object_guid") :
						bot.sendMessage(target, "درد و بلات تو سر سوری👩", message_id=msg.get("message_id"))
					elif msg.get("text") == "😂😂" and msg.get("author_object_guid") :
						bot.sendMessage(target, "خنده هات شروع فاجعه بود", message_id=msg.get("message_id"))
					elif msg.get("text") == "😂😂😂" and msg.get("author_object_guid") :
						bot.sendMessage(target, "خنده هات شروع واقعه بود", message_id=msg.get("message_id"))
					
					elif msg.get("text") == "اسم" and msg.get("author_object_guid") :
						aj=requests.get('https://api.codebazan.ir/name/?type=json')
						xxc=aj.json()['result']
						bot.sendMessage(target, xxc)
					elif msg.get("text") == "جونت بی بلا" and msg.get("author_object_guid") :
						bot.sendMessage(target, "قاداسین الیم😻", message_id=msg.get("message_id"))
					elif msg.get("text") == "بیوگرافی" and msg.get("author_object_guid") :
						pu = requests.get('http://api.codebazan.ir/bio').text
						bot.sendMessage(target, pu, message_id=msg.get("message_id"))
					elif msg.get("text") == "مناسبت امروز" and msg.get("author_object_guid") :
						rm = requests.get('https://api.codebazan.ir/monasebat/')
						sm = rm.json()[0]['occasion']
						bot.sendMessage(target, "💥🔥" + sm, message_id=msg.get("message_id"))
					
					elif msg.get("text") == "چیستان" and msg.get("author_object_guid") :
						ii = random.randint(1,100)
						sis = requests.get('https://api.codebazan.ir/chistan/')
						tr = sis.json()['Result'][ii]['soal']
						fs = sis.json()['Result'][ii]['javab']
						bot.sendMessage(target, tr, message_id=msg.get("message_id"))
						time.sleep(2)
						bot.sendMessage(nam, "ℹ"+fs, message_id=msg.get("message_id"))
					elif msg.get("text").startswith("!ping"):
						try :
							response = get("http://api.codebazan.ir/ping/?url=rubika.ir").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except :
							bot.sendMessage(target, "❌", message_id=msg["message_id"])
							
					elif msg["text"].startswith("-weather"):
						response = get(f"https://api.codebazan.ir/weather/?city={msg['text'].split()[1]}").json()
						#print("\n".join(list(response["result"].values())))
						try:
							bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
							bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
				                    	

					elif msg["text"].startswith("-bego"):
						ldl=msg.get('text').split()[1]
						try:
							bot.sendMessage(target, ldl)
						except:
							bot.sendMessage(target, "🔥", message_id=msg["message_id"])
							
					elif msg["text"].startswith("-proxy"):
						s=requests.get("https://api.codebazan.ir/mtproto/json")
						l=s.json()['tedad']
						ls=random.randint(0,l)
						hs=s.json()['Result'][ls]['server']
						hd=s.json()['Result'][ls]['port']
						hj=s.json()['Result'][ls]['secret']
						bot.sendMessage(target, "https://t.me/proxy?server="+hs+"&port="+hd+"&secret="+hj, message_id=msg["message_id"])
						
					elif msg["text"].startswith("-test"):
						response = get(f"https://api.codebazan.ir/codemelli/?code={msg['text'].split()[1]}")
						lk=response.json()['Result']
						#print("\n".join(list(response["result"].values())))
						try:
							bot.sendMessage(target, "🔺"+lk, message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "متاسفانه نتیجه‌ای موجود نبود!", message_id=msg["message_id"])
							     
					
							
					
					elif msg["text"].startswith("-timer"):
						ldl=msg.get('text').split()[1]
						try:
							bot.setGroupTimer(target, ldl)
							bot.sendMessage(target, "تایمر فعال شد ✅\n به مدت :"+ldl)
						except:
							bot.sendMessage(target, "❌", message_id=msg["message_id"])
					    
                                
                               
							
					
					
					elif msg.get("text").startswith("!tran"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							
							
					
					elif msg.get("text").startswith("!font"):
						#print("\n".join(list(response["result"].values())))
						try:
							response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
							bot.sendMessage(msg.get("author_object_guid"), "\n\n".join(list(response["result"].values())[:25])).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])


					elif msg.get("text").startswith("!jok"):
						
						
						try:
							response = get("https://api.codebazan.ir/jok/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
						
					elif msg.get("text").startswith("!add") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!lock" :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "!unlock" :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "!start" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"بای بای {user} 🗑️", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام {user} عزیز به گروه {name} خوش اومدی 😃\nلطفا قوانین رو رعایت کن 🥰", message_id=msg["message_id"])
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"بای بای {user} 🗑️", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"سلام {user} عزیز به گروه {name} خوش اومدی 😃\nلطفا قوانین رو رعایت کن 🥰", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
			
answered = [bot.getGroupAdmins]

while True:
        try:
                min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
                messages = bot.getMessages(target,min_id)
                for msg in messages:
                        if msg["type"]=="Text" and not msg.get("message_id") in answered:
                                if msg.get("text"):
                                        mop = open("data.txt","r",encoding="utf")
                                        ooo = mop.read().split("|/|")
                                        for i in ooo:
                                                ii = i.split("|=|")
                                                if msg.get("text") in ii[0]:
                                                        bot.sendMessage(target, ii[1], message_id=msg["message_id"])
                                        mop.close()
                                        
                                
                                if msg.get("text").startswith("!learn"):
                                        try:
                                                data = msg.get("text").split("\n")
                                                f = open("data.txt","a",encoding="utf")
                                                f.write(str(data[1] + "|=|" + data[2] + "|/|" + "\n" ))
                                                f.close()
                                                bot.sendMessage(target, "آها یاد گرفتم✅", message_id=msg.get("message_id"))
                                        except:
                                                bot.sendMessage(target, "لطفا دستورات را درست وارد کنید ❌", message_id=msg.get("message_id"))
                                if msg.get("text").startswith("!stoping"):
                                        try:
                                                sleeped = True
                                                bot.sendMessage(target, "✅", message_id=msg.get("message_id"))
                                        except:
                                                bot.sendMessage(target, "لطفا دستورات را درست وارد کنید ❌", message_id=msg.get("message_id"))
                               
                        answered.append(msg.get("message_id"))
        except:
                pass
			
