// FriendListCard.jsx
import "./friend-list.css";
import FriendCard from "../FriendCard";

export default function FriendListCard({ friends, onSelectedFriend, selectedFriend, onDeleteFriend }) {
    return (
        <ul>
            {friends.map((friend, index) => (
                <FriendCard
                    friend={friend}
                    key={index}
                    onSelectedFriend={onSelectedFriend}
                    selectedFriend={selectedFriend}
                    onDeleteFriend={onDeleteFriend}
                />
            ))}
        </ul>
    );
}