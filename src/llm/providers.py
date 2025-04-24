require('dotenv').config()
const express = require('express')
const cors = require('cors')
const path = require('path')
const providers = require('./src/llm/providers')

const app = express()
const port = process.env.PORT || 3000

// Middleware
app.use(cors())
app.use(express.json())
app.use(express.static('public'))

// Get available providers and models
app.get('/api/providers', (req, res) => {
  const providerInfo = Object.entries(providers).map(([id, provider]) => ({
    id,
    name: provider.name,
    models: provider.models
  }))
  res.json(providerInfo)
})

// Generate article endpoint
app.post('/api/generate-article', async (req, res) => {
  try {
    const { topic, provider: providerId, model } = req.body

    if (!topic) {
      return res.status(400).json({ error: 'Topic is required' })
    }

    if (!providerId || !providers[providerId]) {
      return res.status(400).json({ error: 'Invalid provider' })
    }

    if (!model || !providers[providerId].models.includes(model)) {
      return res.status(400).json({ error: 'Invalid model for provider' })
    }

    const provider = providers[providerId]
    const prompt = `Write a short, informative article about ${topic}. The article should be between 200-300 words.`

    try {
      const article = await provider.generate(provider.client, model, prompt)
      res.json({ article, provider: provider.name, model })
    } catch (error) {
      console.error(`Error with ${provider.name}:`, error)
      res.status(500).json({ error: `Failed to generate article using ${provider.name}` })
    }
  } catch (error) {
    console.error('Error:', error)
    res.status(500).json({ error: 'Failed to process request' })
  }
})

app.listen(port, () => {
  console.log(`Server running on port ${port}`)
}) 
