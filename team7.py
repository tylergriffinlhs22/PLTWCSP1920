####
# BETRAYAL ENGINE V0
####

team_name = 'CHLnGR'# Only 10 chars displayed
strategy_name = 'BETRAYAL V1.0.0'
strategy_description = '''first release of the betrayal engine'''
    
def move(my_history, their_history, my_score, their_score):
    '''doesnt do anything unless the enemy has betrayed or the enemy is winning, its a jealous engine'''
    if not(my_history): #its round 1, dont 
        return 'c'
    elif 'b' in their_history or my_score <= their_score:
        return 'b' # finish them
    else:
        return 'c' # they havent betrayed yet
        