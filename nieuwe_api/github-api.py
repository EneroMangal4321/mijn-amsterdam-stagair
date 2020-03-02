from flask import Flask, json, jsonify, Response, request
import requests
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def get_repo():
    username = request.args.get("username")
    repos_url = "https://api.github.com/users/%s/repos" % (username)
    repos_response = requests.get(repos_url)
    if repos_response.status_code != 200:
        return "Je hebt een verkeerde gebruikersnaam ingevuld. Vul de goede gebruikersnaam in."
    repos_response_list = repos_response.json()
    item_list = []

    for repos_info_response in repos_response_list:
        try:
            commit_url = "https://api.github.com/repos/%s/%s/commits" % (username, repos_info_response["name"])
        except:
            return "Je hebt een verkeerde gebruikersnaam ingevuld. Vul de goede gebruikersnaam in."
        commit_response = requests.get(commit_url)
        commit_response_list = commit_response.json()
        eerste_item = commit_response_list[0]['commit']['message']

        item = {
            "repository_name": repos_info_response["name"],
            "last_submitted_commit": eerste_item
        }
        item_list.append(item)
    
    item_list_json = json.dumps(item_list, sort_keys=False)
    return Response(item_list_json, mimetype='application/json') #jsonify(item_list)
   

if __name__ == "__main__":
    app.run(debug=True)
