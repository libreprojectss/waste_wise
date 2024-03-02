import centroid_locations from "../../models/centroid_locations.js"


function calculate_distance(lat1, lon1, lat2, lon2){
    return Math.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)
}
const calculate_density_ratio=(cluster_object)=>{
    if(cluster_object.max_radius==0){
        return 0
    }
    const density_ratio=cluster_object.points.length/(Math.PI*(cluster_object.max_radius**2))
    return density_ratio*10000
}
async function group_coordinates(coordinates){
    const dbLocations=await centroid_locations.find().select(["-__v","-_id"])
    const clusters=[
    ]
    for (let i=0; i<dbLocations.length; i++){
        clusters.push({
            centroid: dbLocations[i],
            points: [],
            max_radius: 0,
            density_ratio:0
        })
    }
    for (let i=0; i<coordinates.length; i++){
        let selected_location=[]
        let min_length=Infinity
        let max_radius=0
        for (let j=0; j<clusters.length; j++){
            const distance=calculate_distance(coordinates[i].lat, coordinates[i].lng, clusters[j].centroid.lat, clusters[j].centroid.lng)
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
        const formattedCoordinate = {
            "lat": coordinates[i].lat,
            "lng": coordinates[i].lng,
            "pickup_identifier":coordinates[i].pickup_identifier
        };
        selected_location?.points?.push(JSON.stringify(formattedCoordinate))
        selected_location.max_radius=max_radius
    }

    for(const j of clusters){
        j.density_ratio=calculate_density_ratio(j)
    }
    return clusters
}

export  const generate_priority_queue=async(call,callback)=>{
    const coordinates = call.request.coordinate;
    const clusters=await group_coordinates(coordinates)
    clusters.sort((a,b)=>(b.density_ratio-a.density_ratio))
    console.log(clusters)
    const response = { cluster: clusters };
    callback(null, response);

}
