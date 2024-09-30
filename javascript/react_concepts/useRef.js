import React, {useRef} from 'react';

export function App(props) {
  const name = useRef("hello Aunt");
  const Submit = () => {console.log(name.current.value)}
  console.log("rendered", name.current)
  return (
    <div className='App'>
      <h1>Hello React.</h1>
      <input ref={name} type="text" placeholder="enter name" defaultValue={name?.current}/>
      <button onClick={Submit}>Submit</button>
    </div>
  );
}