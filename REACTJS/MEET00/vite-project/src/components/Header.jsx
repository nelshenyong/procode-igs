const Header = () => {
    const headerStyle = {
      display: 'flex',
      justifyContent: 'space-between',
    }
    return (
      <header>
        <nav style={headerStyle}>
          <a href="#">Home</a>
          <a href="#">About</a>
          <a href="#">Doc</a>
          <a href="#">Contact</a>
        </nav>
      </header>
    )
  }

  export default Header;