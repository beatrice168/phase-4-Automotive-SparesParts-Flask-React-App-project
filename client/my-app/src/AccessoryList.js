import React, { useEffect} from 'react'

const AccessoryList = ()=> {
    // const [data, setData] = useState('')

useEffect(()=>{
    fetch('http://127.0.0.1:5555/showroom')
    .then(r => r.json())
    .then(data => console.log(data))
},[])

return (
    <>

        <h1>hello</h1>

    </>
)

}

export default AccessoryList
