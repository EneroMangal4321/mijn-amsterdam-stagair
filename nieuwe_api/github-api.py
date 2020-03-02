from flask import Flask, json
import requests
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def get_repo():
    repos_url = "https://api.github.com/users/EneroMangal4321/repos"
    repos_response = requests.get(repos_url)
    repos_response_list = repos_response.json()
    for x in repos_response_list:
        print("{")
        print("repo:"  + json.dumps(x["name"]))
        commit_url = "https://api.github.com/repos/EneroMangal4321/" + x["name"] + "/commits"
        commit_response = requests.get(commit_url)
        commit_response_list = commit_response.json()
        eerste_item = commit_response_list[0]['commit']['message']
        print("commit:" + json.dumps(eerste_item))
        print("}")

    return {"repos": repos_response.json()} 
   

if __name__ == "__main__":
    app.run(debug=True)
