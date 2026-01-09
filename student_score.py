'''Implement a class Student. For the purpose of this exercise, a student has a name and a total quiz score. Supply an appropriate constructor and methods getName(), addQuiz(score), getTotalScore(), and getAverageScore(). The constructor should accept the student name and list of scores.

getName() - returns the student name
addQuiz(score) - adds additional score to the scores list
getTotalScore() - returns the total of the scores list
getAverageScore() - returns the average score
'''

class Student: # =None e =[] são valores default para as variáveis
    def __init__(self, name=None, scores=[]): 
        self.name = name
        self.scores = scores
        
    # Getter methods
    def getName(self):
        return self.name

    def getTotalScore(self):
        self.totalScore = sum(self.scores)
        return self.totalScore
    
    def getAveregeScore(self):
        if len(self.scores) == 0:
            return 0
        self.avgScore = sum(self.scores) / len(self.scores)
        return self.avgScore
    
    # Setters methods
    def addScore(self, score):
        self.scores.append(score)
        

# Inicialização do objeto
student = Student("Arthur", [5, 10, 8])


student.addScore(7)
student.addScore(8)

print(student.getName()) # ou print(student.name)
print(student.getTotalScore())
print(student.getAveregeScore())
