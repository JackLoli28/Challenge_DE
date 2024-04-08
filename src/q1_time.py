from datetime import datetime
from typing import List, Tuple
import json


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_user_counts = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            created_at = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            username = tweet['user']['username']

            if created_at in date_user_counts:
                if username in date_user_counts[created_at]:
                    date_user_counts[created_at][username] += 1
                else:
                    date_user_counts[created_at][username] = 1
            else:
                date_user_counts[created_at] = {username: 1}

    sorted_dates = sorted(date_user_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    result = []
    for date, user_counts in sorted_dates:
        max_user = max(user_counts, key=user_counts.get)
        result.append((date, max_user))

    return result


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_user_counts = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            created_at = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            username = tweet['user']['username']

            if created_at in date_user_counts:
                if username in date_user_counts[created_at]:
                    date_user_counts[created_at][username] += 1
                else:
                    date_user_counts[created_at][username] = 1
            else:
                date_user_counts[created_at] = {username: 1}

    sorted_dates = sorted(date_user_counts.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]

    result = []
    for date, user_counts in sorted_dates:
        max_user = max(user_counts, key=user_counts.get)
        result.append((date, max_user))

    return result