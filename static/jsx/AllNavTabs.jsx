class AllNavTabs extends React.Component {
    render () {
        console.log(this.props.campuses);

        let navTabs = [];

        for (let each of this.props.campuses) {
            let navTab = <NavTab building={ each.building }
                                 street={ each.street }
                                 active={ each.active } />;
            navTabs.push(navTab);
        }

        return (
            <ul className="nav nav-tabs">
                { navTabs }
            </ul>
        );
    }
}