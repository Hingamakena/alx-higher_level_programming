#!/usr/bin/node

const { argv } = require('node:process')
const count = parseInt(argv[2])

for (let i = 0; i < count; i++){
  for (let j = 0; j < count; j++) {
    console.log('X');
  }
  console.log('\n')
  console.log('X');
}
