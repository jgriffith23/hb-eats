class RestaurantCategories extends React.Component {
    render () {
        return (
            <div className="category-list">
                { this.props.categories.join(", ") }
            </div>
        )
    }
}