class RestaurantList extends React.Component {
    constructor(props) {
        super(props);
    }

    render () {
        let restaurants = [];

        // "building" is a list of objects containing restaurant info.
        // generate a Restaurant component for each object, and return them
        // all together wrapped in a div.
        for (let each of this.props.building) {
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