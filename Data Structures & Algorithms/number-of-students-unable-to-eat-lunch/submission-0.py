class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        itters = 0
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                itters = 0
            else:
                students.append(students[0])
                students.pop(0)
                itters += 1
            if itters >= len(students):
                break
        return len(students)