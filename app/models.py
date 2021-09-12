class News:
    '''
    News class to define News Objects
    '''
    def __init__(self,id,name,url,description,category, country):
        self.id =id
        self.name= name
        self.url = url
        self.description = description
        self.category = category
        self.country = country



class Articles:
    get_articles = []
    def __init__(self,title,author,url,description, urlToImage, publishedAt, content):
        self.title = title
        self.author = author
        self.url = url
        self.description= description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content