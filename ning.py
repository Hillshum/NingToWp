#!/usr/bin/env python3

from io import BytesIO
import json
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element

f = open('start.json')

j = json.load(f)


root = Element('rss')

tree = ElementTree(root)

channel = Element('channel')
root.append(channel)
link = Element('link')
link.text = "https://treeoflifemothering.com"
channel.append(link)


title = Element('title')
channel.append(title)
title.text = "Tree of Life Mothering"


out = BytesIO()
tree.write(out)

out.seek(0)
print(out.read())

# for i in tree.iter():
#     print(i)
