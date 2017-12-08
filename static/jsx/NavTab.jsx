class NavTab extends React.Component {
    constructor (props) {
        super(props);
        this.active = this.props.active;
    }

    render () {
        let url = "/?building=" + this.props.building;

        return (
            <li role="presentation" className={(this.active) ? "active" : ""}>
                <a href={url}>{ this.props.building } { this.props.street }</a>
            </li>
        );
    }
}