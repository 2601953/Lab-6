def movie_ticket_price(children, adults, seniors, time):
    a_total = adults * 15
    c_total = children * 5
    s_total = seniors * 12

    # Assuming only one discount 
    if(adults >= 2 and seniors == 1):
        c_total = max(0, c_total - (5 * 2))
        s_total = max(0, s_total - (12 * 0.5))
    
    if(adults >= 2):
        c_total = max(0, c_total - (5 * 2))

    if(seniors >= 1):
        c_total = max(0, c_total - 5)

    total = a_total + c_total + s_total

    if(time < 15):
        total *= 0.95

    if(total >= 0): 
        return total
    else: # Wont ever be < 0 but just in case
        return None

