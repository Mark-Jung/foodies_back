from .headline_aljaz import get_aljaz_words
from .headline_cnn import get_cnn_words
from .headline_fox import get_fox_words
from .headline_nyt import get_nyt_words
from .headline_theblaze import get_theblaze_words
from .headline_wsj import get_wsj_words
from models.words import WordModel

def get_words(self, name):
    if name == "aljaz":
        return get_aljaz_words()
    elif name == "cnn":
        return get_cnn_words()
    elif name == "fox":
        return get_fox_words()
    elif name == "nyt":
        return get_nyt_words()
    elif name == "theblaze":
        return get_theblaze_words()
    elif name == "wsj":
        return get_wsj_words()

def update_single(self, name):
    news_org = find_by_name(name)
    if news_org is None:
        new = WordModel(name, get_words(name))
        new.save_to_db()
    news_org.words = get_words(name)
    news_org.save_to_db()

def update_all(self):
    all_news_orgs = ["aljaz", "cnn", "fox", "nyt", "theblaze", "wsj"]
    for name in all_news_orgs:
        update_single(name)
