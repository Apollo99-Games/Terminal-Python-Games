from BlackJackPlayer import player

player_test = player(1)

player_test.points = 21

assert player_test.player_bust() == True

player_test.points = 15

assert player_test.player_bust() == False

player_test.points = 30

assert player_test.player_bust() == True 

player_test.points = 19

assert player_test.player_bust() == False

player_test.points = 0

assert player_test.player_bust() == False

player_test.points = 20

assert player_test.player_bust() == False

player_test.points = 22

assert player_test.player_bust() == True 

player_test.points = 1

assert player_test.player_bust() == False


