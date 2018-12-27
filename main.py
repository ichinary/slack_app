import requests
import requests_oauthlib
import json
import random


class TwitterClass:

    def __init__(self, beautiful_name):
        self.consumer_key  = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        self.consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        self.access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        self.access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        self.urls = 'https://api.twitter.com/1.1/search/tweets.json'
        self.beautiful_name = beautiful_name
        self.url_lists = []


    def get_tweet(self): # ツイッターから指定した名前のtweetを取得
        oauth = requests_oauthlib.OAuth1(
            self.consumer_key,
            self.consumer_secret,
            self.access_token,
            self.access_token_secret)

        query = self.beautiful_name
        lang = "ja"
        result_type="recent" # 最新のツイートを取得
        count = 100 # 1回あたりの最大取得ツイート数（最大100）
        max_id = ''
        params = {'q':query,'lang':lang,'result_type':result_type,'count':count,'max_id':max_id}
        return requests.get(url=self.urls, params=params, auth=oauth).json()

    def correct_image(self):
        tweets = self.get_tweet()
        for item in tweets['statuses']:
            if 'media' in item['entities'].keys():
                self.url_lists.append(item['entities']['media'][0]['media_url'])
            else:
                pass
        return self.url_lists

    def select_image(self):
        lists = self.correct_image()
        return random.choice(lists)



class SlackClass:
    def __init__(self, image_url):
        self.slack_url = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        self.image_url = image_url
    def post_to_channel(self):
        params = {
            'text': self.image_url, # 投稿するテキスト
            'username': u'XX XX', # 投稿のユーザー名
            'icon_url': u'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            'link_names': 1, # メンションを有効にする
        }
        return requests.post(self.slack_url, data=json.dumps(params))



def hello_world():
    a = TwitterClass('XX XX')
    b = a.select_image()
    c = SlackClass(b)
    return c.post_to_channel()

#hello_world()
