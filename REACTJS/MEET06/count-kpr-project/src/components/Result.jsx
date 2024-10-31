import React from 'react';

const Result = ({ results }) => {
    // Extract results for easier access
    const {
        propertyPrice,
        downPaymentPercentage,
        monthlyIncome,
        loanDuration,
        fixedInterestRate,
        fixedPeriod,
        floatingInterestRate,
        floatingPeriod,
    } = results;

    // Calculate the values
    const downPayment = (propertyPrice * downPaymentPercentage) / 100;
    const loanAmount = propertyPrice - downPayment;

    const fixedInterest = (loanAmount * fixedInterestRate) / 100;
    const totalFixedInterest = fixedInterest * (fixedPeriod / 12); // Assuming fixed period in months
    const totalLoanWithFixedInterest = loanAmount + totalFixedInterest;

    const monthlyInstallment = totalLoanWithFixedInterest / loanDuration; // Monthly installment for the total loan amount

    const loanDurationInYears = loanDuration / 12;
    const floatingInterest = (loanAmount * floatingInterestRate) / 100;
    const totalFloatingInterest = floatingInterest * (floatingPeriod / 12);
    const totalLoanWithFloatingInterest = totalLoanWithFixedInterest + totalFloatingInterest;

    return (
        <div className="result">
            <h2>Opsi Strategimu</h2>
            <p>
                Analisa: Total bunga KPR yang harus kamu bayarkan adalah Rp {totalFixedInterest + totalFloatingInterest} setara dengan {((totalFixedInterest + totalFloatingInterest) / loanAmount) * 100}% dari pokok pinjamanmu.
            </p>
            <p>
                Cicilan KPRmu dalam rentang Rp {monthlyInstallment} - {monthlyInstallment * 1.2} atau setara dengan {((monthlyInstallment / monthlyIncome) * 100).toFixed(2)}% - {(((monthlyInstallment * 1.2) / monthlyIncome) * 100).toFixed(2)}% dari penghasilan bulananmu.
            </p>
            <p>
                Rasio: {loanDurationInYears < 5 ? 'Sangat sehat' : 'Sehat'}
            </p>
            <p>
                Kamu bisa mempertimbangkan untuk melunasi KPRmu lebih awal. Kamu bisa menambah cicilan bulananmu menjadi Rp {monthlyInstallment * 1.2} - Rp {monthlyInstallment * 1.5} dan bisa menyelesaikan KPR mu dalam {(loanDuration * 0.8)} bulan.
            </p>

            <h2>Strategimu</h2>
            <p>
                Pokok pinjaman: Rp {loanAmount}
            </p>
            <p>
                Jumlah periode: {loanDuration} Bulan ({loanDurationInYears.toFixed(2)} Tahun)
            </p>
            <p>
                Bunga fix: {fixedInterestRate}% ({fixedPeriod} Bulan)
            </p>
            <p>
                Total bunga periode fix: Rp {totalFixedInterest.toFixed(2)}
            </p>
            <p>
                Bunga floating: {floatingInterestRate}% ({floatingPeriod} Bulan)
            </p>
            <p>
                Total bunga periode floating: Rp {totalFloatingInterest.toFixed(2)}
            </p>
            <p>
                % Total bunga KPR dari pokok pinjaman: {(((totalFixedInterest + totalFloatingInterest) / loanAmount) * 100).toFixed(2)}%
            </p>
            <p>
                Sisa pokok pinjaman setelah periode fix: Rp {loanAmount - totalFixedInterest}
            </p>

            <h2>Angsuran</h2>
            <table>
                <thead>
                    <tr>
                        <th>Bulan</th>
                        <th>Jumlah Angsuran</th>
                    </tr>
                </thead>
                <tbody>
                    {/* You can generate rows for each month here */}
                    {[...Array(loanDuration)].map((_, index) => (
                        <tr key={index}>
                            <td>{index + 1}</td>
                            <td>Rp {monthlyInstallment.toFixed(2)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <h2>Biaya Lain</h2>
            <p>
                Biaya lain KPR ini adalah estimasi dengan berbagai variabel umum dalam dunia KPR, silakan disesuaikan dengan kondisi masing-masing.
            </p>
            <p>
                Total biaya lain: ± Rp {(totalFixedInterest + totalFloatingInterest) * 0.1}
            </p>
            <p>
                Rincian:
            </p>
            <ul>
                <li>Biaya BPHTB: kamu harus mengisi NJOO-TKP terlebih dahulu Klik di sini.</li>
                <li>Biaya AJB: Rp {(totalFixedInterest + totalFloatingInterest) * 0.05}</li>
                <li>Biaya balik nama: Rp {(totalFixedInterest + totalFloatingInterest) * 0.05}</li>
                <li>Biaya bank: ± Rp {(totalFixedInterest + totalFloatingInterest) * 0.05}</li>
            </ul>
        </div>
    );
};

export default Result;