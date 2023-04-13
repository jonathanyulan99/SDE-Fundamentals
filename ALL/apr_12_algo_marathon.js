const findPaths = (matrix, x = 0, y = 0) => { // returns number
    if (x < 0 || y < 0 || x >= matrix.length || y >= matrix[0].length) {
        return 0;
    }
    if (x === 0 && y === matrix[0].length - 1) {
        return 1;
    }

    return findPaths(matrix, x + 1, y + 1) + findPaths(matrix, x, y + 1) + findPaths(matrix, x - 1, y + 1);
}

// N * M
const findPathsMemoized = (matrix) => {
    const memo = {};

    const helper = (x = 0, y = 0) => { // returns number
        if (memo[`${x}-${y}`]) {
            return memo[`${x}-${y}`];
        }

        if (x < 0 || y < 0 || x >= matrix.length || y >= matrix[0].length) {
            return 0;
        }
        if (x === 0 && y === matrix[0].length - 1) {
            return 1;
        }

        const result = helper(x + 1, y + 1) + helper(x, y + 1) + helper(x - 1, y + 1);
        memo[`${x}-${y}`] = result;
        return result;
    }

    return helper(0, 0)
}

const testMatrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

console.log(findPathsMemoized(testMatrix))