from alfred import Item
from datetime import datetime
import json

def main(query):
    dt = parse(query)
    return json.dumps({"items":[timestamp(dt).dic]})

def parse(query):
    return datetime.now()

def timestamp(dt):
    ts = dt.strftime("%s")
    i = Item(title=ts, 
             subtitle="POSIX timestamp",
             arg=ts,
             uid="timestamp")
    return i
