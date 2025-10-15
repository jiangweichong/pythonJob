import express from 'express';
import { AppConfig } from './types';

const app = express();

const config: AppConfig = {
    port: 3000,
    env: 'development',
};

app.use(express.json());

// Define routes here
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(config.port, () => {
    console.log(`Server is running on http://localhost:${config.port} in ${config.env} mode`);
});