import { useState } from "react";

export default function Addition()
{
    let [num1, setNum1] = useState(Math.floor(Math.random() * 10));
    let [num2, setNum2] = useState(Math.floor(Math.random() * 10));
    let [score, setScore] = useState(Math.floor(Math.random() * 10));
    return (
        <>

            <h2>Addition Calculation Quizz</h2>
            <p>Score: {score}</p>
            <form action="">
                <p>What is {num1} + {num2}?</p>
                <input type="number" name="" placeholder="Your Name" id="" required/>
                <button type="submit">Submit</button>
            </form>
        </>
    )
}