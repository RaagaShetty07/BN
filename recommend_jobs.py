#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from itertools import chain

with open("jobs.json", "r") as JSON:
    jobs = json.load(JSON)

with open("members.json", "r") as JSON:
    members = json.load(JSON)

# Given candidate profile bio and job lists, identify the right job by matching the words/keys.
# For example: software developer in bio should match with word "developer" in job description.
def score_jobs_based_on_the_profile(list1, list2):
    list2_lower = [element.lower() for element in list2]

    set2_lower = set(list2_lower)

    list1_filtered = [element for element in list1 if element.lower() not in set2_lower]

    return len(list1_filtered)


# Find the job with highest score( technically least numbers)
def find_matching_job(lst):
    if not lst:
        return []

    min_value = min(lst)

    positions = [index for index, value in enumerate(lst) if value == min_value]

    return positions


def print_results(lst, lst2):
    for i in lst:
        print(lst2[i])


for i in members:
    members_string = []
    final_job_matching_score = []
    final_job_details = []
    s1 = i["bio"].replace(",", "")
    members_string = s1.split()
    for j in jobs:
        jobs_string = []
        jobs_string = j["title"].split()
        jobs_string.append(j["location"])
        # print(members_string)
        # print(jobs_string)
        k = score_jobs_based_on_the_profile(jobs_string, members_string)
        # print(k)
        # print("===========")
        final_job_matching_score.append(k)
        final_job_details.append(j)
    print("name:", i["name"])
    print_results(find_matching_job(final_job_matching_score), final_job_details)
    print("==================================")
