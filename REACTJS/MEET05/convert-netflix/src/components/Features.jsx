import React from 'react';

function Features() {
  return (
    <section className="features__container">
      <div className="feature">
        <div className="feature__details">
          <h3 className="feature__title">Enjoy on your TV.</h3>
          <h5 className="feature__sub__title">
            Watch on smart TVs, PlayStation, Xbox, Chromecast, Apple TV,
            Blu-ray players and more.
          </h5>
        </div>
        <div className="feature__image__container">
          <img
            src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/tv.png"
            alt="Feature image"
            className="feature__image"
          />
          <div className="feature__backgroud__video__container">
            <video
              autoPlay
              loop
              muted
              className="feature__backgroud__video"
            >
              <source
                src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/video-tv-in-0819.m4v"
                type="video/mp4"
              />
            </video>
          </div>
        </div>
      </div>
      {/* Feature 2 */}
      <div className="feature">
        <div className="feature__details">
          <h3 className="feature__title">
            Download your shows to watch offline.
          </h3>
          <h5 className="feature__sub__title">
            Save your favourites easily and always have something to watch.
          </h5>
        </div>
        <div className="feature__image__container">
          <img
            src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/mobile-0819.jpg"
            alt="Feature image"
            className="feature__image"
          />
          <div className="feature__2__poster__container">
            <div className="poster__container">
              <img
                src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/boxshot.png"
                alt="poster"
                className="poster"
              />
            </div>
            <div className="poster__details">
              <h4>Stranger Things</h4>
              <h6>Downloading...</h6>
            </div>
            <div className="download__gif__container">
              <img
                src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/download-icon.gif"
                alt="downloading gif"
                className="gif"
              />
            </div>
          </div>
        </div>
      </div>
      {/* Feature 3 */}
      <div className="feature">
        <div className="feature__details">
          <h3 className="feature__title">Watch everywhere.</h3>
          <h5 className="feature__sub__title">
            Stream unlimited movies and TV shows on your phone, tablet,
            laptop, and TV.
          </h5>
        </div>
        <div className="feature__image__container feature__3__image__container">
          <img
            src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/device-pile-in.png"
            alt="Feature image"
            className="feature__image feature__3__image"
          />
          <div
            className="feature__backgroud__video__container feature__3__backgroud__video__container"
          >
            <video
              autoPlay
              loop
              muted
              className="feature__backgroud__video feature__3__backgroud__video"
            >
              <source
                src="https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/video-devices-in.m4v"
                type="video/mp4"
              />
            </video>
          </div>
        </div>
      </div>
      {/* Feature 4 */}
      <div className="feature">
        <div className="feature__details">
          <h3 className="feature__title">Create profiles for children.</h3>
          <h5 className="feature__sub__title">
            Send children on adventures with their favourite characters in a
            space made just for them—free with your membership.
          </h5>
        </div>
        <div className="feature__image__container">
          <img
            src="https://occ-0-4023-2164.1.nflxso.net/dnm/api/v6/19OhWN2dO19C9txTON9tvTFtefw/AAAABVxdX2WnFSp49eXb1do0euaj-F8upNImjofE77XStKhf5kUHG94DPlTiGYqPeYNtiox-82NWEK0Ls3CnLe3WWClGdiJP.png?r=5cf"
            alt="Feature image"
            className="feature__image"
          />
        </div>
      </div>
    </section>
  );
}

export default Features;