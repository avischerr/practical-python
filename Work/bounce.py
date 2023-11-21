initial_height = 100
current_height = 100
bouncing = 3/5
bounce_ctr = 1

while bounce_ctr <= 10:
    current_height = round(current_height * bouncing, ndigits=4)
    print(current_height)
    bounce_ctr += 1