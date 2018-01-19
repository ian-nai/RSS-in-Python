import feedparser
import io

def get_feed():

    keyword = raw_input("Please enter a keyword to search: ")
   
    data = []
    with io.open('feed_list.txt', encoding='utf-8') as myfile:
        for i in myfile.readlines():
            data.append(i)
            
    feeds = [] 
    for url in data:
        feeds.append(feedparser.parse(url))

    posts = []
    for url in data:
        posts.extend(feedparser.parse(url).entries)
    '''
    for post in posts:
        print post.title
    '''
   
    for a, post in enumerate(posts):
        if keyword in post.summary:
            print a, post.title, "\n", post.link, "\n", post.author, "\n", post.summary
            
    print "Total # of Entries in Feeds: ", len(posts)
    
get_feed()
