#Letters and points scores as two seperate lists
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Letters and point score stored as dictionary
letters_to_points = {k: v for k, v in zip(letters, points)}

#Adding blank tile
letters_to_points[" "] = 0

#Test of dictionary
##print(letters_to_points)

#Function to calculate the score of a word in scrabble
def score_word(word):
    word_upper = word.upper()  #All uppercase to match dictionary
    point_total = 0

    for i in range(len(word_upper)):
        if word_upper[i] in letters_to_points:
            point_total += letters_to_points[word_upper[i]]

    return point_total


#test to check scores
##print(score_word("brownie")) ## 15
##print(score_word("zoo")) #12
##print(score_word("scrabble")) #14

#test input of {players: [words played]}
player_to_words = {'player1': ['blue', 'tennis', 'exit'] , 'wordNerd': ['earth', 'eyes', 'machine'], 'Lexi Con': ['eraser', 'belly', 'husky'], 'Prof Reader': ['zap', 'coma', 'period']}

#Dictionary to score players point
player_to_points = {}

#Calculate current score from this position
for players in player_to_words:
    player_points = 0
    for word in player_to_words[players]:
        player_points += score_word(word)
    player_to_points[players] = player_points

#Function for adding word to those played
def play_word(player, word):
    player_to_words[player].append(word)
    points1 = score_word(word)
    player_to_points[player] += points1
    print("{player} played the word {word} for {points1}.".format(player=player, word=word, points1=points1))
    print("Updated score:")
    print(player_to_points)
    return

#Simulating an extra round
play_word("player1", "scrabble")
play_word("wordNerd", "bilbo")
play_word("Lexi Con", "baggins")
play_word("Prof Reader", "toast")

#print(player_to_points)

#print(player_to_words)