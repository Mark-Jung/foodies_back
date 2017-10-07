from os import path
from wordcloud import WordCloud
from scraper.headline_nyt import get_nyt_words
from scaper.headline_aljaz import get_aljaz_words
from scaper.headline_cnn import get_cnn_words
from scaper.headline_fox import get_fox_words
from scaper.headline_theblaze import get_theblaze_words
from scaper.headline_wsj import get_wsj_words



text = get_nyt_words()

wordcloud = WordCloud().generate(text)

image = wordcloud.to_image()
image.show()


