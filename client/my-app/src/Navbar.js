import React from 'react'
import {NavLink} from 'react-router-dom'
import './link.css';

function Navbar () {
  return (
    <div style={{color:"black"}} className='l'>
    <nav className='links'>
      <NavLink exact to='/'>Home</NavLink>
      <NavLink to='/accessory'>Accessory</NavLink>
      <NavLink to='/accessoryList'>Accessory List</NavLink>
    </nav>
    </div>
  )
}

export default Navbar
