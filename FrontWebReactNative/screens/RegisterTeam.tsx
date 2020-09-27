import { StatusBar } from 'expo-status-bar';
import React, {useState} from 'react';
import { StyleSheet, Text, View, TouchableOpacity, TextInput } from 'react-native';
import globalStyles from '../styles/globalStyles'


function register_team ( team_name, player_name) {
    console.log(team_name);
    console.log(player_name);

    return fetch(global.url+'register_team')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
          console.error(error);
        });
};


function RegisterTeam () {
    return  ( <RegisterTeam_with_function onSubmit = { register_team }/>);

};

function RegisterTeam_with_function ( {onSubmit} ) {

    const [team_name_input, setTeam_name_input] = useState('');
    const [player_name_input, setPlayer_name_input] = useState('');

    return (
        <View style={globalStyles.container}>
            <Text style={globalStyles.text}>Nombre de tu equipo</Text>
            <TextInput style={globalStyles.textInupt}
                accessibilityLabel="team-name"
                onChangeText = {text => setTeam_name_input(text) }
                testID="register_team_text_input"
            />
            <Text style={globalStyles.text}>Tu Nombre</Text>
            <TextInput style={globalStyles.textInupt}
                accessibilityLabel="player-name"
                onChangeText = {text => setPlayer_name_input(text) }
                testID="register_player_text_input"

            />
            <TouchableOpacity onPress= { () => onSubmit(team_name_input, player_name_input)   } >
                <Text>Crea tu equipo</Text>
            </TouchableOpacity>
        </View>
    );

};


export default RegisterTeam;
export { RegisterTeam, RegisterTeam_with_function };



