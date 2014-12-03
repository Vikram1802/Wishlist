# Regex to separate email id's from json format data
# Directly run this script to get an output data

import csv
import re
regex = re.compile("""
    ([^:]*)  # Match and capture any characters except colons
    :[ ]*    # Match a colon, followed by optional spaces
    (.*)     # Match and capture the rest of the line""", 
    re.VERBOSE)
with open("F:/Beachbody_amazon/Ara/wishlists/wishlist_bb_only.txt") as infile, open("F:/Beachbody_amazon/Ara/wishlists/bb_only.csv", "wb") as outfile:
    writer = csv.writer(outfile)
    for line in infile:
       writer.writerow(regex.match(line).groups())