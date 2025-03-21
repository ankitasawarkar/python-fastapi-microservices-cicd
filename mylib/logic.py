import wikipedia


def wiki(name="Image Processing", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki

def search_wiki(name="Image Processing"):
    """Search name in wikipedia"""

    my_wiki = wikipedia.search(name)
    return my_wiki
