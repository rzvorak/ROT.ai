import { useState, useEffect } from 'react'
import { ArrowUpIcon } from '@heroicons/react/24/outline';
import './Graph.css'
import Chart from './Chart'

function Graph({ input, isGraphSlidingIn, isGraphSlidingOut, onButtonClick, onAnimationEnd }) {
    const [fill, setFill] = useState("");  
    const [text, setText] = useState(""); 
    const [fullText, setFullText] = useState("");
    const [animationEnded, setAnimationEnded] = useState(false);
  
    useEffect(() => {
      setFill(input === "" ? "-enter a word..." : "-" + input);  
    }, [input]);
  
    useEffect(() => {
      setText("");
      setFullText("" + fill);
    }, [fill]);

  const initialData = [5, 5, 5, 5, 5, 5];
  const [chartData, setChartData] = useState(initialData);

  const generateRandomData = () => {
    const newData = chartData.map((value) => {
      // Generate random change between -2 and 2
      const randomChange = Math.random() * 4 - 2;
      const newValue = value + randomChange;

      // Ensure the value doesn't go below zero
      return Math.max(0, newValue);
    });

    // Update the chart data state
    setChartData(newData);
  };

    
  const handleAnimationEnd = () => {
    if (input !== "") {
      generateRandomData(); 
    }
    onAnimationEnd(); 
    setAnimationEnded(true); 
  };

  const handleButtonClick = () => {
    onButtonClick();
  }

  useEffect(() => {
    if (animationEnded) {
      let index = 0;
      const interval = setInterval(() => {
        if (index < fullText.length - 1) {
          setText((prev) => prev + fullText[index]); 
          index += 1;
        } else {
          clearInterval(interval); 
        }
      }, 50); 
    }
  }, [animationEnded, fullText]);



    return(
        <>
            <div className={isGraphSlidingOut ? "graph-slideout graph" 
                : isGraphSlidingIn ? "graph-slidein graph" 
                : "graph"} onAnimationEnd={handleAnimationEnd}>
                <div className="graph__plot">
                    <Chart className="graph__chart" dataPoints={chartData}/>
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