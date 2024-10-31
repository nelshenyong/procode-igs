import { useState } from "react";
import "./form.css";

export default function FormSplitBill({ selectedFriend, handleSplitBill }) {
    const [amount, setAmount] = useState("");
    const [myBill, setMyBill] = useState("");
    const friendBill = amount ? amount - myBill : "";
    const [whoIsPaying, setWhoIsPaying] = useState("");

    function handleSubmit(e) {
        e.preventDefault();
        if (!amount || !myBill) return;
        handleSplitBill(whoIsPaying === "user" ? friendBill : -myBill);
    }

    return (
        <form className="form-split-bill" onSubmit={handleSubmit}>
            <h2>Patungan Bareng si {selectedFriend.name}</h2>

            <label htmlFor="totalTagihan">💵 Total Tagihan</label>
            <input
                type="number"
                id="totalTagihan"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
            />

            <label htmlFor="tagihanKamu">💵 Tagihan Kamu</label>
            <input
                type="number"
                id="tagihanKamu"
                value={myBill}
                onChange={(e) => setMyBill(e.target.value)}
            />

            <label htmlFor="tagihanTeman">💵 Tagihan {selectedFriend.name}</label>
            <input type="text" id="tagihanTeman" disabled value={friendBill} />

            <label htmlFor="opsiTeman">Ditalangin Sama</label>
            <select
                id="opsiTeman"
                value={whoIsPaying}
                onChange={(e) => setWhoIsPaying(e.target.value)}
            >
                <option value="user">Kamu</option>
                <option value="friend">{selectedFriend.name}</option>
            </select>

            <button type="submit" className="button">Tambah</button>
        </form>
    );
}
