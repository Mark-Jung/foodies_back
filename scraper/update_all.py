from os import path
from wordcloud import WordCloud
from .headline_aljaz_full import get_aljaz_words
from .headline_cnn_full import get_cnn_words
from .headline_fox_full import get_fox_words
from .headline_nyt_full import get_nyt_words
from .headline_theblaze_full import get_theblaze_words
from .headline_wsj_full import get_wsj_words
from models.words import WordModel

d = path.dirname(__file__)

def scrape_words(name):
    if name == "aljaz":
        return get_aljaz_words()
    elif name == "cnn":
        return get_cnn_words()
    elif name == "fox":
        return get_fox_words()
    elif name == "nyt":
        text = get_nyt_words()
        return text
    elif name == "theblaze":
        return get_theblaze_words()
    elif name == "wsj":
        return get_wsj_words()

def update_single(name):
    news_org = WordModel.find_by_name(name)
    # if news_org cannot be found, add new
    if news_org is None:
        new = WordModel(name, scrape_words(name))
        new.save_to_db()
        # print(new.words)
        wordcloud = WordCloud().generate(new.words)
        wordcloud.to_file(path.join(d, str(name)+".png"))
        wordcloud.to_image().show()
    else:
        news_org.words = scrape_words(name)
        news_org.save_to_db()
        if (len(news_org.words) == 0):
            pass
        else:
            # print(news_org.words)
            wordcloud = WordCloud().generate(news_org.words)
            wordcloud.to_file(path.join(d, str(name)+".png"))
            wordcloud.to_image().show()


def update_all():
    all_news_orgs = ["aljaz", "cnn", "fox", "nyt", "theblaze", "wsj"]
    for name in all_news_orgs:
        update_single(name)
