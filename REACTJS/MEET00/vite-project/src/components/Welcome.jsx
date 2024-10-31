export default function Welcome(props)
{
    if (!props.name) 
        return (
            <>
                <button>Welcome!</button>
            </>
        )
        
    return (
        <>
            <button>Welcome {props.name}!</button>
        </>
    )
}