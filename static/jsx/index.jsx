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
      fetch("/restaurants.json")
      .then(response => response.json())
      .then(jsonRestaurants => this.setState({ 
        visibleRestaurants: jsonRestaurants["683"],
        campuses: Object.keys(jsonRestaurants)
      }));
    }

    render () {
      return (
        <div>
        <AllNavTabs buildings={ this.state.campuses }/>
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