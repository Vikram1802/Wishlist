#Regex to separate email id's from json format data

import csv
import re
regex = re.compile("""
    ([^:]*)  # Match and capture any characters except colons
    :[ ]*    # Match a colon, followed by optional spaces
    (.*)     # Match and capture the rest of the line""", 
    re.VERBOSE)
with open("F:/Beachbody_amazon/Ara/wishlists/wishlist_bb_amazon.txt") as infile, open("F:/Beachbody_amazon/Ara/wishlists/out.csv", "wb") as outfile:
    writer = csv.writer(outfile)
    for line in infile:
       writer.writerow(regex.match(line).groups())