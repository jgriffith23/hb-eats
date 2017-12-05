"use strict";

function HBEatsSite(props) {
    fetch("/restaurants.json")
    .then(function(response) {
      return response.json();
    }).then(function(jsonRestaurants) {
      console.log(jsonRestaurants);    
    });
    
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