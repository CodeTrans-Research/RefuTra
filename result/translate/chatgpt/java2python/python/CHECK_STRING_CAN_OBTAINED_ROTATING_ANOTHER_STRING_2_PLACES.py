def f_gold(str1, str2):
    if len(str1) != len(str2):
        return False
    clock_rot = ""
    anticlock_rot = ""
    len_str2 = len(str2)
    anticlock_rot = anticlock_rot + str2[len_str2 - 2:] + str2[:len_str2 - 2]
    clock_rot = clock_rot + str2[2:] + str2[:2]
    return str1 == clock_rot or str1 == anticlock_rot