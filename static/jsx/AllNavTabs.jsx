class AllNavTabs extends React.Component {
    render () {
        return (
            <ul className="nav nav-tabs">
                <NavTab building="683" active={ true } />
                <NavTab building="450" />
            </ul>
        );
    }
}