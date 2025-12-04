from transformers import pipeline

summ = pipeline("summarization")
sent = pipeline("sentiment-analysis")

texts = ["This restaurant is a true gem, offering a complete dining experience that excels in every category. The atmosphere is inviting and comfortable, the service is exceptionally friendly and attentive, and the food is fresh, flavorful, and beautifully presented. From savory appetizers to expertly prepared main courses, every dish was a delight, making it a must-visit for anyone seeking a memorable Asian meal. We will definitely be returning to explore more of the menu and can’t wait to plan our next visit.",
         "BAD HYGIENE & CONCERNING FOOD SAFETY! Went there today, and there was a bug in the soup. Maybe I was the lucky customer that got some extra protein in my soup as gift. Talked to the staff, none of whole were able to communicate in English, and ended up getting a refund for my order. I would like potential customers to be aware of this and watch out for any extra gift in the soup.",
         "Not my favorite.",
         "Not authentic."]

for text in texts:
    summary = text
    if len(text) > 200:
        summary = summ(text, max_length=60)[0]['summary_text']

    sentiment = sent(summary)
    print(f"\nText: {text}\nSentiment: {sentiment}")