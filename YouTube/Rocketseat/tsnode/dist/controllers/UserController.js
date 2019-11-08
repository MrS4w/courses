"use strict"; function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }Object.defineProperty(exports, "__esModule", {value: true});

var _User = require('../schemas/User'); var _User2 = _interopRequireDefault(_User);

class UserController {
   async index(req, res) {
    const users = await _User2.default.find();
    return res.json(users);
  }

   async store(req, res) {
    const user = await _User2.default.create(req.body);
    return res.json(user);
  }
}

exports. default = new UserController();
