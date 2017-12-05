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