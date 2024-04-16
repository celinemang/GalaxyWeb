import React, { useState } from 'react';
import axios from 'axios';
import Papa from 'papaparse';

const FileUpload = () => {
    const [file, setFile] = useState(null);
    const [fileData, setFileData] = useState([]);
    const [error, setError] = useState("");

    const submitFile = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', file);
        try {
            const response = await axios.post('http://localhost:5000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            parseFileData(response.data.fileData);
        } catch (error) {
            console.error('Error uploading file:', error);
            setError("Failed to upload file.");
        }
    };

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const parseFileData = (data) => {
        // Assuming data is a CSV string
        Papa.parse(data, {
            complete: (results) => {
                setFileData(results.data);
                setError("");
            },
            header: true
        });
    };

    return (
        <div>
            <form onSubmit={submitFile}>
                <input type="file" onChange={handleFileChange} />
                <button type="submit">Upload</button>
            </form>
            {error && <div style={{ color: 'red' }}>{error}</div>}
            {fileData.length > 0 && (
                <div>
                    <h3>File Data:</h3>
                    <table>
                        <thead>
                            <tr>
                                {Object.keys(fileData[0]).map(key => <th key={key}>{key}</th>)}
                            </tr>
                        </thead>
                        <tbody>
                            {fileData.map((row, index) => (
                                <tr key={index}>
                                    {Object.values(row).map((val, idx) => <td key={idx}>{val}</td>)}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
};

export default FileUpload;
