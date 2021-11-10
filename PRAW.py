import sys
import praw
import csv
import pandas as pd
from pandas import DataFrame
from selenium import webdriver

# reddit log in
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
reddit = praw.Reddit(
    user_agent="Comment Extraction (by /u/USERNAME)",
    client_id="jmML3pLGBhM1zg",
    client_secret="3MidvTa_ETPVWAPXbvkxDUqqWxTtzA",
    username="Prawcollection",
    password="Prawpass1!",
)
# csv open
with open("book2.csv") as csvfile:
    data = list(csv.reader(csvfile))
    # Create an empty dataframe containing the columns we want
    df = pd.DataFrame(columns=["body", "author", "score", "post id", "utc"])
    for row in data:
        submission = reddit.submission(id=row[0])
        submission.comments.replace_more(limit=None)
        for comment in submission.comments:
            # Create a dictionary containg key-value pairs of the column
            # name and its value
            df_row = {
                "body": comment.body,
                "author": comment.author,
                "score": comment.score,
                "post id": comment.submission,
                "utc": comment.created_utc,
            }
            # Append the new column to the dataframe
            # this returns a new dataframe with a copy of the original data
            # along with the new row. We store it back into the variable holding
            # the original dataframe.
            df = df.append(df_row, ignore_index=True)
    # saves csv without headers
    df.to_csv("Comments.csv", index=False, header=False)
