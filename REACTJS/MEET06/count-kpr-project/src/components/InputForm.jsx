import React, { useState } from "react";

const InputForm = ({ onCalculate }) => {
  const [propertyPrice, setPropertyPrice] = useState("");
  const [downPaymentPercentage, setDownPaymentPercentage] = useState("");
  const [monthlyIncome, setMonthlyIncome] = useState("");
  const [loanDuration, setLoanDuration] = useState("");
  const [fixedInterestRate, setFixedInterestRate] = useState("");
  const [fixedPeriod, setFixedPeriod] = useState("");
  const [floatingInterestRate, setFloatingInterestRate] = useState("");
  const [floatingPeriod, setFloatingPeriod] = useState("");

  const handleCalculate = () => {
    // Calculate logic here
    const results = {
      propertyPrice: propertyPrice,
      downPaymentPercentage: downPaymentPercentage,
      monthlyIncome: monthlyIncome,
      loanDuration: loanDuration,
      fixedInterestRate: fixedInterestRate,
      fixedPeriod: fixedPeriod,
      floatingInterestRate: floatingInterestRate,
      floatingPeriod: floatingPeriod,
    };
    onCalculate(results);
  };

  return (
    <div className="input-form">
      <input
        type="number"
        placeholder="Harga Properti"
        value={propertyPrice}
        onChange={(e) => setPropertyPrice(e.target.value)}
      />
      {propertyPrice && (
        <>
          <input
            type="number"
            placeholder="DP (%)"
            value={downPaymentPercentage}
            onChange={(e) => setDownPaymentPercentage(e.target.value)}
          />
          {downPaymentPercentage && (
            <>
              <input
                type="number"
                placeholder="Penghasilan Bulanan"
                value={monthlyIncome}
                onChange={(e) => setMonthlyIncome(e.target.value)}
              />
              {monthlyIncome && (
                <>
                  <input
                    type="number"
                    placeholder="KPR Berapa Lama (bulan)"
                    value={loanDuration}
                    onChange={(e) => setLoanDuration(e.target.value)}
                  />
                  {loanDuration && (
                    <>
                      <input
                        type="number"
                        placeholder="Bunga Fix (%)"
                        value={fixedInterestRate}
                        onChange={(e) => setFixedInterestRate(e.target.value)}
                      />
                      {fixedInterestRate && (
                        <>
                          <input
                            type="number"
                            placeholder="Periode Bunga Fix (bulan)"
                            value={fixedPeriod}
                            onChange={(e) => setFixedPeriod(e.target.value)}
                          />
                          {fixedPeriod && (
                            <>
                              <input
                                type="number"
                                placeholder="Bunga Floating (%)"
                                value={floatingInterestRate}
                                onChange={(e) =>
                                  setFloatingInterestRate(e.target.value)
                                }
                              />
                              {floatingInterestRate && (
                                <>
                                  <input
                                    type="number"
                                    placeholder="Periode Bunga Floating (bulan)"
                                    value={floatingPeriod}
                                    onChange={(e) =>
                                      setFloatingPeriod(e.target.value)
                                    }
                                  />
                                  {floatingPeriod && (
                                    <button onClick={handleCalculate}>
                                      Tampilkan Hasil
                                    </button>
                                  )}
                                </>
                              )}
                            </>
                          )}
                        </>
                      )}
                    </>
                  )}
                </>
              )}
            </>
          )}
        </>
      )}
    </div>
  );
};

export default InputForm;
