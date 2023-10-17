# TSU-CHENG, LU
# ITM 513 (02)     07/07/2023
# Lab6 
# Description: This program will accurate the student scores, and display their average and range

class Student:

    Scores = {}

    # initializing the constructor method
    def __init__(self, name, grade):
        self.name = name
        self.initialgrade = grade
        self.grade = grade
    
    def getScores(self):

        answer_key = []
        # read into answer_key list, the answer key from file
        answer_key = [line.strip() for line in open("answers.txt", 'r')]

        student_answers = []
        # read into student_answers list, student answers from file
        student_answers = [line.strip().split(',') 
                           for line in open("data.txt", 'r')]
        total_score = 100

        #---start your loop processing logic here---#
        for student in student_answers:
            if student[0].lower() == self.getName().lower():
                for i in range(1, len(answer_key) + 1):
                    if student[i].lower() != answer_key[i - 1]:
                        total_score -= 10
        #---end your loop processing logic here---#

    #---continue the class definition#
        self.grade = total_score
        Student.Scores[self.getName()] = total_score

    def getName(self):
        return self.name

    @staticmethod
    def sortDict():
        return sorted(Student.Scores.items())
    
    def getInitialgrade(self):
        return self.initialgrade
    
    def getNewgrade(self):
       return self.grade
    
    def getAveragegrade(self):

        return (self.initialgrade + self.grade) / 2
    
    def getGraderange(self):
        return abs(self.getNewgrade() - self.getInitialgrade())

    def getOverallAverageGrade():
        total = 0
        for student in student_objs:
            total += student.getAveragegrade()
        return total / len(student_objs)

    def getOverallAveragerange():
        total = 0
        for student in student_objs:
            total += abs(student.getNewgrade() - student.getInitialgrade())
        return total / len(student_objs)
    #---end the class definition#

#student objects
student_objs = [
    Student('Sammy Student', 65),
    Student('Betty sanchez', 45),
    Student('Alice brown', 100),
    Student('tom Schulz', 50),
    Student('Tsucheng Lu', 90),
]

#display the outputs
for student in student_objs:
    student.getScores()

for student in student_objs:
    print(student.getName(), "has Old score:", student.getInitialgrade())
    print(student.getName(), "has New score:", student.getNewgrade())
    print("Average Grade:", student.getAveragegrade())
    print("Grade Range:", student.getGraderange())
    print()

print("Overall Average Grade:", Student.getOverallAverageGrade())
print("Overall Average Range:", Student.getOverallAveragerange())