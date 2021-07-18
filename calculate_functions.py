def calculate_boyed_weight(l, ppf, bf):
    if l < 0 or ppf < 0:
        return 0
    else:
        return (l * ppf * bf) / 2000


def cal_total_wt(*args):
    total_wt = 0
    for arg in args:
        total_wt += arg
    return total_wt

def block_ton_miles(total_depth, block_weight):
    if total_depth<0 or block_weight<0:
        return 0
    else:
        miles_block = total_depth * 2 / 5280
        tons_miles_block = block_weight * miles_block
        return tons_miles_block

# ------Function to Calculate Drilling Miles. It is called inside dill_miles_data() in Computation class.----------
def calculate_drill_miles(total_depth, block_weight, str_wt, ream):
    def string_miles():
        miles_string = total_depth / 5280
        ton_miles_string = str_wt * miles_string
        return ton_miles_string

    def string_miles_ream():
        miles_string_ream = total_depth * 2 / 5280
        ton_miles_string_ream = (str_wt + block_weight) * miles_string_ream
        return ton_miles_string_ream

    total_drilling_miles = float(block_ton_miles(total_depth, block_weight)) + float(string_miles()) + (
            (string_miles_ream()) * ream)
    return total_drilling_miles
