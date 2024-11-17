import { useState } from 'react'
import { MagnifyingGlassIcon } from '@heroicons/react/24/outline';
import './Title.css'

function Title({ onButtonClick, isTitleSlidingOut, isTitleSlidingIn, onAnimationEnd }) {
  const [inputValue, setInputValue] = useState("");

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  }

   
  const handleButtonClick = () => {  
    onButtonClick(inputValue);
  };


  return (
    <>
      <div className={isTitleSlidingIn ? "title-slidein title" 
        : isTitleSlidingOut ? "title-slideout title" 
        : "title"} onAnimationEnd={onAnimationEnd}>

        <div className="title__header">
          <h1>ROT.AI</h1>
        </div>

        <div className="title__input">
          <input className="search" value={inputValue} onChange={handleInputChange}></input>
          <button className="title__input__button" onClick={handleButtonClick}>
            <MagnifyingGlassIcon className="search__icon" />
          </button>
        </div>

      </div>
    </>
  )
}

export default Title