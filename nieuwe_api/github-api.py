from flask import Flask, json, jsonify, Response, request
import requests
import urllib3

app = Flask(__name__)

@app.route("/")
def test():
    username = get_username()
    repos_response_list = get_repositories(username)
    for x in repos_response_list:
        naam_repo = x["name"]
        laatste_commit = get_last_commit(naam_repo, username)
        print(naam_repo, laatste_commit)
        item_list_json = make_json_output(naam_repo, laatste_commit)
    return output(item_list_json)
    # last_commit = get_last_commit(repos_response_list, username)
    # item_list_json = make_json_output(repos_response_list, last_commit)
    # return output(item_list_json)

#get the username from the url
def get_username():
    username = request.args.get("username")
    return username

#get all the repositories from the given github user
def get_repositories(username):
    repos_url = "https://api.github.com/users/%s/repos" % (username)
    repos_response = requests.get(repos_url)
    if repos_response.status_code != 200:
        return "Je hebt een niet bestaande gebruikersnaam ingevuld. Vul de goede gebruikersnaam in."

    repos_response_list = repos_response.json()
    return repos_response_list

#get the last commit from all the repositories
def get_last_commit(repo_name, username):
    commit_url = "https://api.github.com/repos/%s/%s/commits" % (username, repo_name)
    commit_response = requests.get(commit_url)
    commit_response_list = commit_response.json()
    
    laatste_commit = commit_response_list[0]['commit']['message']
    # print("Dit is een", laatste_commit)
    return laatste_commit
    # print("hallo ", repos_response_list)
    # for repos_info_response in naam:
    #     commit_url = "https://api.github.com/repos/%s/%s/commits" % (username, repos_info_response["name"])
    #     commit_response = requests.get(commit_url)
    #     commit_response_list = commit_response.json()
    #     eerste_item = commit_response_list[0]['commit']['message']
    #     return eerste_item

#create a valid json output from the given information 
def make_json_output(repo_name, laatste_commit):
    item_list = []
    item = {
            "repository_name": repo_name,
            "last_submitted_commit": laatste_commit
        }
    item_list.append(item)
    item_list_json = json.dumps(item_list, sort_keys=False)
    print(item_list_json)
    return item_list_json

#return repositories and last commits from the repositories of the given github user
def output(item_list_json):
    return Response(item_list_json, mimetype='application/json') #jsonify(item_list)



if __name__ == "__main__":
    app.run(debug=True)

#Check of er uberhoubt een username is ingevuld met een if statement bovenaan.
#Verdeel de code in verschillende functies op.
# 
