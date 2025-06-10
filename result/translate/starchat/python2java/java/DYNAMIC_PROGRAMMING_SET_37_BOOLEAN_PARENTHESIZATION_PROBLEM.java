public static int f_gold(char[] symb, char[] oper, int n){

        int[][] F = new int[n+1][n+1]; 
        int[][] T = new int[n+1][n+1]; 

        for(int i = 0; i < n; ++i){ 
            if (symb[i] == 'T') 
                T[i][i] = 1; 
            else 
                F[i][i] = 1; 
        } 
  
        for(int gap = 1; gap < n; ++gap ){ 
            for(int i = 0; i < n-gap; ++i ){ 
                int j = i + gap; 
                T[i][j] = F[i][j] = 0; 

                for(int g = 0; g<gap; ++g){ 
                    int k = i + g; 
                    int tik = T[i][k] + F[i][k]; 
                    int tkj = T[k+1][j] + F[k+1][j]; 
                    switch(oper[k]) {
                        case '|': 
                            F[i][j] += F[i][k]*F[k+1][j] + T[i][k]*T[k+1][j];
                            break; 
                        case '&':  
                            T[i][j] += T[i][k]*T[k+1][j]; 
                            F[i][j] += ((tik*tkj)-(T[i][k]*T[k+1][j])); 
                            break; 
                        case '^': 
                            T[i][j] += F[i][k]*T[k+1][j]+T[i][k]*F[k+1][j];
                            F[i][j] += F[i][k]*F[k+1][j]+T[i][k]*T[k+1][j];
                            break; 
                    } 
                } 
            } 
        } 
        return T[0][n-1]; 
    }