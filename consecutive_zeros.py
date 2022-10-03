def consecutive_zeros(binary):
    highest_streak = 0
    current_streak = 0
    for char in binary:
        if char == "0":
            current_streak += 1
        else:
            if highest_streak < current_streak:
                highest_streak = current_streak
            current_streak = 0
    return highest_streak
    

print(consecutive_zeros("1001101000110"))    
