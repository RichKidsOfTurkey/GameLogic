# GameLogic
# Table of Contens
* [General info](#general-info)
* [Technologies](#technologies)
* [Ground Rules and General Notes](#Ground-Rules-and-General-Notes)
* [Classes](#Classes)
* [Setup](#setup)
    

###Ground Rules and General Notes
* stats:
     1. score
     2. rebound
     3. block
     4. steal
     5. assist
  * stat distributions:

      1. score
    
        1.5 to 29.7
        common:     1.50 to 8.55 
        uncommon:   8.55 to 15.60 
        rare:       15.60 to 22.65  
        legendary:  22.65 to 29.70   
      2. rebound:
    
        0.0 to 15.1
        common:     0.00 to 3.78
        uncommon:   3.78 to 7.55
        rare:       7.55 to 11.33
        legendary:  11.33 to 15.10
      3. block:

        0.0 to 2.8
        common:     0.00 to 0.65
        uncommon:   0.70 to 1.40
        rare:       1.40 to 2.10
        legendary:  2.10 to 2.80
      4. steal:
    
        0.2 to 2.0
        common:     0.00 to 0.65
        uncommon:   0.65 to 1.10
        rare:       1.10 to 1.55
        legendary:  1.55 to 2.00
      5. assist:
  
        0.3 to 10.0
        common:     0.30 to 2.73
        uncommon:   2.73 to 5.15
        rare:       5.15 to 7.58
        legendary:  7.58 to 10.00

* teams contains 3 player
* 1000 packs (one pack contains 4 players)
* 4000 players (400 - 800 - 1200 - 1600)

###Classes:

gen_player
* It contains generate_player() function you can give how many players and in 
what rarity you want to generate ,and it will return player array 
* player array looks like this:
 

        {'overall rarity': [2.6, 'legendary'], 
            'player name': 'Patrick', 
            'score': 23.34, 
            'rebound': 13.4, 
            'block': 1.58, 
            'steal': 1.4, 
            'assist': 8.91, 
            'player_index': 3602
            },........

