def f_gold(XY, n, Xmin, Ymin, Xmax, Ymax):
        print("Point inside the viewing pane:")
        for i in range(n):
            if (XY[i][0] >= Xmin and XY[i][0] <= Xmax) and (XY[i][1] >= Ymin and XY[i][1] <= Ymax):
                print("[" + str(XY[i][0]) + ", " + str(XY[i][1]) + "] ")
        print("\nPoint outside the viewing pane:")
        for i in range(n):
            if (XY[i][0] < Xmin or XY[i][0] > Xmax) or (XY[i][1] < Ymin or XY[i][1] > Ymax):
                print("[" + str(XY[i][0]) + ", " + str(XY[i][1]) + "] ")