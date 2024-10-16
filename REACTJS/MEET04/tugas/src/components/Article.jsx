import { useContext } from "react";
import { GlobalContext } from "../context";

export default function Article(props){
    const user = useContext(GlobalContext);

    const articleStyle = {
        textAlign : 'left',
        backgroundColor : 'salmon',
        padding : '10px',
        marginBottom : '20px'
    }

    return (
        <div style={articleStyle} >
            <h3 style={{marginBottom : 0}}>{props.title}</h3>
            <small>
                Date : {props.date}, tags: {props.tags.join(", ")}{" "}
            </small>
            <div>
                <small>Ditulis oleh {user.username}</small>
            </div>
        </div>
    )
}