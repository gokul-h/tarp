import sys

search_term = text_input = str(sys.argv[1])
no_of_urls = 10

# Azure settings
subscription_key = "a018086497784da9a60874870fb6fad2"
assert subscription_key
search_url = "https://api.bing.microsoft.com/v7.0/search"

import requests

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"q": search_term, "responseFilter": "webpages", "count": no_of_urls}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

search_term = text_input + " site:http://wiki.ros.org/ "
no_of_urls = 10

# Fetch Data
import requests

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"q": search_term, "responseFilter": "webpages", "count": no_of_urls}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results_wiki = response.json()

# Create a new tkinter window
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create two frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Create a new treeview widget in each frame
tree1 = ttk.Treeview(frame1, columns=('url', 'snippet'))
# tree1.heading('#0', text='Index')
tree1.heading('url', text='URL')
tree1.heading('snippet', text='Snippet')
tree1.pack(side=tk.LEFT)

tree2 = ttk.Treeview(frame2, columns=('url', 'snippet'))
# tree2.heading('#0', text='Index')
tree2.heading('url', text='URL')
tree2.heading('snippet', text='Snippet')
tree2.pack(side=tk.LEFT)

# Insert the JSON data into each treeview widget
for i, result in enumerate(search_results['webPages']['value']):
    item1 = tree1.insert('', 'end', values=(result['url'], result['snippet']))

for i, result in enumerate(search_results_wiki['webPages']['value']):
    item2 = tree2.insert('', 'end', values=(result['url'], result['snippet']))

# Add headings to each frame
tk.Label(frame1, text="Helpful resources").pack()
tk.Label(frame2, text="ROS Wiki Resources").pack()

# Pack the frames into the window
frame1.pack(side=tk.LEFT)
frame2.pack(side=tk.RIGHT)

# Start the tkinter event loop
root.mainloop()
