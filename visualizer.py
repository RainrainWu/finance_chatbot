# import os
# from github import Github
from dotenv import load_dotenv

ENDPOINT = "https://rainrainwu.github.io/finance_visualizer/"

load_dotenv()
embed = (
    "<iframe"
    " id=\"igraph\""
    " scrolling=\"no\""
    " style=\"border:none;\""
    " seamless=\"seamless\""
    " src=\"{source}\""
    " height=\"525\""
    " width=\"100%\""
    ">"
    "</iframe>"
)


class GithubUser():

    def __init__(self):
        pass
        # self.user = Github(os.getenv("GITHUB_TOKEN"),
        #                    timeout=600).get_user("RainrainWu")

    def update_visualizer(self, src):
        pass
        # repo = self.user.get_repo("finance_visualizer")
        # target = repo.get_contents("")[1]
        # repo.update_file(target.path, "update visualizer",
        #                  embed.format(source=src),
        #                  target.sha, branch="master")
