// https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1

class Solution {
  matSearch(matrix, N, M, X) {
    let height = 0;
    let width = M - 1;

    while (height <= N - 1 && width >= 0) {
      if (matrix[height][width] == X) return 1;
      if (matrix[height][width] > X) width--;
      if (matrix[height][width] < X) height++;
    }
    return 0;
  }
}
