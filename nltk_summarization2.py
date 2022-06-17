import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

text = "It is now clear that Russia is seeking to overthrow Ukraine's democratically elected government. Its aim is that Ukraine be freed from oppression and 'cleansed of the Nazis'. President Zelensky said he had been warned 'the enemy has designated me as target number one; my family is target number two'. This false narrative of a Ukraine seized by fascists in 2014 has been spun regularly on Kremlin-controlled TV. Mr Putin has spoken of bringing to court 'those who committed numerous bloody crimes against civilians'. What Russia\'s plans are for Ukraine are unknown, but it faces stiff resistance from a deeply hostile population. In January, the UK accused Moscow of plotting to install a pro-Moscow puppet to lead Ukraine\'s government - a claim rejected at the time by Russia as nonsense. One unconfirmed intelligence report suggested Russia aimed to split the country in two. In the days before the invasion, when up to 200,000 troops were near Ukraine\'s borders, Russia\'s public focus was purely on the eastern areas of Luhansk and Donetsk. By recognising the separatist areas controlled by Russian proxies as independent, Mr Putin was telling the world they were no longer part of Ukraine. Then he revealed that he supported their claims to far more Ukrainian territory. The self-styled people\'s republics cover little more than a third of the whole of Ukraine\'s Luhansk and Donetsk regions, but the rebels covet the rest, too."

def nltk_summarizer2(raw_text):
	stopWords = set(stopwords.words("english"))
	words = word_tokenize(raw_text)
	word_frequencies = {}  
	for word in nltk.word_tokenize(raw_text):  
		if word not in stopWords:
			if word not in word_frequencies.keys():
				word_frequencies[word] = 1
			else:
				word_frequencies[word] += 1

	maximum_frequncy = max(word_frequencies.values())

	for word in word_frequencies.keys():  
		word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

	sentence_list = nltk.sent_tokenize(raw_text)
	sentence_scores = {}  
	for sent in sentence_list:  
		for word in nltk.word_tokenize(sent.lower()):
			if word in word_frequencies.keys():
				if len(sent.split(' ')) < 30:
					if sent not in sentence_scores.keys():
						sentence_scores[sent] = word_frequencies[word]
					else:
						sentence_scores[sent] += word_frequencies[word]



	summary_sentences = heapq.nlargest(8, sentence_scores, key=sentence_scores.get)

	summary = ' '.join(summary_sentences)  
	return summary
