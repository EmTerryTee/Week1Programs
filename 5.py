MAX_LAB_CAP = 24
group_1, group_2, group_3, group_1_stu, group_2_stu, group_3_stu = "One", "Two", "Three", 113, 175, 12


def comp_lab_group_calc(group, group_total):
    num_of_groups = group_total // MAX_LAB_CAP
    remaining_students = group_total % MAX_LAB_CAP
    if num_of_groups == 0:
        print(f'Group {group} does not need to be split, {remaining_students} students do not exceed lab capacity.')
    elif remaining_students == 0:
        print(f'Group {group} can be split into {num_of_groups} with no remaining students.')
    else:
        print(f'Group {group} must be split into {num_of_groups}, with {remaining_students} '
              f'students occupying the smallest group.')


comp_lab_group_calc(group_1, group_1_stu)
comp_lab_group_calc(group_2, group_2_stu)
comp_lab_group_calc(group_3, group_3_stu)
comp_lab_group_calc("Four", 144)