// Copyright (c) 2019-present, Facebook, Inc.
// All rights reserved.
//
// This source code is licensed under the license found in the
// LICENSE file in the root directory of this source tree.
//

import java.util. *;
import java.util.stream.*;
import java.lang.*;

public class CHECK_IF_X_CAN_GIVE_CHANGE_TO_EVERY_PERSON_IN_THE_QUEUE{
static int f_gold ( int notes [ ] , int n ) {
  int fiveCount = 0 ;
  int tenCount = 0 ;
  for ( int i = 0 ;
  i < n ;
  i ++ ) {
    if ( notes [ i ] == 5 ) fiveCount ++ ;
    else if ( notes [ i ] == 10 ) {
      if ( fiveCount > 0 ) {
        fiveCount -- ;
        tenCount ++ ;
      }
      else return 0 ;
    }
    else {
      if ( fiveCount > 0 && tenCount > 0 ) {
        fiveCount -- ;
        tenCount -- ;
      }
      else if ( fiveCount >= 3 ) {
        fiveCount -= 3 ;
      }
      else return 0 ;
    }
  }
  return 1 ;
}


static boolean f_filled ( int[] notes, int n ) {
        int fiveCount = 0, tenCount = 0;
        for ( int i = 0; i < n; i++ ) {
            if ( notes[i] == 5 ) fiveCount++;
            else if ( notes[i] == 10 ) {
                if ( fiveCount > 0 ) {
                    fiveCount--;
                    tenCount++;
                } else return false;
            } else {
                if ( fiveCount > 0 && tenCount > 0 ) {
                    fiveCount--;
                    tenCount--;
                } else if ( fiveCount >= 3 ) fiveCount -= 3;
                else return false;
            }
        }
        return true;
    }

public static void main(String args[]) {
    int n_success = 0;
    List<int [ ]> param0 = new ArrayList<>();
    param0.add(new int[]{5, 5, 5, 10, 20});
    param0.add(new int[]{5,5,5,20,10});
    param0.add(new int[]{5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,10,10,10,10,10,10,10,10,10,10,10,10});
    param0.add(new int[]{10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,18});
    param0.add(new int[]{5,5,20});
    param0.add(new int[]{10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5});
    param0.add(new int[]{5,10,20,5,5,5,5,5,5,5,5,5,5,5,5});
    param0.add(new int[]{-82,-10,-78,-84,68,62,10,20,-86,-98,92,70,40,-12,-20,-36,8,-70,6,8,44,-24,8,-18,76,-54,-14,-94,-68,-62,-24,-36,-74,92,92,-80,48,56,94});
    param0.add(new int[]{10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5});
    param0.add(new int[]{46,46,93,57,82,34,83,80,77,36,80,85,69,28,9,56,49,27,83,25,1,80,99,14,69,82,79,71,74,34});
    List<Integer> param1 = new ArrayList<>();
    param1.add(4);
    param1.add(5);
    param1.add(27);
    param1.add(12);
    param1.add(2);
    param1.add(17);
    param1.add(7);
    param1.add(31);
    param1.add(25);
    param1.add(20);
    for(int i = 0; i < param0.size(); ++i)
    {
        if(f_filled(param0.get(i),param1.get(i)) == f_gold(param0.get(i),param1.get(i)))
        {
            n_success+=1;
        }
    }
    System.out.println("#Results:" + n_success + ", " + param0.size());
}
}