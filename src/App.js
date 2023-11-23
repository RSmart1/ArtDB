// App.js
import React from 'react';
import './App.css';
import './index.css'; 
import { BrowserRouter as Router, Route, Switch, Link, Routes } from 'react-router-dom';
import SubmissionForm from './Components/SubmissionForm';
import OutputScreen from './Components/OutputScreen';

function App() {
  return (
    <div>
    <Router>
      {/* <Navbar /> */}
      <Routes>
        <Route path="/" element={< SubmissionForm/>} />
        <Route path="/OutputScreen" element={<OutputScreen/>} />
        
      </Routes>
    </Router>
    </div>
  );
}

//   return (
//       {/* <Switch>
//         <Route exact path = "/" component={SubmissionForm} />
//         <Route path = "output" component={OutputScreen} />
//     </Switch> */}
//       <SubmissionForm/> 
//       {/* <OutputScreen/> */}
//   );
// }

export default App;