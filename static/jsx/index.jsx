"use strict";

class HBEatsSite extends React.Component {
    constructor (props) {
      super(props);
      this.getData = this.getData.bind(this);
      this.state = {
        visibleRestaurants: [],
        campuses: []
      };
    }

    getData (evt, building = "683") {
      console.log("getData was called");
      if (evt) {
        evt.preventDefault();
        console.log(building);
        console.log(this);
      }
      fetch(`/campuses?building=${building}`)
      .then(response => response.json())
      .then(jsonCampuses => this.setState({ 
        campuses: jsonCampuses.campuses
      }));

      fetch(`/restaurants?building=${building}`)
      .then(response => response.json())
      .then(jsonRestaurants => this.setState({ 
        visibleRestaurants: jsonRestaurants.restaurants
      }));
    }

    componentWillMount() {
      this.getData();
      // fetch("/campuses")
      // .then(response => response.json())
      // .then(jsonCampuses => this.setState({ 
      //   campuses: jsonCampuses.campuses
      // }));

      // fetch("/restaurants")
      // .then(response => response.json())
      // .then(jsonRestaurants => this.setState({ 
      //   visibleRestaurants: jsonRestaurants.restaurants
      // }));
      
    }

    render () {
      return (
        <div>
        <AllNavTabs campuses={ this.state.campuses } handler={ this.getData }/>
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