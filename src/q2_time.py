import json
import emoji
from collections import Counter
from typing import List, Tuple

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emojis = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            content = tweet.get('content', '')
            emojis += [c for c in content if c in emoji.UNICODE_EMOJI['en']]
    emoji_count = Counter(emojis).most_common(10)
    return emoji_count
