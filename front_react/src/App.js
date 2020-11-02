import React from 'react';
import { Route, Link} from 'react-router-dom'

import First  from './containers/First';
import Second  from './containers/Second';

// import logo from './logo.svg';
// import './App.css';

function App() {
  return (
    <div>
        <ul>
            <li><Link to={"/first"}>First</Link> </li>
            <li><Link to={"/second"}>Second</Link> </li>
        </ul>
      Hello World React !!! add3
        <hr/>
          <Route  path={'/first'} component={First}/>
          <Route  path={'/second'} component={Second}/>
    </div>
  );
}

export default App;
