class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq = Counter(students)
        i, j = 0, 0
        while i < len(sandwiches) and j < len(students):
            if students[j] == sandwiches[i]:
                freq[students[j]] -= 1
                i += 1
                j += 1
                
            else:
                if freq[sandwiches[i]] == 0:
                    break
                students.append(students[j])
                j += 1
                
        return sum(freq.values())
            