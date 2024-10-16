import { Link, Outlet } from "react-router-dom";

function Layout() {
  return (
    <>
      <nav>
        <a href="/">
          <div className="logo"></div>
        </a>
        <ul>
          <Link to={"/"}>DISNEY+ HOSTAR</Link>
          <Link to={"/movie"}>MOVIES</Link>
          <Link to={"/parks"}>PARKS</Link>
          <Link to={"/cruise"}>CRUISE</Link>
        </ul>
      </nav>

      <Outlet />

      <footer style={{ marginTop: "20px", textAlign: "center" }}>
        <div className="logo-footer"></div>
        <div className="sec-1">
          <Link to={"/"}>DISNEY+ HOSTAR</Link>
          <Link to={"/movie"}>MOVIES</Link>
          <Link to={"/parks"}>PARKS</Link>
          <Link to={"/cruise"}>CRUISE</Link>
        </div>
        <div className="sec-2">
          <Link to={"/"}>About Disney</Link>
          <Link to={"/"}>Support</Link>
          <Link to={"/"}>Carrers</Link>
          <Link to={"/"}>Term of Use</Link>
          <Link to={"/"}> Supplemental Privacy Policy for Indonesia </Link>
          <Link to={"/"}>Privacy Policy</Link>
          <Link to={"/"}>Interest-Based Ads</Link>
        </div>
        <div className="sec-3">
            <p>©Disney ©Disney/Pixar © ™ Lucasfilm Ltd. © Marvel, Disney Entertainment</p>
        </div>
      </footer>
    </>
  );
}

export default Layout;
