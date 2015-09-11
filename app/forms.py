from flask_wtf import Form
from wtforms import IntegerField, SelectField, TextField, validators

#SelectField field to specify state-size
class StatesizeForm(Form):
    size = SelectField("state", choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")])

#Integer field to get characters
class CharactersForm(Form):
    characters = Integerfield("characters", [validators.Required(), validators.NumberRange(min = 0)])

#SelectField dropdown of text options for sources, pulled from database dynamically as community may add to it
class SelectSourceForm(Form):
    source = SelectField("source") #choices will be added dynamically

#TextField to get hashtag for twitter source-creation
class HashTagForm(Form):
    hashtag = TextField("hashtag", [validators.required()])

#IntegerField to get number of desired tweets to generate
class NumTweetsForm(Form):
    numTweets = IntegerField("characters", [validators.Required(), validators.NumberRange(min = 0)])

#TextField to get subreddit for reddit source-creation
class SubredditForm(Form):
    subreddit = Textfield("subreddit", [validators.required()])

#IntegerField to get number of tweets to search through in source-creation
class NumberTweets(Form):
    numberTweets = IntegerField("numberTweets", [validators.required(), validators.NumberRange(min = 1)])
