<<<<<<< HEAD
import { React, useState } from "react";
import Exchange from "./Exchange";
import axios from "axios";

const Converter = () => {
  const currencies = ["BTC", "BNB", "XMR", "LTC", "ETH", "USD", "NGN"];
  const [chosenPrimaryCurrency, setChosenPrimaryCurrency] = useState("BTC");
  const [chosenSecondaryCurrency, setChosenSecondaryCurrency] = useState("BTC");
  const [amount, setAmount] = useState(1);
  const [result, setResult] = useState(0);

  const [exchangedData, setExchangedData] = useState({
    primaryCurrency: "BTC",
    secondaryCurrency: "BTC",
    exchangeRate: 0,
  });

  console.log(amount);

  const convert = () => {
    const options = {
      method: "GET",
      url: "http://localhost:8000/convert",
      params: {
        from_currency: chosenPrimaryCurrency,
        function: "CURRENCY_EXCHANGE_RATE",
        to_currency: chosenSecondaryCurrency,
      },
    };

    axios
      .request(options)
      .then((response) => {
        console.log(response.data);
        setResult(response.data * amount);
        setExchangedData({
          primaryCurrency: chosenPrimaryCurrency,
          secondaryCurrency: chosenSecondaryCurrency,
          exchangeRate: response.data,
        });
      })
      .catch((error) => {
        console.error(error);
      });
  };

  console.log(exchangedData);

  return (
    <div className="converter">
      <h2>Currency Converter</h2>
      <div className="input-box">
        <table>
          <tbody>
            <tr>
              <td>Primary Currency:</td>
              <td>
                <input
                  type="number"
                  name="amount-1"
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                />
              </td>
              <td>
                <select
                  name="option-1"
                  value={chosenPrimaryCurrency}
                  className="currency-options"
                  onChange={(e) => setChosenPrimaryCurrency(e.target.value)}
                >
                  {currencies.map((currency, _index) => (
                    <option key={_index}>{currency}</option>
                  ))}
                </select>
              </td>
            </tr>
            <tr>
              <td>Secondary Currency:</td>
              <td>
                <input
                  type="number"
                  name="amount-1"
                  value={result}
                  disabled={true}
                />
              </td>
              <td>
                <select
                  name="option-2"
                  value={chosenSecondaryCurrency}
                  className="currency-options"
                  onChange={(e) => setChosenSecondaryCurrency(e.target.value)}
                >
                  {currencies.map((currency, _index) => (
                    <option key={_index}>{currency}</option>
                  ))}
                </select>
              </td>
            </tr>
          </tbody>
        </table>
        <button id="convert-button" onClick={convert}>
          Convert
        </button>
      </div>
      <Exchange exchangedData={exchangedData} />
    </div>
  );
};

export default Converter;
=======
import { React, useState } from "react";
import Exchange from "./Exchange";
import axios from "axios";

const Converter = () => {
  const currencies = ["BTC", "BNB", "XMR", "LTC", "ETH", "USD", "NGN"];
  const [chosenPrimaryCurrency, setChosenPrimaryCurrency] = useState("BTC");
  const [chosenSecondaryCurrency, setChosenSecondaryCurrency] = useState("BTC");
  const [amount, setAmount] = useState(1);
  const [result, setResult] = useState(0);

  const [exchangedData, setExchangedData] = useState({
    primaryCurrency: "BTC",
    secondaryCurrency: "BTC",
    exchangeRate: 0,
  });

  console.log(amount);

  const convert = () => {
    const options = {
      method: "GET",
      url: "http://localhost:8000/convert",
      params: {
        from_currency: chosenPrimaryCurrency,
        function: "CURRENCY_EXCHANGE_RATE",
        to_currency: chosenSecondaryCurrency,
      },
    };

    axios
      .request(options)
      .then((response) => {
        console.log(response.data);
        setResult(response.data * amount);
        setExchangedData({
          primaryCurrency: chosenPrimaryCurrency,
          secondaryCurrency: chosenSecondaryCurrency,
          exchangeRate: response.data,
        });
      })
      .catch((error) => {
        console.error(error);
      });
  };

  console.log(exchangedData);

  return (
    <div className="converter">
      <h2>Currency Converter</h2>
      <div className="input-box">
        <table>
          <tbody>
            <tr>
              <td>Primary Currency:</td>
              <td>
                <input
                  type="number"
                  name="amount-1"
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                />
              </td>
              <td>
                <select
                  name="option-1"
                  value={chosenPrimaryCurrency}
                  className="currency-options"
                  onChange={(e) => setChosenPrimaryCurrency(e.target.value)}
                >
                  {currencies.map((currency, _index) => (
                    <option key={_index}>{currency}</option>
                  ))}
                </select>
              </td>
            </tr>
            <tr>
              <td>Secondary Currency:</td>
              <td>
                <input
                  type="number"
                  name="amount-1"
                  value={result}
                  disabled={true}
                />
              </td>
              <td>
                <select
                  name="option-2"
                  value={chosenSecondaryCurrency}
                  className="currency-options"
                  onChange={(e) => setChosenSecondaryCurrency(e.target.value)}
                >
                  {currencies.map((currency, _index) => (
                    <option key={_index}>{currency}</option>
                  ))}
                </select>
              </td>
            </tr>
          </tbody>
        </table>
        <button id="convert-button" onClick={convert}>
          Convert
        </button>
      </div>
      <Exchange exchangedData={exchangedData} />
    </div>
  );
};

export default Converter;
>>>>>>> ef7c89f (chore: initial local project setup for xamehi)
