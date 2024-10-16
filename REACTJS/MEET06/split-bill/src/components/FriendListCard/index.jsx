import "./friend-list.css";
import FriendCard from "../FriendCard";

export default function FriendListCard({ friends }) {
    return(
        <ul>
            {friends.map((friend, index) => (

                <FriendCard
                    friend={friend}
                    key={index}
                    />
            ))}
        </ul>
    );
}