class RestaurantList extends React.Component {
    constructor(props) {
        super(props);

        // FIXME: Get the state via AJAX?
        this.state = {
            "683": [
            {
              "address": "704 Sutter St", 
              "categories": [
                "Japanese", 
                "Sushi Bars", 
                "Asian Fusion"
              ], 
              "distanceAway": "249.0 ft", 
              "dollarSigns": 2, 
              "img": "https://s3-media2.fl.yelpcdn.com/bphoto/896N7UXBJk9rzG9BFZY1rw/o.jpg", 
              "name": "Sanraku", 
              "timeAway": "1.0 min", 
              "yelpURL": "https://www.yelp.com/biz/sanraku-san-francisco-2?adjust_creative=oH33mM4Gu5dN2sYrEpJZ-w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=oH33mM4Gu5dN2sYrEpJZ-w"
            }, 
            {
              "address": "679 Sutter St", 
              "categories": [
                "Mexican"
              ], 
              "distanceAway": "7.0 ft", 
              "dollarSigns": 2, 
              "img": "https://s3-media3.fl.yelpcdn.com/bphoto/0iXpzQAzmGR246ZKOnQacg/o.jpg", 
              "name": "Matador", 
              "timeAway": "1.0 min", 
              "yelpURL": "https://www.yelp.com/biz/matador-san-francisco-2?adjust_creative=oH33mM4Gu5dN2sYrEpJZ-w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=oH33mM4Gu5dN2sYrEpJZ-w"
            }
        ]};
    }

    render () {
        let restaurants = []

        for (let each of this.state[this.props.building]) {
            console.log(each);
            let restaurant = <Restaurant key={ each.name }
                                         address={ each.address } 
                                         categories={ each.categories }
                                         distanceAway={ each.distanceAway }
                                         dollarSigns={ each.dollarSigns }
                                         img={ each.img }
                                         name={ each.name }
                                         timeAway={ each.timeAway }
                                         yelpURL={ each.yelpURL }
                             />
            restaurants.push(restaurant);
        }

        return (
            <div>
                { restaurants }
            </div>
        );
    }
}