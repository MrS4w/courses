const { Schema, model } = require('mongoose');

const DevSchema = new Schema({
  name: {
    type: String,
    required: true
  },
  user: {
    type: String,
    required: true
  },
  bio: String,
  avatar: {
    type: String,
    required: true
  },
  likes: [{ type: Schema.Types.ObjectId, ref: 'Dev' }],
  dislikes: [{ type: Schema.Types.ObjectId, ref: 'Dev' }],
  createdAt: {
    type: Date,
    default: Date.now
  }
});

module.exports = model('Dev', DevSchema);
