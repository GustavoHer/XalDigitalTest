#!/usr/bin/env python
# coding: utf-8


import requests
from datetime import datetime

def answers_number(item, ans, not_ans):
    
    if item['is_answered'] == True:
        ans += 1
    else:
        not_ans += 1
    
    return ans, not_ans

def view_count(item, flag, answer):
    
    if int(item['view_count']) < flag:
        flag = int(item['view_count'])
        answ = item['title']
    
    return flag, answer
    
def get_data(url):

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

    return data



ans = 0
not_ans = 0
flag = 99999999
oldest_answer, rep = [], []

url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
data = get_data(url)


for item in data['items']:
    ans,not_ans = answers_number(item, ans, not_ans)
    flag, answer = view_count(item, flag, answer)
    oldest_answer.append(item['last_activity_date'])
    rep.append(item['owner']['reputation'])
    



oldest = datetime.utcfromtimestamp(min(oldest_answer)).strftime('%Y-%m-%d %H:%M:%S')
newest = datetime.utcfromtimestamp(max(oldest_answer)).strftime('%Y-%m-%d %H:%M:%S')
answers_dict = {"Respuestas contestadas:":ans, "No contestadas:": not_ans, "Menor numero de visitas:": flag, 
               "Respuesta con menor número de visitas:":answer, "Respuesta más vieja:": oldest, "Respuesta mas actual:": newest,
               "Owner con mayor reputación:": max(rep)}


for key in answers_dict:
    value = answers_dict[key]
    print(key, value)





