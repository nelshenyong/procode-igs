import React, { useState } from 'react';

function FAQSection() {
  const [openIndexes, setOpenIndexes] = useState([]);

  const toggleAccordion = (index) => {
    if (openIndexes.includes(index)) {
      setOpenIndexes(openIndexes.filter(i => i !== index));
    } else {
      setOpenIndexes([...openIndexes, index]);
    }
  };

  const faqData = [
    {
      question: "What is Netflix?",
      answer: "Netflix is a streaming service that offers a wide variety of award-winning TV shows, movies, anime, documentaries and more – on thousands of internet-connected devices. You can watch as much as you want, whenever you want, without a single ad – all for one low monthly price. There's always something new to discover, and new TV shows and movies are added every week!"
    },
    {
      question: "How much does netflix cost?",
      answer: "Watch Netflix on your smartphone, tablet, Smart TV, laptop, or streaming device, all for one fixed monthly fee. Plans range from ₹ 199 to ₹ 799 a month. No extra costs, no contracts."
    },
    {
      question: "Where can i watch?",
      answer: "Watch anywhere, anytime, on an unlimited number of devices. Sign in with your Netflix account to watch instantly on the web at netflix.com from your personal computer or on any internet-connected device that offers the Netflix app, including smart TVs, smartphones, tablets, streaming media players and game consoles. You can also download your favourite shows with the iOS, Android, or Windows 10 app. Use downloads to watch while you're on the go and without an internet connection. Take Netflix with you anywhere."
    },
    {
      question: "How do I cancel?",
      answer: "Netflix is flexible. There are no annoying contracts and no commitments. You can easily cancel your account online in two clicks. There are no cancellation fees – start or stop your account anytime."
    },
    {
      question: "What can I watch from Netflix?",
      answer: "Netflix has an extensive library of feature films, documentaries, TV shows, anime, award-winning Netflix originals, and more. Watch as much as you want, anytime you want."
    },
    {
      question: "Is Netflix good for kids?",
      answer: "The Netflix Kids experience is included in your membership to give parents control while kids enjoy family-friendly TV shows and films in their own space. Kids profiles come with PIN-protected parental controls that let you restrict the maturity rating of content kids can watch and block specific titles you don't want kids to see."
    }
  ];

  return (
    <section className="FAQ__list__container">
      <h1 className="FAQ__heading">Frequently Asked Questions</h1>
      <div className="FAQ__list">
        {faqData.map((item, index) => (
          <div className="FAQ__accordian" key={index}>
            <button 
              className="FAQ__title"
              onClick={() => toggleAccordion(index)}
            >
              {item.question}
              <i className={`fal ${openIndexes.includes(index) ? 'fa-times' : 'fa-plus'}`}></i>
            </button>+
            <div 
              className="FAQ__visible"
              style={{ maxHeight: openIndexes.includes(index) ? '1000px' : '0' }}
            >
              <p>{item.answer}</p>
            </div>
          </div>
        ))}
      </div>
      <div className="FAQ__get__started__email">
        <h3>
          Ready to watch? Enter your email to create or restart your
          membership.
        </h3>
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

export default FAQSection;
