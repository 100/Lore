import praw
import itertools

PUNCT = ['!', '.', '?', ',', ';', ' ']
FORMATTING = ['*', '**', '^', '~~', '\*', '`', '>', '[', ']', '---', '\.']

def createSource(subreddit, numSubmissions): #submission = # of submissions to crawl for comments in subreddit
    r = praw.Reddit(user_agent='Lore by d-soni')
    submissions = r.get_subreddit(subreddit).get_hot(limit=numSubmissions)
    commentsList = []
    for submission in submissions:
        submission.replace_more_comments(limit=None)
        commentsList.append(praw.helpers.flatten_tree(submission.comments))
    comments = itertools.chain.from_iterable(commentsList)
    commentTexts = [comment.body for comment in comments]
    source = ""
    for text in commentTexts:
        for element in FORMATTING:
            text = text.replace(element, '') #remove formatting characters
        text = text.replace('\n', '') #remove newlines 
        ' '.join(text.split()) #ensure only 1 space is added while multiple \n may exist
        if text[-1:] not in PUNCT:
            text = text + "."  #if no punctuation, add period (may be incorrect, but most often correct)
        source = source + text + " " #concatenate all comments into a large source text
    return source
