import requests
import json

mensagem = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=04cbfaf5e44863ac8ec9d6ab3a302fc917cff66c')

mensgem_Json = json.dumps(mensagem)
print (mensagem_json)
