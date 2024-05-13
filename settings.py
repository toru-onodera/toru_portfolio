import os
from dotenv import load_dotenv

# .envファイルの内容を読み込む
load_dotenv()

# os.environdeで環境変数を表示
# print(os.environ['APP_ID'])
os.environ['APP_ID']