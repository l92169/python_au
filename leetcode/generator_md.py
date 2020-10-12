class LeetCodeSol:
    def __init__(self, title, link, code):
        self.title = title
        self.link = link
        self.code = code

    def get_md_title(self, source_lines):
        title = source_lines[0].split(". ")[1][:-1]
        return title

    def get_md_link(self, source_lines):
        link = source_lines[1].split("/")[-2]
        return link

    def get_md_formatsolution(self, source_lines):
        code = source_lines[3::]
        new_code = ""
        for new_line in code:
            new_code += new_line[4:]
        new_code = "```python\n" + new_code + "\n```"
        return new_code

    def get_Leetcodelink(self, source_lines):
        leetlink = source_lines[1]
        return leetlink


with open("source_leetcode_data.txt", 'r') as in_file:
    source_lines = in_file.readlines()
title = source_lines[0].split(". ")[:-1]
link = source_lines[1].split("/")[-2]
code = source_lines[3::]
leetlink = source_lines[1]
plus, other = '', ''
with open("intervals.md", 'r') as in_file:
    source_lines1 = in_file.readlines()
for i in range(1, len(source_lines1)):
    if source_lines1[i][0] == "+":
        plus += source_lines1[i]
    else:
        other += source_lines1[i]
out_file = open("intervals.md", 'w')
out_file.write("# {}\n\n{}".format("Intervals", plus))
out_file.write("+ [{}](#{}){}\n".format(LeetCodeSol.get_md_title(title, source_lines), LeetCodeSol.get_md_link(link, source_lines), other))
out_file.write("\n## {}\n\n".format(LeetCodeSol.get_md_title(title, source_lines)))
out_file.write("{}\n".format((LeetCodeSol.get_Leetcodelink(leetlink, source_lines))))
out_file.write("{}".format(LeetCodeSol.get_md_formatsolution(code, source_lines)))
out_file.close()
