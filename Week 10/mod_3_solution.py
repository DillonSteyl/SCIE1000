def travel(current_month, num_months):
    month = (current_month + num_months)%12
    if 2<=month<5:
        return(1)
    elif 5<=month<8:
        return(2)
    elif 8<=month<11:
        return(3)
    else:
        return(0)
