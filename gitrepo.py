from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST'])
def index():

    # route to render homepage
    return render_template("index.html")

@app.route("/search", methods=['GET', 'POST'])
def search_repos():
    # Get username input from html form
    #remove this with html update
    #username = "octocat"
    username = request.form["username"]

    # Build url with specified username, call api
    repo_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(repo_url)
    if response.status_code == 200:
        repo_info = response.json()
        #dict keys from json we want to display in html, may remove with json update
        keep_info = ["name", "description", "git_url", "language", "stargazers_count"]
        #goes through dict (repo in repo_info) and keeps only designated keys (k in keep_info)
        repos = [{k: repo[k] for k in keep_info} for repo in repo_info]
        #print(filtered_list)

        #print(repo_info)

    else:
        print(f"Repositories not retrieved, received status code: {response.status_code}")
    #this returns right - check notes but think you can start on html and passing this info over to display
    return render_template("index.html", username=username, repos=repos)


if __name__ == "__main__":
    app.run(debug=True)