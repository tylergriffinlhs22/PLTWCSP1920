####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'CHLnGR'# Only 10 chars displayed
strategy_name = 'BETRAYAL V0.0.1'
strategy_description = '''first beta build of the betrayal engine'''
    
def move(my_history, their_history, my_score, their_score):
    '''doesnt do anything unless the enemy has betrayed'''
    if not(my_history): #its round 1, dont 
        return 'c'
    elif 'b' in their_history:
        return 'b' # finish them
    else:
        return 'c' # they havent betrayed yet