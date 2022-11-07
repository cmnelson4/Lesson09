import requests

url_ddg = "https://api.duckduckgo.com"
president_match = official_list = [
    "lincoln",
    "jackson",
    "johnson",
    "obama",
    "harrison",
    "buren",
    "clinton",
    "coolidge",
    "arthur",
    "trump",
    "eisenhower",
    "adams",
    "roosevelt",
    "pierce",
    "bush",
    "washington",
    "bush",
    "ford",
    "cleveland",
    "truman",
    "hoover",
    "garfield",
    "buchanan",
    "polk",
    "madison",
    "monroe",
    "carter",
    "biden",
    "adams",
    "kennedy",
    "adams",
    "tyler",
    "johnson",
    "buren",
    "fillmore",
    "nixon",
    "reagan",
    "hayes",
    "roosevelt",
    "jefferson",
    "grant",
    "harding",
    "harrison",
    "taft",
    "mckinley",
    "wilson",
    "taylor",
]


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=presidents of the united states&format=json")
    rsp_data = resp.json()

    presidents_returned = []
    for pres in rsp_data["RelatedTopics"]:
        presidents_returned.append(
            pres["Text"].split("-")[0].replace(".", "").lower().strip().split()[-1]
        )

    for pres in president_match:
        assert pres in presidents_returned


test_ddg0()
