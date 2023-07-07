import React,{useState} from 'react'
function Accessory() {
  const [formData, setFormData] =  useState({
    location: "", 
    accessories: "",
    description: "",
    price: "",
    image: "",
  })
  function handleOnChange(event) {
    setFormData({
      ...formData,
      [event.target.name]: event.target.value,
    })
  }
  function handleSubmit(event) {
    event.preventDefault()
    const post = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body:JSON.stringify(formData),
    }
    fetch('http://127.0.0.1:5555/showroom',post)
    .then(response => response.json())
    .then(data => setFormData(data))
    .catch (error => console.log (error))
  }


  return (
    <form onSubmit={handleSubmit} className="accessory-form">
        <input onChange={handleOnChange} type= "text" name = "location" value ={formData.location} placeholder = "location" required/>
        <input onChange={handleOnChange} type = "text" name = "accessories" value = {formData.accessories} placeholder = "accessory"required/>
        <input onChange={handleOnChange} type = "text" name = "description"value = {formData.description} placeholder = "description"required/>
        <input onChange={handleOnChange} type = "text" name = "price" value = {formData.price} placeholder = "price"required/>
        <input onChange={handleOnChange} type = "text" name = "image" value = {formData.image} placeholder = "image"required/>
        <button type= "submit" > add Accessory</button>
    </form>


  )
}
export default Accessory