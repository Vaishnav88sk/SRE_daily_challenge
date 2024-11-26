import json
from datetime import datetime

with open("buckets.json", "r") as file:
    data = json.load(file)

print("Bucket Summary:")
for bucket in data["buckets"]:
    print(f"Name: {bucket['name']}, Region: {bucket['region']}, "
          f"Size: {bucket['sizeGB']} GB, Versioning: {bucket['versioning']}")

current_date = datetime.now()


def days_since_created(created_on):
    created_date = datetime.strptime(created_on, "%Y-%m-%d")
    return (current_date - created_date).days

unused_buckets = []
for bucket in data["buckets"]:
    if bucket["sizeGB"] > 80 and days_since_created(bucket["createdOn"]) > 90:
        unused_buckets.append(bucket)

print("\nBuckets > 80 GB and unused for 90+ days:")
for bucket in unused_buckets:
    print(f"Name: {bucket['name']}, Region: {bucket['region']}, Size: {bucket['sizeGB']} GB")



cost_report = {}
deletion_queue = []
archival_candidates = []



for bucket in data["buckets"]:
    region = bucket["region"]
    department = bucket["tags"]["team"]
    cost_report.setdefault(region, {}).setdefault(department, 0)
    cost_report[region][department] += bucket["sizeGB"]

    if bucket["sizeGB"] > 50:
        print(f"\nRecommendation: Cleanup for {bucket['name']} (Size: {bucket['sizeGB']} GB)")

    if bucket["sizeGB"] > 100 and days_since_created(bucket["createdOn"]) > 20:
        deletion_queue.append(bucket)
    
    if bucket["sizeGB"] > 80 and days_since_created(bucket["createdOn"]) > 180:
        archival_candidates.append(bucket)

print("\nCost Report:")
for region, departments in cost_report.items():
    print(f"Region: {region}")
    for dept, cost in departments.items():
        print(f"  Department: {dept}, Total Size: {cost} GB")

print("\nBuckets marked for deletion: ")
for bucket in deletion_queue:
    print(f"Name: {bucket['name']}, Region: {bucket['region']}, Size: {bucket['sizeGB']} GB")

print("\nBuckets recommended for archival (e.g., Glacier): ")
for bucket in archival_candidates:
    print(f"Name: {bucket['name']}, Region: {bucket['region']}, Size: {bucket['sizeGB']} GB")
