class NavTab extends React.Component {
    constructor (props) {
        super(props);
    }

    render () {
        let url = "/?building=" + this.props.building;

        return (
            <li role="presentation" className={(this.props.active) ? "active" : ""}>
                <a href={url} onClick={ (evt) => this.props.handler(evt, this.props.building) }>
                  { this.props.building } { this.props.street }
                </a>
            </li>
        );
    }
}