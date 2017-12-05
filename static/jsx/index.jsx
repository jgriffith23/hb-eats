"use strict";

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