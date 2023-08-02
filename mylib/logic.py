import wikipedia
from textblob import TextBlob

def wiki(name="War Goddess", length=1):
    '''this is wikipedia fetcher'''
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name):
    '''search wikipedia for names'''
    return wikipedia.search(name)

def phrases(name):
    '''return phrases from wiki'''
    blob = TextBlob(wiki(name))
    return blob.noun_phrases