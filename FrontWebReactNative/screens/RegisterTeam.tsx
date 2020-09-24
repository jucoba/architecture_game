import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';
import globalStyles from '../styles/globalStyles'

import { render, fireEvent } from '@testing-library/react-native';

const register_team = () => {

    return fetch(global.url+'register_team')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
          console.error(error);
        });
};

function RegisterTeam() {

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
            <Button
                onPress={register_team}
                style={globalStyles.button}
                title="Crea tu equipo"
                color="#841584"
            />
        </View>
    );

};

export default RegisterTeam ;



