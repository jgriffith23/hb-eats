"use strict";


class Restaurant extends React.Component {
    render() {
        const name = this.props.name;
        return <h1>{ name }</h1>;
    }
}

function HBEatsSite(props) {

    let restaurants = fetch("/restaurants.json?building=450")
    .then(function(response) {
        return response.json()
    })
    .then(function(data) {
        console.log(data.info); 
    });

    console.log(restaurants);

    return (
        <Restaurant name={`${restaurants[0].name}`} />
    );

}

ReactDOM.render(
    <ReactRouter.Router history={ ReactRouter.hashHistory }>
        <ReactRouter.Route path="/" component={ HBEatsSite }>
        </ReactRouter.Route>
    </ReactRouter.Router>,

    document.getElementById('root')
);