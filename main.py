import os
from datetime import datetime
from pprint import pprint
from subprocess import call

def read_and_parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    problems = content.split('====X====')
    problem_data = []
    for problem in problems:
        lines = problem.strip().split('\n')
        if len(lines) < 3:
            continue
        platform_name = lines[0].strip()
        problem_name = lines[1].strip()
        code = '\n'.join(lines[2:])
        problem_data.append((platform_name, problem_name, code))

    return problem_data

def create_files(problem_data):
    current_date = datetime.now().strftime('%d-%m-%Y')

    for i in problem_data:
        platform_name, problem_name, code = i
        directory = os.path.join(platform_name)
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_name = f"{problem_name.replace(' ', '_')}.md"
        file_path = os.path.join(directory, file_name)

        content = f"""
# {problem_name}

Date: {current_date}

## Solution
#### Python
```python
{code}
```
        """
    
        with open(file_path, 'w') as file:
            file.write(content)

def table(problem_data):
    current_date = datetime.now().strftime('%d-%m-%Y')
    with open("README.md", 'a') as file:
        for i in problem_data:
            platform_name, problem_name, code = i
            file.write(f"| {problem_name} | {platform_name} | {current_date} |\n")

def post(problem_data):
    print(f"🌟 Day {(datetime.now() - datetime(2024, 8, 4)).days} of #100DaysOfCode! 🌟")
    print("")
    print("Today's Problems:")
    print("")
    for i in problem_data:
        platform_name, problem_name, code = i
        print(f"{platform_name}: {problem_name}")
    print("#CodingChallenge #Programming #DSA")

def git():
    msg = f"Day {(datetime.now() - datetime(2024, 8, 4)).days} of 100: 100 Days Coding Challenge"
    print(msg)
    commands = [
        "git add .",
        f'git commit -m "{msg}"',
        "git push"
    ]
    for i in commands:
        call(i)

def main():
    input_file = 'problems.txt'
    problem_data = read_and_parse_file(input_file)
    create_files(problem_data)
    table(problem_data)
    inp = input("Confirm to push changes to git: ")
    if inp == "1":
        git()
    print()
    post(problem_data)

main()

'''
CodeForces

====X====
CodeWars

====X====
GeekForGeeks

====X====
HackerEarth

====X====
HackerRank

====X====
LeetCode

'''
