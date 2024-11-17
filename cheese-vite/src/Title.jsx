import { useState } from 'react'
import { MagnifyingGlassIcon } from '@heroicons/react/24/outline';
import './Title.css'

function Title() {
  return (
    <>
      <div className="title">
        <div className="title__header">
          <h1>ROT.AI</h1>
        </div>

        <div className="title__input">
          <input className="search"></input>

          <button className="title__input__button">
            <MagnifyingGlassIcon className="search__icon" />
          </button>
            
        </div>

      </div>
    </>
  )
}

export default Title