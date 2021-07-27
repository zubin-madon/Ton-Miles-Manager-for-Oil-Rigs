import functions

def test_calculate_boyed_weight_():
    assert functions.calculate_boyed_weight(2000, 29, 0.75) == 43500/2000
    assert functions.calculate_boyed_weight(0, 29, 0.75) == 0
    assert functions.calculate_boyed_weight(-2000, 29, 0.75) == 0



def test_total_weight_():
    assert functions.cal_total_wt(2000,4000,6000,8000) == 20000



def test_block_ton_miles_():
    assert functions.block_ton_miles(3000, 20) == 22.72727272727273
    assert functions.block_ton_miles(0, 20) == 0
    assert functions.block_ton_miles(2000, 0) == 0
    assert functions.block_ton_miles(0, -20) == 0
    assert functions.block_ton_miles(-2000, 0) == 0



def test_calculate_drill_miles_():
    assert functions.calculate_drill_miles(total_depth=3000, block_weight=20, str_wt=150, ream=2)==494.31818181818187
    assert functions.calculate_drill_miles(total_depth=3000, block_weight=20, str_wt=150, ream=0)==107.95454545454547



def test_liner_miles_():
    assert functions.liner_miles(dp_length=3000, dp_bw=20, liner_length=1000, liner_bw=70, total_depth=4000, block_weight=20)==99.43181818181819



def test_jarring_miles_():
    assert functions.jarring_miles(dist_trav=30, weight_tons=120, strokes_per_hr=45, hrs_jarring=3)==92.04545454545455
    assert functions.jarring_miles(dist_trav=-20, weight_tons=120, strokes_per_hr=45, hrs_jarring=3)==0
    assert functions.jarring_miles(dist_trav=30, weight_tons=120, strokes_per_hr=-40, hrs_jarring=3) ==0
    assert functions.jarring_miles(dist_trav=30, weight_tons=120, strokes_per_hr=65, hrs_jarring=-3) ==0
