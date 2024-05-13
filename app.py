from flask import Flask, request, render_template, redirect, url_for
import api_manager

# アプリ生成
app = Flask(__name__)

# ルーティング
@app.route("/")
def form():
    return render_template('form.html')

@app.route("/summon", methods=['GET', 'POST'])
def summon():
    if request.method == 'POST':
        result = api_manager.get_dish()
        return render_template('summon.html', data=result)
    else: 
        return redirect(url_for('form'))


    
if __name__ == "__main__":
    app.run()