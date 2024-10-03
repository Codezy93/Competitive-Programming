import os
from datetime import datetime
import subprocess

class l00DaysCodingChallenge:
    def __init__(self, filename, current_date):
        self.filename = filename
        self.current_date = current_date
        self.start_date = datetime(2024, 8, 4)
        self.days = (self.current_date - self.start_date).days
        self.check_base_file()
        self.problem_data = self.read_and_parse_file()
        self.create_files()
        self.table()
        self.git()
        self.post()

    def read_and_parse_file(self):
        with open(self.filename, 'r') as file:
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

    def create_files(self):
        for i in self.problem_data:
            platform_name, problem_name, code = i
            directory = os.path.join(platform_name)
            if not os.path.exists(directory):
                os.makedirs(directory)
            file_name = f"{problem_name.replace(' ', '_')}.md"
            file_path = os.path.join(directory, file_name)
            content = f"# {problem_name}\n\nDate: {self.current_date}\n\n## Solution\n\n#### Python\n```python\n{code}\n ```"
        with open(file_path, 'w') as file:
            file.write(content)

    def table(self):
        with open("README.md", 'a') as file:
            for i in self.problem_data:
                platform_name, problem_name, code = i
                file.write(f"| {problem_name} | {platform_name} | {self.current_date} |\n")

    def post(self):
        print(f"🌟 Day {self.days} of #100DaysOfCode! 🌟\n\nToday's Problems:\n\n")
        [print(f"{i[0]}: {i[1]}") for i in self.problem_data]
        print("\n\n#CodingChallenge #Programming #DSA")

    def git(self):
        msg = f"Day {self.days} of 100: 100 Days Coding Challenge"
        date_str = f"{self.current_date.strftime('%Y-%m-%d')} 11:11:11"
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", msg], env=env, check=True)
        subprocess.run(["git", "push"], check=True)

    def check_base_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write('CodeForces\n\n====X====\nCodeWars\n\n====X====\nGeekForGeeks\n\n====X====\nHackerEarth\n\n====X====\nHackerRank\n\n====X====\nLeetCode\n\n')

if __name__ == "__main__":
    filename = input("Enter filename (default: 'problems.txt'): ") or "problems.txt"
    change_date = input("Want to change date? (y/n): ").strip().lower()
    if change_date == 'y':
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        current_date = datetime(year, month, day)
    else:
        current_date = datetime.now()
    challenge = l00DaysCodingChallenge(filename, current_date)