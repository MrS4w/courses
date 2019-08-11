import React, { Component } from 'react';
import socket from 'socket.io-client';
import api from '../services/api';

import twitterLogo from '../twitter.svg';
import './Timeline.css';

import Tweet from '../components/Tweet';

export default class Timeline extends Component {
    state = {
        tweets: [],
        newTweet: ''
    };

    async componentDidMount() {
        this.subscribeToEvents();

        const response = await api.get('tweets');

        this.setState({ tweets: response.data });
    }

    subscribeToEvents = () => {
        const io = socket('http://localhost:3000');

        io.on('tweet', data => {
            this.setState({ tweets: [data, ...this.state.tweets] });
        });

        io.on('like', data => {
            this.setState({
                tweets: this.state.tweets.map(tweet =>
                    tweet._id === data._id ? data : tweet
                )
            });
        });
    };

    handleNewTweet = async e => {
        if (e.keyCode !== 13) return;

        e.preventDefault();

        const content = this.state.newTweet;
        const author = localStorage.getItem('@GoTwitter:username');

        await api.post('tweets', { content, author });

        this.setState({ newTweet: '' });
    };

    handleTweetChange = e => {
        this.setState({ newTweet: e.target.value });
    };

    render() {
        return (
            <div className="timeline-wrapper">
                <img height="24" src={twitterLogo} alt="GoTwitter" />

                <form>
                    <textarea
                        value={this.state.newTweet}
                        onChange={this.handleTweetChange}
                        onKeyDown={this.handleNewTweet}
                        placeholder="O que está acontecendo?"
                    />
                </form>

                <ul className="tweet-list">
                    {this.state.tweets.map(tweet => (
                        <Tweet key={tweet._id} tweet={tweet} />
                    ))}
                </ul>
            </div>
        );
    }
}
