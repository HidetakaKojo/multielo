import math

class Player:
    def __init__(self, name, order, pre_rating=1000):
        self.name = name
        self.order = order
        self.pre_rating = pre_rating
        self.post_rating = None
        self.place = None

class Match:
    def __init__(self, players, K = 32, D = 400.0):
        self.players = players
        self.K = K
        self.D = D

    def get_player(self, name):
        for p in self.players:
            if p.name == name:
                return p


    def calcualte_place(self):
        if len(self.players) < 1:
            return

        sorted_players = sorted(self.players, key=lambda x: x.order)
        same_place_players = []
        order = None
        for i, p in enumerate(sorted_players):
            p.place = i + 1
            if p.order == order:
                same_place_players.append(p)
            else:
                if len(same_place_players) > 0:
                    place = float(sum([x.place for x in same_place_players])) / len(same_place_players)
                    for x in same_place_players:
                        x.place = place
                order = p.order
                same_place_players = [p]
        place = float(sum([x.place for x in same_place_players])) / len(same_place_players)
        for x in same_place_players:
            x.place = place

    def calculate_rating(self):
        self.calcualte_place()
        for p in self.players:
            est = 0.0
            for o in self.players:
                if p == o:
                    continue

                est += 1 / (1 + math.pow(10, (o.pre_rating - p.pre_rating)/self.D))

            players_num = len(self.players)
            games_num = players_num * (players_num - 1) / 2
            est = est / games_num
            score = (players_num - p.place) / games_num

            p.post_rating = p.pre_rating + self.K * (score - est)
