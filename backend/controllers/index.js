const express = require('express')
const router = express.Router()



router.use('/players', require('./players'))

router.get('/', (req, res) => {
  res.send('Hello World')
})

module.exports = router