import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, TextInput } from 'react-native';
import globalStyles from '../styles/globalStyles'

import { render, fireEvent } from '@testing-library/react-native';

function register_team () {

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

    return (
        <View style={globalStyles.container}>
            <Text style={globalStyles.text}>Nombre de tu equipo</Text>
            <TextInput style={globalStyles.textInupt}
                accessibilityLabel="team-name"
            />
            <Text style={globalStyles.text}>Tu Nombre</Text>
            <TextInput style={globalStyles.textInupt}
                accessibilityLabel="player-name"
            />
            <TouchableOpacity onPress= { onSubmit } >
                <Text>Crea tu equipo</Text>
            </TouchableOpacity>
        </View>
    );

};


export default RegisterTeam;
export { RegisterTeam, RegisterTeam_with_function };



