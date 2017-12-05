class RestaurantOtherInfo extends React.Component {
    render () {
        return (
            <div className="other-info">
                Price: { "$".repeat(this.props.dollarSigns) } <br /> 
                Address: { this.props.address }<br />
                Distance from Hackbright: { this.props.distanceAway } <br />
                Time to walk from Hackbright: { this.props.timeAway } <br />
            </div>
        )
    }
}