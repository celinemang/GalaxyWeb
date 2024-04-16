import React, { useState } from "react";
import Papa from "papaparse";
import "./App.css";

const allowedExtensions = ["csv"];

const App = () => {
    const [data, setData] = useState([]);
    const [file, setFile] = useState("");
    const [error, setError] = useState("");

    const handleFileChange = (e) => {
        setError("");
        if (e.target.files.length) {
            const inputFile = e.target.files[0];
            const fileExtension = inputFile?.type.split("/")[1];
            if (!allowedExtensions.includes(fileExtension)) {
                setError("Please input a csv file");
                return;
            }
            setFile(inputFile);
        }
    };

    const handleParse = () => {
        if (!file) return alert("Enter a valid file");
        const reader = new FileReader();
        reader.onload = async ({ target }) => {
            const csv = Papa.parse(target.result, {
                header: true,
            });
            const parsedData = csv?.data;
            setData(parsedData);
            // Call function to process or visualize data
        };
        reader.readAsText(file);
    };

    return (
        <div className="App">
            <h1 className="geeks">Galaxy Web</h1>
            <h3>Read CSV file </h3>
            <div className="container">
                <label htmlFor="csvInput" style={{ display: "block" }}>
                    Enter CSV File
                </label>
                <input
                    onChange={handleFileChange}
                    id="csvInput"
                    name="file"
                    type="file" // 'file' should be lowercase
                />
                <div>
                    <button onClick={handleParse}>Parse</button>
                </div>
            </div>
        </div>
    );
};

export default App;
