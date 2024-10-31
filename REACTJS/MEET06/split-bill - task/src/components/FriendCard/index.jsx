import "./friend.css"

export default function FriendCard({ friend, onSelectedFriend, selectedFriend, onDeleteFriend }) {
    const isSelected = selectedFriend?.id === friend.id
    
    return (
        <li className={isSelected ? "selected" : ""}>
            <img src={friend.image} alt={friend.name} />
            <h3>{friend.name}</h3>
            {friend.balance < 0 && (
                <p className="red">
                    Kamu berhutang Rp{Math.abs(friend.balance)} ke kamu
                </p>
            )}
            {friend.balance > 0 && (
                <p className="green">
                    {friend.name} berhutang Rp{Math.abs(friend.balance)} ke kamu
                </p>
            )}
            {friend.balance === 0 && <p>Kamu dan {friend.name} tidak ada hutang</p>}
            <button className="button" onClick={() => onSelectedFriend(friend)}>
                {isSelected ? "Tutup" : "Pilih"}
            </button>
            <button className="button button-delete" onClick={() => onDeleteFriend(friend.id)}>
                Hapus
            </button>
        </li>
    );
}