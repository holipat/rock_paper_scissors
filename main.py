import random

def print_score(hero_score, computer_score):
  print(f"Hero score: {hero_score}")
  print(f"Computer score: {computer_score}")
  
def rock_paper_scissors_ALEYNA_BERGAMA():

  action_list = ["magic", "human", "nature", "technology"]
  yes_or_no = ["yes", "no"]
  hero_score = 0
  computer_score = 0

  is_nature_destroyed = False
  tech_count = 0

  round_number = 0
  print("""Welcome to the universe! Overcome challenges, defeat the computer and save your world from the meteor shower.
  Let's tell you how you can beat the computer.
  Magic and nature are in harmony and balance.
  But technology kills the magic.
  Magic drives humans mad.
  Humans destroy nature.
  Technology is superior to humans and nature. But be careful. Don't get addicted.
  Once harm is done to nature, it takes revenge on humans and technology.
  Unless the meteor destroys the world before you do. Sorry, not you, the computer. "You must win the battle by winning 3 rounds and prevent the computer from using the meteor.""")
  while True:
    is_understood = input("Is it clear, hero? yes or no?").strip().lower()
    if is_understood == "yes":
      print("Lets begin!")
      break
    elif is_understood == "no":
      print("""If you can't get it, then let me explain it this way.
      Magic <=> Nature
      Magic > Human
      Technology > Magic
      Technology > Human
      Technology> Nature
      Human > Nature
      You may defeat nature the first time, but once you defeat it, it will take its revenge on you. Ups, not you. Technology and human.
      And don't forget. Meteor > Everything
      """)
      break
    else:
      print("Please try writing in lower case and just answer my question!")

  while hero_score < 3 or computer_score < 3:
    round_number +=1
    print(f"~~~Round {round_number} begins!~~~")
    hero_choice = input("Please write your action, hero. Magic, human, nature, technology or meteor?").strip().lower()
    is_hero_crazy = False
    while True:
      if hero_choice in action_list:
        break
      elif hero_choice == "meteor":
        print("Congratulations, you've defeated the computer. You've destroyed your world! And yourself! Can you call that a victory?")
        print("I don't want to play with you anymore..!")
        is_hero_crazy=True
        break
      else:
        print("Please try writing in lower case and don't write anything random that comes to your mind!")
        hero_choice = input("Please write your action, hero. Magic, human, nature, technology or meteor?")

    if is_hero_crazy == True:
      break

    print(f"The hero chose {hero_choice}")

    computer_choice = random.choice(action_list)
    print(f"The computer chose {computer_choice}")

    if hero_choice == computer_choice:
      print(f"Okay, you both chose the same thing. So nothing happened. Great!")
      hero_score += 1
      computer_score += 1
      print_score(hero_score, computer_score)

    elif hero_choice == "magic":
      if computer_choice == "nature":
        print("They are in harmony.")
        hero_score += 1
        computer_score += 1
        print_score(hero_score, computer_score)
      elif computer_choice == "human":
        print("Magic may be for dragons, but it's definitely not for humans.")
        hero_score += 1
        print_score(hero_score, computer_score)
      elif computer_choice == "technology":
        print("Let's be honest. The magic of the real world is technology.")
        computer_score += 1
        print_score(hero_score, computer_score)

    elif hero_choice == "human":
      if computer_choice == "technology":
        print("Are machines better than humans? At least they don't kill each other.")
        computer_score += 1
        print_score(hero_score, computer_score)
      elif computer_choice == "magic":
        print("Magic may be for dragons, but it's definitely not for humans.")
        computer_score += 1
        print_score(hero_score, computer_score)
      elif computer_choice == "nature":
        if is_nature_destroyed == False:
          print("Human against nature. Human has won. For now...")
          hero_score += 1
          is_nature_destroyed = True
          print_score(hero_score, computer_score)
        else:
          print("Of course, there would be consequences for what was done. Nature took its revenge.")
          computer_score += 1
          print_score(hero_score, computer_score)

    elif hero_choice == "technology":
      tech_count += 1
      if tech_count > 1:
        print("Are you addicted? Let's find a solution to this.")
        hero_score -= 1
        tech_count = 0
        print_score(hero_score, computer_score)
      else:
        if computer_choice == "human":
          print("Are machines better than humans? At least they don't kill each other.")
          hero_score += 1
          print_score(hero_score, computer_score)
        elif computer_choice == "magic":
          print("Let's be honest. The magic of the real world is technology.")
          hero_score += 1
          print_score(hero_score, computer_score)
        elif computer_choice == "nature":
          if is_nature_destroyed == False:
            print("Technology was inspired by nature. Now it has surpassed it. Next time, there might be no future.")
            hero_score += 1
            is_nature_destroyed = True
            print_score(hero_score, computer_score)
          elif is_nature_destroyed == True:
            print("Of course, there would be consequences for what was done. Nature took its revenge.")
            computer_score += 1
            print_score(hero_score, computer_score)

    elif hero_choice == "nature":
      if computer_choice == "magic":
        print("They are in harmony.")
        hero_score += 1
        computer_score += 1
        print_score(hero_score, computer_score)
      elif computer_choice == "human":
        if is_nature_destroyed == False:
          print("Human against nature. Human has won. For now...")
          computer_score += 1
          is_nature_destroyed = True
          print_score(hero_score, computer_score)
        elif is_nature_destroyed == True:
          print("Of course, there would be consequences for what was done. Nature took its revenge.")
          hero_score += 1
          print_score(hero_score, computer_score)
      elif computer_choice == "technology":
        if is_nature_destroyed == False:
          print("Technology was inspired by nature. Now it has surpassed it. Next time, there might be no future.")
          computer_score += 1
          is_nature_destroyed = True
          print_score(hero_score, computer_score)
        elif is_nature_destroyed == True:
          print("Of course, there would be consequences for what was done. Nature took its revenge.")
          hero_score += 1
          print_score(hero_score, computer_score)

    if hero_score == 3:
      answer = input("Congratulations, you won! Do you want to play again? Yes or no?").strip().lower()
      if answer == "yes":
        hero_score = 0
        computer_score = 0
        is_nature_destroyed = False
        round_number = 0
        continue
      else:
        print("Brave hero, we will call on you again when we need you. Until then, farewell.")
        break
    elif computer_score == 3:
      hero_choice = input("Please write your action, hero. Magic, human, nature, technology or meteor?")
      print("Haha! It doesn't matter anyway.")
      print("The computer chose meteor and destroy everything!!!!!!!!")
      print("You lost, we lost everything!!! But... There is an another chance. If you want, you can rewind the time and try again. Yes or no?")
      answer = input().strip().lower()
      if answer == "yes":
        c_choice = random.choice(yes_or_no)
        if c_choice == "yes":
          hero_score = 0
          computer_score = 0
          is_nature_destroyed = False
          round_number = 0
        else:
          print("But i don't want to.")
      else:
        print("Run away like a coward!")
        break
    
rock_paper_scissors_ALEYNA_BERGAMA()