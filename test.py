import tkinter as tk
import yake
from difflib import SequenceMatcher
import pandas
import os

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def run_code(com):
    print(com)
    os.system(com)

root= tk.Tk()

canvas1 = tk.Canvas(root, width=1500, height=800)
canvas1.pack()

label = tk.Label(root, text="Enter the Description of the Robot")
canvas1.create_window(750, 100, window=label)

entry1 = tk.Entry(root) 
canvas1.create_window(750, 140, window=entry1)


def test_func():  
    x1 = entry1.get()
    keyword_extractor = yake.KeywordExtractor(top=10, stopwords=None)
    keywords = keyword_extractor.extract_keywords(x1)

    kws = [kw for kw, _ in keywords]

    nodes_data = pandas.read_csv('nodes.csv')
    data_keywords = list(nodes_data.Keywords)
    nodes_list = list(nodes_data.Node)
    commands_list = list(nodes_data.Commands)
    print(commands_list)
    
    suggested_nodes = []
    Threshold = 0.7

    for word in kws:
        for i in range(len(data_keywords)):
            keywords_in_node = data_keywords[i].split(',')
            max = 0
            for k in keywords_in_node:
                score = similar(word, k)
                if score > max:
                    max = score

            if max > Threshold:
                suggested_nodes.append(i)
    
    suggested_nodes = list(set(suggested_nodes))
    print(suggested_nodes)

    label2 = tk.Label(root, text="Suggested Nodes to be launched")
    canvas1.create_window(750, 400, window=label2)

    d = 0
    for i in range(len(suggested_nodes)):
        button = tk.Button(text=nodes_list[suggested_nodes[i]], command=lambda: run_code(commands_list[suggested_nodes[i]]))
        canvas1.create_window(750, 450+d, window=button)
        d = d + 50
    
button1 = tk.Button(text='Get Suggested Nodes', command=test_func)
canvas1.create_window(750, 200, window=button1)

button1 = tk.Button(text='Nodes.py', command=lambda: run_code('python3 nodes.py ' + str(entry1.get())))
canvas1.create_window(750, 250, window=button1)

button1 = tk.Button(text='Mining,py', command=lambda: run_code('python3 mining.py ' + str(entry1.get())))
canvas1.create_window(750, 300, window=button1)

button1 = tk.Button(text='Add Data entry', command=lambda: run_code('python3 add_data.py'))
canvas1.create_window(750, 350, window=button1)

root.mainloop()