import React from 'react'


 function ManipulateAccessory({id,deleteAccessory,toggleForm,image,location,accessories,description,price}) {
  return (
    <div className='item'>
        <p>{location}</p>
        <p>{accessories}</p>
        <p>{description}</p>
        <p>{price}</p>
        <img src={image} alt='img'className='img' />
        <button onClick={toggleForm} className="btn">
        Update
      </button>
     {/* <button onClick={()=> updateAccessory(id)} className="btn" >update</button> */}
     <button onClick={()=> deleteAccessory(id)} className="btn" >delete</button>
    </div>
  )
}
export default  ManipulateAccessory