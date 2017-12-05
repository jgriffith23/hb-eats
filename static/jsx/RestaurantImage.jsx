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