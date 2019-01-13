const express = require('express')
const router  = express.Router()
// const Joi     = require('joi')

const MongoClient = require('mongodb').MongoClient
const DB_URI = 'mongodb://mongo:27017'

router.post('/', (req, res) => {
  console.log('POST /')
  console.log('Request body', req.body)

  MongoClient.connect(DB_URI).then(db => {
    const myDB = db.db('blackjack-data')
    myDB.collection('players').insertOne(req.body).then((result) => {
      console.log(result.result)
      console.log(result.ops[0])

      res.send(result.ops[0])
      db.close()
    })
  })
})

router.get('/', (req, res) => {
  console.log('GET /players')

  if (req.query) {
    console.log('Request query detected', req.query)
    MongoClient.connect(DB_URI).then(db => {
      const myDB = db.db('blackjack-data')

      myDB.collection('players').findOne(req.query, (err, document) => {
        console.log('Query result', document)
        res.send(document)
        db.close()
      })
    })
  } else {
    MongoClient.connect(DB_URI).then(db => {
      const myDB = db.db('blackjack-data')

      myDB.collection('players').find({}).toArray((err, result) => {
        if (err) throw err
        res.send(result)
        db.close()
      })
    })
  }
})

router.put('/:id', (req, res) => {
//look up course, if not present, return 404
//validate, if fails, 400 bad request
//update and return player
})

router.get('/:id', (req, res) => {
  res.send(req.params.id)
})



module.exports = router

// function validatePlayer(player) {
//   const schema = {
//     name: Joi.string().min(3).required()
//   }

//   return Joi.validate(player, schema)
// }

// })
// const result = Joi.validate(req.body, schema)
// if (result.error) {
//   res.status(400).send(result.error.details)
// } else {
//   res.send(req.body.name)
// }