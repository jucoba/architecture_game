import React from 'react';

function get_url() {
    if (__DEV__) {
        return "http://localhost:5000/";
    }else {

        return "/";
    }
};

export { get_url };