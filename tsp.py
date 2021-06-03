import pandas as pd
from datetime import datetime
import requests
import re
import json
import math
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

data = pd.read_csv('coords.csv')
data.plus = [re.sub("\+","%2B", str(x)) for x in data.plus]
data.plus = [re.sub(" ", "%20", str(x)) for x in data.plus]
URL_0 = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins="
n = data.shape[0]
k = math.ceil(n/10)
distance = [[0 for i in range(n)] for j in range(n)]
duration = [[0 for i in range(n)] for j in range(n)]
for t in range(k):
    for s in range(k):
        URL = URL_0 + data.plus[t*10]
        if n > t*10:
            row = min(10,n-t*10)
            for i in range(1,row):
                URL = URL + "|" + data.plus[i]
        URL = URL + "&destinations=" + data.plus[s*10]
        if n > s*10:
            col = min(10, n-s*10)
            for i in range(1,col):
                URL = URL + "|" + data.plus[i]
        URL = URL + "&key=YOUR_GOOGLE_API_KEY"
        RESPONSE = requests.get(URL)
        formateado = eval(str(RESPONSE.content))
        my_json = formateado.decode('utf8').replace("'",'"')
        datos = json.loads(my_json)
        for i in range(row):
            for j in range(col):
                distance[i][j] = datos["rows"][i]["elements"][j]['distance']['value']
                duration[i][j] = datos["rows"][i]["elements"][j]['duration']['value']

d_mat = np.multiply(np.array(distance), np.array(duration))
print("Solving")
per,dist = solve_tsp_dynamic_programming(d_mat)
res = data.iloc[per,:]
t = str(datetime.now())
with open('results/status_'+ t + '.txt','w') as f:
    f.write(t + "\t" + str(dist))
res.to_csv("results/order_" + t + ".csv")
