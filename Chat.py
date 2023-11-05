import openai
openai.api_key = "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"
#prompt = "MEnga kvant fizikasini sodda qilib tushuntirib ber "

def chat(buyuruq):
	a=0;
	natija=""
	if len(buyuruq)>4:
		openai.Completion.create(engine="text-davinci-003", prompt="Menga faqat o'zbek tilida javob ber", max_tokens=500)
		response = openai.Completion.create(engine="text-davinci-003", prompt=buyuruq, max_tokens=500)
		response=response['choices'][0]['text']
		response=response.split("\n")
		for i in response:
			if a>=1:
				natija+=i
			a+=1
		return natija
	else:
		#print(len(buyuruq))
		return "Javob olish uchun kamida 5 ta harifda iborat savol bering!!!"
if __name__=='__main__':

	print(chat("Salom"))