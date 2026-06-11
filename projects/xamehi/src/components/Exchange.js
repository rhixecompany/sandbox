import React from "react";

const Exchange = ({ exchangedData }) => {
  return (
    <div className="exchange">
      <h3>Exchange Rate</h3>
      <h1>{exchangedData.exchangeRate}</h1>
      <p>
        {exchangedData.primaryCurrency} to {exchangedData.secondaryCurrency}
      </p>
    </div>
  );
};

export default Exchange;
