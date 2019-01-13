const express = require('express')
const app = express()

require('dotenv').config()
const PORT = process.env.PORT || 3000

app.use(express.json())
app.use(require('./controllers'))

app.listen(PORT, () => {
  console.log(`Listening on port ${PORT} . . . .`)
})