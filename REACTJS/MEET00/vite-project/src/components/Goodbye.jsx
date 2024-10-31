export default function Goodbye({name})
{
    return (
        <button>
            Gooodbye { name ? `, ${name}.` : "!"}!
        </button>
    )
}