import yaml
import sqlite3
import os

with open(os.path.join('config', 'topics.yaml'), 'r') as file:
    topic_items = yaml.safe_load(file)

connection = sqlite3.connect(os.path.join('data', 'news_aggregator.db'))
cursor = connection.cursor()

success_count = 0
failure_count = 0

for topic_item in topic_items :
    keywords = ','.join(topic_item['keywords'])
    db_tuple = (topic_item['name'], keywords, topic_item['enabled'])
    try :
        cursor.execute("""INSERT INTO topics
                       (name, keywords, enabled) VALUES (?, ?, ?) 
                       ON CONFLICT(name) do UPDATE SET 
                       keywords = excluded.keywords, 
                       enabled = excluded.enabled;
                       """, db_tuple)
        success_count+=1
    except Exception as e :
        print(f"Failed to insert {topic_item['name']}: {e}")
        failure_count += 1

connection.commit()
connection.close()

print(f"Successfully added/updated {success_count} topics")
print(f"Failed to add/update {failure_count} topics")
