# Day 2 of SRE Challenge

## Challenge 2: (Cloud Storage Optimization)
Using a provided JSON file (buckets.json), create a Python script to analyze, modify, and optimize S3 bucket metadata.

Requirements:
Using the provided JSON file, implement the following:

1. Print a summary of each bucket: Name, region, size (in GB), and versioning status

2. Identify buckets larger than 80 GB from every region which are unused for 90+ days. 

3. Generate a cost report: total s3 buckets cost grouped by region and department. 

       Highlight buckets with:
            Size > 50 GB: Recommend cleanup operations.
            Size > 100 GB and not accessed in 20+ days: Add these to a deletion queue.
4. Provide a final list of buckets to delete (from the deletion queue). For archival candidates, suggest moving to Glacier.

## Outputs: 

![Screenshot 1](https://github.com/Vaishnav88sk/SRE_daily_challenge/blob/main/Day_2/outputs/Day2_Screenshot_1.png?raw=true)

![Screenshot 2](https://github.com/Vaishnav88sk/SRE_daily_challenge/blob/main/Day_2/outputs/Day2_Screenshot_2.png?raw=true)
