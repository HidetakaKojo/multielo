# MultiELO

ELO rating for multiple players. see [this site](http://sradack.blogspot.com/2008/06/elo-rating-system-multiple-players.html)


Useage:

```
from multielo import Player, Match

match = Match([Player("001", 2, 1600), Player("002", 1, 1400), Player("003", 2, 1200), Player("0004", 2, 1100), Player("005", 1, 1500)])
match.calcualte_rating()

match = Match([Player("001", 2, 1600), Player("002", 1, 1400), Player("003", 2, 1200), Player("004", 2, 1100), Player("005", 1, 1500)])
match.calculate_rating()
match.get_player("001").post_rating # 1592.781879614913
match.get_player("002").post_rating # 1404.1313425824455
match.get_player("003").post_rating # 1199.608938491919
match.get_player("004").post_rating # 1101.1037956367375
match.get_player("005").post_rating # 1502.3740436739854
```
