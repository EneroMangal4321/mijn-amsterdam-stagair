from flask import Flask, json, jsonify, Response, request
import requests

app = Flask(__name__)

@app.route("/")
def check_for_user():
    username = get_username()
    repo_output_dict = get_repositories(username)
    repos_response = repo_output_dict["repos_response"]
    repos_url = repo_output_dict["repos_url"]
    repos_response_list = repo_output_dict["repos_response_list"]

    if repos_response.status_code == 200:
        return show_repos_and_last_commit(repos_response_list)
    return f"FAIL: {repos_response.status_code}. Vul een geldige gebruiker in."

def show_repos_and_last_commit(repos_response_list):
    username = get_username()
    item_list = []
    for x in repos_response_list:
        naam_repo = x["name"]
        laatste_commit = get_last_commit(naam_repo, username)
        item = make_dict(naam_repo, laatste_commit)
        item_list.append(item)
    return output(item_list)

#get the username from the url
def get_username():
    username = request.args.get("username")
    return username

#get all the repositories from the given github user
def get_repositories(username):
    repos_url = "https://api.github.com/users/%s/repos" % (username)
    repos_response = requests.get(repos_url)

    repos_response_list = repos_response.json()
    return {"repos_response_list" : repos_response_list, "repos_response" : repos_response, "repos_url" : repos_url}

#get the last commit from the given repository
def get_last_commit(repo_name, username):
    commit_url = "https://api.github.com/repos/%s/%s/commits" % (username, repo_name)
    commit_response = requests.get(commit_url)
    commit_response_list = commit_response.json()
    print("dit is", commit_response_list)
    if commit_response_list:
        laatste_commit = commit_response_list[0]['commit']['message']
    else:
        laatste_commit = "Deze repo heeft geen commits."

    return laatste_commit
    

#create a dict from the given information 
def make_dict(repo_name, laatste_commit):

    item = {
            "repository_name": repo_name,
            "last_submitted_commit": laatste_commit
        }
    
    return item


def output(item_list):
    return jsonify(item_list)



if __name__ == "__main__":
    app.run(debug=True)

#Check of er uberhoubt een username is ingevuld met een if statement bovenaan.
#Verdeel de code in verschillende functies op.
# 
