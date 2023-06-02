import React, { useEffect, useState } from "react";

const Counter = () => {
  const [counter, setCounter] = useState([]);

  const fetchUserData = () => {
    fetch("http://127.0.0.1:5555/count", {
      credentials: "include",
      mode: "cors",
    })
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setCounter(data);
      });
  };

  useEffect(() => {
    fetchUserData();
  }, []);

  return <p>Counter: {counter.value}</p>;
};

export default Counter;
