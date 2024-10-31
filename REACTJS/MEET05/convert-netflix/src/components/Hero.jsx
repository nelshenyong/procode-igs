import React from 'react';

function Hero() {
  return (
    <section className="hero">
      <div className="hero__bg__image__container">
        <img
          src="https://assets.nflxext.com/ffe/siteui/vlv3/9c5457b8-9ab0-4a04-9fc1-e608d5670f1a/710d74e0-7158-408e-8d9b-23c219dee5df/IN-en-20210719-popsignuptwoweeks-perspective_alpha_website_small.jpg"
          alt="BG hero image"
          className="hero__bg__image"
        />
      </div>
      <div className="hero__bg__overlay"></div>
      <div className="hero__card">
        <h1 className="hero__title">
          Unlimited Movies TV,<br />
          Shows and More.
        </h1>
        <p className="hero__subtitle">Watch anywhere and cancel anytime.</p>
        <p className="hero__description">
          Ready to watch? Enter your email to create or restart your
          membership.
        </p>
        <div className="email__form__container">
          <div className="form__container">
            <input type="email" className="email__input" placeholder=" " />
            <label className="email__label">Email Address</label>
          </div>
          <button className="primary__button">
            Get Started <i className="fal fa-chevron-right"></i>
          </button>
        </div>
      </div>
    </section>
  );
}

export default Hero;