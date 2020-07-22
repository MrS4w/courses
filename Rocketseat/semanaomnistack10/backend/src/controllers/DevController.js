const axios = require('axios');
const Dev = require('../models/Dev');
const parseStringAsArray = require('../utils/ParseStringAsArray');

module.exports = {
  async search(request, response) {
    const devs = await Dev.find();

    return response.json(devs);
  },

  async create(request, response) {
    const { github_username, techs, latitude, longitude } = request.body;

    const apiResponse = await axios.get(
      `https://api.github.com/users/${github_username}`
    );

    let dev = await Dev.findOne({ github_username });

    if (!dev) {
      const { name = login, avatar_url, bio } = apiResponse.data;

      const techsArray = parseStringAsArray(techs);

      const location = {
        type: 'Point',
        coordinates: [longitude, latitude],
      };

      dev = await Dev.create({
        name,
        github_username,
        bio,
        avatar_url,
        techs: techsArray,
        location,
      });
    }

    return response.json(dev);
  },
};
