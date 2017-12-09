"use strict";

class HBEatsSite extends React.Component {
    constructor (props) {
      super(props);

      // We have to bind getData here or else the subcomponent click events that
      // use it won't have the correct context to update the component's state.
      this.getData = this.getData.bind(this);

      // Store what can change: the restaurants, and the campuses.
      this.state = {
        visibleRestaurants: [],
        campuses: []
      };
    }

    // Fetch JSON from the server to populate the page. Can respond to a 
    // click event or just get called when the page loads.

    getData (evt, building = "683") {

      // We won't be able to preventDefault if there was no evt.
      if (evt) {
        evt.preventDefault();
      }

      // No matter what, request the JSON data and update the component's
      // state with the correct info.

      fetch(`/campuses?building=${building}`, { method: "GET" })
      .then(response => response.json())
      .then(jsonCampuses => this.setState({ 
        campuses: jsonCampuses.campuses
      }));

      fetch(`/restaurants?building=${building}`, { method: "GET" })
      .then(response => response.json())
      .then(jsonRestaurants => this.setState({ 
        visibleRestaurants: jsonRestaurants.restaurants
      }));
    }

    // When the component mounts eventually, call getData to update its state.

    componentWillMount() {
      this.getData();      
    }

    // Render the two large page components.
    render () {
      return (
        <div>
        <AllNavTabs campuses={ this.state.campuses } handler={ this.getData }/>
        <RestaurantList building={ this.state.visibleRestaurants }/>
        </div>
      )
    };

}

// Render the HBEatsSite component in the root div.
ReactDOM.render(
    <ReactRouter.Router history={ ReactRouter.hashHistory }>
        <ReactRouter.Route path="/" component={ HBEatsSite }>
        </ReactRouter.Route>
    </ReactRouter.Router>,

    document.getElementById('root')
);