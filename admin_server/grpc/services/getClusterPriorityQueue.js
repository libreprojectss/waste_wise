
const Locations=[
    {
        name:"Location 1",
        lat: 37.826,
        long: -122.422
    },
    {
        name:"Location 2",
        lat: -29.145,
        long: 153.456
    },
    {
        name:"Location 3",
        lat: 45.678,
        long: -75.890
    },
    {
        name:"Location 4",
        lat: -12.345,
        long: 67.890
    }
]

function calculate_distance(lat1, lon1, lat2, lon2){
    return Math.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)
}
const calculate_density_ratio=(cluster_object)=>{
    const density_ratio=cluster_object.points.length/(Math.PI*(cluster_object.max_radius**2))
    return density_ratio*10000
}
function group_coordinates(coordinates){
    const clusters=[]
    for (let i=0; i<Locations.length; i++){
        clusters.push({
            centroid: Locations[i],
            points: [],
            max_radius: 0,
            density_ratio:0
        })
    }
    for (let i=0; i<coordinates.length; i++){
        let selected_location=0
        let min_length=Infinity
        let max_radius=0
        for (let j=0; j<clusters.length; j++){
            const distance=calculate_distance(coordinates[i].lat, coordinates[i].long, clusters[j].centroid.lat, clusters[j].centroid.long)
            if(distance<min_length){
                selected_location=clusters[j]
                min_length=distance
            }
            if(distance>max_radius) {
            max_radius=distance
        }
        
        }
        if( max_radius< selected_location.max_radius){
            max_radius=selected_location.max_radius
        }
        selected_location.points.push(JSON.stringify(coordinates[i]))
        selected_location.max_radius=max_radius
    }

    for(const j of clusters){
        j.density_ratio=calculate_density_ratio(j)
    }
    return clusters
}

export const generate_priority_queue=(call,callback)=>{
    const coordinates = call.request.coordinate;
    const clusters=group_coordinates(coordinates)
    clusters.sort((a,b)=>(b.density_ratio-a.density_ratio))
    const response = { cluster: clusters };
    callback(null, response);

}
