import openai
openai.api_key = "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"

def rasim(buyuruq):
	response = openai.Image.create(
	  prompt=buyuruq,
	  n=1,
	  size="1024x1024")

	return response['data'][0]['url']

if __name__=='__main__':
	print(rasim("Future car"))