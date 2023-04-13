function queensAttacktheKing(queens, king) {
    // a bunch of helper functions:
    const positiveSlope = (x, y) => x - y;
    const negativeSlope = (x, y) => x + y;
    const distance = (p1, p2) => Math.sqrt(Math.pow(p2[0] - p1[0], 2) + Math.pow(p2[1] - p1[1], 2));
    const direction = (q, k) => {
        if (q === k) return "=";
        return q > k ? "+" : "-";
    };

    // On what rows, columns and diagonals is the king?
    const [kx, ky] = king;
    const kp = positiveSlope(kx, ky);
    const kn = negativeSlope(kx, ky);

    // Select only queens on the same horizontal, vertical and diagonals
    queens = queens.filter(
        (q) => {
            const [qx, qy] = q;
            const qp = positiveSlope(qx, qy);
            const qn = negativeSlope(qx, qy);
            return qx === kx || qy === ky || qp === kp || qn === kn;
        }
    );

    // Add a label for each to group them by direction on that axis and
    // find the distance to the king.
    queens = queens.map(
        (q) => {
            const [qx, qy] = q;
            const qp = positiveSlope(qx, qy);
            const qn = negativeSlope(qx, qy);
            const label = `${direction(qx, kx)}${direction(qy, ky)}`;
            return { queen: q, label: label, distance: distance(q, king) };
        }
    );

    // Now find the closest queen in each direction on each axis.
    const best = {};
    for (const qd of queens) {
        if (!best[qd.label]) {
            best[qd.label] = qd;
        } else if (qd.distance < best[qd.label].distance) {
            best[qd.label] = qd;
        }
    }

    // The best map is grouped by the direction labels, now pull
    // out just the queens to return.
    return Object.entries(best).map((entry) => entry[1].queen);
}