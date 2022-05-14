class BTEr: 
    def __init__(self, age: int, sex, ethnicity, location, education_level, education_interest, computer_status, mc_edition, 
    join_period, learn_type, in_main:bool, in_bt:bool, staff_status, sm_interest, sm_use): 
        self.age = age
        self.sex = sex 
        self.ethnicity = ethnicity
        self.location = location 
        self.education_level = education_level # level is current education level. Using current because most of bte's community has not graduated
        self.education_interest = education_interest # interest is the current, completed or envisioned major
        self.computer_status = computer_status 
        self.mc_edition = mc_edition
        self.join_period = join_period
        self.learn_type = learn_type
        self.in_main = in_main
        self.in_bt  = in_bt 
        self.staff_status = staff_status
        self.sm_interest = sm_interest # sm stands for "social media"
        self.sm_use = sm_use 

class Staff(BTEr): 
    def __init__(self, age: int, sex, ethnicity, location, education_level, education_interest, computer_status, mc_edition, 
    join_period, learn_type, in_main:bool, in_bt:bool, staff_status, sm_interest, sm_use, 
    is_main_staff:bool, build_status, enjoy_building, enjoy_staff, why_staff): 
        super().__init__(age, sex, ethnicity, location, education_level, education_interest, computer_status, mc_edition, join_period,
        learn_type, in_main, in_bt, staff_status, sm_interest, sm_use) 
        self.is_main_staff = is_main_staff
        self.build_status = build_status
        self.enjoy_building = enjoy_building 
        self.enjoy_staff = enjoy_staff
        self.why_staff = why_staff 
        
class No_MC(BTEr): 
    def __init__(self, age: int, sex, ethnicity, location, education_level, education_interest, computer_status, mc_edition, 
    join_period, learn_type, in_main:bool, in_bt:bool, staff_status, sm_interest, sm_use, why_no_mc, participate_in_future):
        super().__init__(age, sex, ethnicity, location, education_level, education_interest, computer_status, mc_edition, join_period,
        learn_type, in_main, in_bt, staff_status, sm_interest, sm_use)
        self.why_no_mc = why_no_mc
        self.participate_in_future = participate_in_future 