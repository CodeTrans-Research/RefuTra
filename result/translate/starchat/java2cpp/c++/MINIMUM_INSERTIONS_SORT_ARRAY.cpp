int f_gold ( vector<int> arr ) {
    	vector<int> lis ( arr.size(), 1 );
    	for ( int i = 0; i < arr.size(); i++ ) {
    		for ( int j = 0; j < i; j++ ) {
    			if ( arr[i] >= arr[j] && lis[i] < lis[j] + 1 ) {
    				lis[i] = lis[j] + 1;
    			}
    		}
    	}
    	int max = 0;
    	for ( int i = 0; i < arr.size(); i++ ) {
    		if ( max < lis[i] ) {
    			max = lis[i];
    		}
    	}
    	return arr.size() - max;
    }