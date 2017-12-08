"use strict";

class HBEatsSite extends React.Component {
    constructor (props) {
      super(props);
      this.state = {
        visibleRestaurants: [],
        campuses: []
      };

    }

    componentDidMount() {
      fetch("/campuses")
      .then(response => response.json())
      .then(jsonCampuses => this.setState({ 
        campuses: jsonCampuses.campuses
      }));

      fetch("/restaurants")
      .then(response => response.json())
      .then(jsonRestaurants => this.setState({ 
        visibleRestaurants: jsonRestaurants.restaurants
      }));


    }

    render () {
      return (
        <div>
        <AllNavTabs campuses={ this.state.campuses }/>
        <RestaurantList building={ this.state.visibleRestaurants }/>
        </div>
      )
    };

}

ReactDOM.render(
    <ReactRouter.Router history={ ReactRouter.hashHistory }>
        <ReactRouter.Route path="/" component={ HBEatsSite }>
        </ReactRouter.Route>
    </ReactRouter.Router>,

    document.getElementById('root')
);