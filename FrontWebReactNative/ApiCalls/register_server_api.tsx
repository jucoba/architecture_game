import React from 'react';


function register_team_api_call ( team_name, player_name) {
    console.log(team_name);
    console.log(player_name);

    return fetch(
        global.url+'register_team', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                team_name: team_name,
                player_name: player_name
            })
        }
    )
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(
        (error) => {
            console.error(error);
        }
    );
};

export { register_team_api_call }