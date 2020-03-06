from getData import get_text
from clearData import clear_text
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image
import os 

if 'text.p' not in os.listdir():
    get_text()

text, stopwords = clear_text('text.p', 'stopwords.txt')
mask = np.array(Image.open("img/br.png"))
wordcloud_br = WordCloud(stopwords=stopwords, background_color="white", mode="RGBA", max_words=1000, mask=mask).generate(text)

# create coloring from image
image_colors = ImageColorGenerator(mask)
plt.figure(figsize=[10,10])
plt.imshow(wordcloud_br.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")

# store to file
plt.savefig("wordcloudBR.png", format="png")