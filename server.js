require('dotenv').config()
const express = require('express')
const cors = require('cors')
const OpenAI = require('openai')

const app = express()
const port = process.env.PORT || 3000

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
})

// Middleware
app.use(cors())
app.use(express.json())
app.use(express.static('public'))

// Generate article endpoint
app.post('/api/generate-article', async (req, res) => {
  try {
    const { topic } = req.body

    if (!topic) {
      return res.status(400).json({ error: 'Topic is required' })
    }

    const completion = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "system",
          content: "You are a helpful assistant that generates short, informative articles."
        },
        {
          role: "user",
          content: `Write a short, informative article about ${topic}. The article should be between 200-300 words.`
        }
      ],
      temperature: 0.7,
      max_tokens: 500
    })

    const article = completion.choices[0].message.content
    res.json({ article })
  } catch (error) {
    console.error('Error:', error)
    res.status(500).json({ error: 'Failed to generate article' })
  }
})

app.listen(port, () => {
  console.log(`Server running on port ${port}`)
}) 