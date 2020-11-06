import React from 'react';


function get_team_api(id: int) {
    return fetch(
        global.url+'team/'+id, {
            method: 'GET'

        }
    )
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(
        (error) => {
            console.error(error);
        }
    );

}

