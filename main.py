player_score = 0

player_name = input("Welcome to GC mini golf! What is your name?")
hole_count = int(input(f"Hi, {player_name}! Would you like to play 3 or 6 holes today?"))
course_par = hole_count * 3

for h in range(1,hole_count+1):
    stroke_count = 0
    stroke_count = int(input(f"How many putts for hole {h}? (par is 3)"))
    player_score += stroke_count

final_par = player_score - course_par

if final_par == 0:
    print(f"Good game, {player_name}. Your total score was: 0.")
elif final_par > 0:
    print(f"Nice try, {player_name}. Your total score was: +{final_par}.")
else:
    print(f"Great job, {player_name}! Your total score was: {final_par}")