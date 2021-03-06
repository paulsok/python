class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists
        
    def score(self, goals_number=1):
        self.goals += goals_number 
    
    def make_assist(self, ass_number=1):
        self.assists += ass_number
    
    def statistics(self):
        print('%s %s - голы: %s, передачи: %s' % (self.surname, self.name, self.goals, self.assists))


leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics()
