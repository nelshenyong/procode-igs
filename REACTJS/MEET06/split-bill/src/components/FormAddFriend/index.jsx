import { useState } from "react";

export default function FormAddFriend({ onAddNewFriend }) {
    const [name, setName] = useState("");
    const defaultImgUrl = "https://i.pravatar.cc/48/";
    const [imageUrl, setImageUrl] = useState(defaultImgUrl);

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!name || !imageUrl) return;

        const id = crypto.randomUUID();
        const newFriend = {
            id,
            name,
            image: `${imageUrl}?=${id}`,
            balance: 0,
        };

        onAddNewFriend(newFriend);
        setName("");
        setImageUrl(defaultImgUrl);
    };

    return (
        <form className="form-add-friend" onSubmit={handleSubmit}>
            <label htmlFor="name">🤷🏻‍♂ Nama</label>
            <input
                type="text"
                id="name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />

            <label htmlFor="imageUrl">📸 Gambar</label>
            <input
                type="text"
                id="imageUrl"
                value={imageUrl}
                onChange={(e) => setImageUrl(e.target.value)}
            />

            <button className="button">Tambah</button>
        </form>
    );
}
