from q1_time import q1_time
from q1_memory import q1_memory
from q2_time import q2_time
from q2_memory import q2_memory
from q3_time import q3_time
from q3_memory import q3_memory

# Ruta al archivo JSON con datos de tweets
file_path = 'C:/Users/jack.loli/Documents/farmers-protest-tweets-2021-2-4.json'

# Llamar a las funciones correspondientes
top_dates_and_users = q1_time(file_path)
memory_usage_q1 = q1_memory(file_path)
top_emojis_time = q2_time(file_path)
memory_usage_q2 = q2_memory(file_path)
top_users_time = q3_time(file_path)
memory_usage_q3 = q3_memory(file_path)

# Imprimir resultados de q1_time y q1_memory
print("Top 10 dates and most active users:")
for date, user in top_dates_and_users:
    print(f"Date: {date}, Most active user: {user}")

print("\nMemory usage for q1_memory:")
for date, memory in memory_usage_q1:
    print(f"Date: {date}, Memory usage: {memory}")

# Imprimir resultados de q2_time y q2_memory
print("\nTop 10 emojis and their counts (Time-optimized):")
for emoji, count in top_emojis_time:
    print(f"Emoji: {emoji}, Count: {count}")

print("\nMemory usage for q2_memory:")
for emoji, memory in memory_usage_q2:
    print(f"Emoji: {emoji}, Memory usage: {memory}")

# Imprimir resultados de q3_time y q3_memory
print("\nTop 10 users and their mention counts (Time-optimized):")
for user, count in top_users_time:
    print(f"User: {user}, Mention count: {count}")

print("\nMemory usage for q3_memory:")
for user, memory in memory_usage_q3:
    print(f"User: {user}, Memory usage: {memory}")