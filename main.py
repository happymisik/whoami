# -*-coding:utf-8-*-
import pandas as pd
from flask import Flask, request, json
import random

app = Flask(__name__)

commonResponse = {
    'version': '2.0',
    'resultCode': 'OK',
    'output': {}
}

df = pd.read_csv("dinosourquize.csv", encoding='utf-8')
num = 0
list_from_df = df.values.tolist()
for data in list_from_df:
    print("{}번 문제 : {}".format(num  + 1, list_from_df[num][1]))
    print("{}번문제의 힌트1 : {}".format(num + 1, list_from_df[num][2]))
    print("{}번문제의 힌트2 : {}".format(num + 1, list_from_df[num][3]))
    print("{}번문제의 힌트3 : {}".format(num + 1, list_from_df[num][4]))
    print("{}번문제의 힌트4 : {}".format(num + 1, list_from_df[num][5]))
    print("{}번문제의 힌트5 : {}".format(num + 1, list_from_df[num][6]))
    num = num + 1
    # print("{}번 문제 : {}".format(num+1,list_from_df[num][0]))

print(list_from_df[0][0])


def getUtteranceParameter():
    data = request.get_json()
    print(data)
    return data['action']['parameters']


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/startGameAction', methods=['POST'])
def createQuize():

    response = commonResponse
    randomNumber = random.randrange(0, 50)

    response['output']['quiz'] = list_from_df[randomNumber][1]
    response['output']['hint1'] = list_from_df[randomNumber][2]
    response['output']['hint2'] = list_from_df[randomNumber][3]
    response['output']['hint3'] = list_from_df[randomNumber][4]
    response['output']['hint4'] = list_from_df[randomNumber][5]
    response['output']['hint5'] = list_from_df[randomNumber][6]

    print(randomNumber)
    print(response)

    return json.dumps(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)

