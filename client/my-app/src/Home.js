import React from 'react'
import car from './image/car.png'
function Home() {
  return (
    <>
    <div className='n'>
     {/* <div>Home</div> */}
     <img src={car} alt='car' className='car'/>
    </div>
    </>
  )
}
export default Home