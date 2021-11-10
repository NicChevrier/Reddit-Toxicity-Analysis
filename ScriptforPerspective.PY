import json
import time
import csv
import pandas as pd
from googleapiclient import discovery

# Set up google api
API_KEY = "AIzaSyD5LqdbU9kZFfhW3ofHUXclfrfSwALI8Qo"

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,)

# Get the toxicity probability of a comment in a dataframe row
def get_toxicity(row):
    analyze_request = {
        "comment": {"text": row["body"]},
        "requestedAttributes": {"TOXICITY": {}},
        "languages": ["en"],
    }

    response = client.comments().analyze(body=analyze_request).execute()
    
    if not hasattr(response, "__getitem__"):
        json.dumps(response, sort_keys=True, indent=4)
        time.sleep(0.12)
        return -13376969
    time.sleep(0.12)
    return response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]


# Read the csv from file
df = pd.read_csv(
    "imagetextmod.csv", header=None, names=["body", "author", "score", "post id", "utc"]
)
# Create a new column with the probability score of comment toxicity
df["score"] = df.apply(get_toxicity, axis=1)

# Write modified dataframe to file
df.to_csv("modimages_analyzed.csv", index=False, header=True)
