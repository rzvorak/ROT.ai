import React, { useState } from 'react'
import Title from './Title'
import Graph from './Graph'
import './App.css'

function App() {
  const [input, setInput] = useState("");

  const [isTitleSlidingOut, setIsTitleSlidingOut] = useState(false);
  const [isGraphSlidingIn, setIsGraphSlidingIn] = useState(false);

  const [isGraphSlidingOut, setIsGraphSlidingOut] = useState(false);
  const [isTitleSlidingIn, setIsTitleSlidingIn] = useState(false);

  
  const handleTitleClick = (inputValue) => {
    console.log("value: " + inputValue);
    setInput(inputValue);
    setIsGraphSlidingIn(true);
    setIsTitleSlidingOut(true);
  }

  const handleGraphClick = () => {
      setIsTitleSlidingIn(true);
      setIsGraphSlidingOut(true);
  }

  const handleTitleAnimationEnd = () => {
    if (isTitleSlidingOut && isTitleSlidingIn) {
      setIsTitleSlidingOut(false); 
      setIsTitleSlidingIn(false); 
    }
  };

  const handleGraphAnimationEnd = () => {
    if (isGraphSlidingOut && isGraphSlidingIn) {
      setIsGraphSlidingOut(false); 
      setIsGraphSlidingIn(false); 
    }
  };

  return (
    <>
      <div className="app__container">  
        <Title onButtonClick={handleTitleClick} isTitleSlidingOut={isTitleSlidingOut} 
        isTitleSlidingIn={isTitleSlidingIn}  onAnimationEnd={handleTitleAnimationEnd}/>
        <Graph input={input} onButtonClick={handleGraphClick} isGraphSlidingIn={isGraphSlidingIn} 
        isGraphSlidingOut={isGraphSlidingOut} onAnimationEnd={handleGraphAnimationEnd}/>
      </div>
    </>
  )
}

export default App