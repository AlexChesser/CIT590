def main():
    return

def is_game_over(computer_score, human_score):
    if(computer_score == human_score):
        return False
    elif(computer_score >= 100 or human_score >= 100):
        return True
    else:
        return False

if __name__ == '__main__':
    main()