import React  from 'react';


const register_team_api_call = async ( team_name, player_name) => {

    try {
        let response = await fetch(
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
        );
        let json = await response.json();
        return json.id;
    } catch(error) {
        console.log(error)
    }

};

export { register_team_api_call }