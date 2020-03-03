from flask import Flask, json, jsonify, Response, request
import requests
import urllib3

app = Flask(__name__)

@app.route("/")
#get the username from the url
def get_username():
    username = request.args.get("username")

#get all the repositories from the given github user
def get_repositories(username):
    repos_url = "https://api.github.com/users/%s/repos" % (username)
    repos_response = requests.get(repos_url)
    if repos_response.status_code != 200:
        return "Je hebt een niet bestaande gebruikersnaam ingevuld. Vul de goede gebruikersnaam in."
    repos_response_list = repos_response.json()
    return
    
#get the last commit from all the repositories
def get_last_commit(repos_response_list, username):
    for repos_info_response in repos_response_list:
        commit_url = "https://api.github.com/repos/%s/%s/commits" % (username, repos_info_response["name"])
        commit_response = requests.get(commit_url)
        commit_response_list = commit_response.json()
        eerste_item = commit_response_list[0]['commit']['message']
        return

#create a valid json output from the given information 
def make_json_output(repos_info_response, eerste_item):
    item_list = []
    item = {
        "repository_name": repos_info_response["name"],
        "last_submitted_commit": eerste_item
    }
    item_list.append(item)
    item_list_json = json.dumps(item_list, sort_keys=False)
    return

#return repositories and last commits from the repositories of the given github user
def output(item_list):
    return Response(item_list_json, mimetype='application/json') #jsonify(item_list)

if __name__ == "__main__":
    app.run(debug=True)

#Check of er uberhoubt een username is ingevuld met een if statement bovenaan.
#Verdeel de code in verschillende functies op.
