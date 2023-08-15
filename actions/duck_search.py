from duckduckgo_search import DDGS


def duckduckgo_search(query, max_search_result=3):
    with DDGS() as ddgs:
        responses = list()
        for i, r in enumerate(ddgs.text(query, region='wt-wt', safesearch='off', timelimit='y')):
            if i == max_search_result:
                break
            responses.append(r)
        return responses