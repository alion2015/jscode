import csv
import re

def extract_topics_from_csv(file_path):
    topics_count = {}
    
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            client_cmd = row['client_cmd']
            matches = re.findall(r'"topic":"([^"]+)"', client_cmd)
            for topic in matches:
                if topic in topics_count:
                    topics_count[topic] += 1
                else:
                    topics_count[topic] = 1
                if(topic.startswith("usr")):
                    print(row["#account_id"])

    return topics_count

if __name__ == "__main__":
    csv_file_path = "data.csv"
    topics_count_dict = extract_topics_from_csv(csv_file_path)
    
    print("Topics and their occurrence count (sorted by occurrence count in descending order):")
    sorted_topics = sorted(topics_count_dict.items(), key=lambda x: x[1], reverse=True)
    #grpfEs2E1hvgZs
    
