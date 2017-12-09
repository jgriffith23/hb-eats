class AllNavTabs extends React.Component {
    render () {

        let navTabs = [];

        for (let each of this.props.campuses) {
            let navTab = <NavTab key={ each.building }
                                 building={ each.building }
                                 street={ each.street }
                                 active={ each.active } 
                                 handler={ this.props.handler } />;
            navTabs.push(navTab);
        }

        return (
            <ul className="nav nav-tabs">
                { navTabs }
            </ul>
        );
    }
}