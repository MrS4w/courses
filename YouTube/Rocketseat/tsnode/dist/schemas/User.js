"use strict";Object.defineProperty(exports, "__esModule", {value: true});var _mongoose = require('mongoose');







const UserSchema = new (0, _mongoose.Schema)(
  {
    email: String,
    firstName: String,
    lastName: String
  },
  {
    timestamps: true
  }
);

exports. default = _mongoose.model('User', UserSchema);
