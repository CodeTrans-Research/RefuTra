def f_gold(stack1, stack2, stack3, n1, n2, n3):
        sum1 = sum(stack1[:n1])
        sum2 = sum(stack2[:n2])
        sum3 = sum(stack3[:n3])
        top1, top2, top3 = 0, 0, 0
        ans = 0
        while True:
            if top1 == n1 or top2 == n2 or top3 == n3:
                return 0
            if sum1 == sum2 and sum2 == sum3:
                return sum1
            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= stack1[top1]
                top1 += 1
            elif sum2 >= sum3 and sum2 >= sum1:
                sum2 -= stack2[top2]
                top2 += 1
            else:
                sum3 -= stack3[top3]
                top3 += 1