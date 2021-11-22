import sys
import praw
import csv
import pandas as pd
from pandas import DataFrame
from selenium import webdriver

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
reddit = praw.Reddit(
    user_agent="Comment Extraction (by /u/USERNAME)",
    client_id="jmML3pLGBhM1zg",
    client_secret="3MidvTa_ETPVWAPXbvkxDUqqWxTtzA",
    username="Prawcollection",
    password="Prawpass1!",
)
with open("book2.csv") as csvfile:
    data = list(csv.reader(csvfile))
    df = pd.DataFrame(columns=["body", "author", "score", "post id", "utc"])
    for row in data:
        submission = reddit.submission(id=row[0])
        submission.comments.replace_more(limit=None)
        for comment in submission.comments:
            df_row = {
                "body": comment.body,
                "author": comment.author,
                "score": comment.score,
                "post id": comment.submission,
                "utc": comment.created_utc,
            }
        
            df = df.append(df_row, ignore_index=True)
    df.to_csv("Comments.csv", index=False, header=False)
