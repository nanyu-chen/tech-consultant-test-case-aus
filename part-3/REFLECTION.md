# Reflection

## 1. Duration of the Technical Test
I completed the technical test within 2 hours, approximately 1 hour and 55 minutes. The actual implementation of the tasks took about 1 hour, while the remaining time was spent on resolving library dependencies and improving the app's performance.

## 2. Difficulty Level
The test was straightforward, but maintaining a high standard was not too easy. The basic implementation of the two tasks wasn't particularly challenging, but there were some tricky aspects to the questions. Here’s the breakdown:

### Easy Parts
- Implementing the basic functionality for both parts.
- Part 1, which involved fundamental Flask concepts and usage.
- Part 2, as I'm proficient in data processing with Python.

### Challenging Parts
1. **API Issues**: The given API (http://api.icndb.com/jokes/random/) returned a 404 error. After investigation, I found that the original API hadn't been maintained for three years. I resolved this by finding an alternative API (https://api.chucknorris.io/) through Google.

2. **Library Compatibility**: The `xlrd` library provided in the task no longer supports `.xlsx` files. I opted to use `pandas` for data processing instead of `openpyxl`, as `pandas` preserves zero values as default, while `openpyxl` adds complexity and requires manually handling each empty value when there are no sales in the 15 minutes period.

3. **Performance Optimization**: After building the basic app, I noticed the response time was slow when requesting the API 10 times using a for loop. I then thought of async requests to improve performance. I hadn’t really used asynchronous operations in Flask, so I spent time on Flask's official documentation to find the best way to write async requests to the API. This significantly improved response times:
   - Without logging: 5s
   - With logging: 8s
   - With retry and exponential backoff: 4s
   - With async (10 requests): 1s
   - With async and retry: 3s

4. **Reliability Optimization**: Given the recent global technical outage caused by a CrowdStrike patch update on Microsoft, I kept the idea of having the Flask server app reliable in mind. I implemented retry with exponential backoff to add an extra layer of reliability to return the desired output to the users of this Flask app.

5. **Library Dependency Conflicts**: Unifying requirements to ensure the app runs smoothly across different environments was unexpectedly challenging. I initially used a virtual environment without specifying library versions. When adding a `requirements.txt` file for clarity, I encountered dependency errors. I carefully read the new error messages in the terminal and adjusted library versions accordingly, updating the requirements to ensure anyone with access to my repo could easily spin up a Flask server.

## 3. Resources Used
- **Google**
- **Stack Overflow**
  - e.g., when resolving Mac user port conflicts issue: [Stack Overflow Link](https://stackoverflow.com/questions/72795799/how-to-solve-403-error-with-flask-in-python)
- **Official Documentation**
  - e.g., [Python Documentation](https://docs.python.org/)
  - [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html)
- **GitHub Repositories**
  - [icndb Repository](https://github.com/lorciv/icndb)
  - [ICNDB API Topics](https://github.com/topics/icndb-api)

## 4. Problem-Solving Process
When running the app, I noticed that despite no changes in the code, the app's response was unstable. I ruled out network issues and checked if the API endpoint was the problem without using the endpoint, encountering an "access denied" error. Suspecting it might be related to cookies, I tested using incognito mode and another browser, which slightly improved stability but not significantly. I then searched on Google and found a relevant Stack Overflow thread. The tech community provided insights on how other Mac users were having port conflicts on port 5000. During local tests, I tested the app on port 8080 instead, which resolved the issue. I noted to change the port back to 5000 when publishing the new commit.

## 5. Key Experiences and Notes
- I employed a Test-Driven Development (TDD) approach, which proved invaluable for ensuring high code quality and clearly defining the API's expected behavior upfront. TDD facilitated early issue detection and provided confidence in the code's correctness during changes and optimizations.

- Although I considered using Flask Blueprints for better modularity, I decided against it because the task only involved a single endpoint, making Blueprints unnecessary overhead for such a small-scale application. Instead, I manually modularized the code in the GitHub repository, which provided sufficient clarity.

- I utilized both `requirements.in` and `requirements.txt` files, which is considered a best practice in dependency management. The `requirements.in` file contains top-level dependencies without specific versions, making it easier to maintain and update. The `requirements.txt` file, generated from `requirements.in` using a tool like `pip-compile`, includes all dependencies with pinned versions, ensuring reproducible builds across different environments. This approach balances flexibility with reproducibility and helps avoid "works on my machine" problems by specifying exact versions.

- I encountered a `GET /favicon.ico HTTP/1.1 404` error due to a missing icon. Given the time constraints and its minimal impact on app functionality, I chose to ignore this issue for now.

- While writing this reflection document, I created a new empty environment to test the repo, where I intended to distribute the same dependencies for all users of this app, and discovered a missing library in the requirements, which I promptly added.
