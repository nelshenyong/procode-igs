import "./form.css"

export default function FormSplitBill(){

    return(
        <form action="" className="form-split-bill">
            <h2>Patungan Bareng si</h2>

            <label htmlFor="totalTagihan">💵Total Tagihan</label>
            <input 
                type="text"
                id="totalTagihan"
            />

            <label htmlFor="tagihanKamu">💵Tagihan kamu</label>
            <input 
                type="text" 
                id="tagihanKamu"
            />

            <label htmlFor="tagihan">💵Tagihan</label>
            <input type="text" id="tagihan" disabled />

            <label htmlFor="opsiTeman">Ditalangin sama</label>
            <select name="" id="opsiTeman">
                <option value="user">Kamu</option>
                <option value="friend"></option>
            </select>

            <button className="button">Tambah</button>
        </form>
    );
}