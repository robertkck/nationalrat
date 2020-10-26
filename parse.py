import feedparser

url = "https://www.parlament.gv.at/Filter/PAKT/VHG/filter.psp?view=RSS&jsMode=&xdocumentUri=&filterJq=&view=&NRBR=NR&GP=XXVI&VHG=GESVOR&GESVOR=ALLE&SUCH=&listeId=100&LISTE=Anzeigen&FBEZ=FP_001"
feed = feedparser.parse(url)

entry = feed.entries[1]

print(entry.keys())