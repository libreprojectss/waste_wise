//Algorithm that separates various coordinates to location groups also identifies the radius of the cluster based on the farthest point from the centroid
//list of coordinates ehich are in format  {lat: 0.0, lng: 0.0} the values should be 20 and random
const random_coordinates=[
    { "lat": 37.826, "lng": -122.422 },
    { "lat": -29.145, "lng": 153.456 },
    { "lat": 45.678, "lng": -75.890 },
    { "lat": -12.345, "lng": 67.890 },
    { "lat": 55.432, "lng": 12.345 },
    { "lat": -8.901, "lng": 145.678 },
    { "lat": 33.456, "lng": -118.901 },
    { "lat": -41.234, "lng": 174.567 },
    { "lat": 20.567, "lng": 78.901 },
    { "lat": -3.456, "lng": 102.345 },
    { "lat": 61.789, "lng": -149.567 },
    { "lat": -23.456, "lng": 47.890 },
    { "lat": 38.901, "lng": -77.234 },
    { "lat": -14.567, "lng": 167.890 },
    { "lat": 53.234, "lng": 9.012 },
    { "lat": -17.890, "lng": 31.234 },
    { "lat": 48.901, "lng": -66.789 },
    { "lat": -9.012, "lng": 140.567 },
    { "lat": 35.678, "lng": -80.123 },
    { "lat": -25.678, "lng": 132.345 }
]

const Locations=[
    {
        name:"Location 1",
        lat: 37.826,
        lng: -122.422
    },
    {
        name:"Location 2",
        lat: -29.145,
        lng: 153.456
    },
    {
        name:"Location 3",
        lat: 45.678,
        lng: -75.890
    },
    {
        name:"Location 4",
        lat: -12.345,
        lng: 67.890
    }
]

function calculate_distance(lat1, lon1, lat2, lon2){
    return Math.sqrt((lat1-lat2)**2 + (lon1-lon2)**2)
}
const calculate_density_ratio=(cluster_object)=>{
    const density_ratio=cluster_object.points.length/(Math.PI*(cluster_object.max_radius**2))
    return density_ratio*10000
}
function group_coordinates(){
    const clusters=[]
    for (let i=0; i<Locations.length; i++){
        clusters.push({
            centroid: Locations[i],
            points: [],
            max_radius: 0,
            density_ratio:0
        })
    }
    for (let i=0; i<random_coordinates.length; i++){
        let selected_location=0
        let min_length=Infinity
        let max_radius=0
        for (let j=0; j<clusters.length; j++){
            const distance=calculate_distance(random_coordinates[i].lat, random_coordinates[i].lng, clusters[j].centroid.lat, clusters[j].centroid.lng)
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
        selected_location.points.push(JSON.stringify(random_coordinates[i]))
        selected_location.max_radius=max_radius
    }

    for(const j of clusters){
        j.density_ratio=calculate_density_ratio(j)
    }
    return clusters



}

const generate_priority_queue=()=>{
    const clusters=group_coordinates()
    clusters.sort((a,b)=>(b.density_ratio-a.density_ratio))
    return clusters

}

console.log("result")
console.log(generate_priority_queue())