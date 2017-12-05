"use strict";

class AllNavTabs extends React.Component {
    render () {
        return (
            <ul className="nav nav-tabs">
                <NavTab building="683" active={ true } />
                <NavTab building="450" />
            </ul>
        );
    }
}

class RestaurantOtherInfo extends React.Component {
    render () {
        return (
            <div className="other-info">
                Price: { "$".repeat(this.props.dollarSigns) } <br /> 
                Address: { this.props.address }<br />
                Distance from Hackbright: { this.props.distanceAway } <br />
                Time to walk from Hackbright: { this.props.timeAway } <br />
            </div>
        )
    }
}

class RestaurantCategories extends React.Component {
    render () {
        return (
            <div className="category-list">
                { this.props.categories.join(", ") }
            </div>
        )
    }
}

class RestaurantImage extends React.Component {
    render () {
        return (
            <div className="col-xs-12 col-md-12">
                <img className="img-responsive img-rounded thumbnail restaurant-img" 
                     src={ this.props.img } />
            </div>
        );
    }
}

class RestaurantHeading extends React.Component {
    render () {
        return (
            <h4 className="rest-name"> 
                <a href="{ this.props.url }"> 
                    { this.props.name }
                </a> 
            </h4>
        );
    }
}

class Restaurant extends React.Component {

    render() {
        const name = this.props.name;
        const categories = ["apple", "berry"]

        return (
            <div className="col-xs-6 col-xs-offset-1 col-md-4">
                <div className="container well well-lg">
                    <RestaurantHeading name={ this.props.name } url={ this.props.yelpURL }/>
                    <div className="row info">
                        <div className="col-xs-12 col-md-12">
                            <RestaurantCategories categories={ this.props.categories } />
                            <RestaurantOtherInfo dollarSigns={ this.props.dollarSigns }
                                                 address={ this.props.address }
                                                 distanceAway={ this.props.distanceAway }
                                                 timeAway={ this.props.timeAway }/>
                            <RestaurantImage img={ this.props.img } />
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

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

function HBEatsSite(props) {

    return (
        <div>
        <AllNavTabs buildings={["683", "450"]}/>
        <RestaurantList building="683"/>
        </div>
    );

}

ReactDOM.render(
    <ReactRouter.Router history={ ReactRouter.hashHistory }>
        <ReactRouter.Route path="/" component={ HBEatsSite }>
        </ReactRouter.Route>
    </ReactRouter.Router>,

    document.getElementById('root')
);