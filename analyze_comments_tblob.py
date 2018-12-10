from textblob import TextBlob
import pandas as pd
from sklearn.metrics import accuracy_score

def analyze_comments(sentiment_df):
	for index, row in sentiment_df.iterrows():
	    stripped_whitespace = row[0].replace("\r", "")
	    sentiment_df.at[index,'comment']=stripped_whitespace
	    comment =  sentiment_df.at[index,'comment']
	    blob = TextBlob(comment)

	    if blob.sentiment.polarity>=0:
	    	sentiment_df.at[index, 'tblob_label']= '1'
	    else:
	    	sentiment_df.at[index, 'tblob_label']= '0'
	return sentiment_df