import json
from collections import Counter
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    usernames = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet.get('content', '')
            usernames += [word[1:] for word in content.split() if word.startswith('@')]
    username_count = Counter(usernames).most_common(10)
    return username_count