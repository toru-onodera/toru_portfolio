import requests
import random
import settings

# urlの作成
def get_dish():
    REQUESTS_URL = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426'

    APP_ID = settings.os.environ['APP_ID']
    
    # メニューを指定(categoryIdの変更でメニュー範囲の変更可)
    item_parameters  = {
        'applicationId': APP_ID,
        'format':'json',
        'formatVersion': 2,
        'elements':'recipeDescription,recipeTitle,recipeIndication,recipeCost,recipeMaterial,recipeUrl',
        'categoryId':'36-494'
        }

    # jsonデータの取得
    
    res = requests.get(REQUESTS_URL, item_parameters)
    result = res.json()
    
    return result['result'][random.randint(0,3)]





