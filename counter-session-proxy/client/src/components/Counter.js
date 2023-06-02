import React, { useEffect, useState } from "react";

const Counter = () => {
  const [counter, setCounter] = useState([]);

  const fetchUserData = () => {
    fetch("/count")
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

  return (
    <>
      <p>Counter: {counter.value}</p>
    </>
  );
};

export default Counter;
