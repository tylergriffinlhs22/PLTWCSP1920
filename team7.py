####
# BETRAYAL ENGINE V0
####

team_name = 'CHLnGR'# Only 10 chars displayed
strategy_name = 'BETRAYAL V1.0.1'
strategy_description = '''second release of the betrayal engine'''
    
def move(my_history, their_history, my_score, their_score):
    '''doesnt do anything unless the enemy has betrayed, nothin works better tbh'''
    if not(my_history): #its round 1, dont 
        return 'c'
    elif 'b' in their_history:
        return 'b' # finish them
    else:
        return 'c' # they havent betrayed yet
        