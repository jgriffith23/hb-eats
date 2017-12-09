class NavTab extends React.Component {
    constructor (props) {
        super(props);
        this.active = this.props.active;
    }

    render () {
        let url = "/?building=" + this.props.building;
        console.log(this.props);

        return (
            <li role="presentation" className={(this.active) ? "active" : ""}>
                <a href={url} onClick={ (evt) => this.props.handler(evt, this.props.building) }>
                  { this.props.building } { this.props.street }
                </a>
            </li>
        );
    }
}