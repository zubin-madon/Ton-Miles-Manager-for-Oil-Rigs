def calculate_boyed_weight(l, ppf, bf):
    if l<0 or ppf<0:
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


def calculate_trip_miles(dc1_trip_length, dc2_trip_length, hwdp_trip_length, bha_wt, dp1_trip_length, dp2_trip_length,
                         dp2_trip_bw, dp1_trip_bw, total_depth, block_weight):
    bha_miles_a = (dc1_trip_length + dc2_trip_length + hwdp_trip_length) / 5280
    bha_ton_miles_a = (bha_wt / 2) * bha_miles_a
    bha_miles_b = (dp1_trip_length + dp2_trip_length) / 5280

    bha_ton_miles_b = bha_wt * bha_miles_b
    dp2_miles = dp2_trip_length / 5280
    dp2_ton_miles = (dp2_trip_bw / 2) * dp2_miles
    dp1_miles_a = dp1_trip_length / 5280
    dp1_ton_miles_a = (dp1_trip_bw / 2) * dp1_miles_a
    dp1_ton_miles_b = dp1_trip_bw * dp2_miles
    total_tripping_miles = float(
        block_ton_miles(total_depth, block_weight)) + bha_ton_miles_a + bha_ton_miles_b + dp1_ton_miles_a + dp1_ton_miles_b + dp2_ton_miles
    return total_tripping_miles


def calculate_casing_miles(lower_csg_length, mid_csg_length, top_csg_length, lower_csg_bw, mid_csg_bw,
                           top_csg_bw, total_depth, block_weight):
    lower_csg_miles = lower_csg_length / 5280
    mid_csg_miles = mid_csg_length / 5280
    top_csg_miles = top_csg_length / 5280
    lower_tm = (lower_csg_bw / 2) * lower_csg_miles
    mid_tm = (mid_csg_bw / 2) * mid_csg_miles
    top_tm = (top_csg_bw / 2) * top_csg_miles
    mid_on_top_tm = top_csg_miles * mid_csg_bw
    lower_on_midtop_tm = ((mid_csg_length + top_csg_length) / 5280) * lower_csg_bw
    total_casing_miles = lower_tm + mid_tm + top_tm + mid_on_top_tm + lower_on_midtop_tm + float(block_ton_miles(total_depth, block_weight))
    return total_casing_miles


def liner_miles(dp_length, dp_bw, liner_length, liner_bw, total_depth, block_weight):
    dp_miles = dp_length / 5280
    dp_tonmiles = dp_miles * (dp_bw / 2)
    liner_miles = liner_length / 5280
    liner_tonmiles = liner_miles * liner_bw / 2
    liner_tm_on_dp = dp_miles * liner_bw
    if dp_length > 0:
        block_miles_two = block_weight * dp_miles
        dp_pooh_tonmiles = dp_miles * dp_bw / 2
        total_liner_ton_miles = float(block_ton_miles(total_depth, block_weight)) + block_miles_two + dp_pooh_tonmiles + dp_tonmiles \
                                + liner_tonmiles + liner_tm_on_dp
    else:
        total_liner_ton_miles = float(block_ton_miles(total_depth, block_weight)) + float(liner_tonmiles)

    return total_liner_ton_miles


def jarring_miles(dist_trav, weight_tons, strokes_per_hr, hrs_jarring):
    if dist_trav<0 or strokes_per_hr<0 or hrs_jarring<0:
        return 0
    else:
        distance_miles = dist_trav / 5280
        ton_miles_per_strk = distance_miles * weight_tons
        ton_miles_per_hour = ton_miles_per_strk * strokes_per_hr
        total_jarring_miles = ton_miles_per_hour * hrs_jarring

        return total_jarring_miles
