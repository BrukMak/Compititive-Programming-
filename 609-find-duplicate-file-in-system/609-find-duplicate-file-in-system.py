class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for path in paths:
            directory, files = path.split(" ", 1)
            for file in files.split():
                file_content = file[file.index("("):-1]
                data[file_content].append(directory+"/"+file[0:file.index("(")])
        
        return [v for k, v in data.items() if len(v) >= 2]