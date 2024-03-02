function calculateDistance(coord1, coord2) {
    const { lat: lat1, lng: lon1 } = coord1;
    const { lat: lat2, lng: lon2 } = coord2;

    const R = 6371; // Radius of the Earth in kilometers

    const dLat = (lat2 - lat1) * Math.PI / 180;  // Convert degrees to radians
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a =
        Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distance = R * c; // Distance in kilometers

    return distance;
}

function findMaxRadius(cluster, center) {
    let maxRadius = 0;
    let maxRadiusCoord = null;

    for (const coord of cluster) {
        const distance = calculateDistance(coord, center);
        if (distance > maxRadius) {
            maxRadius = distance;
            maxRadiusCoord = coord;
        }
    }

    return { maxRadius, maxRadiusCoord };
}

function clusterLocations(clientLocations, centerLocations) {
    const clusters = [];

    // Initialize clusters
    for (const center of centerLocations) {
        clusters.push({
            centroid: {
                location_name: center.location_name,
                lat: center.lat,
                lng: center.lng
            },
            points: [],
            max_radius: 0.0,
            density_ratio: 0.0
        });
    }

    // Assign each client location to the nearest center
    for (const clientCoord of clientLocations) {
        let minDistance = Infinity;
        let nearestCenterIndex;

        for (let i = 0; i < centerLocations.length; i++) {
            const distance = calculateDistance(clientCoord, centerLocations[i]);
            if (distance < minDistance) {
                minDistance = distance;
                nearestCenterIndex = i;
            }
        }

        clusters[nearestCenterIndex].points.push(clientCoord);
    }

    // Find max radius for each cluster and calculate density ratio
    for (const cluster of clusters) {
        const { centroid, points } = cluster;
        const { maxRadius, maxRadiusCoord } = findMaxRadius(points, { lat: centroid.lat, lng: centroid.lng });
        cluster.max_radius = maxRadius;
        cluster.density_ratio = points.length / (Math.PI * maxRadius * maxRadius);
    }

    return clusters;
}

const generate_priority_queue = () => {
    const clusters = clusterLocations(clientLocations,centerLocations)
    for (const cluster of clusters){
        for(let point=0;point<cluster.points.length;point++){
            cluster.points[point]=JSON.stringify(cluster.points[point])
        }
    }
    clusters.sort((a, b) => (b.density_ratio - a.density_ratio))
    return clusters

}

console.log(generate_priority_queue())