class RestaurantList extends React.Component {
    constructor(props) {
        super(props);
    }

    render () {
        let restaurants = []

        console.log("in RestaurantList render: ");
        console.log(this.props.building);

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