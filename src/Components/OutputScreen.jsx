// OutputScreen.jsx
import React, { useState } from 'react';
import './OutputScreen.css'
import './SubmissionForm.css'

const OutputScreen = () => {
    const [action,setAction] = useState("Submit");
    return(<div className="container">
        
        <div className="headerContainer"><div className="titleHeader">Wallace Collection, London </div></div>

        <div className="body"></div>



    </div>)
};

export default OutputScreen;