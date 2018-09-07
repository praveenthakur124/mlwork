import pickle


def category_opt(text):
    cat_dict = {'Auto & Vehicles': 0,
                'Beauty': 1,
                'Comedy': 2,
                'Education': 3,
                'Entertainment': 4,
                'Fashion & Style': 5,
                'Food & Drinks': 6,
                'Gaming': 7,
                'Health & Fitness': 8,
                'Kids & Animation': 9,
                'Music': 10,
                'News & Politics': 11,
                'Science & Tech': 12,
                'Sports': 13}

    vect = pickle.load(open("/home/praveen/Python_Work/vectcat.pkl", "rb"))
    text_dtm = vect.transform(text)
    cat_pred = pickle.load(open("/home/praveen/Python_Work/VideoCategoryClassificationPredict.pkl", "rb"))
    result = cat_pred.predict(text_dtm)

    for k, v in cat_dict.items():
        if result == v:
            print(k)


category_opt(["""I have a Discord Serverhttps://discord.gg/CevGcYc"""])
