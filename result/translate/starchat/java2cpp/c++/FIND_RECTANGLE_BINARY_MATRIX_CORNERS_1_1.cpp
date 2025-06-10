bool f_gold ( int matrix [ ] [ ] ) {
    int rows = matrix.length;
    if (rows == 0) return false;
    int columns = matrix[0].length;
    vector<vector<int>> visited(rows, vector<int>(columns, 0));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns - 1; j++) {
            if (matrix[i][j] == 1 && matrix[i][j + 1] == 1) {
                if (visited[i][j] == 1 || visited[i][j + 1] == 1) return true;
                visited[i][j] = 1;
                visited[i][j + 1] = 1;
                if (j > 0 && visited[i][j - 1] == 1) return true;
                if (j < columns - 2 && visited[i][j + 2] == 1) return true;
            }
        }
    }
    return false;
}