import express from 'express';
import cors from 'cors';
import fetch from 'node-fetch';

const app = express();
const port = 3000;

app.use(cors());

app.get('/translate', async (req, res) => {
  try {
    const lang = req.query.lang || 'en';
    const apiUrl = `https://www.fourtonfish.com/hellosalut/?lang=${lang}`;

    const response = await fetch(apiUrl);

    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }

    const data = await response.json();
    res.json(data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
