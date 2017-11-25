import requests
from typing import List


def get_trending_words(operator: str) -> List[str]:
    url = 'http://commutelondon.com/CommuteLondon/CommuteLondon?getrequest=wordlistrelated&gettocname={}'.format(operator)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/62.0.3202.94 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    words = [line.split('!|!') for line in response.text.split('~|~')]

    seen = set()
    seen_add = seen.add
    return [word[0] for word in words if word[0] != '' and not (word[0] in seen or seen_add(word[0]))]


if __name__ == "__main__":
    words = get_trending_words("VT+EAST+COAST")
    print(words, "({})".format(len(words)))
