from flask import Flask, json
import requests
from pprint import pprint

app = Flask(__name__)

@app.route("/")
def get_repo():
    repos_url = "https://api.github.com/users/EneroMangal4321/repos"
    response = requests.get(repos_url)
    response_list = response.json()
    for x in response_list:
        print(x["name"])
    return {"repos": response.json()}

@app.route("/commits")
def get_commits():
    commit_url = "https://api.github.com/repos/EneroMangal4321/mijn-amsterdam-stagair/commits"
    commit_response = requests.get(commit_url)
    commit_response_list = commit_response.json()
    for x in commit_response_list:
        print(x)
    return {"commits": commit_response.json()}
   

if __name__ == "__main__":
    app.run(debug=True)
