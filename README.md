# BN

recommend_jobs.py identifies the potential jobs for the given candidate based on the candidate's bio.

How does recommend_jobs algo works for below sample?

Person's bio:   [{ "name": "Joe", "bio": "I'm a designer from London, UK" }]
Jobs available: [{"title": "Sales Internship", "location": "London"},{ "title": "UX Designer","location": "London"}]

Solution:

Step 1: Split the person bio description into tokens.
  [{"I'm", "a", "designer", "from", "London", "UK"}]

Step 2: Iterate through the job listings and split the job description into tokens.
  [{"Sales", "Internship", "London"}, {"UX", "Designer", "London"}

Step 3: Compare and remove the duplicate tokens of job with person bio. The o/p would look like this
  [{"Sales", "Internship"}, {"UX"}] ==> London and Designer are the common words between job and person's bio.

Step 4: Identify the job listing with minimum words left
    ["UX"]

Step 5: Print the original description of the identified job along with person name

Limitations:
1. If a candidate mentions he/she is looking for a job "Outside of London" or "Not in London", program won't consider this choice and suggests the jobs listed in London.
2. If a candidate doesn't mention any particular location, all the job listings will be recommended.
3. If a candidate mentiones "design" in bio and the job listing has "Designer", program fails to identify this as potential job.
   
  

  



