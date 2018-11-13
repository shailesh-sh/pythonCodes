import requests
import tkinter as tk
from bs4 import BeautifulSoup


def Convert():
	qVal = entryCurrency1.get()+"_"+entryCurrency2.get()
	url = "http://free.currencyconverterapi.com/api/v5/convert?q="+ qVal +"&compact=y"
	html_code = requests.get(url).text
	#print(html_code)
	html_code = html_code.split(":")
	try:
		html_code = ''.join(c for c in html_code[2] if c.isdigit())
		rate = (float(html_code)/1000000)
	except:
		labelSpace["text"]="Use Correct Country Code"
	try:
		feedAmount = float(entryAmount.get())
		amount = float(feedAmount)*rate
		labelResult["text"] = amount
	except:
		labelResult["text"] = "Invalid Amount"



def Reverse():
	qVal = entryCurrency2.get()+"_"+entryCurrency1.get()
	url = "http://free.currencyconverterapi.com/api/v5/convert?q="+ qVal +"&compact=y"
	html_code = requests.get(url).text
	html_code = html_code.split(":")
	try:
		html_code = ''.join(c for c in html_code[2] if c.isdigit())
		rate = (float(html_code)/1000000)
	except:
		labelSpace["text"]="Use Correct Country Code"
	try:
		feedAmount = float(entryAmount.get())
		amount = float(feedAmount)*rate
		labelResult["text"] = amount
	except:
		labelResult["text"] = "Invalid Amount"


root =tk.Tk()
root.title("Currency Converter")
labelCurrency1 = tk.Label(root, text="Base Currency")
labelCurrency1.pack()

entryCurrency1 = tk.Entry(root, bg="white")
entryCurrency1.pack()

labelCurrency2 = tk.Label(root, text="Conversion Currency")
labelCurrency2.pack()

entryCurrency2=tk.Entry(root, bg="white")
entryCurrency2.pack()

labelAmount = tk.Label(root, text="Amount")
labelAmount.pack()

entryAmount = tk.Entry(root, bg="white")
entryAmount.pack()

labelResult = tk.Label(root,text="")
labelResult.pack()

labelSpace = tk.Label(root,text="")
labelSpace.pack()

btnConvert = tk.Button(root, text="Convert", relief ="groove", width="20", command=Convert)
btnConvert.pack()

btnReverse = tk.Button(root, text="Reverse", relief ="groove", width="20", command=Reverse)
btnReverse.pack()

root.mainloop()