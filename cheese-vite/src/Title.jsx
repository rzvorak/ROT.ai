import { useState } from 'react'
import { MagnifyingGlassIcon } from '@heroicons/react/24/outline';
import './Title.css'

function Title({ onButtonClick, isTitleSlidingOut, isTitleSlidingIn, onAnimationEnd }) {
  const [inputValue, setInputValue] = useState("");
  const [output, setOutput] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  }

  const handleButtonClick = async (e) => {  
    e.preventDefault();
        try {
            // Make a POST request to the Flask server
            const response = await fetch('http://localhost:5000/get-trend', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ word }),
            });

            // Parse the response as JSON
            const data = await response.json();

            // Check if there was an error in the response
            if (response.ok) {
                setOutput(data.output);  // Set the output from the model
                setError(null);  // Clear any previous errors
            } else {
                setError(data.error);  // Set the error message from the server
                setOutput(null);  // Clear previous output
            }
        } catch (err) {
            // Handle errors in the fetch request
            setError('An error occurred: ' + err.message);
            setOutput(null);  // Clear previous output
        }
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