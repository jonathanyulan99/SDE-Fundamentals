function solution(node) {
    var results = [];

    function findLeaves(root) {

        if (root == null) {
            return 0;
        }

        let leftHeight = findLeaves(root.left);

        let rightHeight = findLeaves(root.right);

        let maxHeight = Math.max(leftHeight, rightHeight) + 1
        if (results.length < maxHeight) {
            results.push([]);
        }

        results[maxHeight - 1].push(root.value)
        return maxHeight
    }
    findLeaves(node)
    return results;
}