import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


final_set = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
split1_set = set([11,12,14,15,16])
split2_set = set([17,18,19,20,21])
player_dict = {1:"Mike",2:"Tony",3:"Ryan",4:"Anish",5:"Damion",6:"Sheel",7:"Carlos",
               8:"Adam",9:"Dominic",10:"Nick",11:"Bill",12:"Denzil",13:"Todd G",14:"Ahmed",
               15:"Karthik",16:"Brian",17:"Sean",18:"Steve",19:"Jaime",20:"Rob",
               21:"Jason"} #player list
vals = list(player_dict.values())
keys =  list(player_dict.keys())

player_count = 21 #change this to edit number of players

def get_players(player_list, week):
  #Gets two random different players
  check0 = 0
  while check0 == 0:
    player1 = random.randint(1,player_count)
    if player1 in player_list or ((week == True and player1 in split2_set) or (week == False and player1 in split1_set)):
      pass 
    else:
      check0 = 1
      player_list.append(player1)

  check1 = 0
  while check1 == 0:
    player2 = random.randint(1,player_count)
    if player2 in player_list or ((week == True and player2 in split2_set) or (week == False and player2 in split1_set)):
      pass
    else:
      check1 = 1
      player_list.append(player2)
    
  return player1, player2


def assign_pairs(week, pair_list):
  pair_list_backup = pair_list[:] #backup for master pair list before this week's pairs are added
  week_pair_list = [] #pairs that have been matched this week
  player_list = [] #players that have been paired this week
  temp_pair = ''
  if week == True:
    count = 8 #Edit this to change the number of matches in a week, for split1 and split2
  else:
    count = 8

  counter = 0
  while counter != count:
    check2 = 0
    while check2 == 0:
      player1, player2 = get_players(player_list, week)
      pair = set([player1,player2])
      
      if pair in pair_list:
        player_list.remove(player1)
        player_list.remove(player2)
        
        if temp_pair == pair: #infinite loop checker, resets everything
          week_pair_list = []
          player_list = []
          temp_pair = ''
          counter = 0
          pair_list = pair_list_backup[:] #using backup
          continue

        temp_pair = pair
        continue

      else:
        check2 = 1
        pair_list.append(pair)
        week_pair_list.append(pair)

      counter += 1
  
  return week_pair_list, pair_list


def print_week(week_pair_list, week_number):
  print(f'Week {week_number}')
  for x, pair in enumerate(week_pair_list):
    temp_list = list(week_pair_list[x])
    print(f'{player_dict[temp_list[0]]} and {player_dict[temp_list[1]]}')
  print()



""" def read_pre_data(pair_list,vals,keys):
    tennis_singles = pd.read_csv('3.75 Singles Winter 2023.csv',skiprows=3) #importing information
    games_played = tennis_singles.iloc[0:16,2:26] #cutting down to useful info, edit this if table format is changed

    col_len = (len(games_played.iloc[0:,0]))
    row_len = (len(games_played.iloc[0,0:]))
    games_played_list = []
    
    for col in range(col_len): #creating a list of all the names
        for row in range(row_len):
            item = (games_played.iloc[col,row])
            if item == 'nan' or type(item) == float:
                continue
            games_played_list.append(item)
    games_played_list.append('')

    for x, person in enumerate(games_played_list):
        if person == 'vs.':
            if games_played_list[x+1].title().strip() in vals and games_played_list[x-1].title().strip() in vals:
                player2 = (keys[vals.index(games_played_list[x+1].title().strip())])
                player1 = (keys[vals.index(games_played_list[x-1].title().strip())])
                pair_list.append({player1,player2})
                
    return pair_list
             """


def main():
  week = True #week = true is split 1, false is split 2
  pair_list = [] #edit this to add existing pairs {#,#}
  #pair_list = read_pre_data(pair_list,vals,keys)

  week_number = 1
  for x in range(8): #Number of Weeks
    week_pair_list,pair_list = assign_pairs(week, pair_list)
    print_week(week_pair_list, week_number)
    week_number += 1

    if week == True:
      week = False
    else:
      week = True
  


main()


