/*
Time Complexity = O(N) **calculating all the angles of our summits 
Space Complexity = O(1) Compute Space in constant time and just look at slopes ** 

Pseudocode:
Second iteration from the origin/start to our peak/highest angle
angle = rise/run
rise = array[i]
run = i 
initialize max as -Inf or 0 

Steps:
1) Start with max (y) at 0 and also maxPosition at 0 (x) and update max and maxPosition only if max is higher 
    a) if maxPosition is zero then we are at the summit and return true
2) Calculate slope/rise over run to summit (rise over run = )
3) Iterate from origin to summit
      i) calculate the line of sight y at that x and if y is < to the height then your view is obscured to the summit (return false)
4) return true
*/

function canSeeTrueSummit(elevations) {
    let maxPosition = 0;

    for (let i = 0; i < elevations.length; i++) {
        if (elevations[i] > elevations[maxPosition]) {
            maxPosition = elevations[i];
        }
    }

    const slopeToSummit = elevations[maxPosition] / maxPosition;
    for (let i = 1; i < maxPosition; i++) {
        if (elevations[i] / i > slopeToSummit) {
            return false;
        }
    }
    return true;
}

console.log(canSeeTrueSummit([0, 1, 2, 3, 4, 5]), true);
console.log(canSeeTrueSummit([0, 2, 3]), false);
console.log(canSeeTrueSummit([0, 1, 1, 2, 3, 4, 5, 4, 3, 3, 9, 9, 9, 8, 7, 7]), false);
console.log(canSeeTrueSummit([0, 1, 1, 2, 3, 4, 5, 4, 3, 3, 11, 10, 9, 8, 7, 7]), false);
console.log(canSeeTrueSummit([0, -1, -2, -3]), true);