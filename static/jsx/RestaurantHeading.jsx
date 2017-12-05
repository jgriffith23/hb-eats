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