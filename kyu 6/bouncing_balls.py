def bouncing_ball(h, bounce, window):
    # your code
    if h > 0 and 0 < bounce < 1 and window < h:
        number_of_bounce = 0
        while h > window:
            number_of_bounce += 1
            h *= bounce
            if h>window:
                number_of_bounce += 1
            print(h)
        return number_of_bounce
    return -1