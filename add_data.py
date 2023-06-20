import tkinter as tk
from csv import writer
import pandas
import os
import yake


def AddData():
    name = entry1.get()
    desc = entry2.get()
    com = entry3.get()

    keyword_extractor = yake.KeywordExtractor(top=10, stopwords=None)
    keywords = keyword_extractor.extract_keywords(desc)
    # data = [name, keywords, com]

    # with open('nodes.csv', 'a') as f:
    #     w = writer(f)
    #     w.writerow(data)
    #     f.close()

    data = pandas.DataFrame({'Nodes': [name], 'Keywords': keywords, 'Commands': [com]})
    data.to_csv('nodes.csv', mode = 'a')

root= tk.Tk()

canvas1 = tk.Canvas(root, width=1500, height=800)
canvas1.pack()

label = tk.Label(root, text="Enter Data points")
canvas1.create_window(800, 100, window=label)

label = tk.Label(root, text="Enter Node name")
canvas1.create_window(500, 130, window=label)
entry1 = tk.Entry(root) 
canvas1.create_window(500, 150, window=entry1)

label = tk.Label(root, text="Enter Description")
canvas1.create_window(800, 130, window=label)
entry2 = tk.Entry(root) 
canvas1.create_window(800, 150, window=entry2)

label = tk.Label(root, text="Enter Node name")
canvas1.create_window(1100, 130, window=label)
entry3 = tk.Entry(root) 
canvas1.create_window(1100, 150, window=entry3)


button1 = tk.Button(text='Add Data entry', command=lambda: AddData)
canvas1.create_window(800, 200, window=button1)


root.mainloop()