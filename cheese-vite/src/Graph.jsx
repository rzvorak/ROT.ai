import { useState, useEffect } from 'react'
import { ArrowUpIcon } from '@heroicons/react/24/outline';
import './Graph.css'
import Chart from './Chart'

function Graph({ input, isGraphSlidingIn, isGraphSlidingOut, onButtonClick, onAnimationEnd }) {
    const [fill, setFill] = useState("");  // Initially empty, will update based on `input`
    const [text, setText] = useState(""); // State for the progressively displayed text
    const [fullText, setFullText] = useState(""); // Initialize empty, will set dynamically
    const [animationEnded, setAnimationEnded] = useState(false);
  
    // Update `fill` based on `input`
    useEffect(() => {
      setFill(input === "" ? "-enter a word..." : "-" + input);  // Update `fill` when `input` changes
    }, [input]);
  
    // Dynamically update `fullText` when `fill` changes
    useEffect(() => {
      setText("");
      setFullText("" + fill);
    }, [fill]);

     // Function to handle animation end and trigger the letter-by-letter text display
  const handleAnimationEnd = () => {
    onAnimationEnd(); // Call the parent onAnimationEnd callback
    setAnimationEnded(true); // Set animation as finished
  };

  const handleButtonClick = () => {
    onButtonClick();
    
  }

  // Effect to update text letter by letter after animation ends
  useEffect(() => {
    if (animationEnded) {
      let index = 0;
      const interval = setInterval(() => {
        if (index < fullText.length - 1) {
          setText((prev) => prev + fullText[index]); // Add the next letter to the text
          index += 1;
        } else {
          clearInterval(interval); // Stop once all letters are displayed
        }
      }, 50); // Delay between letters (adjust as necessary)
    }
  }, [animationEnded, fullText]);



    return(
        <>
            <div className={isGraphSlidingOut ? "graph-slideout graph" 
                : isGraphSlidingIn ? "graph-slidein graph" 
                : "graph"} onAnimationEnd={handleAnimationEnd}>
                <div className="graph__plot">
                    <Chart className="graph__chart"/>
                </div>
                <div className="graph__details">
                    <div className="graph__details__set">
                        <div className="graph__text__container">
                            <h3 className="graph__text">{text}</h3>
                        </div>
                    </div>
                    <div className="graph__details__control">
                        <button className="graph__details__button" onClick={handleButtonClick}>
                            <ArrowUpIcon className="up__icon" />
                        </button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Graph