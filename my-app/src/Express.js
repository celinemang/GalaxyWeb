const express = require('express');
const cors = require('cors');
const app = express();

const corsOptions = {
    origin: 'http://localhost:3000', // Allow only HTTP from localhost:3000
    credentials: true, // Allow cookies to be sent
    optionsSuccessStatus: 200 // Legacy browsers support for CORS
};

app.use(cors(corsOptions));

// Define routes here

app.listen(5000, () => {
    console.log('Server is running on http://localhost:5000');
});
