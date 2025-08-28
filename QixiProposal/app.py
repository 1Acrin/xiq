from flask import Flask, render_template

# 初始化 Flask 应用
app = Flask(__name__)

# 首页路由（求婚选择页面）- 修正模板文件名称
@app.route('/')
def proposal():
    return render_template('proposal.html')  # 这里之前写成了 index.html，现在修正为 proposal.html

# 信件页面路由（同意后跳转）
@app.route('/letter')
def letter():
    return render_template('letter.html')

# 本地运行入口
if __name__ == '__main__':
    app.run(debug=True)