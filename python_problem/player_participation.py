#player participation analysis
cricket = {"PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"}
football = {"PKM", "ALN", "RMZ", "CS", "MCS"}
badminton = {"PKM", "ALN", "NV", "KM", "RMV"}

#Players who play all three
all_three = cricket & football & badminton
print("Players who play all three games:", list(all_three))

#Players who play exactly one game
all_players = cricket | football | badminton
one_game_players = []
for player in all_players:
    games_played = sum([
        player in cricket,
        player in football,
        player in badminton
    ])
    if games_played == 1:
        one_game_players.append(player)

print("Players who play exactly one game:", one_game_players)
