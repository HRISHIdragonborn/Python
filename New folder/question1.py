import requests
import csv
res = requests.get('https://api.kite.trade/instruments')
t = res.iter_lines()
data = csv.reader(text, delimiter=',')
    
