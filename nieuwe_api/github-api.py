from flask import Flask, json, jsonify, Response, request
import requests
import urllib3

app = Flask(__name__)

@app.route("/")
def test():
    username = get_username()
    # repos_response_list = get_repositories(username)
    # eerste_item = get_last_commit(repos_response_list, username)
    return get_repositories(username)
    # return get_last_commit(repos_response_list,username)
#get the username from the url
def get_username():
    username = request.args.get("username")
    # repositories = get_repositories(username)
    # laatste_commit = get_last_commit(repositories, username)
    # json_output = make_json_output(repositories, laatste_commit)
    return username

#get all the repositories from the given github user
def get_repositories(username):
    repos_url = "https://api.github.com/users/%s/repos" % (username)
    repos_response = requests.get(repos_url)
    if repos_response.status_code != 200:
        return "Je hebt een niet bestaande gebruikersnaam ingevuld. Vul de goede gebruikersnaam in."
    repos_response_list = repos_response.json()
    repos_response_list_json = json.dumps(repos_response_list)
    return Response(repos_response_list_json, mimetype='application/json')

#get the last commit from all the repositories
def get_last_commit(repos_response_list, username):
    commit_list = []
    for repos_info_response in repos_response_list:
        print("tf is dit", repos_info_response)
        commit_url = "https://api.github.com/repos/%s/%s/commits" % (username, repos_info_response["name"])
        
        commit_response = requests.get(commit_url)
        commit_response_list = commit_response.json()
        print("1")
        commit_list.append(commit_response_list[0]['commit']['message'])
        print("2")
    commit_list.json()
    return repos_info_response
        

#create a valid json output from the given information 
def make_json_output(repos_info_response, eerste_item):
    print(repos_info_response)
    item_list = []
    item = {
        {"repository_name": repos_info_response["name"],
        "last_submitted_commit": eerste_item}
    }
    item_list.append(item)
    item_list_json = json.dumps(item_list, sort_keys=False)
    return item_list_json


#return repositories and last commits from the repositories of the given github user
def output(item_list):
    return Response(item_list_json, mimetype='application/json') #jsonify(item_list)



if __name__ == "__main__":
    app.run(debug=True)

#Check of er uberhoubt een username is ingevuld met een if statement bovenaan.
#Verdeel de code in verschillende functies op.
