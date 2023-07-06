import React from 'react'
import {NavLink} from 'react-router-dom'

const Navbar = () => {
  return (
    <nav>
      <NavLink exact to= '/'>Home</NavLink>
      <NavLink to= '/accessory'>Accessory</NavLink>
      <NavLink to= '/accesory list'>Accessory List</NavLink>
    </nav>
  )
}

export default Navbar
