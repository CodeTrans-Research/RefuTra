def f_gold(str1, str2):
        if len(str1)!= len(str2):
            return False
        clock_rot = ""
        anticlock_rot = ""
        len = len(str2)
        anticlock_rot = anticlock_rot + str2[len-2:] + str2[:len-2]
        clock_rot = clock_rot + str2[2:] + str2[:2]
        return str1 in [clock_rot, anticlock_rot]