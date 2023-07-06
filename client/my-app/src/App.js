import './App.css';
import Header from './Header';
import Navbar from './Navbar';
import {Route} from 'react-router-dom'
import AccessoryList from './AccessoryList'
import Accessory from './Accessory'
import Home from './Home'

function App() {
  return (
    <div className="App">
      <Header/>
      <Navbar/>
      {/* <Switch> */}
        <Route exact path='/'Component={Home}/>
        <Route path='/accessory' Component={Accessory}/>
        <Route path='/accessorylist' Component={AccessoryList}/>
      {/* </Switch> */}
    </div>
  );
}

export default App;
