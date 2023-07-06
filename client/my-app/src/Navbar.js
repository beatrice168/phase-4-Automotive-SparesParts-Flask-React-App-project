import React from 'react'
// import {NavLink} from 'react-router-dom'
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav>
      <Link  to= '/'>Home</Link>
      <Link to= '/accessory'>Accessory</Link>
      <Link to= '/accessorylist'>AccessoryList</Link>
    </nav>
  )
}

export default Navbar
